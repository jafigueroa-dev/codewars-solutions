def tower_builder(n_floors):
    tower = []
    d = n_floors * 2 - 1
    for i in range(n_floors):
        tower.append((" " * i) + ("*" * d) + (" " * i))
        d -= 2
    return tower[::-1]