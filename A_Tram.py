n = int(input())
max_number = 0
total_passengers = 0
for i in range(n):
    a, b = map(int, input().split())
    total_passengers = total_passengers - a + b
    if total_passengers > max_number:
        max_number = total_passengers
print (max_number)        