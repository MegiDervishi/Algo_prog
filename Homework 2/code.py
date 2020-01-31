#alfo
import math

#Exercise 1
def coinchange(amount, D):
    n = amount + 1
    tab = [n]*n #dp table with length n and entry n
    tab[0] = 0 #initialize at 0 as 0 coins require 0 change
    bestcoins = [0]*n #array stores the optimal coins
    
    #subproblems:
    #  find optimal number of coins/type of coins used
    #  for each amount (i) from 1 to n 
    for i in range(1,amount+1):
        c = 0  
        for k in range(len(D)):
            #
            if tab[i] > tab[i-D[k]]+1:
                c = D[k] #min d_k
                tab[i] = tab[i-D[k]]+1;
        bestcoins[i] = c

    if tab[amount] > amount: return "No change"
    
    result = []
    i = amount
    while i > 0:
        result.append(bestcoins[i])
        i -= bestcoins[i]
    return result



#Exercise 3
def mergeTwoArrays(A, B):
    C = []
    i, j  = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        elif A[i] == B[j]:
            C.append(A[i])
            C.append(B[j])
            i += 1
            j += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        for k in range (i, len(A)):
            C.append(A[k])
    if j < len(B):
        for k in range (j, len(B)):
            C.append(B[k])
    return C

#Exercise 5
def searchMatrix(A, x):
    #Your code goes here
    i = 0
    j =-1
    n = len(A)
    if n == 1 and (A[0] == x or A[0] == [x]): return True
    elif n == 1 and (A[0] != x or A[0] != [x]): return False
    else:
        while i < n and j > -n-1:
            if A[i][j] < x:
                i += 1
            elif A[i][j] > x:
                j -= 1
            else:
                return True
        return False

#A = [[-1,1,2,3],[3,5,6,15],[4,6,7,19],[5,10,15,20]]

#Exercise 4
def subsequence(S, T):
    m, n= len(T), len(S)
    tab = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(m):
        if S[n-1] == T[i]: tab[n-1][i] = 1
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            tab[j][i] += tab[j][i+1]
            if T[i] == S[j]:
                tab[j][i] += tab[j+1][i+1]
            #print(tab)
    return tab[0][0]



def trial(S,T):
    m = len(S)
    n = len(T)
    tab = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n):
        if S[m-1] == T[i]: tab[m-1][i] = 1
    for t in range(n-1,-1,-1):
        for s in range(m-1,-1,-1):
            tab[s][t] += tab[t+1][s]
            if T[s] == S[t]:
                tab[s][t] += tab[t+1][s+1]
    



S = "rabbbit"
T = "rabbit"






