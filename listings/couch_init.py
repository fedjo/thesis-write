class CouchDBConfigWriter(base._BaseConfigWriter):
  """CouchDB configuration storage type

  """
  def __init__(self, ... ):
    super(CouchDBConfigWriter, self).__init__()
                . . .
    # CouchDB initialization
    # Setup the connection with Couch Server for all databases
    self._hostip = netutils.Hostname.GetIP(self._my_hostname)
    ip = self._hostip
    port = constants.DEFAULT_COUCHDB_PORT

    # Get database instances
    self._cfg_db = utils.GetDBInstance(CLUSTER_DB, ip, port)
    self._nodes_db = utils.GetDBInstance(NODES_DB, ip, port)
    self._networks_db = utils.GetDBInstance(NETWORKS_DB, ip, port)
    self._instances_db = utils.GetDBInstance(INSTANCES_DB, ip, port)
    self._nodegroups_db = utils.GetDBInstance(NODEGROUPS_DB, ip, port)

    self._OpenConfig()
