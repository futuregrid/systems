Welcome to FuturGrid Systems Scripts
=========================================

Systems Scripts
  * Documentation: http://futuregrid.github.com/systems
  * Source: https://github.com/futuregrid/systems
  * Issues: https://github.com/futuregrid/systems/issues

Script to list the projects or full name of a user
======================

Script Name::

   fg-user-project-info.py

To install this script, please, put the .py file and the FGLdapCacert.pem in the same directory.

    By default it points to the FG master ldap to retrieve the project/group info. To use a different ldap, put such content in a file named futuregrid.cfg also in the same directory::

    [LDAP]
    LDAPHOST=im3r.idp.iu.futuregrid.org

To run, python 2.7 and ldap module is required. On india, 'module load python_w-cmd2' will set the environment properly.

To integrate the functionality into another python program, just grab everything but the main() function, and call getuserProjs() from within your program.

Known Bugs and Feature Requests
=====================

* we do not yet have a setup.p script
* flags such as -txt, -html -JSON need to be added

.. toctree::
   :maxdepth: 2

.. todo   intro

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

