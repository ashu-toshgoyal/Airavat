from pynput import keyboard

stop_loop = False

def on_press(key):
    global stop_loop
    try:
        if key.char == 'q':
            print("Q was pressed. Exiting loop...")
            stop_loop = True
            return False  # Stops the listener
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Running loop. Press 'q' to stop.")
while not stop_loop:
    # Your logic here
    pass  # Replace with actual code

listener.join()
