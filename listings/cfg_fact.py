# Lookup table for configuration storage types
_CONFIG_DATA_TYPES = {
  constants.CFG_DISK: default.DiskConfigWriter,
  constants.CFG_COUCHDB: couch.CouchDBConfigWriter
  }

def GetConfigWriterClass(name):
  """Returns the class for a configuration data storage type

  @type name: string
  @param name: Configuration storage type

  """
  try:
    return _CONFIG_DATA_TYPES[name]
  except KeyError:
    msg = "Unknown configuration storage type: %r" % name
    raise errors.ConfigurationError(msg)


def GetConfigWriter(name, **kargs):
  """Factory function for configuration storage methods.

  @type name: string
  @param name: Configuration storage type

  """
  return GetConfigWriterClass(name)(**kargs)
