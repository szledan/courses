import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

file=open(sys.argv[1],'r')
Lines=file.readlines()
count=0
for line in Lines:
    count+=1
    print("Line{}: {}".format(count,line.strip()))
