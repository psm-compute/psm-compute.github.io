OAR tips
========

Cancel all jobs
---------------

Cancel all your jobs at once by typing:

.. code:: bash

    oarstat -u username | awk '{print $1}' | xargs -n 1 oardel

where username should be replaced by your ID.

Submit multiple jobs
--------------------

