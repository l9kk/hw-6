string1 = "rasp"
string2 = "spar"
is_anagram = sorted(string1.lower()) == sorted(string2.lower())
print("anagram" if is_anagram else "non-anagram")