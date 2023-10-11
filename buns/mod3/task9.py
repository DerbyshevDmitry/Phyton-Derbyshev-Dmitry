def robot_location(N):
    x, y = 0, 0
    # Количество полных циклов
    full_cycles = N // 4

    # Остаток шагов
    remaining_steps = N % 4

    x += full_cycles
    y += full_cycles

    if remaining_steps == 1:
        x = 0
        x -= full_cycles + 1
    elif remaining_steps == 2:
        y = 0
        y -= full_cycles + 1
        x = 0
        x -= full_cycles + 1
    elif remaining_steps == 3:
        x = 0
        x += full_cycles + 1
        y = 0
        y -= full_cycles + 1

    return (x, y)

# Введите количество шагов N
N = int(input("Количество шагов: "))
result = robot_location(N)
print(result)





