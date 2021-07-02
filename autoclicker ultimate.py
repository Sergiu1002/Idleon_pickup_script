from pynput.mouse import Button, Controller
import keyboard

n = int(input("start at x(atleast 64 in order to work): "))
m = int(input("start and return at y(atleast 32 in order to work): "))
o = int(input("stop and return at y(max 1039): "))

mouse = Controller()
mouse.position = (n, m)

c3 = 0
c4 = 0

mouse.press(Button.left)
while True:
    mouse.move(1, 0)
    c3 += 1
    if c3 > 1850:
        c3 = 0
        c4 += 1
        mouse.move(-1920, 2)
    if c4*2 > o:
        c4 = 0
        mouse.move(0, -1079)
        mouse.move(0, m)
    if keyboard.is_pressed('f1'):
        break
