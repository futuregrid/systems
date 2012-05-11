Documentation of the Systems scripts
==============

### CLI tool to get user project info:

* Accessing to LDAP is done via anonymous binding, however the server is firewalled. It should work only from within FG domain.
* The FG LDAP server ssl certificate is a self-signed one, and the ca certificate file 'FGLdapCacert.pem' is distributed together with the script.
* Python ldap module is required.
* Python 2.7 is recommended. For 2.6, manually install argparse module should be fine too.

* As an example for set up - in india, put the .py and .pem files together in the same directory, then

       module load python_w-cmd2

will set up the necessary python environment - load python 2.7 and python ldap module.

* To run:

        ./fg-user-project-info.py -u LDAPUID

will print out the project ids;

        ./fg-user-project-info.py -u LDAPUID -t
        
will include also the project title;

        ./fg-user-project-info.py -u LDAPUID -t -l
        
will also include the link to the project url in the portal.

* You could also integrate the functions into your code and manipulate the output directly in python.

See Also:

http://futuregrid.github.com/systems