#Write program that takes astring and display it without 
#the vowels(e, i, o, u, a, A, U, O, E, I)
#my answer code
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    no_vowels = ''.join([char for char in s if char not in vowels])
    return no_vowels
input_string = input("Enter a string: ")
result = remove_vowels(input_string)
print("String without vowels:", result)