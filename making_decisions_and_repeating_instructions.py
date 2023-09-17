def all_numbers():
    """
    Create a Python program that prints all the numbers from 0 to 4 except two distinct numbers entered by the user.
    Note : Use 'continue' statement.

    If user input is
    ```
    3
    2
    ```
    Expected Output :
    '0 1 4'
    """

    num1 = int(input())
    num2 = int(input())

    #enter your code here '0\n1\n2' != '0 1 2'

    for x in range(5):
     if (x == num1 or x == num2):
        continue
     print(x,end=' ')
       


def dog_years():
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    human max 20 (break)/ if n human <= 2 dog age = 10.5
    dog yr1: 10.5 human
    dog yr2: 10.5 human 21
    dog yr3: 21 + n-2*4
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    
    if h_age <= 2:
        dog_age = h_age*10.5
    else:
        dog_age = 21 + (h_age -2)*4
        print(dog_age)

    ```
    """

    h_age = int(input("Input a dog's age in human years: \n"))
    if h_age <= 2:
        d_age = h_age*10.5
    else:
        d_age = (21 + ((h_age-2)*4))
        a = "The dog's age in dog's years is "
        print(a + str(d_age))
          
              
  
    
    #enter your code here



def consonant_or_vowel():
    """
    Build a program to check whether an alphabet is a consonant or vowel.

    Expected Output:
    ```
    Input a letter of the alphabet: k
    k is a consonant.
      l = input("Input a letter of the alphabet: ")
    for x
    if l != [a, e, i, o, u]:
        print(l + " is a constant")

    ```
    """
    #is

    l = input("Input a letter of the alphabet: ")
    x = [ "a", "e", "i", "o", "u "]
    if l != x:
     print (l + " is a consonant.")
   

    #enter your code here


def month_numbers():
    """
    Create a program to as input month's name to the number of days it has. The first letter of the month name should always be a capital letter

    Expected Output:
    ```
    List of months: January, February, March, April, May, June, July, August, September, October, November, December
    Input the name of Month: February
    No. of days: 28/29 days
    ```
    31 days namely January, March, May, July, August, October, and December.
    30 days in a year are April, June, September, and November.
    February has 28 days
    """

    print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
    month_name = input("Input the name of Month: ")
    


    #enter your code here

   
    if month_name == "January" or month_name == "March" or month_name == "May" or month_name == "July" or month_name == "August"or month_name == "October"or month_name == "December":
     print ("No. of days: 31 days")
    elif month_name == "April" or month_name ==  "June" or month_name ==  "September" or month_name ==  "November":
     print ("No. of days: 30 days")
    elif month_name == "February":
     print("No. of days: 28/29 days")


def pyramids():
    """
    Using a for loop, write a program to print the following pattern:

    @
    @@
    @@@
    @@@@
    @@@@@
    @@@@
    @@@
    @@
    @
    """

    rows = int(input())
    for i in range(0, rows):
        for j in range(0, i + 1):
            #enter your code here
             print("@", end=' ')
        print("\r")

    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            #enter your code here
             print("@", end=' ')
        print("\r")


def fibonacci():
    """
    The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
    The Fibonacci series from 0 to 4181 is `0,  1 , 1,  2,  3,  5,  8 , 13,  21,  34 , 55,  89,  144,  233,  377,  610,  987,  1597  ,2584,  4181`
    Write a program that will take as user input any two consecutive numbers between 0 and `4181` in the Fibonacci sequence, e.g. `1` `1` or `34` `55`.
    Use a loop to print out the next 10 numbers in the sequence that follow the 2 entered as input e.g. If input is
    ```
    0
    1
    ```
    the output will be:
    ```
    Fibonacci sequence:
    0 1 1 2 3 5 8 13 21 34
    ```

    if the input is
    ```
    55
    89
    ```
    the output will be:
    ```
    Fibonacci sequence:
    55  89  144  233  377  610  987
    ```
    The program should stop printing after `987`. Any number in the series after 987 should not be printed
    """

    # first two numbers
    num1 = int(input())
    num2 = int(input())

    print("Fibonacci sequence:")
    # run loop 10 times
    for i in range(10):
        # print next number of a series
        
        
        if not (num1 > 987):
            print(num1,end="  ")
            newVal = num1 + num2
            num1 = num2
            num2= newVal 
            
            #enter your code here


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    # all_numbers()
    # dog_years()
    # consonant_or_vowel()
    # month_numbers()
    # pyramids()
    # fibonacci()
