OAR tips
========

This page collect some tips and tricks for managing jobs using the OAR system of |GRICAD|.

.. |GRICAD| raw:: html

    <a href="https://gricad-doc.univ-grenoble-alpes.fr/hpc/joblaunch/job_management/" target="_blank">GRICAD</a>

Submit Jobs with Dependencies
-----------------------------

You can submit jobs with dependencies using the following example. Assuming that
you have two job scripts, `job1.sh` and `job2.sh`, and that you wish to submit
`job2.sh` `after` `job1.sh` is done.

1. Submit `job1.sh` and capture its job ID:

   .. code-block:: bash

      job1_id=`oarsub -S ./job1.sh |grep OAR_JOB_ID|awk -F'=' '{print $2}'`

2. Submit `job2.sh` so that it starts only after the completion of `job1.sh`:

   .. code-block:: bash

      oarsub -S ./job2.sh  -a $job1_id

In this example, `job2.sh` will wait for `job1.sh` to complete
before starting, using the job ID (`job1_id`).

Cancel All Your Jobs at Once
----------------------------

You can cancel all your jobs at once by typing:

.. code:: bash

    oarstat -u username | awk '{print $1}' | xargs -n 1 oardel

where username should be replaced by your ID.

Launch Multiple Jobs
--------------------

Here, tips to efficiently launch multiple jobs are provided.

Batch Job Submission
____________________

Assuming that one has the job submission script named *sub.sh* with name *lmp-myvariable-0*,
that launch a lammps input script named *input.lmp* by passing a variable
named *myvariable* into it. Additionally, here the job ID is used as an input for the random seed, allowing for example different initial configurations:

.. code:: bash

    #!/bin/bash
    #OAR -n lmp-myvariable-0
    #OAR -l /nodes=1/cpu=1/core=4,walltime=48:00:00
    #OAR --stdout log-water.out
    #OAR --stderr log-water.err
    #OAR --project tamtam

    # Path to the LAMMPS MPI executable
    lmp=/path/lmp_mpi

    myvariable=0

    # Run LAMMPS using MPI, with 4 processes, using the input from 'input.lmp'
    mpirun -np 4 ${lmp} -in input.lmp -var nb2 ${myvariable} -var seedin $OAR_JOBID

If one wants to launch the current job, one simply have to type:

.. code:: bash

    chmod +x sub.sh
    oarsub -S ./sub.sh

and a single job with name *lmp-myvariable-0* will be send.
To launch multiple simulations with different values of *myvariable*,
say 0, 1, and 2, one can create a second bash script, named *multi-sub.sh*,
and containing:

.. code:: bash

    #!/bin/bash
    set -e

    for myvariable in 0 1 2
    do
        # deal with OAR -n
        newline='#OAR -n lmp-myvariable-'$myvariable
        oldline=$(cat sub.sh | grep '#OAR -n lmp-myvariable-')
        sed -i '/'"$oldline"'/c\'"$newline" sub.sh
        # deal with myvariable
        newline='myvariable='$myvariable
        oldline=$(cat sub.sh | grep 'myvariable =')
        sed -i '/'"$oldline"'/c\'"$newline" sub.sh
        chmod +x sub.sh
        oarsub -S ./sub.sh
    done

The *newline* command creates a new line that will replace the line
containing *myvariable* in the script sub.sh
The *oldline=* command finds the current line in sub.sh that contains 'myvariable =',
storing it in the variable oldline. This assumes there is exactly one such line,
otherwise the behavior may be unexpected. Then, sed is used to replace the old
line with the new line (newline) in *sub.sh*.

Then, simply run *multi-sub.sh* by typing:

.. code:: bash

    bash multi-sub.sh
