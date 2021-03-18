import sys
file=open(sys.argv[1], 'r')
Lines=file.readlines()
file.close()
for line in Lines:
    if line.strip()=="":
        continue
    num=float(line.strip())
    isprime="1"
    if num<1:
        isprime="-"
    elif num/int(num)!=1:
        isprime="-"
    elif num==1:
        isprime="0"
    elif num==2:
        isprime="1"
    elif num %2==0:
        isprime="0"
    else:
        guard=num/2
        for n in range(3, int(guard), 2):
            if num %n==0:
                isprime="0"
                break
    print("{} {}".format(num, isprime))
