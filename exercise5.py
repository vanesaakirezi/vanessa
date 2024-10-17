#a palindrome number is string that reads the same forward and
#backward (for example madam and noox).
#Write function that takes string as an argument and 
#returns the true if the string is palindrome and false other wise
# my code
def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1] 

print(is_palindrome("madam"))  
print(is_palindrome("noon"))   
print(is_palindrome("hello"))  
