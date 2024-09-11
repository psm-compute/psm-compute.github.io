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

Create a bash (``.sh``) file with the following content:

.. code-block:: bash

    #!/bin/bash
    #OAR -n test
    #OAR -l /nodes=1/cpu=1/core=4,walltime=12:00:00
    #OAR --stdout log.out
    #OAR --stderr log.err
    #OAR --project tamtam

    mpirun -np 4 /PATH-TO-LAMMPS/lmp_mpi -in input.lmp

where ``input.lmp`` is your LAMMPS input file, and there the project was assumed
to be `tamtam` (to adapt to your case). Here, 4 CPU cores are requested,
as well as a total duration of 12 hours. Then, make the file file executable with
chmod and launch it using:

.. code-block:: bash

    chmod +x ./myfile.sh
    oarsub -S ./myfile.sh
