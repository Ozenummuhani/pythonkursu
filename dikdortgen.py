satir=int (input ("dikdörtgenin kisa kenari: "))
sutun =int (input("dikdörtgenin uzun kenari: "))

def draw_rectangle (width, height):
    for i in range (height):
        for j in range (width):
            if i == 0 or i ==height -1 or j == 0 or j == width - 1:
                print ("-", end ="")
            else:
                print (" ", end="")
        print ()

draw_rectangle (sutun, satir) 