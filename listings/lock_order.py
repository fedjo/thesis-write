def ExecOpCode(opcode):
  # Depending on the opcode given get the appropriate LU class instance.
  lu = lu_class(opcode)

  # Purely lock-related functions.
  # Update all the opcode parameters to their canonical form,
  # (e.g. user passed names are expanded to the internal lock/resource
  # name). Then known needed locks are declared.
  lu.ExpandNames()

  # While most of LUs declare their locks at ExpandNames time, sometimes
  # there is the need to calculate some locks after having acquired the
  # ones before, because we can't know which resources we need before
  # locking the previous level.
  lu.DeclareLocks()

  ## At this point every function is called with the appropriate lock held.

  # This method checks the prerequists for the execution of this LU.
  lu.CheckPrereq()

  # This method implements the actual work, the opcode execution.
  lu.Exec()

  ## All acquired locks released, locks declared for removal are removed.
