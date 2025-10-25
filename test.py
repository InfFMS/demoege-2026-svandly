count = 0
mas = [0] * 20

def rec(n):
    mas[n] += 1
    if n < 0 or mas[n] == 1:
        return
    tf = 0
    global count
    if n == 2 and tf == 1:
        count += 1
        return
    if n == 7:
        return
    if n == 13:
        tf = 1
    rec(n - 1)
    rec(n - 4)
    rec(n % 3)
    tf = 0
    return

a = int(input())

print(count)

# m = (2**25/3845627)
# print(m)
