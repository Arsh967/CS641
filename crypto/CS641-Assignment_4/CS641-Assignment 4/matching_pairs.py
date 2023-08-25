import binascii

alpha_map = {
    0: 'f', 1: 'g', 2: 'h', 3: 'i', 4: 'j', 5: 'k', 6: 'l', 7: 'm',
    8: 'n', 9: 'o', 10: 'p', 11: 'q', 12: 'r', 13: 's', 14: 't', 15: 'u'
}

# Open the file containing random strings
with open('crypto/random_strings.txt', 'r') as f:
    random_strings = f.readlines()


# Open a new file to store the pairs whose XOR is 0000902010005000
with open('crypto/matching_pairs.txt', 'w') as f:
    # Iterate through all pairs of random strings
    for i in range(len(random_strings)):
        for j in range(i+1, len(random_strings)):
            # Convert the strings to binary and perform XOR
            bin_i = random_strings[i]
            bin_j = random_strings[j]
            xor = int(bin_i,2)^int(bin_j,2)
            #print(xor)
            # Check if the XOR is equal to 0x0000902010005000
            if xor == 0x0000902010005000:
                #print('hehe')
                # Convert the pairs to ASCII and write them to file
                alphabets = ''
                for i in range(0, len(bin_i), 4):
                    if bin_i[i]=='\n':
                        break
                    bits = bin_i[i:i+4]  # Extract 4 bits
                    num = int(bits, 2)     # Convert to integer
                    alpha = alpha_map[num] # Map to alphabet
                    alphabets += alpha      # Append to result string
                f.write(f"{alphabets}\n")
                alphabets = ''
                for i in range(0, len(bin_j), 4):
                    if bin_j[i]=='\n':
                        break
                    bits = bin_j[i:i+4]  # Extract 4 bits
                    num = int(bits, 2)     # Convert to integer
                    alpha = alpha_map[num] # Map to alphabet
                    alphabets += alpha      # Append to result string
                f.write(f"{alphabets}\n")
