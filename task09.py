a = int(input("1-tomonni kiriting: "))
b = int(input("2-tomonni kiriting: "))
c = int(input("3-tomonni kiriting: "))

if a == b and b == c:
    print("Teng tomonli")
elif a == b or a == c or b == c:
    print("Teng yonli")
else:
    print("Turli tomonli")
