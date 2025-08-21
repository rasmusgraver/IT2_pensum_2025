
# Demo av at man kan angi hvor mange plasser et tall skal fylle:
# (Høyrestille tallet)
x = 10**6
for i in range(10):
    x = x / 3
    print(f"x = {x:12.3f}")

# Demo av at man kan fylle inn mange ting, også regning, i f-strings:
a=5
b=7
print(f"a={a} og b={b} og produktet blir {a*b:12.2f}")
