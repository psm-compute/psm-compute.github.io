OARSUB tips
===========

Cancel all jobs
---------------

.. code:: bash

    oarstat -u username | awk '{print $1}' | xargs -n 1 oardel

where username should be replaced by your ID.