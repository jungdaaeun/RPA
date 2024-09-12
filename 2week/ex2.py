a=123
b=15.556

print(a, "and", b, sep='@', end='\n\n')

print("a:{0} b:{1}".format(a,b))
print(f"a:{a} b:{b}")

print(f"a:{a} b:{b:2f}")
print("a:%05d b:%.2f" % (a,b))
