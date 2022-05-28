# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    #get the length of the strings
    len_1 = len(word)
    len_2 = len(anagram)

    if len_1 != len_2:
        return False
    
    word = sorted(word)
    anagram = sorted(anagram)

    
    for i in range(0,len_1):
        if word[i] != anagram[i]:
            return False
    return True

print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("crack", "track"))
print(find_anagram("fowl", "wolf"))

