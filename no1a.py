def fokuslensa(n, r1, r2):
    return 1 / ((n-1) * (1/r1 + 1/r2))

n = 1.5
r1 = 22
r2 = 17.5

f = fokuslensa(n, r1, r2)
print(f"Jarak fokus lensa adalah : ",f, "cm")
