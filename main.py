import keyboard

def keyPressed():
    while True:
        ### Row 0 ##
        # /
        if keyboard.is_pressed(53):
            return [0, 1]

        # *
        elif keyboard.is_pressed(55):
            return [0, 2]

        # -
        elif keyboard.is_pressed(74):
            return [0, 3]
        

        ### Row 1 ##
        # NumPad 7
        elif keyboard.is_pressed(71):
            return [1, 0]

        # NumPad 8
        elif keyboard.is_pressed(72):
            return [1, 1]

        # NumPad 9
        elif keyboard.is_pressed(73):
            return [1, 2]

        # +
        elif keyboard.is_pressed(78):
            return [1, 3]


        ### Row 2 ##
        # NumPad 4
        elif keyboard.is_pressed(75):
            return [2, 0]

        # NumPad 5
        elif keyboard.is_pressed(76):
            return [2, 1]

        # NumPad 6
        elif keyboard.is_pressed(77):
            return [2, 2]
        
        # Backspace
        elif keyboard.is_pressed(14):
            return [2, 3]
        

        ### Row 3 ###
        # NumPad 1
        elif keyboard.is_pressed(79):
            return [3, 0]

        # NumPad 2
        elif keyboard.is_pressed(80):
            return [3, 1]

        # NumPad 3
        elif keyboard.is_pressed(81):
            return [3, 2]
        
        # Enter
        elif keyboard.is_pressed(28):
            return [3, 3]


        ### Row 4 ###
        # NumPad 0
        elif keyboard.is_pressed(82):
            return [4, 0]

        # NumPad 000
        elif keyboard.is_pressed(11):
            return [4, 1]

        # Decimal (,)
        elif keyboard.is_pressed(83):
            return [4, 2]

while True:
    print( keyPressed() )