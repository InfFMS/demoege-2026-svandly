n = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 +81**2023 - 2 * 27**2024 - 6561
arr = []
while n > 0:
    arr.append(n % 27)
    n //= 27

count = 0
for i in arr:
    if i > 9:
        count += 1

print(count)