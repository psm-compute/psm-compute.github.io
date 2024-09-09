.. _git-tips:

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

8. Create a Pull Request
________________________

Finally, open your web browser and navigate to the GitHub page for this project: 

`<https://github.com/psm-compute/psm-compute.github.io>`_

After pushing your changes, you should see a message indicating the recent pushes. Click on **"Compare & pull request"**.

On the right side of the page, select your reviewers, and add a description if needed. This will create a pull request for your changes to be reviewed and merged.


7. Delete the Branch Locally (Optional)
_______________________________________

If you no longer need the branch locally, you can delete it:

.. code:: bash

    git branch -d update_readme
