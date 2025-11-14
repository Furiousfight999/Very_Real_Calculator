#This time in Python

q1 = input("What is your first number?")
print(q1)

q2 = input("What is your second number?")
print(q2)

q3 = input('''would you like to:
1. add?
2. subtract?
3. multiply?
4. divide?
5. sacifice to the mesh network?
''')
if q3 == 1 or 2 or 3 or 4:
    x = 0
    print("Do it yourself, Idiot")
    while(x < 10):
        exec("C:\Windows\System32\calc.exe", "r")
        x += 1
elif q3 == 5:
    print("SACRIFICE! SACRIFICE! SACRIFICE! SACRIFICE! SACRIFICE! SACRIFICE!")
    exec(".\Mesh_network.pkt")
else:
    exec(".\TotallyRealCalculator")