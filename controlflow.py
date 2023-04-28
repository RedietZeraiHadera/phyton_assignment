# Write a function that uses while, if and continue 
# statements to print all the even numbers between 0 and 50. 
def even_numbers():
    x=1
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)          
# Write a function that takes an integer argument and prints "Prime" 
# if the number is prime, and "Not prime" if the number is not prime.        
# def identify_prime_numbers(num):
def identify_prime_numbers(num):
    if num < 1:
     print('not prime')
    else:
     for i in range(2, num):
        if num % i == 0:
            print('not prime')
            break
        else:
            print('prime')
identify_prime_numbers(20)

# Write a function that takes a list of integers as input and prints the 
# sum of all the even numbers in the list.

def sum_of_even_numbers(nums):
    sum_even = 0
    for num in nums:
        if num%2==0:
            sum_even+=num
    print(sum_even)    
nums =[1,2,3,4,5,6,7,8,9,10]
sum_of_even_numbers(nums)
# Write a function that takes any two integers as input, and prints the sum of all
# the numbers between the two integers (inclusive) that are divisible by 3.
def sum_between_integers(num1,num2):
    sum = 0
    for i in range(num1,num2+1):
        if i%3==0:
            sum+=i
    print(sum)    
    sum_between_integers(10,20)
            

    
