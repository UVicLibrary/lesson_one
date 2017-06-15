input_filename = 'input.txt'
output_filename = 'output.txt'

# store contents of input file in string named "original_file_contents"
with open(input_filename, 'r') as f:
    original_file_contents = f.read()

modified_file_contents = ""
#---------------------
# write code here
#---------------------




#---------------------
#
#---------------------

# write the string "modified_file_contents" to output file
with open(output_filename, 'w') as f:
    f.write(modified_file_contents)