def _ClusterObjectPrepare(config_data):
  """Prepares the config_data.cluster object for writing to disk.

  We separated the config.data object into it's most heavy loaded
  components {nodes, instances, nodegroups, networks, cluster} but
  the memory represantation remain as it was. So before we write
  the cluster part of the config.data to disk we should first flush
  the rest config.data components.

  @type data: L{objects.ConfigData}
  @param data: configuration data
  @rtype: dict
  @return: The config_data object ready for writing to disk

  """
  data = objects.ConfigData.ToDict(config_data)
  data['nodegroups'] = {}
  data['nodes'] = {}
  data['instances'] = {}
  data['networks'] = {}

  return data
