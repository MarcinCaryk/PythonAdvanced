# Załóżmy, że chcemy utworzyć listę wyjściową, która zawiera tylko liczby parzyste

ls = [1, 2, 3, 4, 4, 5, 6, 7, 7, 11, 15, 18]

out_ls = [var for var in ls if var % 2 == 0]

print("Output List using list comprehensions:", out_ls)


# Załóżmy, że chcemy utworzyć listę wyjściową zawierającą kwadraty wszystkich liczb od 1 do 9

out_ls2 = [var ** 2 for var in range(1, 10)]

print("Output List using list comprehensions:", out_ls2)

# Załóżmy, że chcemy utworzyć słownik wyjściowy, który zawiera tylko liczby nieparzyste

ls = [1, 2, 3, 4, 5, 6, 7, 11, 13, 22, 56, 77, 84, 92, 101]

out_ls3 = {var: var ** 3 for var in ls if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:", out_ls3)

# Mając dwie listy zawierające nazwy krajów i odpowiadające im stolice,
# skonstruuj słownik, który odwzorowuje stany z ich stolicami

kraj = ['Polska', 'Niemcy', 'Francja']
stolica = ['Warszawa', 'Berlin', 'Paryz']

out4 = {key: value for (key, value) in zip(kraj, stolica)}

print("Output Dictionary using dictionary comprehensions:", out4)