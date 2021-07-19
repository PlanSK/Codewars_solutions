def dirReduc(arr: list)->list:
    new_s = ','.join(arr)
    for _ in range(len(arr)):
        new_s = new_s.replace('NORTH,SOUTH','')
        new_s = new_s.replace('SOUTH,NORTH','')
        new_s = new_s.replace('WEST,EAST','')
        new_s = new_s.replace('EAST,WEST','')
        new_s = new_s.replace(',,', ',')
    return [element for element in new_s.split(',') if element]
        

a = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
u = ['NORTH', 'WEST', 'SOUTH', 'EAST']
b = ['NORTH', 'NORTH', 'SOUTH', 'NORTH'] 
# ['NORTH', 'NORTH']
c = ['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']
# ['EAST', 'NORTH']
print('*', dirReduc(a))
print('*', dirReduc(u))
print('*', dirReduc(b))
print('*', dirReduc(c))