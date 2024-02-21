data = [1,2,3,4,5]
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        maximum = data[j]
print(maximum)