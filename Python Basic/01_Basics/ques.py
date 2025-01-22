k, m = map(int, input().split())
tasks = []
for i in range(k):
  ele = int(input())
  tasks.append(ele)

o = sum(tasks) / m
print(int(o))

k, m = map(int, input().split())
tasks = list(map(int, input().split()))

o = sum(tasks) / m
print(int(o))