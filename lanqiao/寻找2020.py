import os
import sys

with open("2020.txt" , 'r', encoding="utf-8") as fr:
    date = fr.readlines()

print(len(date))
print(len(date[0]))
print(len(date[1]))
row = len(date)
col = len(date[0]) - 1


ans = 0
for i in range(row):
    for j in range(col):
        if date[i][j] == '2':
            
            if j < col - 3:
                if date[i][j+1] == date[i][j+3] == '0' and date[i][j+2] == '2':
                    ans += 1
                    
            if i < row - 3:
                if date[i+1][j] == date[i+3][j] == '0' and date[i+2][j] == '2':
                    ans += 1

            if i < row - 3 and j < col - 3:
                if date[i+1][j+1] == date[i+3][j+3] == '0' and date[i+2][j+2] == '2':
                    ans += 1

print(ans)

