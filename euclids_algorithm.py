a, b = sorted(map(int,input().split()))
r = b%(a*(b//a))

A, B = a, b

while r>0:
    print(f"{b}={a}*{b//a}+{r}")
    b = a
    a = r
    r = b%a

print(f"{b}={a}*{b//a}+{r}")
print(f"GCD({B},{A})={a}")
