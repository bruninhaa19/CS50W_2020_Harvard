# creat an empty ser

s = set()

# aadd element to set

s.add(1)
s.add(2)
s.add(3)
s.add(3)         # no number appears 2x
s.add(4)
s.add(5)
s.add(0)         # ordem numérica

s.remove(2)

print(s)

print(f"The set has {len(s)} elements")       #lenght of the sequence