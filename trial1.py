# class Loan(self, amount):
#     self.amount = amount
#     def acceptRequest():
from matplotlib import pyplot

def get_loan_info():
    loan = {}
    amount = float(input("How much do you want to borrow"))
    loan['principal'] = amount
    interest_rate = float(input("What interest rate are you working with?"))
    loan['rate'] = interest_rate/100

    desired_monthly_payment = float(input("How much do you desire to pay?"))
    loan['monthly payment'] = desired_monthly_payment
    loan['money paid'] = 0
    return loan

def show_loan_info(loan, months:int):
    months = 2
    print(f'After {months} months, the principal is {loan["principal"]}, and the money paid is {loan["money paid"]}')
    for k, v in loan.items():
        print(f'{k} : {v}')

def collect_interest(loan):
    updated_principal = loan['principal'] + loan['principal'] * loan['rate']/12
    loan['principal'] = updated_principal

def make_monthly_payment(loan):
    updated_principal = loan['principal'] - loan['monthly payment']
    if updated_principal > 0:
        loan['monthly payment'] += loan['money paid']
    elif updated_principal < 0:
        loan['monthly payment'] += loan['money paid'] + updated_principal
        updated_principal = 0

def summarise_loan(loan, months:int,amount:float):
    """[summary]
    Display the results of paying off loan
    Args:
        loan ([type]): [description]
        months (int): [description]
        principal (float): [description]
    """
    print(f'{amount}\n it took {months} to pay back. at the rate of  {loan["rate"]} ')
    print(f' Your monthly payment was {loan["monthly payment"]}')
    print(f' You spent £{str(round(loan["money paid"],2))} in total')

    interest = round(loan['money paid'] - amount,2)
    print("You spent " + str(interest) + "on interest")

def create_graph(data, loan):
    x_values = []
    y_values = []

    for point in data:
        x_values.append(point[0])
        y_values.append(point[1])

    pyplot.plot(x_values, y_values)
    pyplot.title(str(100*loan['rate'])+ "% interest with " +str(loan['monthly payment']) + " Monthly Payment")          
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")

    pyplot.show()

print("Welcome to the loan app")
month_number = 0
my_loan= get_loan_info()
amount = my_loan['principal']
data_to_plot = []

show_loan_info(my_loan, month_number)
input('Please press enter to begin paying off your loan')

while my_loan['principal'] >0:
    if my_loan['principal'] > amount:
        break

    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)

if my_loan['principal'] <= 0:
    summarise_loan(my_loan,month_number, amount)
    create_graph(data_to_plot, my_loan)

else:
    print("\n You would never be able to pay off you loan")
    print("\n You cannot get ahead of interest")







    
