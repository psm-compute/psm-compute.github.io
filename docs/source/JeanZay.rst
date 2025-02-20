Jean-Zay tips
===========



LAMMPS
-------

Examples of sbatch job scripts are provided to run LAMMPS on CPU only and on both CPU and GPU. It is not always beneficial to use all available GPUs and CPUs on a node. For instance, tests conducted with a solid polymer electrolyte box containing 22,840 atoms, using the PPPM solver, SHAKE algorithm, and an external field, demonstrated that the optimal configuration was 1 GPU and 8 CPU cores. Using additional resources negatively impacted the calculation performance.

CPU example

.. code-block:: bash

  #!/bin/bash
  #SBATCH --nodes=1               # Number of Nodes
  #SBATCH --ntasks-per-node=32    # Number of MPI tasks per node
  #SBATCH --cpus-per-task=1       # Number of OpenMP threads
  #SBATCH --hint=nomultithread    # Disable hyperthreading
  #SBATCH --job-name=JOB_NAME        # Jobname
  #SBATCH --output=%x.o%j         # Output file %x is the jobname, %j the jobid
  #SBATCH --error=%x.o%j          # Error file
  #SBATCH --time=20:00:00         # Expected runtime HH:MM:SS (max 100h)
  #SBATCH --account=<account>@cpu       # To specify cpu accounting: <account> = echo $IDRPROJ
  ##SBATCH --partition=cpu_p1            # To specify partition (see IDRIS web site for more info)
  ##SBATCH --qos=qos_cpu-dev      # Uncomment for job requiring less than 2 hours
  ##SBATCH --qos=qos_cpu-t4      # Uncomment for job requiring more than 20h (up to 4 nodes)
         
  # Cleans out the modules loaded in interactive and inherited by default
  module purge
  
  # Load the module
  
  module load lammps/20230328-mpi
  
  # Execute commands
  srun lmp -i in.run

                       

GPU example 

.. code-block:: bash

  #!/bin/bash
  #SBATCH --nodes=1               # Number of Nodes
  #SBATCH --ntasks-per-node=8
  #SBATCH --cpus-per-task=1       # Number of OpenMP threads
  #SBATCH --gres=gpu:1
  #SBATCH --hint=nomultithread    # Disable hyperthreading
  #SBATCH --output=output.dat         # Output file %x is the jobname, %j the jobid
  #SBATCH --error=error.dat          # Error file
  #SBATCH --time=0:10:00         # Expected runtime HH:MM:SS (max 100h)
  #SBATCH --account=<account>@v100       # To specify cpu accounting: <account> = echo $IDRPROJ
  #SBATCH --job-name=JOB_NAME        # Jobname
  ###SBATCH --qos=qos_gpu-dev
  # Cleans out the modules loaded in interactive and inherited by default
  module purge

  # Load the module
  module load lammps/20230802-mpi-cuda
  set -x
  srun lmp -sf gpu -pk gpu 1 -in in.run

