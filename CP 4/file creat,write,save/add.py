import sys

print(sys.argv)
print(type(sys.argv))
print(len(sys.argv))


arguments = sys.argv
print("number 2 of list",arguments[3])

a = arguments[1]

b = arguments[2]

print("sum of list_index [1] + [2] ",int(a)+int(b))