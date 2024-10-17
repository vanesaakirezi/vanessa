#Write a running program that reads from the positive integer and
#display it in words.
# answer code
def number_to_words(num):
    if num == 0:
        return "zero"
    below_20 = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
        "seventeen", "eighteen", "nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", 
        "ninety"
    ]
    
    thousands = ["", "thousand", "million", "billion"]

    def words(n):
        if n < 20:
            return below_20[n]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else ' ' + below_20[n % 10])
        elif n < 1000:
            return below_20[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + words(n % 100))
        else:
            for i, word in enumerate(thousands):
                if n < 1000 ** (i + 1):
                    return words(n // (1000 ** i)) + ' ' + word + ('' if n % (1000 ** i) == 0 else ' ' + words(n % (1000 ** i)))

    return words(num).strip()

# Input from user
try:
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("Please enter a positive integer.")
    else:
        print(number_to_words(number))
except ValueError:
    print("Invalid input. Please enter a positive integer.")