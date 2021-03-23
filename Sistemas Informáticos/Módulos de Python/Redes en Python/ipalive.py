import subprocess
import os
import sys

ipRange = sys.argv[1]

firstIpOfRange = list(map(int, ipRange.split("-")[0].split(".")))
secondIpOfRange = list(map(int, ipRange.split("-")[1].split(".")))

def checkRange():
    if os.name == 'nt': # Windows
        if str("mil") in str(subprocess.Popen(["ping", '.'.join([str(elem) for elem in firstIpOfRange]), "-n", "1"],stdout=subprocess.PIPE).stdout.read()): # If ping response contains string "mil", short for milli-seconds or milisegundos
            print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
        else:
            print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
    else: # Any OS but Windows (Unix)
        if  os.system("ping -q -c 1 " + '.'.join([str(elem) for elem in firstIpOfRange]) + " > /dev/null 2>&1") == 0:
            print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
        else:
            print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))



def execCheckRange():
    if firstIpOfRange[0] == secondIpOfRange[0] and firstIpOfRange[1] == secondIpOfRange[1] and firstIpOfRange[2] == secondIpOfRange[2]:
        for i in range(firstIpOfRange[3], secondIpOfRange[3]):
            checkRange()
            firstIpOfRange[3] += 1

    elif firstIpOfRange[0] == secondIpOfRange[0] and firstIpOfRange[1] == secondIpOfRange[1] and firstIpOfRange[2] < secondIpOfRange[2]:
        for i in range(firstIpOfRange[3], 256):
            checkRange()
            firstIpOfRange[3] += 1
        firstIpOfRange[3] = 0
        firstIpOfRange[2] += 1

        for i in range(firstIpOfRange[3], secondIpOfRange[3]):
            checkRange()
            firstIpOfRange[3] += 1





# ESTO ES SAGRAO
##### if firstIpOfRange[0] == secondIpOfRange[0] and firstIpOfRange[1] == secondIpOfRange[1] and firstIpOfRange[2] == secondIpOfRange[2]:
#####     if os.name == 'nt': # Windows
#####         if str("mil") in str(subprocess.Popen(["ping", '.'.join([str(elem) for elem in firstIpOfRange]), "-n", "1"],stdout=subprocess.PIPE).stdout.read()): # If ping response contains string "mil", short for milli-seconds or milisegundos
#####             print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####         else:
#####             print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####     else: # Any OS but Windows (Unix)
#####         if  os.system("ping -q -c 1 " + '.'.join([str(elem) for elem in firstIpOfRange]) + " > /dev/null 2>&1") == 0:
#####             print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####         else:
#####             print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####         
#####     firstIpOfRange[3] += 1
##### 
##### elif firstIpOfRange[0] == secondIpOfRange[0] and firstIpOfRange[1] == secondIpOfRange[1] and firstIpOfRange[2] < secondIpOfRange[2]:
#####     for i in range(firstIpOfRange[3], 256):
#####             if os.name == 'nt': # Windows
#####                 if str("mil") in str(subprocess.Popen(["ping", '.'.join([str(elem) for elem in firstIpOfRange]), "-n", "1"],stdout=subprocess.PIPE).stdout.read()): # If ping response contains string "mil", short for milli-seconds or milisegundos
#####                     print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####                 else:
#####                     print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####             else: # Any OS but Windows (Unix)
#####                 if  os.system("ping -q -c 1 " + '.'.join([str(elem) for elem in firstIpOfRange]) + " > /dev/null 2>&1") == 0:
#####                     print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####                 else:
#####                     print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
##### 
#####             firstIpOfRange[3] += 1
#####     
#####     firstIpOfRange[3] = 0
#####     firstIpOfRange[2] += 1
##### 
#####     for i in range(firstIpOfRange[3], secondIpOfRange[3]):
#####         if os.name == 'nt': # Windows
#####             if str("mil") in str(subprocess.Popen(["ping", '.'.join([str(elem) for elem in firstIpOfRange]), "-n", "1"],stdout=subprocess.PIPE).stdout.read()): # If ping response contains string "mil", short for milli-seconds or milisegundos
#####                 print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####             else:
#####                 print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####         else: # Any OS but Windows (Unix)
#####             if  os.system("ping -q -c 1 " + '.'.join([str(elem) for elem in firstIpOfRange]) + " > /dev/null 2>&1") == 0:
#####                 print("IP {} is up.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####             else:
#####                 print("IP {} is down.".format('.'.join([str(elem) for elem in firstIpOfRange])))
#####         
#####         firstIpOfRange[3] += 1
# FIN DE LO SAGRAO