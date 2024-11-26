from primo import is_prime

for p in range(2, 100):
  for q in range(p + 2, 100):
    if is_prime(p) and is_prime(q) and q - p == 2:
      print(f"({p}, {q})")