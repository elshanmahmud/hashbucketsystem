import sys 

# this block checks passed arguements  
if len(sys.argv)!=3:
    print("Enter arguements n and s correctly pls")
    sys.exit()

try:
    n = int(sys.argv[1])
    s = int(sys.argv[2])
except ValueError:
    print("n and s must be numbers")

if(n<0 or s<0):
    print("n or s cannot be less that 0")
    sys.exit()