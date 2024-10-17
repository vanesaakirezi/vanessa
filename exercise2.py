#Write a python program that ask the user to input apositive integer
#and print all prime numbers less than or equal to the input .
#only accept positive integer as inputs.
""""""
def is_prime(num):
 if num <1:
    return False
 for i in range (2, int(num/2 + 1)):
     if num % i == 0:
        return False
 return true
def print_prime(n):
      for num in range(2,n+1):
         if is_prime(num):
            print(num)
print(45)
  