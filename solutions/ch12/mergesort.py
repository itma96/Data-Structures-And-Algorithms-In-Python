def merge(S1, S2):
    S = [None] * (len(S1) + len(S2))
    i = j = k = 0
    while i < len(S1) and j < len(S2):
        if S1[i] < S2[j]:
            S[k] = S1[i]
            i += 1
        else:
            S[k] = S2[j]
            j += 1

        k += 1

    while i < len(S1):
        S[k] = S1[i]
        i += 1
        k += 1

    while j < len(S2):
        S[k] = S2[j]
        j += 1
        k += 1

    return S

def mergesort(S):
    n = len(S)
    if n < 2:
        return S
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    S1 = mergesort(S1)
    S2 = mergesort(S2)
    
    return merge(S1, S2)

S = [1, 7, 2, 4, 6, 11, 8, 9, 13, 10, 3, 4]
print(mergesort(S))