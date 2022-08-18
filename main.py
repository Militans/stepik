import statistics as st

arr = {1: 0, 2: 0, 3: 0}
count = 0
data = open("\dowdloads\dataset_3363_4 (5).txt")
result = open("resut.txt", 'w')
for i in data:
    count += 1
    a = i.strip().split(';')
    del a[0]
    temp_arr = [eval(k) for k in a]
    for j in range(3):
        arr[j + 1] += temp_arr[j]
    # print(temp_arr)
    result.write(str(st.mean(temp_arr)) + '\n')
    print(str(st.mean(temp_arr)))

for i in arr:
    result.write(str(arr[i] / count) + ' ')
    print(arr[i] / count, end=' ')
result.close()
data.close()
