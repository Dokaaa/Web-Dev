v = int(input())
t = int(input())
s = v * t

if v > 0:
    m = s % 109
else:
    m = (109 + s) % 109
    
print(m)
