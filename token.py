import re
import sys
import os

fileHandle = open(sys.argv[1])

allLines = fileHandle.readlines();
#print allLines

for l in allLines:
    m = re.search("(\s|\"|\'|^|\A)AK[A-Z0-9]{18}(\s|\"|\'|$|\z)", l);
    if m:
        #print "access : %s" % m;
        #print l
        sys.stderr.write ('Access key ID found \n')
        sys.exit(1)
    p = re.search("(\s|\"|'|^)[a-zA-Z0-9~@#$^*()_+=\/[\]{}|\\,.?:-]{40}(\s|\"|'|$|\z)",l);
    if p:
        #print "secret : %s" % p;
        #print l;
        sys.stderr.write ('Secret Access key found \n')
        sys.exit(1)
    r = re.search("(\s|\"|'|^)[a-zA-Z0-9]{64}(\s|\"|'|$|\z)",l);
    if r:
        #print "token : %s" % r;
        #print l;
        sys.stderr.write ('Digital ocean token \n')
        sys.exit(1)