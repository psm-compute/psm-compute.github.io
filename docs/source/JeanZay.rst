Jean-Zay tips
===========



.. code:: bash
  #!/bin/bash
  #SBATCH --nodes=1               # Number of Nodes
  #SBATCH --ntasks-per-node=8
  #SBATCH --cpus-per-task=1       # Number of OpenMP threads
  #SBATCH --gres=gpu:2
  #SBATCH --hint=nomultithread    # Disable hyperthreading
  #SBATCH --output=output.dat         # Output file %x is the jobname, %j the jobid
  #SBATCH --error=error.dat          # Error file
  #SBATCH --time=0:10:00         # Expected runtime HH:MM:SS (max 100h)
  #SBATCH --account=<account>@v100       # To specify cpu accounting: <account> = echo $IDRPROJ
  #SBATCH --job-name=F_gpu        # Jobname
  #SBATCH --qos=qos_gpu-dev
  # Cleans out the modules loaded in interactive and inherited by default
  module purge

  # Load the module
  module load lammps/20230802-mpi-cuda
  set -x
  srun lmp -sf gpu -pk gpu 2 -in in.run
