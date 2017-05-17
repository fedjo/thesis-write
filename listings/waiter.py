class _CouchDBJobFileChangesWaiter(base._BaseJobFileChangesWaiter):
  def Wait(self, timeout):
    """Waits for the job to change.

    @return: Tuple of ('Polling', result) format. If the timeout
             expires result is False, otherwise a new _QueuedJob
             object with the new data returned. 'Polling' is used
             to distinguish this case in utils.Retry function.

    """
    assert timeout >= 0
    result = False
    timeout = int(timeout) + 1
    have_events = self.db_name.changes(filter='filter/job_id',
        id=self.job_id, feed='longpoll', include_docs=True,
        since=self.since, timeout=timeout * 1000)
    if have_events['results']:
      try:
        data = have_events['results'][0]['doc']
        raw = json.loads(data['info'])
        result = _QueuedJob.Restore(self, raw, writable=False,
                                    archived=None)
      except Exception, err:
        raise errors.JobFileCorrupted(err)

    self.since = have_events['last_seq']

    return ('Polling', result)
