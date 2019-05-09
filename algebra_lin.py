# -*- coding: utf-8 -*-
"""
Esercizi su matrice per esame di calcolo numerico

"""

import numpy as np
def elleu(A):
    (m,n)=A.shape
    if m!=n:
        print("attenzione: A non e' quadrata")
        E=np.array([])
        return E,E,E
    L=np.eye(n)
    for k in range(0,n-1):
        if A[k,k]==0:
            print("Attenzione: pivot nullo")
            E=np.array([])
            return E,E,E
        for i in range(k+1,n):
            L[i,k]=A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j]=A[i,j]-L[i,k]*A[k,j]
    U=np.triu(A)
    return L,U

def elleu_pp(A):
    (m,n)=A.shape
    if m!=n:
        print("attenzione: A non e' quadrata")
        E=np.array([])
        return E,E,E
    p=np.array(range(0,n))
    for k in range(0,n-1):
        r=abs(A[k:n,k]).argmax()
        r=r+k
        A[[k,r],:]=A[[r,k],:]
        p[[k,r]]=p[[r,k]]
        if A[k,k]==0:
            print("Attenzione: pivot nullo")
            E=np.array([])
            return E,E,E
        for i in range(k+1,n):
            A[i,k]=A[i,k]/A[k,k]
            for j in range(k+1,n):
                A[i,j]=A[i,j]-A[i,k]*A[k,j]
    P=np.eye(n)
    P=P[p,:]
    L=np.tril(A,-1)+np.eye(n)
    U=np.triu(A)
    return P,L,U
