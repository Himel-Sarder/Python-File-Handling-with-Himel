#




























def reverse_lines(InputFile, output_file):
    with open(InputFile, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            reversed_line = line.strip()[::-1]
            outfile.write(reversed_line + '\n')

# Example usage:
input_file = '../Containers/Practise_container3.txt'
output_file = '../Output/ReversedOutput.txt'
reverse_lines(input_file, output_file)
print("Reversed lines written to", output_file)