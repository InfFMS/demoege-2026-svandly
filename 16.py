
n = [0] * 15548

for i in range(10):
    n[i] = 2*i

for i in range(10, 15548):
    n[i] = n[i-2] + 1

print(8 + 2*n[15548-3])