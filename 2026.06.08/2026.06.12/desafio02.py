"Mostre uma tabuada completa desde 0 x 0 até 10 x 10 usar enquanto aninhado."

i = 0
while i <= 10:
    print (f"\n--- Tabuade de {i} ---\n")
    j = 0
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
