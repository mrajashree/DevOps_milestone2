import sys

fhandle = open(sys.argv[1])

count = 0
code = 0
comment1 = '//'
comment2 = '/*'
comment3 = '*/'
flag = 0

for line in fhandle:
    if comment1 in line:
        count = count + 1;
        
    elif comment2 in line:
        count = count + 1;
        flag = 1;
    
    elif comment3 in line:
        count+=1
        flag = 0;
        
    else:
        if flag==1:
            count+=1
        else:
            code = code + 1;

print ("Comments:Code = %d:%d\n" % (count,code))

ratio = count/code
if(ratio > 2):
    sys.stderr.write("Cannot exceed defined comment:code ratio\n")
    sys.exit(-1)