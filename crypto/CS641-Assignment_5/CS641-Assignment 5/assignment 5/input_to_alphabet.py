import binascii

alpha_map = {
    0: 'f', 1: 'g', 2: 'h', 3: 'i', 4: 'j', 5: 'k', 6: 'l', 7: 'm',
    8: 'n', 9: 'o', 10: 'p', 11: 'q', 12: 'r', 13: 's', 14: 't', 15: 'u'
}

with open("input.txt", "r") as f:
    for line in f:
        nums = line.strip().split()
        decimal_num = int(nums[0])
        binary_num = bin(decimal_num)[2:].zfill(8)
        #print(binary_num)

with open("input.txt", "r") as f, open("bin_input.txt", "w") as out:
    for line in f:
        nums = line.strip().split()
        for i in range(8):
            decimal_num = int(nums[i])
            binary_num = bin(decimal_num)[2:].zfill(8)
            out.write(binary_num + " ")
        out.write("\n")

with open('bin_input.txt', 'r') as f:
    bin_input = f.readlines()

with open('alphabet_input.txt', 'w') as f:
    for i in bin_input:
        nums = i.strip().split()
        #print(nums)
        for j in nums:
            left = j[:4]
            right = j[4:]
            left = int(left,2)
            right = int(right,2)
            f.write(alpha_map[left] + alpha_map[right])
        f.write("\n")