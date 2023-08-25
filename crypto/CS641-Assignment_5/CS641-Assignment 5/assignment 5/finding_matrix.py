from pyfinite import ffield
F = ffield.FField(7)

def MatrixMultiplication(A,v):
    rows = 8
    cols = 8
    # v will have the same number of rows and only single column
    ans = [0,0,0,0,0,0,0,0]
    for i in range(rows):
        for j in range(cols):
            ans[i] = Add(ans[i], Multiply(v[j], A[i][j]))
    return ans

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

def E(p,e):
    for i in range(8): 
        p[i] = Expo(p[i], e[i])
    return p

def EAEAE(A,e,p):
    c = []
    for i in range(len(p)):
        c.append(p[i])
    c = E(c,e)
    c = MatrixMultiplication(A,c)
    c = E(c,e)
    c = MatrixMultiplication(A,c)
    c = E(c,e)
    return c



A = [[84, 0, 0, 0, 0, 0, 0, 0],
[119, 70, 0, 0, 0, 0, 0, 0],
[0, 30, 43, 0, 0, 0, 0, 0],
[0, 0, 7, 12, 0, 0, 0, 0],
[0, 0, 0, 118, 112, 0, 0, 0],
[0, 0, 0, 0, 96, 11, 0, 0],
[0, 0, 0, 0, 0, 89, 27, 0],
[0, 0, 0, 0, 0, 0, 28, 38]]

exponents = [23, 118, 38, 76, 93, 47, 24, 23]

plaintexts = open("refined_input.txt", "r")
ciphers = open("refined_output.txt", "r")

inputs = []
outputs = []

for _ in range(8):
    inputs.append(plaintexts.readline().split())
    outputs.append(ciphers.readline().split())

plaintexts.close()
ciphers.close()

for off_d in range(2,8):
    for c in range(8-off_d):
        i = c + off_d
        ins = [16*(ord(inputs[c][j][2*c]) - ord('f')) + (ord(inputs[c][j][2*c+1]) - ord('f')) for j in range(128)]
        outs = [16*(ord(outputs[c][j][2*(i)]) - ord('f')) + (ord(outputs[c][j][2*(i)+1]) - ord('f')) for j in range(128)]
        for k in range(1,128):
            A[i][c] = k
            f = 1
            for index, (x, y) in enumerate(zip(ins, outs)):
                p = [0,0,0,0,0,0,0,0]
                p[c] = x
                cipher = EAEAE(A,exponents,p)
                if y != cipher[i]:
                    f = 0
                    A[i][c] = 0
                    break 
            if f:
                A[i][c] = k
                break



print(A)
print(exponents)