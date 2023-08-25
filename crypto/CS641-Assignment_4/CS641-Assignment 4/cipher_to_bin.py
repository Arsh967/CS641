def map_to_number(char):
    """Maps a character to its corresponding number."""
    # Define the mapping from characters to numbers
    mapping = {'f': 0, 'g': 1, 'h': 2, 'i': 3, 'j': 4, 'k': 5, 'l': 6, 'm': 7,
               'n': 8, 'o': 9, 'p': 10, 'q': 11, 'r': 12, 's': 13, 't': 14, 'u': 15}
    return mapping[char]

with open('crypto/cipher_pairs.txt', 'r') as f:
    input_strings = f.readlines()

with open('crypto/cipher_to_bin.txt', 'w') as f:
    for input_string in input_strings:
        # Remove any leading/trailing whitespace characters
        input_string = input_string.strip()

        # Map each character to its corresponding number
        numbers = [map_to_number(c) for c in input_string]

        # Convert the list of numbers to a binary string with a length of 64 bits
        binary_string = ''.join(format(num, '04b') for num in numbers)
        binary_string = binary_string.zfill(64)  # zero-pad on the left if necessary

        # Print the binary string for this input string
        f.write(f"{binary_string}\n")
