# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input()) 
    global direction
    direction = ""

    if 0 <= initial_tx <= 39 and 0 <= initial_ty <= 17:
        direction_x, direction_y = "", ""
        
        if light_x < initial_tx:
            direction_x = "W"
            initial_tx -= 1

        elif light_x > initial_tx:
            direction_x="E"
            initial_tx += 1

        if light_y < initial_ty:
            direction_y="N"
            initial_ty -= 1

        elif light_y > initial_ty:
            direction_y = "S"
            initial_ty += 1

        direction = direction_y + direction_x

    print(direction)

