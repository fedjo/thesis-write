from ganeti.config import base

class DiskConfigWriter(base._BaseConfigWriter):
  """Disk storage configuration type

  """
  def __init__(self, cfg_file=None, ... ):
    super(DiskConfigWriter, self).__init__()

    if cfg_file is None:
      self._cfg_file = pathutils.CLUSTER_CONF_FILE
    else:
      self._cfg_file = cfg_file

                . . .

    self._OpenConfig()
