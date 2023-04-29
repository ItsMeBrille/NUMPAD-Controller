import keyboard

def keyPressed():
    while True:
        # NumLock
        if keyboard.is_pressed(69):
            return [0, 0]
        # /
        if keyboard.is_pressed(53):
            return [0, 1]

        # *
        if keyboard.is_pressed(55):
            return [0, 2]

        # -
        if keyboard.is_pressed(74):
            return [0, 3]

        # NumPad 7
        if keyboard.is_pressed(71):
            return [1, 0]

        # NumPad 8
        if keyboard.is_pressed(72):
            return [1, 1]

        # NumPad 9
        if keyboard.is_pressed(73):
            return [1, 2]

        # +
        if keyboard.is_pressed(78):
            return [1, 3]

        # NumPad 4
        if keyboard.is_pressed(75):
            return [2, 0]

        # NumPad 5
        if keyboard.is_pressed(76):
            return [2, 1]

        # NumPad 6
        if keyboard.is_pressed(77):
            return [2, 2]

        # NumPad 1
        if keyboard.is_pressed(79):
            return [3, 0]

        # NumPad 2
        if keyboard.is_pressed(80):
            return [3, 1]

        # NumPad 3
        if keyboard.is_pressed(81):
            return [3, 2]

        # NumPad 0
        if keyboard.is_pressed(82):
            return [4, 1]

        # Decimal (,)
        if keyboard.is_pressed(83):
            return [4, 2]
    
while True:
    print(keyPressed())
    break