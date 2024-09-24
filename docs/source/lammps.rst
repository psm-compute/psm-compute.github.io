LAMMPS tips
===========

Choose where to compile LAMMPS
------------------------------

If the code must be accessed only by you, you can save it in your ``/home/`` folder on
Dahu/Bigfoot. If you want the code to be available to all the member from
your group, you can use ``/bettik/PROJECTS/``. For instance, for the members of `tamtam`:

.. code-block:: bash

    /bettik/PROJECTS/pr-tamtam/

Download LAMMPS 
---------------

From the |LAMMPS| webpage, download the version of your choice.
For instance, from the terminal, download the last stable release:

.. code-block:: bash

    wget https://download.lammps.org/tars/lammps.tar.gz
    tar -xzvf lammps.tar.gz

.. |LAMMPS| raw:: html

    <a href="https://www.lammps.org/download.html" target="_blank">LAMMPS</a>


Compile LAMMPS
--------------

For compiling in serial, simply navidate to the ``src/`` folder, and type:

.. code-block:: bash

    make serial

For compilling in parallel, you will need to load manually openmpi and gcc using NIX:

.. code-block:: bash

    source /applis/site/nix.sh
    nix-shell -p openmpi -p gcc

Then, from the ``src/`` folder, type:

.. code-block:: bash

    make mpi

Run LAMMPS
----------

Create a bash file named *sub.sh* with the following content:

.. code-block:: bash

    #!/bin/bash
    #OAR -n test
    #OAR -l /nodes=1/cpu=1/core=4,walltime=12:00:00
    #OAR --stdout log.out
    #OAR --stderr log.err
    #OAR --project tamtam

    # Path to the LAMMPS executable
    lmp=/path/lmp_mpi

    mpirun -np 4 ${lmp} -in input.lmp

where ``input.lmp`` is your LAMMPS input file, and where the project was assumed
to be `tamtam` (to adapt to your case). Here, 4 CPU cores are requested,
as well as a total duration of 12 hours. Then, make the file file executable with
chmod and launch it using:

.. code-block:: bash

    chmod +x ./sub.sh
    oarsub -S ./sub.sh

Launch multiple jobs using bash
_______________________________

Assuming that one has the job submission script named *sub.sh* with name *lmp-myvariable-0*,
that launch a lammps input script named *input.lmp* by passing a variable
named *myvariable* into it. Additionally, here the job ID is used as an
input for the random seed, allowing for example different initial configurations:

.. code:: bash

    #!/bin/bash
    #OAR -n lmp-myvariable-0
    #OAR -l /nodes=1/cpu=1/core=4,walltime=12:00:00
    #OAR --stdout log.out
    #OAR --stderr log.err
    #OAR --project tamtam

    # Path to the LAMMPS executable
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
