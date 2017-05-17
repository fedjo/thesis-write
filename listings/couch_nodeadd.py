@locking.ssynchronized(_config_lock)
def AddNode(self, node, ec_id):
  """Add a node to the configuration.

  """
  # In-object updates
  node._id = node.name
  node.serial_no = 1
  node.ctime = node.mtime = time.time()
  self._config_data.nodes[node.name] = node
  self._config_data.cluster.serial_no += 1

  # Write the cluster object to the 'config_data' database.
  data = _ClusterObjectPrepare(self._config_data)
  self._WriteConfig(db_name=self._cfg_db, data=data)

  # Write the node object to the 'nodes' database.
  data = objects.Node.ToDict(node)
  self._WriteConfig(db_name=self._nodes_db, data=data)

  # Enable continuous replication if node marked as MC.
  if node.master_candidate:
    for db in constants.CONFIG_DATA_DBS:
      utils.UnlockedReplicateSetup(hostip, node.primary_ip, db)
