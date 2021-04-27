def dbl_linear(n):
  u = [1]
  for i in u:
    u.append((i * 2) + 1)
    u.append((i * 3) + 1)
    if len(u) > n *10:
      break
  return sorted(list(set(u)))[n]