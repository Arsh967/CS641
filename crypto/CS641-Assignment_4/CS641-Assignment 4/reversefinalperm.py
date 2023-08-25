#Ciphertext's reverse final permutation
#takes cipher_to_bin.txt as input and gives reversefinalperm.txt as output
#reverse final permutation is initial permutation

def initial_permutation(block):     #64-bit input
    """
    Performs initial permutation on the given 64-bit block.
    """
    permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
                         60, 52, 44, 36, 28, 20, 12, 4,
                         62, 54, 46, 38, 30, 22, 14, 6,
                         64, 56, 48, 40, 32, 24, 16, 8,
                         57, 49, 41, 33, 25, 17, 9, 1,
                         59, 51, 43, 35, 27, 19, 11, 3,
                         61, 53, 45, 37, 29, 21, 13, 5,
                         63, 55, 47, 39, 31, 23, 15, 7]
    permuted_block = ''
    for i in permutation_table:
        permuted_block += block[i-1]
    return permuted_block

with open('crypto/cipher_to_bin.txt', 'r') as f:
    bin_cipher = f.readlines()

with open('crypto/reversefinalperm.txt', 'w') as f:
    for i in range(len(bin_cipher)):
        f.write(f"{initial_permutation(bin_cipher[i])}\n")

