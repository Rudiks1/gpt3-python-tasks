import random

#1. Write a program to print "Hello, World!" on the console.

print('Hello, World!')


#2. Write a program that takes two numbers as input and prints their sum.

firstnum=int(input('\nFirst number: '))
secondnum=int(input('Second number: '))
print(f'Sum: {firstnum+secondnum}')


#3. Write a program that checks if a given number is even or odd.

num=int(input('\nNumber: '))
if num % 2 == 0: print('Even number')
else: print('Odd number')


#4. Write a program that calculates the factorial of a given number.

num=int(input('\nNumber: '))
result=1
for i in range(1,num+1): result*=i
print(f'Factorial: {result}')


#5. Write a program that takes a string as input and counts the number of vowels in it.

string=str(input('\nString: '))
vowels=['a', 'e', 'i', 'o', 'u']
count=0
for letter in string:
    if letter in vowels: count+=1
print(f'Number of vowels: {count}')


#6. Write a program that prints the Fibonacci sequence up to a given number of terms.

num=int(input('\nNumber: '))
fib=[0,1]
if num>=2:
    for i in range(num-2): fib.append(fib[-1]+fib[-2])
    print(fib)
elif num==1: print([fib[0]])


#7. Write a program that checks if a given string is a palindrome.  

string=str(input('\nString: ')).lower()
if string==string[::-1]: print("It's palindrome!")
else: print("It isn't palindrome!")


#8. Write a program that finds the largest element in a given list.

lst=[random.randint(1,100) for _ in range(10)]
print(f'\nLargest number: {max(lst)}')


#9. Write a program that checks if a given number is prime.

num=int(input('\nNumber: '))
if num % 2 !=0 and num !=1:
    for i in range(3,num):
        if num % i == 0:
            print("It isn't a prime number!")
            break
    else:
        print("It is a prime number!")
elif num==2:
    print("It is a prime number!")
else:
    print("It isn't a prime number!")


#10. Write a program that reverses a given string.

string=str(input('\nString: '))
print(string[::-1])