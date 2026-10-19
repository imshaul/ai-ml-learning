import math
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# print(f"Hello {name}")
# print(f"You are {age} years old")
# print("-"*70)
# first_int = int(input("Enter first integer : "))
# second_int = int(input("Enter second integer : "))
# print("-"*70)
# print(f"Sum of the integers is {first_int + second_int}")
# print(f"Difference : {first_int - second_int}")
# print(f"Product : {first_int * second_int}")
# print(f"Quotient : {first_int // second_int}")
# print(f"Remainder : {first_int % second_int}")
# print("-"*70)
# num = int(input("Enter a check to check wether it is positive or negetive \n"))
# if num > 0 :
#     print("The Number is positive")
# else :
#     print("Negetive")
# print("-"*70)
# for a in range(10):
#     print(a)
# print("-"*70)

# print(math.factorial(120))
# print("-"*70)
# entr_name = input("Enter your name : ")
# reversed_txt = ""
# for a in range(len(entr_name)-1,-1,-1):
#     print(entr_name[a])

# inp = input("Give a sentence to check vowels in it \n")
# count = 0
# for i in inp:
#     if i.lower() in "aeiou":
#         count+=1
# print(f"its vowel\n vowel count is {count}")
   
# num = input("Enter nums : ").split()
# largest = int(num[0])
# smallest = int(num[0])
# total = 0
# for n in num:
#     n = int(n)

#     if n>largest:
#         largest = n
#     if n<smallest:
#         smallest = n
#     total += n
# avg = total/len(num)
# print(largest)
# print(smallest)
# print(avg)

# def is_prime(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input("Num: "))
# if is_prime(n):
#     print("Prime")
# else:
#     print("Not Prime")


nums = "30 30 10 10 40"
print(nums.split())
for num in nums:
    print(num)