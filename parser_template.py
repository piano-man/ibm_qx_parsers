import json

with open(<file with json data>) as f:
    data = json.load(f)
x = list(data.keys())
y = list(data.values())
res = []
result = {}
count = 0
for item in x:
    val = "{0:08b}".format(int(item, 16)) #converting hexadecimal values to binary values
    value = str(val)
    res.append(value)
            
for i in range(len(res)):
    prob = (y[i]*100)/1024
    result[res[i]] = prob

for item in result:
	//logic to calculate the number of times the expected result is obtained

for item in result:
	//logic to calculate the Average QBER

