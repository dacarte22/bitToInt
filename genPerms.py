import subprocess

#Generate test cases of 8 bit values
def bit_permutations(n):
    if not n:
        return

    for i in range(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s

        yield s
#Function Call
binPerms = list(bit_permutations(8))
intPerms = list()
for p in binPerms:
    intPerms.append(int(str(p), 2))


#Sort input and correct output
dic = {}


#Generate Test Cases for Bash Script
permLen = len(binPerms)
#for i in range(0, permLen):
    #print("./binToInt", binPerms[i], intPerms,  "> testResults.txt")
    


script_file_name = "binsToTest.txt"
with open(script_file_name, "w") as testScript:
    #testScript.write("#!/bin/bash\n")
    #testScript.write("gcc -o bitToInt bitToInt.c\n")
    for p in binPerms:
        #testScript.write("bitToInt./ "+str(p)+" > testResults.txt\n")
        testScript.write(str(p)+"\n")

with open("test.sh", "w") as script:
    script.write("#!/bin/bash\n")
    script.write("gcc -o bitToInt bitToInt.c\n")
    for p in binPerms:
        script.write("./bitToInt "+str(p)+"\n")   #+" > testResults.txt\n")
        #testScript.write(str(p)+"\n")



file_name = "intSolutions.txt"
with open(file_name, "w") as file:
    # Write text to the file
    for p in intPerms:
        file.write(str(p)+"\n")


bash_command = "ls -l"

# Run the Bash command
completed_process = subprocess.run(bash_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
