.. _git-tips:

GIT tips
========

If you are new to Git and GitHub, this page helps you getting started by explaining
how to make some modification to a repository. The explaining assumes that you
are trying to modify this website, but it should work for most repositories.

1. Set Up Your SSH Key
______________________

To securely connect with GitHub, you'll need to add your SSH key to your GitHub
account. |public_key|, you can find how to add your public key to your account.

.. |public_key| raw:: html

    <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account" target="_blank">here</a>

2. Clone a GitHub Repository
____________________________

If you are not a member of the `psm-compute` organization, fork
the repository (i.e. create a duplicate of the repository in your own GitHub account),
then clone it (see below).

If you are a member, natigate to the |repository|, click on `Code`, then copy
the `SSH` link and clone the repository using  :code:`git clone` : 

.. |repository| raw:: html

   <a href="https://github.com/psm-compute/psm-compute.github.io" target="_blank">here</a>

.. code:: bash

    git clone git@github.com:psm-compute/psm-compute.github.io.git

This command will create a local copy of the repository on your computer.

3. Check the Status of Your Repository
______________________________________

From you computer, when you start making modifications to the files, it's a
you can check the status of your repository to see if there are any changes:

.. code:: bash

    git status

4. Create and Switch to a New Branch
____________________________________

To make changes without affecting the main branch, create a new branch:

.. code:: bash

    git branch update_readme

and then, switch to the new branch:

.. code:: bash

    git checkout update_readme

5. Edit Files and Stage Changes
_______________________________

Make the necessary edits to the files. For example, to edit the `README.md` file,
use a text editor like `vi`:

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

    git commit -m "Modified the README.md file"

Next, push your changes to GitHub:

.. code:: bash

    git push

If it's the first time you're pushing from this branch, you'll need to set the
upstream branch:

.. code:: bash

    git push --set-upstream origin update_readme

7. Create a Pull Request
________________________

Finally, open your web browser and navigate to the GitHub repository (|repository|): 
After pushing your changes, you should see a message indicating the recent
pushes. Click on **"Compare & pull request"**. On the right side of the page,
select your reviewers, and add a description if needed. This will create a pull
request for your changes to be reviewed and merged.

8. Delete the Branch Locally (Optional)
_______________________________________

Once your changes are merged with the main branch, and if you no longer need the
branch locally, you can delete it:

.. code:: bash

    git branch -d update_readme
