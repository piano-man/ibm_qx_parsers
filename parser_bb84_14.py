#14 qubit case parser
import json

with open('./bb84_14.json') as f:
    data = json.load(f)
x = list(data.keys())
y = list(data.values())
res = []
result = {}
count = 0
for item in x:
    val = "{0:08b}".format(int(item, 16))
#    print(val)
    value = str(val)
    if len(value) != 14:
        iter = 14-len(value)
        while iter > 0:
            value = "0"+value
            iter = iter-1
    res.append(value)
            
for i in range(len(res)):
    prob = (y[i]*100)/1024
    result[res[i]] = prob

for item in result:
    if (item[0] == '0') and (item[1] == '0') and (item[2] == '1') and (item[5] == '1') and (item[8] == '1') and (item[9] == '0') and (item[10] == '0') and (item[11] == '1' and item[12] == '1'):
        count = count+result[item]

qber = 0
for item in result:
    temp = 0
    if (item[0] != '0'):
        temp = temp+1
    if (item[1] != '0'):
        temp = temp+1
    if (item[2] != '1'):
        temp = temp+1
    if (item[5] != '1'):
        temp = temp+1
    if (item[8] != '1'):
        temp = temp+1
    if (item[9] != '0'):
        temp = temp+1
    if (item[10] != '0'):
        temp = temp+1
    if (item[11] != '1'):
        temp = temp+1
    if (item[12] != '1'):
        temp = temp+1
    qber = qber+(result[item]*(temp/3))

##print(sum(result.values()))
print(count)
print(qber)
##print(result.keys())
