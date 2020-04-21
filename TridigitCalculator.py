import json
import sys

with open("ComplexAlgorithm.json") as file:
    files = json.load(file)

def Calculate(eqn):
    eqn = eqn.replace(" ","")
    operator = "".join([i for i in eqn if not i.isdigit()])
    filename = files.get(operator,None)
    if filename:
        with open(filename) as file:
            data = json.load(file)
    else:
        print("Invalid equation.")
        return
    ans = data.get(eqn,"Invalid equation.")
    print(ans)


Calculate(sys.argv[1]) if len(sys.argv) == 2 else print("Provide an equation.")
