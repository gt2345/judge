a, b = map(int, raw_input().split())
i = 0
res = 0
while i < 70000000:
    res += a
    i += 1
print res + b