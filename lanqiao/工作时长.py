"""
from datetime import datetime

with open("./records.txt", "r") as fr:
    data = fr.readlines()
    data = [i.strip() for i in data if i.strip()]
    

data = sorted(data)
time_list = []
for i in data:
    time_list.append(datetime.strptime(i, "%Y-%m-%d %H:%M:%S"))

start_time = time_list[::2]
end_time = time_list[1::2]
cnt = len(start_time)
ans = 0
for i in range(cnt):
    delta = end_time[i] - start_time[i]
    ans += delta.total_seconds()

print(int(ans))

"""
print(5101913)
