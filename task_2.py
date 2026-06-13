#          s/n=1

name=input("enter the name    : ")
age=int(input("enter your age   :  "))
print(f"hello {name}")     
if(age<13):
     print(" ticket type  : Child Ticket")
elif(age >= 13 and age < 60 ):
     print(" ticket type : Adult Ticket")
elif(age >= 60):
     print(" ticket type :Senior Citizen Ticket") 

#             s/n= 2
temperature=int(input("enter the temperature"))

if(temperature < 20):
     print("wether is cold")
elif(20<= temperature <=30 ):
     print("wether is Pleasant")
elif(temperature > 30):
     print("wether is hot")

#           s/n= 3

empname=input("Employee Name  : ")
salary = float(input("Salary    : "))
experience=int(input("Years of Experience  : "))
if(salary >= 50000 and experience >= 5):
 Bonus = salary *0.20
elif(salary >= 30000 and experience >= 3):
 Bonus = salary*0.10
else:
 Bonus =salary*0.5
final_salary = salary + Bonus
print("Bonus amount", Bonus)
print(" final _salary",final_salary)

           # s/n=4

percentage = float(input("enter the percentage   : "))
score=int(input("Entrance Exam Score   :  "))

if percentage >= 70 and score >= 80:
  print(" your Admission Confirmed")
elif percentage >= 60 and score >= 60:
  print(" you Waiting List")
else:
  print(" you are rejected")    


#             s/n= 5
        
c_name=input("enter the customer name : ")
units=int(input("enter the unit"))

if units<=0 and units<= 100: 
   bill=units *2 
elif units<=101  and units<= 300:
  bill= units *4 
elif units>= 300:
  bill=units *6 
if bill > 1000:
    discount=bill* 0.10
else:
    discount =0
final_bill = bill - discount
print("customer_name",c_name)
print("bill_amount",bill)
print("discount",discount)
print("final_bill",final_bill) 



            #s/n- 6


age= int(input("Enter Age: "))
salary = int(input("Enter Salary: "))
experience = int(input("Enter Experience (years): "))
existing_loan = input("Existing Loan? (yes/no): ")

if age >= 21 and salary >= 30000 and experience >= 2 and existing_loan == "no":
    print("Loan Approved")
else:
    if age < 21:
        print("Loan Rejected: under age")
    elif salary < 30000:
        print("Loan Rejected: Salary too low")
    elif experience < 2:
        print("Loan Rejected: Experience less than 2 years")
    elif existing_loan == "y":
        print("Loan Rejected: Existing loan found")

   