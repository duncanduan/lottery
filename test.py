import itertools
import csv
import requests

import requests

url = 'https://github.com/duncanduan/lottery/raw/main/big_lottery.csv'
response = requests.get(url)

with open('big_lottery.csv', 'wb') as f:
    f.write(response.content)


# 读取数据
with open('big_lottery.csv', mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 提取前5个数
result = []
for row in data:
    result.append(row[:5])

# 将数据写入csv文件
with open('first_five.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)



# 读取数据
with open('first_five.csv', mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 生成排列组合
result = []
for row in data:
    permutations = list(itertools.permutations(row, len(row)))
    result.append(permutations)

# 将数据写入csv文件
with open('permutations.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(data)):
        for j in range(len(result[i])):
            writer.writerow(list(result[i][j]))
