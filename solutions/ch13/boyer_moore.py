def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)
    if m == 0:
        return (-1, 0)

    last = {}
    for i, c in enumerate(P):
        last[c] = i

    i, k = m - 1, m - 1

    comparisons = 0
    while i < n:
        comparisons += 1
        if T[i] == P[k]:
            if k == 0:
                return (i, comparisons)
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return (-1, comparisons)

if __name__ == "__main__":
    print(find_boyer_moore("May i have a word with you", "word"))