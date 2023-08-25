from pyfinite import ffield
F = ffield.FField(7)

bin_map = {
    'f': '0000', 'g':'0001','h':'0010', 'i':'0011', 'j':'0100', 'k':'0101', 'l':'0110', 'm':'0111',
    'n':'1000', 'o':'1001', 'p':'1010', 'q':'1011', 'r':'1100', 's':'1101', 't':'1110', 'u':'1111'
}

def Expo(a,n):
    if(n==0):
        return 1
    elif(n==1):
        return a
    elif(n%2==0):
        ans = F.Multiply(Expo(a,n/2),Expo(a,n/2))
        return ans 
    else:
        ans = F.Multiply(a, F.Multiply(Expo(a,n//2),Expo(a,n//2)))
        return ans

def Multiply(a,b):
    return F.Multiply(a,b)

def Add(a,b):
    return a ^ b

def formula (x,a,e):
    return pow(a*pow(a*pow(x,e,127),e,127),e,127)


# with open("refine.txt", "r") as f:
#     P = f.readlines()

# with open("output.txt", "r") as f:
#     C = f.readlines()

plaintexts = open("refined_input.txt", "r")
ciphers = open("refined_output.txt", "r")

# A = [[] for _ in range(8)]
# E = [[] for _ in range(8)]

exponents = [[] for i in range(8)]
possible_aii = [[[] for i in range (8)] for j in range(8)]

inputs = []
outputs = []

for i in range(8):
    inputs.append(plaintexts.readline().split())
    outputs.append(ciphers.readline().split())

    ins = [16*(ord(inputs[i][j][2*i]) - ord('f')) + (ord(inputs[i][j][2*i+1]) - ord('f')) for j in range(128)]
    outs = [16*(ord(outputs[i][j][2*i]) - ord('f')) + (ord(outputs[i][j][2*i+1]) - ord('f')) for j in range(128)]

    for j in range(1, 127):
        for k in range(1, 128):
            f = 1
            for x, y in zip(ins, outs):
                if y != Expo(Multiply(Expo(Multiply(Expo(x, j), k), j), k), j):
                    f = 0
                    break 
            if f:
                exponents[i].append(j)
                possible_aii[i][i].append(k)

plaintexts.close()
ciphers.close()

for i in range(7):

    ins = [16*(ord(inputs[i][j][2*i]) - ord('f')) + (ord(inputs[i][j][2*i+1]) - ord('f')) for j in range(128)]
    outs = [16*(ord(outputs[i][j][2*(i+1)]) - ord('f')) + (ord(outputs[i][j][2*(i+1)+1]) - ord('f')) for j in range(128)]

    for j in range(1, 128):
        for exp1, diag1 in zip(exponents[i+1], possible_aii[i+1][i+1]):
            for exp2, diag2 in zip(exponents[i], possible_aii[i][i]):
                f = 1
                for x, y in zip(ins, outs):
                    if y != Expo(Add(Multiply(Expo(Multiply(Expo(x, exp2), diag2), exp2), j), Multiply(Expo(Multiply(Expo(x, exp2), j), exp1), diag1)), exp1):
                        f = 0
                        break
                if f:
                    exponents[i+1] = [exp1]
                    exponents[i] = [exp2]
                    possible_aii[i+1][i+1] = [diag1]
                    possible_aii[i][i] = [diag2]
                    possible_aii[i+1][i] = [j]

print(possible_aii)
print(exponents)

# for z in range(len(P)):
#    p = P[z]
#    c = C[z]
#    for i in range(0, 15, 2):
#        if (p[i] + p[i+1] != "ff"):
#            x = p[i] + p[i+1]
#            y = c[i] + c[i+1]
#            break
#    i = i/2
# #    x_bin = bin_map[x[0]] + bin_map[x[1]]
# #    x_dec = int(x_bin, 2)
#    x_dec = 16*(ord(x[0]) - ord('f')) + (ord(x[1]) - ord('f'))

# #    y_bin = bin_map[y[0]] + bin_map[y[1]]
# #    y_dec = int(y_bin,2)

#    y_dec = 16*(ord(y[0]) - ord('f')) + (ord(y[1]) - ord('f'))
#    for a in range(1,128):
#        for e in range(1,127):
#            f = 1
#            if (y_dec != Expo(Multiply(Expo(Multiply(Expo(x_dec,e),a),e),a),e)):
#                f = 0
#                break
#            if f:
#                A[int(i)].append(a)
#                E[int(i)].append(e)



#formula(x_dec,a,e)


#print(A)
# for j in A:
#     A_dict = dict()
#     l = len(j)
#     for k in range(l-1, -1, -1):
#         if j[k] not in A_dict:
#             A_dict[j[k]] = 1
#         else:
#             del j[k]
    
# for j in E:
#     E_dict = dict()
#     l = len(j)
#     for k in range(l-1, -1, -1):
#         if j[k] not in E_dict:
#             E_dict[j[k]] = 1
#         else:
#             del j[k]
# print(A)
#print(E)



