systems
=======

place to share system related scripts

* Script to get user project info:
fg-user-project-info.py

** To install, put the .py file and the FGLdapCacert.pem in the same directory.
*** By default it pointed to the FG master ldap to retrieve the project/group info. To use a different ldap, put such content in a file named futuregrid.cfg also in the same directory:

[LDAP]
LDAPHOST=im3r.idp.iu.futuregrid.org

** To run, python 2.7 and ldap module is needed. On india, 'module load python_w-cmd2' will set the environment properly.
** To integrate the functionality into another python program, just grab everything but the main() function, and call getuserProjs() from within your program.