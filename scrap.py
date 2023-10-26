import subprocess

def test(binPerm, intPerm):
    # Define the Bash command you want to run
    bash_command = "gcc -o bitToInt bitToInt.c\n ./bitToInt "+str(binPerm)

    # Run the Bash command
    completed_process = subprocess.run(bash_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check the return code to see if the command was successful
    if completed_process.returncode == 0:
        print("Bash command executed successfully")
        # Print the command's standard output
        print("Command output:")
        print(completed_process.stdout, str(binPerm), str(intPerm))
    else:
        print(f"Error executing the Bash command. Return code: {completed_process.returncode}")
        # Print the command's standard error
        print("Error output:")
        print(completed_process.stderr)


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

binPerms.sort()
#Generate Test Cases for Bash Script
permLen = len(binPerms)
for i in range(permLen):
    test(binPerms[i], intPerms[i])




