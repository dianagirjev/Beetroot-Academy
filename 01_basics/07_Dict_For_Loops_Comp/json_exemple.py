import json

dictionar_nou = {str(i): i for i in range(10)}

# with open("out.json", mode="w") as file:
#     file.write(json.dumps(dictionar_nou))

file = open("out.json", mode="w")
file.close()