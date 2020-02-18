import sys
import subprocess

if len(sys.argv) == 2:
    print('if')
else:
    print('else')

args = sys.argv
commands = ['nslookup', args[1]]

try:
    res = subprocess.check_call(commands)
except:
    print "Error."

print res