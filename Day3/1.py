n = input("Enter a character = ")
k = int(input())
if (ord(n)>96):
    if ord(n)+k>122:
        print(chr((ord(n)+k)-26))
    else:
        print(chr(ord(n)+k))
else:
    if ord(n)+k>90:
        print(chr((ord(n)+k)-26))
    else:
        print(chr(ord(n)+k))