import threading
import tkinter as tk


class instructions_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        root = tk.Tk()
        btn = tk.Label(root, text="Start")
        btn.bind("<Button-1>", lambda x: root.destroy())
        btn.pack()
        root.mainloop()
