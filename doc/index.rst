Welcome to FuturGrid Systems Scripts
=========================================

Systems Scripts
  * A project to create a SLURM based cluster in your cloud and run MPI jobs on it
  * Documentation: http://futuregrid.github.com/systems
  * Source: https://github.com/futuregrid/systems
  * Issues: https://github.com/futuregrid/systems/issues

Finding Projects for a user
===========================

fg-user-project-info.py

* Script to get user project info



To install, put the .py file and the FGLdapCacert.pem in the same directory.
By default it points to the FG master ldap to retrieve the project/group info. 
To use a different ldap, put such content in a file named futuregrid.cfg also 
in the same directory::

        [LDAP]
        LDAPHOST=im3r.idp.iu.futuregrid.org

* To run, python 2.7 and ldap module is required. On india, 'module load python_w-cmd2' will set the environment properly.
* To integrate the functionality into another python program, just grab everything but the main() function, and call getuserProjs() from within your program.

.. toctree::
   :maxdepth: 2

.. todo   intro

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

