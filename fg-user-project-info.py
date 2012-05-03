#!/usr/bin/env python

import sys
import os
import ConfigParser
import urllib2
import re
import argparse
import ldap

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', dest='user', required=True, help="specify an ldap username/uid")
    parser.add_argument('-t', '--withtitle', dest='withtitle', action="store_true", help="whether to include project title")
    parser.add_argument('-l', '--withlink', dest='withlink', action="store_true", help="whether to include url of the projects")
    args = parser.parse_args()
    user = args.user
    withtitle = args.withtitle
    items = getUserProjs(user, args.withtitle, args.withlink)
    for item in items:
        print item
    
def getUserProjs(user, withtitle=False, withlink=False):
    configfile = "futuregrid.cfg"
    userprojs = dict()
    retprojs = []
    config = ConfigParser.ConfigParser()
    if os.path.isfile(configfile):
        config.read('futuregrid.cfg')
        ldaphost = config.get('LDAP', 'LDAPHOST')
    else:
        ldaphost = "im3r.idp.iu.futuregrid.org"
        
    ldap.set_option(ldap.OPT_X_TLS_CACERTFILE, "FGLdapCacert.pem")
    ldapconn = ldap.initialize("ldap://" + ldaphost)

    try:
        ldapconn.start_tls_s()
        ldapconn.bind_s('', '') # anonymous binding
        ldapbasedn = "dc=futuregrid,dc=org"
        ldapscope = ldap.SCOPE_SUBTREE
        ldapfilter = "(&(objectclass=posixGroup)(cn=fg*))"
        ldapattribs = ['cn', 'memberUid']
        ldapresults = list(ldapconn.search_s(ldapbasedn, ldapscope, ldapfilter, ldapattribs))
        for ldapresult in ldapresults:
            #print ldapresult[1]
            if ldapresult[1].has_key('cn'):
                cn = ldapresult[1]['cn'][0]
                projid = cn[2:]
                #print projid
                if ldapresult[1].has_key('memberUid'):
                    for auid in ldapresult[1]['memberUid']:
                        if userprojs.has_key(auid):
                            userprojs[auid].append(int(projid))
                        else:
                            userprojs[auid] = [int(projid)]

        if userprojs.has_key(user):
            projs = userprojs[user]
            retprojs = projs
            if withtitle:
                retprojs = []
                for aprojid in projs:
                    atitle = getProjTitle(aprojid)
                    aret = str(aprojid) + "." + atitle
                    retprojs.append(aret)
            if withlink:
                tmpretprojs = []
                for projidx in range(len(projs)):
                    linked = '<a href="https://portal.futuregrid.org/project/' + str(projs[projidx]) + '">' + str(retprojs[projidx]) + '</a>'
                    tmpretprojs.append(linked)
                retprojs = tmpretprojs
        else:
            retprojs = []
            print "Error: User Dose Not Exist"
    except:
        print "WRONG" + str(sys.exc_info())
    return retprojs
    
def getProjTitle(pid):
    title = ''
    projurl = "https://portal.futuregrid.org/project/" + str(pid)
    req = urllib2.Request(projurl)
    res = urllib2.urlopen(req)
    content = res.read()
    titleregex = re.compile('.+/projects/' + str(pid) + '">(.+)</a>.+')
    m = titleregex.search(content)
    if m is not None:
        title = m.group(1).strip()
    return title

if __name__ == '__main__':
    main()