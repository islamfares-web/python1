import copy
L = [[1, 1], [1, 0]]
def matrixmult(l1, l2):
    l = [] #seting up an empty list
    lt = [] # temp list
    t = 0 # temp
    for i in range(len(l1)): # like given to make a 2 x 2 matrix
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                t += l1[i][k] * l2[j][k]
            lt.append(t)
            t = 0 # resting temp
        l.append(lt)
        lt = [] # resting temp
    return l


def matrixpower(L, n):
    if n == 0:
        return [[1, 0], [0, 0]]
    if n == 1:
        return L
    elif n % 2 == 0: #even
        return matrixpower(matrixmult(copy.deepcopy(L), copy.deepcopy(L)), n // 2)#using deep copy since we hav lists inside losts
    else:
        return matrixmult(matrixpower(copy.deepcopy(L), n - 1), copy.deepcopy(L))


def fibMatrixVersion(n):# odd
    l = matrixpower(L, n)
    return l[1][0]


for i in range(11):
    print("F_", i, ":", fibMatrixVersion(i))
print("F_ 100 :", fibMatrixVersion(100))


# I didnt know how to solve this alone and some help beacuse I didnt fully understand how to creat the 2x2 matrix