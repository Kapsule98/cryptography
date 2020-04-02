print("Choose P and G")
P = int(input())
G = int(input())
print("Choose Private key selected by Alice(a)")
a = int(input())
print("Choose private key selected by Bob(b)")
b = int(input())
x = (G**a) % P
y = (G**b) % P
print("Value computed by Alice and sent to Bob : ",x)
print("Value computed by Bob and sent to Alice : ",y)
AliceKey = (y**a)%P
BobKey = (x**b)%P
print("Key computed by Alice : ",AliceKey)
print("Key computed by Bob : ",BobKey)
