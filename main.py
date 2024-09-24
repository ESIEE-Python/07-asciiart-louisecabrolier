"""
ASCII
"""
def artcode_i(s):
    """
    entrée:s la chaine de caractère à encoder
    sortie:liste de tuples encodant une chaîne de caractères passée en argument
    itératif
    """
    if not s:
        return []
    # Initialisation
    c = [s[0]]
    o = [1]
    n = len(s)
    for k in range(1, n):
        if s[k] == s[k - 1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)
    return list(zip(c, o))

def artcode_r(s):
    """
    entrée: s
    sortie:liste de tuples encodant une chaîne de caractères
    récursif
    """
    if not s:
        return []
    def count_consecutive(s: str, char: str, index: int = 0):
        if index < len(s) and s[index] == char:
            return 1 + count_consecutive(s, char, index + 1)
        return 0
    count = count_consecutive(s, s[0])
    return [(s[0], count)] + artcode_r(s[count:])

def main():
    """
    entrée:une chaine de caractère
    sortie:le programme appliqué
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
