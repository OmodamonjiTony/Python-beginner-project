import tkinter as tk

class ClickCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Click Counter")
        self.master.geometry("300x200")

        self.count = 0

        self.label = tk.Label(master, text="Clicks: 0", font=("Arial", 24))
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Click Me!", font=("Arial", 18), command=self.increment_count)
        self.button.pack(pady=10)

    def increment_count(self):
        self.count += 1
        self.label.config(text=f"Clicks: {self.count}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()