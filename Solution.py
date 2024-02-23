word = "((abc{}))"

openingDelimiters = "({["
closingDelimiters = ")}]"
count = {}
newSet = {}
for i in word:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for keys in count.keys():
    if keys in openingDelimiters or keys in closingDelimiters:
        newSet.update({keys: count.get(keys)})

if (newSet.get("(") == newSet.get(")")) and (newSet.get("{") == newSet.get("}")) and (
        newSet.get("[") == newSet.get("]")):
    print("valid")
else:
    print("invalid")
