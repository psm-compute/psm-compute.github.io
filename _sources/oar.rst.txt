OAR tips
========

Cancel All Jobs
---------------

Cancel all your jobs at once by typing:

.. code:: bash

    oarstat -u username | awk '{print $1}' | xargs -n 1 oardel

where username should be replaced by your ID.

Submit Jobs with Dependencies
-----------------------------

You can submit jobs with dependencies using the following example. Assume you have two job scripts, `job1.sh` and `job2.sh`, that you wish to submit:

1. Submit `job1.sh` and capture its job ID:

   .. code-block:: bash

      job1_id=`oarsub -S ./job1.sh |grep OAR_JOB_ID|awk -F'=' '{print $2}'`

2. Submit `job2.sh` so that it starts only after the completion of `job1.sh`:

   .. code-block:: bash

      oarsub -S ./job2.sh  -a $job1_id

In this example, `job2.sh` will automatically wait for `job1.sh` to complete before starting, using the job ID captured in `job1_id`.

