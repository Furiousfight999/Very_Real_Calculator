#This time in Python

import subprocess
import sys
from pathlib import Path
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
try:
    q3 = int(q3)
except ValueError:
    print("That isn't even a number. Shame on you.")
    exit()
def meshnetwork():
    try:
        meshnetwork_name = "Mesh_network.pkt"
        Githubpath = Path(__file__).resolve().parent
        
        meshnetwork_path = Githubpath / meshnetwork_name
        
        if not meshnetwork_path.exists():
            print(f"Error: '{meshnetwork_name}' not found in {Githubpath}")
            sys.exit(1)
            
        subprocess.run([str(meshnetwork_path)], check=True)
        print("SACRIFICE SACRIFICE SACRIFICE SACRIFICE SACRIFICE SACRIFICE SACRIFICE SACRIFICE SACRIFICE SACRIFICE")
    except subprocess.CalledProcessError as e:
        print(f"Program exited with error code {e.returncode}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
# Check if q3 is in the valid list
if q3 in [1, 2, 3, 4]:
    x = 0
    print("Do it yourself, Idiot")
    while x < 10:
        subprocess.run(r"C:\Windows\System32\calc.exe")
        x += 1
elif q3 == 5:
    meshnetwork()
