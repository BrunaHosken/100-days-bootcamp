# A Tkinter GUI desktop application that tests your typing speed.
import tkinter as tk
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.words = ["hello", "world", "python", "tkinter", "programming", "speed", "test", "coding", "challenge"]
        self.current_word = ""
        self.start_time = 0
        self.high_score = 0

        self.user_input = tk.Entry(root, state=tk.DISABLED)
        self.result_label = tk.Label(root, text="")
        self.score_label = tk.Label(root, text="High Score: {}".format(self.high_score))
        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)

        self.user_input.pack(pady=(30, 10), padx=30)
        self.result_label.pack(pady=10, padx=10)
        self.score_label.pack(pady=10, padx=10)
        self.start_button.pack(pady=10, padx=10)

    def start_test(self):
        self.user_input.config(state=tk.NORMAL)
        self.current_word = random.choice(self.words)
        self.result_label.config(text="Type the word: {}".format(self.current_word))
        self.user_input.delete(0, tk.END)
        self.start_time = time.perf_counter()
        self.user_input.bind("<Return>", self.check_result)

    def check_result(self, event):
        user_input = self.user_input.get().strip().lower()
        elapsed_time = time.perf_counter() - self.start_time

        if user_input == self.current_word:
            self.result_label.config(text="Correct! Time: {:.2f} seconds".format(elapsed_time))
            if elapsed_time < self.high_score or self.high_score == 0:
                self.high_score = elapsed_time
                self.score_label.config(text="High Score: {:.2f} seconds".format(self.high_score))
        else:
            self.result_label.config(text="Incorrect. Try again.")

        self.user_input.config(state=tk.DISABLED)
        self.user_input.unbind("<Return>")
        self.user_input.delete(0, tk.END)
        self.root.after(2000, self.start_test)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()




