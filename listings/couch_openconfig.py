def _OpenConfig(self, accept_foreign):
  """Read the config data from the database.

  """
  raw_data = self._BuildConfigData()

  try:
    # Tranform <couchdb.client.Document> object to <ConfigData> object
    data = objects.ConfigData.FromDict(raw_data)
  except Exception, err:
    raise errors.ConfigurationError(err)

  # Make sure the configuration has the right version

  if (not hasattr(data, "cluster") or
      not hasattr(data.cluster, "rsahostkeypub")):
    raise errors.ConfigurationError("Incomplete configuration"
                                    " (missing cluster.rsahostkeypub)")


  if data.cluster.master_node != self._my_hostname and not accept_foreign:
    msg = ("The configuration denotes node %s as master, while my"
           " hostname is %s; opening a foreign configuration is only"
           " possible in accept_foreign mode" %
           (data.cluster.master_node, self._my_hostname))
    raise errors.ConfigurationError(msg)

  self._config_data = data

  # reset the last serial as -1 so that the next write will cause
  # ssconf update
  self._last_cluster_serial = -1

  # Upgrade configuration if needed
  self._UpgradeConfig()
