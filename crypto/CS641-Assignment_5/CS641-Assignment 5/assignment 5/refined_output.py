with open("output.txt", 'r') as input_file, open("refined_output.txt", 'w') as output_file:
    # Read strings from input file in groups of 127
    strings = []
    for line in input_file:
        strings.append(line.strip())
        if len(strings)%128 == 0:
            output_file.write(' '.join(strings) + '\n')
            strings = []
    
    # Write any remaining strings to output file
    if strings:
        output_file.write(' '.join(strings) + '\n')