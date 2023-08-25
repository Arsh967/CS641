#takes input as reversefinalperm.txt
#gives output as alphaxor.txt which is xor value of pair before Sbox and after key
#gives output as betaxor.txt which is xor value of pair after Sbox and before roundpermutation
##gives output as gamma.txt which pair before key and after expansion

import random
prob = 0.000381 

def expansion(R):       #32-bit input
    E = [R[31], R[0], R[1], R[2], R[3], R[4],
         R[3], R[4], R[5], R[6], R[7], R[8],
         R[7], R[8], R[9], R[10], R[11], R[12],
         R[11], R[12], R[13], R[14], R[15], R[16],
         R[15], R[16], R[17], R[18], R[19], R[20],
         R[19], R[20], R[21], R[22], R[23], R[24],
         R[23], R[24], R[25], R[26], R[27], R[28],
         R[27], R[28], R[29], R[30], R[31], R[0]]
    expanded = ''
    for i in E:
        expanded = expanded + i
    return expanded

def permutate(R):       #32-bit input
    E = [R[8], R[16], R[22], R[30], 
         R[12], R[27], R[1], R[17], 
         R[23], R[15], R[29], R[5],
         R[25], R[19], R[9], R[0], 
         R[7], R[13],  R[24], R[2], 
         R[3], R[28], R[10], R[18],
         R[31], R[11], R[21], R[6], 
         R[4], R[26], R[14], R[20]]
    permute = ''
    for i in E:
        permute = permute + i
    return permute

def bitwise_xor(bin_str1, bin_str2):
    """Returns the bitwise XOR of two binary strings"""
    # Make sure both binary strings have the same length
    if len(bin_str1) != len(bin_str2):
        raise ValueError("Both binary strings should have the same length")
    
    # Convert binary strings to lists of bits
    bits1 = [int(bit) for bit in bin_str1]
    bits2 = [int(bit) for bit in bin_str2]
    
    # Perform bitwise XOR on the bits
    xor_bits = [bits1[i] ^ bits2[i] for i in range(len(bits1))]
    
    # Convert the resulting list of bits back to a string
    xor_str = ''.join([str(bit) for bit in xor_bits])
    
    return xor_str

def hex_to_bin(hex_str):
    binary_str = bin(int(hex_str, 16))[2:]
    return binary_str.zfill(32)

with open('crypto/reversefinalperm.txt', 'r') as f:
    ciphertext = f.readlines()
    
for i in range(0, len(ciphertext), 2):
    c1 = ciphertext[i].strip()
    c2 = ciphertext[i+1].strip()
    # process num1 and num2 here
    lc1 = c1[:32]
    rc1 = c1[32:]
    lc2 = c2[:32]
    rc2 = c2[32:]
    with open('crypto/gamma.txt', 'w') as f:
        f.write(f"{expansion(lc1)}\n")
        f.write(f"{expansion(lc2)}\n")
    with open('crypto/alphaxor.txt', 'w') as f:
        f.write(f"{bitwise_xor(expansion(lc1),expansion(lc2))}\n")
    with open('crypto/betaxor.txt', 'w') as f:
        if random.random() < prob:
            l5 = 0x04000000
        else:
            l5 = random.randint(0, 0xFFFFFFFF)
        l5_bin = bin(l5)[2:].zfill(32)
        xor1 = bitwise_xor(l5_bin,rc1)
        if random.random() < prob:
            l5 = 0x04000000
        else:
            l5 = random.randint(0, 0xFFFFFFFF)
        l5_bin = bin(l5)[2:].zfill(32)
        xor2 = bitwise_xor(l5_bin,rc2)
        xor = bitwise_xor(xor1,xor2)
        f.write(f"{permutate(xor)}\n")



    



