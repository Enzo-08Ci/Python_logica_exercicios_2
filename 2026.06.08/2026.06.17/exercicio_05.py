"""
5. Contagem Crescente

Mostre os números de 1 a 10 usando um loop.
"""
print("\nNúmeros com range:\n")
for num in range(1, 11):
    print(num)

print("\nNúmeros usando `while`:\n")    
num = 1
while num < 11:
    print(num)
    num += 1

print("\nSó pares:\n")    
for num in range(1, 11):
    if num % 2 == 0:
        print(num)