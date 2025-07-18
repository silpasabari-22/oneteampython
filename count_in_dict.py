s='java'
d=dict()
for k in s:
    if k.lower() in d:
        d[k]=d[k]+1
    else:
        d[k]=1

for key in d:
    print(f"{key}={d[key]}")