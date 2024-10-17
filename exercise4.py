#anagram are strings enhancing the 
#same of the letters (for example enlist).
#Write afunction that takes two strings and
 #return the if they are anagram and false 
 #other wise

#Copy code
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')

result = are_anagrams(string1, string2)
print(result)