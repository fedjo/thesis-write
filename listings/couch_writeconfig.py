def _WriteConfig(self, db_name=None, data=None, feedback_fn=None):
  """Write the configuration data to persistent storage.

  """
  assert feedback_fn is None or callable(feedback_fn)

  # Warn on config errors, but don't abort the save - the
  # configuration has already been modified, and we can't revert;
  # the best we can do is to warn the user and save as is, leaving
  # recovery to the user
  config_errors = self._UnlockedVerifyConfig()
  if config_errors:
    errmsg = ("Configuration data is not consistent: %s" %
              (utils.CommaJoin(config_errors)))
    logging.critical(errmsg)
    if feedback_fn:
      feedback_fn(errmsg)

  # Save the ConfigData object to datababse
  try:
    utils.WriteDocument(db_name, data)
  except errors.LockError:
    raise errors.ConfigurationError("The configuration file has been"
                                    " modified since the last write, cannot"
                                    " update")

  self.write_count += 1

  # Write ssconf files on all nodes (including locally)
  if self._last_cluster_serial < self._config_data.cluster.serial_no:
    if not self._offline:
      result = self._GetRpc(None).call_write_ssconf_files(
        self._UnlockedGetOnlineNodeList(),
        self._UnlockedGetSsconfValues())

      for nname, nresu in result.items():
        msg = nresu.fail_msg
        if msg:
          errmsg = ("Error while uploading ssconf files to"
                    " node %s: %s" % (nname, msg))
          logging.warning(errmsg)

          if feedback_fn:
            feedback_fn(errmsg)

    self._last_cluster_serial = self._config_data.cluster.serial_no
