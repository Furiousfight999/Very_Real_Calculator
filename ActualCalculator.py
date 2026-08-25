#calculator
n1 = float(input("what is your first number: "))
n2 = float(input("what is your second number: "))
o1 = float(input("""Would you like to:
1.Add?
2.Subtract?
3.Multiply?
4.Divide?
5.Exponentiation?

"""))
try:
    n1 = int(n1)
except ValueError:
    print("That isn't even a number. Shame on you.")
    exit()
try:
    n2 = int(n2)
except ValueError:
    print("That isn't even a number. Shame on you.")
    exit()
try:
    o1 = int(o1)
except ValueError:
    print("That isn't even a number. Shame on you.")
    exit()
    
def calc():
    if o1 in [1, 2]:
        if o1 == 1:
            print(f"""The sum of {n1} + {n2} is: 
{n1 + n2}.""")
        elif o1 == 2:
            print(f"""The difference of {n1} - {n2} is: 
{n1 - n2}.""")
    elif o1 in [3, 4]:
        if o1 == 3:
            print(f"""The product of {n1} * {n2} is: 
{n1 * n2}.""")
        elif o1 == 4:
            print(f"""The quotient of {n1} / {n2} is: 
{n1 / n2}.""")
    else:
        if o1 == 5:
            print(f"""The product of {n1} ^ {n2} is: 
{n1 ** n2}.""")
        else:
            print("You should learn to follow directions, IDIOT!!")
calc()  