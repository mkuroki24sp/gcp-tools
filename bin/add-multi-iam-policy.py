import sys
import ConfigParser
import json
import subprocess

# for check file exists
import os
import errno

config = ConfigParser.ConfigParser()
if not os.path.exists('../config.ini'):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errono.ENOENT), '../config.ini')
config.read('../config.ini')

projects = json.loads(config.get("iam-roles-config","projects"))
roles = json.loads(config.get("iam-roles-config","roles"))

args = sys.argv
for project in projects:
    for role in roles:
        commands = 'gcloud projects add-iam-policy-binding ' + project + ' --member user:' + args[1] + ' --role ' + role
        print(commands)

#try:
#    res = subprocess.check_call(commands)
#except:
#    print "Error."

#print res
