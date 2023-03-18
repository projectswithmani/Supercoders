result = []
for i in range (11):
    if i%2!=0:
        result.apend(i)
    else:
        result.apend(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for row in mat:
    for ele in row:
        if ele%2!=0:
            result.append(ele**2)
        else:
            result.append(ele**3)
print(result)

#pro comprehension
print([ele**2 if ele%!=0 else ele**3
       for row in mat for ele in row])