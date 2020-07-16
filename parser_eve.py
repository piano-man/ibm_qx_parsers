import json

with open('./eve_unlucky.json') as f:
    data = json.load(f)
x = list(data.keys())
y = list(data.values())
res = []
result = {}
count = 0
for item in x:
    val = "{0:08b}".format(int(item, 16))
    value = str(val)
    if len(value) != 10:
        iter = 10-len(value)
        while iter > 0:
            value = "0"+value
            iter = iter-1
    res.append(value)
            
for i in range(len(res)):
    prob = (y[i]*100)/1024
    result[res[i]] = prob

for item in result:
    if (item[0] == '0') and (item[2] == '1') and (item[3] == '1'):
        count = count+result[item]


qber = 0
for item in result:
    temp = 0
    if (item[0] != '0'):
        temp = temp+1
    if (item[2] != '1'):
        temp = temp+1
    if (item[3] != '1'):
        temp = temp+1
    print(temp)
    qber = qber+(result[item]*(temp/3))

#print(sum(result.values()))
print(count)
print(qber)
#print(result.keys())
