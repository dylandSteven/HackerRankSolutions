strs = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = tuple(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    lista=list(anagrams.values())
    lista=sorted(lista, key=lambda x: (len(x),x[0]))
    return lista
print(group_anagrams(strs))