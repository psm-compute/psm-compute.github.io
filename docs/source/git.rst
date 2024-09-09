GIT tips
========

Getting Started with Git and GitHub
-----------------------------------

1. Set Up Your SSH Key
______________________

To securely connect with GitHub, you'll need to add your SSH key to your GitHub account. Here you can find how to `add your public key <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_ .

2. Clone a GitHub Repository
____________________________

Navigate to the directory where you want to download the repository, then use the :code:`git clone` command:

.. code:: bash

    git clone git@github.com:psm-compute/psm-compute.github.io.git

This command will create a copy of the repository in your specified directory.

3. Check the Status of Your Repository
______________________________________

After cloning, it's a good practice to check the status of your repository to see if there are any changes:

.. code:: bash

    git status

4. Create and Switch to a New Branch
____________________________________

To make changes without affecting the main branch, create a new branch and switch to it. Let's make a test updating `README.md` file.

.. code:: bash

    git branch update_readme
    git checkout update_readme


5. Edit Files and Stage Changes
_______________________________

Make the necessary edits to your files. For example, to edit the `README.md` file, use a text editor like `vi`:

.. code:: bash

    vi README.md

After editing, check the status again to see the changes:

.. code:: bash

    git status

Stage the changes to prepare them for commit:

.. code:: bash

    git add README.md

6. Commit and Push Changes
__________________________

Commit your changes with a descriptive message:

.. code:: bash

    git commit -m "Test change README.md"

Next, push your changes to GitHub. If it's the first time you're pushing from this branch, you'll need to set the upstream branch:

.. code:: bash

    git push

If you encounter an error, you'll typically need to set the upstream for the branch:

.. code:: bash

    git push --set-upstream origin update_readme

7. Delete the Branch Locally (Optional)
_______________________________________

If you no longer need the branch locally, you can delete it:

.. code:: bash

    git branch -d update_readme


Modifying the HTML Webpage
---------------------------

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

- **Never modify files directly in the ``html`` folder.**
- Always make changes in the ``docs/source`` folder, which contains the source files used to generate the HTML.

**Steps for Modifying Content:**

1. **Create a New ``.rst`` File:**

   If you need to add new content, you can create a new ``.rst`` file in the ``docs/source`` directory. Use an existing file, such as ``oar.rst``, as a template for the new file.

   - **Formatting Tips:** For guidance on formatting ``.rst`` files, refer to `appropriate documentation <https://developer.lsst.io/restructuredtext/style.html>`_.


2. **Update the ``index.rst`` File:**

   After adding or modifying ``.rst`` files, update the ``index.rst`` file to include your new content in the table of contents or navigation structure.

4. Re-compile the HTML Webpage
_______________________________

Once you've made your changes, recompile the HTML files by running ``make html`` again from the parent directory (``docs``), where the ``make.bat`` file is located:

.. code-block:: bash

    make html

This will regenerate the HTML files with your latest modifications.

5. Commit and Push Changes
__________________________

After confirming your changes are reflected in the compiled HTML, it's time to commit and push your changes to the repository. For detailed instructions on how to commit and push changes, see see `Getting Started with Git and GitHub <#getting-started-with-git-and-github>`_.
