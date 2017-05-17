def _BuildConfigData(self):
  """This function unifies the config.data from its sub- components,
  because we do not want to change the in-memory represantation of it.

  """
  # Get config.data from the db
  raw_data = self._cfg_db.get("config.data")

  # nodes dictionary
  nodes = {}
  view_nodes = self._nodes_db.view('_all_docs', include_docs=True)
  for row in view_nodes.rows:
    node = row['doc']
    nodes[node['name']] = node

  # instances dictionary
  instances = {}
  view_insts = self._instances_db.view('_all_docs', include_docs=True)
  for row in view_insts.rows:
    instance = row['doc']
    instances[instance['name']] = instance

  # nodegroups dictionary
        . . .

  # networks dictionary
        . . .

  # build the unified config.data object
  raw_data['nodegroups'] = nodegroups
  raw_data['nodes'] = nodes
  raw_data['instances'] = instances
  raw_data['networks'] = networks

  return raw_data
