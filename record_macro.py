from pynput import keyboard, mouse
import time
import os

file = open("recorded_steps.txt", "w")


def on_key_press(key):
    print(f"KeyPress:{key}")
    if (str(key) == 'Key.alt_gr'):
        keyboard_listener.stop()
        mouse_listener.stop()
        return
    file.write(f"KeyPress:{key}\n")


def on_click(x, y, button, pressed):
    if pressed:
        print(f"MouseClick:{button},{x},{y}")
        file.write(f"MouseClick:{button},{x},{y}\n")


keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_click=on_click)

wait_sec = 1

for i in range(wait_sec):
    txt = f"Recording will start in {wait_sec-i} seconds..."
    print(txt, end='')
    time.sleep(1)
    print('\b'*len(txt), end='')
    print(' '*len(txt), end='')
    print('\b'*len(txt), end='')

print("Listening to keypresses and mouse clicks.")
print("Press right alt to stop recording.")

keyboard_listener.start()
mouse_listener.start()

try:
    keyboard_listener.join()
    mouse_listener.join()

except KeyboardInterrupt:
    keyboard_listener.stop()
    mouse_listener.stop()

file.close()

dir = __file__.removesuffix('record_macro.py')
os.system(f"start notepad {dir}recorded_steps.txt")
