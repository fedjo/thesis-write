from ganeti.jqueue import base

class DiskJobQueue(base.BaseJobQueue):
  def __init__(self):
    super(DiskJobQueue, self).__init__()

    # Initialize the queue, and acquire the filelock.
    self.jstore_cl = jstore.GetJStore("disk")
    self._queue_filelock = self.jstore_cl.InitAndVerifyQueue()

    # Read serial file
            . . .

    # More initializations
