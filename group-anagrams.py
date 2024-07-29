strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(arr):
    anagrams = {}

    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []

        anagrams[sorted_str].append(str)

    return list(anagrams.values())


print(group_anagrams(strs))
