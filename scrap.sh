#!/bin/bash



# Check if the input file exists

input_file="binsToTest.txt"
if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' does not exist."
    exit 1
fi

# Check if the program to run is provided




# Read lines from the input file and pass each line as an argument to the program
while IFS= read -r line; do
    ./bitToInt "$line"
done < "$input_file"