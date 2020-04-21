import json
import sys

with open("ComplexAlgorithm.json") as file:
    data = json.load(file)

def Calculate(eqn):
    ans = data.get(eqn,"Invalid equation.")
    print(ans)


Calculate(sys.argv[1]) if len(sys.argv) == 2 else print("Provide an equation.")
