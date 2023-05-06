import keyboard

def keyPressed():
    ### Row 0 ##
    numpad = {
        53 : [0, 1], 55 : [0, 2], 74 : [0, 3], # /, *, -
        71 : [1, 0], 72 : [1, 1], 73 : [1, 2], 78 : [1, 3], # 7, 8 ,9, +
        75 : [2, 0], 76 : [2, 1], 77 : [2, 2], 14 : [2, 3], # 4, 5, 6, Backspace
        79 : [3, 0], 80 : [3, 1], 81 : [3, 2], 28 : [3, 3], # 1, 2, 3, Enter
        82 : [4, 0], 11 : [4, 1], 83 : [4, 2] # 0, 000, Decimal
    }
    
    for key in numpad:
        if keyboard.is_pressed(key):
            return numpad[key]
    return False

if __name__ == "__main__":
    while True:
        print( keyPressed() )