Sphinx tips
===========

Contributing to this Documentation
----------------------------------

1. Compile the HTML Webpage Locally
____________________________________

To compile the HTML files locally, navigate to the parent directory of your project and run:

.. code-block:: bash

    make html

This command will generate the HTML files for your webpage.

**Troubleshooting:**

- If the ``make html`` command fails, you might need to install the necessary dependencies first. You can do this by running:

  .. code-block:: bash

      pip install -r requirements.txt

2. View the Compiled HTML
__________________________

Once the compilation is successful, you can view the HTML files by navigating to the ``docs/build/html`` directory. Open the files in this folder with your preferred web browser to see your webpage.

3. Modify the Documentation
____________________________

**Important:** 

- **Never modify files directly in the** ``html`` **folder.**
- Always make changes in the ``docs/source`` folder, which contains the source files used to generate the HTML.

**Steps for Modifying Content:**

1. **Create a New** ``.rst`` **File:**

   If you need to add new content, you can create a new ``.rst`` file in the ``docs/source`` directory. Use an existing file, such as ``oar.rst``, as a template for the new file.

   - **Formatting Tips:** For guidance on formatting ``.rst`` files, refer to `appropriate documentation <https://developer.lsst.io/restructuredtext/style.html>`_.


2. **Update the** ``index.rst`` **File:**

   After adding or modifying ``.rst`` files, update the ``index.rst`` file to include your new content in the table of contents or navigation structure.

4. Re-compile the HTML Webpage
_______________________________

Once you've made your changes, first delete previous files to avoid conflict:

.. code-block:: bash

   make clean

Second recompile the HTML files by running ``make html`` again from the parent directory (``docs``), where the ``make.bat`` file is located:

.. code-block:: bash

    make html

This will regenerate the HTML files with your latest modifications.

5. Commit and Push Changes
__________________________

After confirming your changes are reflected in the compiled HTML, it's time to commit and push your changes to the repository. For detailed instructions on how to commit and push changes, see :ref:`git-tips`.
