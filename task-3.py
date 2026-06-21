             #s/n=1

balance = 10000
correct_pin=123456
correct_account_number = 12345678


while(True):  
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        
        print(" check your Balance:", balance)

    elif choice == 2:

        amount = int(input("Enter amount: "))

        account_number=int(input("enter the account_number"))

        pin=int(input("enter the  pin"))

        if account_number == correct_account_number and pin == correct_pin:
         
         balance += amount #increment_operator

         print("Deposit Successful")

         print("Current Balance:", balance)

        elif account_number != correct_account_number:
         
         print("Invalid Account Number")

        else:
         
         print("Incorrect PIN")

        break # this used comment while condition stop
    elif choice == 3:

        amount = int(input("Enter amount: "))

        if amount <= balance:
          
          pin=int(input("enter your pin"))

          if pin==correct_pin:
           
           balance -= amount #decrement_operator

           print("Withdrawal Successful")

           check_balance = input("Do you want to check your balance? (yes/no): ")

           if check_balance.lower()=="yes":
    
            print("Remaining Balance:", balance)

           elif check_balance.lower()=="no":
               
               print("Thank you for using our ATM.")
               
           else:
               print("Invalid choice. Please enter 'yes' or 'no'.")
               break
    elif choice == 4:

        print("Thank You!")

        break
    else:
        print("Invalid Choice")



          #   s/n=2

marks = []        #empty list (contains no items).
                   #You can add items to the list using append():

for i in range(1, 6):   #inside the loop runs 5 times.

    mark = int(input(f"Enter mark for subject {i}: ")) # A format string (f-string) is used to insert variables or values inside a string.

    marks.append(mark)  # used to add a new item to the end of a list. 

    total = sum(marks)

    average = total / len(marks)

    if average >= 90:
     grade = "A"
     
    elif average >= 75:
     grade = "B"
     
    elif average >= 60:
     grade = "C"
     
    elif average >=40:
     
     grade = "D"

     print("even if average is high")
    elif average<=40:
          
       grade="e"
       print("fail")
    
         

print("marks",marks)
print("total",total)
print("average",average)
print("grade",grade)
      
                    # s/n=3

password = input("Enter password: ")

contains_number = 0  
contains_upper = 0 #uppercase letter

for ch in password:
    digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if ch in digits:
      contains_number += 1
    

    if password == password.upper() and password != password.lower():
        contains_upper+= 1

if len(password) >= 8  and contains_number > 0 and contains_upper > 0:
    print("Strong Password")
else:
    print("Weak Password")

             #s/n=4


total = 0
count =0

while(True):
    price = float(input("Enter product price: "))

    if price == 0:
        break

    total += price    #total=100
                       #total=total+price
                       #total=100+200=300//
    count += 1         #count=1

           # Calculate discount

if total > 5000:
    discount = total * 0.20
    
elif total > 3000:
    discount = total * 0.10
elif total <3000:
    discount = 0

final_amount = total - discount    # final amount calculate(total-discount)

print("Total  =", total)
print("number of products :",count)
print("Discount =", discount)
print("Final Amount =", final_amount)


         #s/n=5

number = 27
attempts = 0

for attempts in range(0,6):
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Correct!")
        break
    elif guess >number:
        print("Too High")
    else:
        print("Too Low")

if attempts == 5 and guess != number:
    print("Game Over")

       # s/n=6

        
                 #index -    0       1          2
details = []       #salary, experience, attendance]

salary = float(input("Enter Basic Salary: "))
experience = int(input("Enter Years of Experience: "))
attendance = float(input("Enter Attendance Percentage: "))

details.append(salary)
details.append(experience)
details.append(attendance)

bonus = 0

# Experience bonus
if details[1] > 10:
    bonus = details[0] * 0.20
elif details[1] > 5:
    bonus = details[0] * 0.10

# Attendance bonus
if details[2] > 95:
    bonus += 5000

# Total salary before tax
total_salary = details[0] + bonus

# Tax
if total_salary > 100000:
    tax = total_salary * 0.10
elif total_salary > 50000:
    tax = total_salary * 0.05
else:
    tax = 0

# Final salary
final_salary = total_salary - tax

print("Basic Salary =", details[0])
print("Bonus =", bonus)
print("Tax =", tax)
print("Final Salary =", final_salary)



           #s/n=7

details = []

age = int(input("Enter age: "))
day = input("Enter day (weekday/weekend): ").lower()
tickets = int(input("Enter number of tickets: "))

details.append(age)
details.append(day)
details.append(tickets)

# details[0] = age
# details[1] = day
# details[2] = tickets

if details[0] < 12:
    price = 100
elif details[0] > 60:
    price = 120
else:
    price = 200

total = price * details[2]

if details[1] == "weekend":
    total = total + total * 0.20

if details[2] > 5:
    total = total - total * 0.10

print("Final amount: ₹", total)
