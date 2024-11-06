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

Record the last Job ID and state
--------------------------------

It can be useful to record the ID of the last launched job.

.. code:: bash

    oarsub -S ./myjob.sh
    oarstat -u username | awk '{print $1}' | tail -n 1 > last_job_id.txt

where username should be replaced by your ID. The file `last_job_id.txt`
will contain the ID of the last launched job. You can also record the entire state
of the job:

.. code:: bash

    last_job_id=$(oarstat -u username | awk '{print $1}' | tail -n 1)
    oarstat -u username -j "$last_job_id" > last_job_state.txt

Launch Multiple Jobs
--------------------

Here, tips to efficiently launch multiple jobs are provided.

.. SG: this will be completed when Romain send me an example.

.. code:: bash

    #!/bin/bash
    ...
    #OAR --array 50

    id=`echo "$OAR_JOB_ID - $OAR_ARRAY_ID + 2" | bc -l`  # <---- This id runs from 0 to 50, each job gets one, with which you can e.g. index a bash array
    temperatures=(0.25 0.5 1 .... )
    T=${temperatures[${id}]}

Measure the CPU Usage per User
------------------------------

This script runs `oarstat`, and then calculates the CPU cores per user.
The output will list each user along with the total
number of CPU cores they are using (Running and waiting).

Create a Bash Script (for instance named `cpu_usage.sh`), and copy the
following lines into the file:

.. code:: bash

    #!/bin/bash

    oarstat | awk '
        /^[0-9]+/ {
            # $3 is the user, $2 is the job status, and we look for "R=" to get the core count
            job_status = $2
            user = $3

            # Find the core count for the job
            for (i=1; i<=NF; i++) {
                if ($i ~ /^R=[0-9]+/) {
                    # Extract the core count from the "R=" field
                    split($i, core_count, "=")
                    
                    # Increment cores based on job status (R for running, W for waiting)
                    if (job_status == "R") {
                        running_cores[user] += core_count[2]
                    } else if (job_status == "W") {
                        waiting_cores[user] += core_count[2]
                    }
                }
            }
        }
        # After processing all lines, print the total cores for each user for running and waiting jobs
        END {
            printf "%-10s %-15s %-15s\n", "User", "Running Cores", "Waiting Cores"
            for (user in running_cores) {
                printf "%-10s %-15d %-15d\n", user, running_cores[user], waiting_cores[user]
            }
        }
    ' | sort


Run the following command to give execution permissions to the script:

.. code:: bash

    chmod +x cpu_usage.sh
    ./cpu_usage.sh

It will return something like:

.. code:: bash

    calvof     102             0              
    farutial   2               0              
    gravells   100             24             
    joyeuxm    280             0              
    jungg      114             0              
    mhirizn-   4               0              
    nagasawt   2               0              
    ozawam     50              0              
    quilliec   2               0              
    User       Running Cores   Waiting Cores 
