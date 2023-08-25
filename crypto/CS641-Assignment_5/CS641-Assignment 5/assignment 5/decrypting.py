from pyfinite import ffield
F = ffield.FField(7)

def to_encoding(v):
    ans = ""
    for i in range(8):
        bin_str = format(v[i], '0>8b')
        char1 = chr(ord('f') + int(bin_str[:4],2))
        char2 = chr(ord('f') + int(bin_str[4:],2))
        ans += char1
        ans += char2
    return ans

def to_ascii(v):
    ans = ""
    for i in range(8):
        ans += chr(v[i])
    return ans

def make_vector(p):
    vec = []
    for i in range(8):
        vec.append(16*(ord(p[2*i]) - ord('f')) + (ord(p[2*i+1]) - ord('f')))
    return vec

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

A = [[84, 0, 0, 0, 0, 0, 0, 0], [119, 70, 0, 0, 0, 0, 0, 0], [14, 30, 43, 0, 0, 0, 0, 0], [97, 17, 7, 12, 0, 0, 0, 0], [99, 35, 13, 118, 112, 0, 0, 0], [24, 48, 29, 32, 96, 11, 0, 0], [9, 124, 20, 103, 30, 89, 27, 0], [3, 15, 87, 23, 20, 67, 28, 38]]

exponents =[23, 118, 38, 76, 93, 47, 24, 23]

cipher = "msjjkrhffnfmhqfrgthtmghjhkfsghkq"

cipher1 = cipher[:16]
cipher2 = cipher[16:]

out1 = make_vector(cipher1)
out2 = make_vector(cipher2)

p = [0 for _ in range(8)]
q = [0 for _ in range(8)]

for i in range(8):
    for j in range(1,128):
        p[i] = j
        x = EAEAE(A, exponents, p)
        if x[i] == out1[i]:
            p[i] = j
            break
        else:
            p[i] = 0

for i in range(8):
    for j in range(1,128):
        q[i] = j
        x = EAEAE(A, exponents, q)
        if x[i] == out2[i]:
            q[i] = j
            break
        else:
            q[i] = 0
# print(to_encoding(p) + to_encoding(q))
print(p)
print(q)
print(to_ascii(p) + to_ascii(q))

