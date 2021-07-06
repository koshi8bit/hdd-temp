import subprocess
 
process = subprocess.Popen(["sensors"],shell=False,stdout=subprocess.PIPE)
data = process.communicate()    # returns tuple
temp = int(data[0].split()[5][1:3])
print temp