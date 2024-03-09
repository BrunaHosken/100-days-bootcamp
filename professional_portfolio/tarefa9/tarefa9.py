# An online writing app where if you stop typing, your work will disappear.

import tkinter as tk
import threading
import time

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")

        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=10, width=40)
        self.text_area.pack(padx=10, pady=10)

        self.timer_interval = 5  # seconds
        self.timer_running = False
        self.last_typing_time = time.time()

        self.start_timer()

        self.root.bind("<Key>", self.on_key_pressed)

    def on_key_pressed(self, event):
        self.last_typing_time = time.time()

    def start_timer(self):
        self.timer_running = True
        threading.Thread(target=self.check_typing_timer).start()

    def check_typing_timer(self):
        while self.timer_running:
            time.sleep(1)
            if time.time() - self.last_typing_time > self.timer_interval:
                self.delete_text()

    def delete_text(self):
        self.text_area.delete(1.0, tk.END)
        self.last_typing_time = time.time()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
