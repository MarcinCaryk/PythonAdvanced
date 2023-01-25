# Załóżmy, że chcemy utworzyć zestaw wyjściowy, który zawiera tylko liczby parzyste.
ls = [1, 2, 3, 4, 5, 6, 7, 11, 13, 22, 56, 77, 84, 92, 101]

out = {var for var in ls if var % 2 == 0}

print("Output Set using set comprehensions:", out)

# generator

output_gen = (var for var in ls if var % 2 == 0)

print("Output values using generator comprehensions:", end=' ')

for var in output_gen:
    print(var, end=' ')


# Warunkowe if list comprehentions
out2 = [ x for x in range(30) if x % 2 == 0]
print("\nOutput using list comprehensions with if condition:", out2)

# Zagnieżdzone if w list comprehentions
out3 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print("Output using list comprehensions with nested if condition:", out3)

# if else w list comprehention
out4 = ["Even" if i%2==0 else "Odd" for i in range(10)]
print("Output using list comprehensions with if else condition:", out4)

# Transponowana macierz przy użyciu zagnieżdzonej pętli

matrix = [[1, 2], [3,4], [5,6], [7,8]]
out5 = [[row[i] for row in matrix] for i in range(2)]
print("Output using list comprehensions with nested for:", out5)