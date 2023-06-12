import sys
import os
import glob

print(sys.argv)
op = 5
def aa():
    print(op)
    # op = 6 eroare
aa()

x = 0

print(os.name) # Windows NT
print(os.getcwd())
print(dir()) # toate modulele, var cu care lucram

temp = glob.glob("*.py")
print(temp)
if len(temp) >= 1:
    a = 1
    # citim din fisier
else:
    a = 2
    # creem un fisier nou

sys.exit(0)
print("200")