f = lambda s: s**2
dat = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_power_dat = [g for s in dat if (g := f(s)) > 20]
print("Output using list comprehensions with nested for:", filtered_power_dat)


data = {"A": [40, 62, 65], "B": [35, 62, 70, 82], "C": [28, 45, 80], "D":[91, 77]}
out = {g: mean for g in data if (mean := (sum(data[g]) // len(data[g]))) > 60}
print("Output using list comprehensions with nested for:", out)
