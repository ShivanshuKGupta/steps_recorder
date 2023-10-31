import pyautogui as pygui
from pynput import keyboard
import time

file = open("recorded_steps.txt", "r")
lines = file.readlines()


def on_key_press(key):
    if (str(key) == 'Key.alt_gr'):
        keyboard_listener.stop()
        exit(0)


keyboard_listener = keyboard.Listener(on_press=on_key_press)

keyboard_listener.start()

flag = True
while (flag and keyboard_listener.is_alive()):
    flag = False
    for line in lines:
        [cmd, value] = line.split(':')
        value = value.removesuffix('\n')
        print(cmd, value)
        if (cmd == 'MouseClick'):
            [click, x, y] = value.split(',')
            pygui.moveTo(x=int(x), y=int(y))
            if (click == 'Button.left'):
                pygui.leftClick()
            elif (click == 'Button.right'):
                pygui.rightClick()
            else:
                raise Exception(f"Not identifiable button click: {click}")
        elif (cmd == 'KeyPress'):
            value = value.removeprefix("'")
            value = value.removesuffix("'")
            value = value.removeprefix("Key.")
            if (value.count('_') > 0):
                value = value.replace('_', '')
            pygui.hotkey(value)
        elif (cmd == 'Delay'):
            print(f"Sleeping for {value} milliseconds")
            time.sleep(float(value))
        elif (cmd == 'Restart'):
            print("Restarting")
            flag = True
            break
        else:
            raise Exception(f'No such command exists: {cmd}')
