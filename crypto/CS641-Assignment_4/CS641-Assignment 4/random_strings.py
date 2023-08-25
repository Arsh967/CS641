import random

# Open a file for writing
with open("crypto/random_strings.txt", "w") as f:
    # Generate 100000 random strings of 64 bits and write them to the file
    for i in range(10000):
        # Generate a random 64-bit string
        rand_str = "".join([str(random.randint(0, 1)) for j in range(64)])
        # Write the string to the file, followed by a newline character
        f.write(rand_str + "\n")
