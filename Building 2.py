class Building:
    total = 0
    def __init__(self):
        Building.total += 1


buildings =[Building() for _ in range(40)]

for i, building in enumerate(buildings):
    print(f'Building {i+1} created. Total buildings: {Building.total}')