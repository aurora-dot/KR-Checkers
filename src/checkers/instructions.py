import threading
import tkinter as tk


class instructions_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        root = tk.Tk()
        root.title("Instructions")
        labels = [
            tk.Label(root, text="Rules:"),
            tk.Label(root, text=""),
            tk.Label(root, text="White while not king can only go up"),
            tk.Label(root, text="Red while not king can only go down"),
            tk.Label(root, text="When king, you can move in either direction"),
            tk.Label(root, text="You can only travel diagonally"),
            tk.Label(
                root,
                text="You cannot travel over your own piece however to capture a counter you can do so",  # noqa: E501
            ),
            tk.Label(
                root,
                text="You win if you take out all their counters or if you force them into no moves. This applies for the other team too",  # noqa: E501
            ),
            tk.Label(
                root, text="To draw, you both have to have no moves available"
            ),
            tk.Label(
                root, text="You can set the difficulty using the side panel"
            ),
            tk.Label(root, text="To show move hints, click show help"),
        ]

        for label in labels:
            label.pack()

        root.mainloop()
