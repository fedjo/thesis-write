class _BaseConfigWriter(object):
  """Base class for the configuration storage abstraction.

  """
  def __init__(self):
    self.write_count = 0
    self._lock = _config_lock
    self._config_data = None

    # Temporary reservation manager initialization
                      . . .

    self._my_hostname = netutils.Hostname.GetSysName()
    self._last_cluster_serial = -1
    self._context = None
