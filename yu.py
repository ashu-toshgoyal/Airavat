import tkinter as tk
import time
import threading

# Splash text as multiline string
splash_text = """
############################################
#                                          #
#         MADE BY ASHU AND MANYA           #
#                                          #
#         WELCOME TO PROJECT ARIA          #
#                                          #
############################################
"""

def show_main_app():
    splash.destroy()

    # Main App Window
    main_app = tk.Tk()
    main_app.title("Aria Main App")
    main_app.geometry("300x200")
    tk.Label(main_app, text="Welcome to Aria!", font=("Helvetica", 16)).pack(pady=60)
    main_app.mainloop()

def typewriter_effect(label, text, delay=50):
    def inner():
        label_text = ""
        for char in text:
            label_text += char
            label.config(text=label_text)
            time.sleep(delay / 1000.0)
        # Delay then load main app
        time.sleep(1)
        show_main_app()
    threading.Thread(target=inner).start()

# Splash Screen Window
splash = tk.Tk()
splash.title("Splash")
splash.geometry("400x200")
splash.configure(bg="black")
splash.overrideredirect(True)  # Remove title bar
splash.eval('tk::PlaceWindow . center')

# Label to hold splash text
splash_label = tk.Label(splash, text="", fg="lime", bg="black", font=("Courier", 10), justify="left")
splash_label.pack(expand=True)

# Start typing the splash text slowly
typewriter_effect(splash_label, splash_text, delay=25)

splash.mainloop()
