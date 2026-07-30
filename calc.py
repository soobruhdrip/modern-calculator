import tkinter as tk


class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""

        title = tk.Label(
            root,
            text="Modern Calculator",
            font=("Segoe UI", 20, "bold"),
            bg="#1e1e1e",
            fg="white"
        )
        title.pack(pady=(15, 5))

        self.display = tk.Entry(
            root,
            font=("Segoe UI", 24),
            justify="right",
            bd=0,
            bg="#2d2d2d",
            fg="white",
            insertbackground="white"
        )
        self.display.pack(fill="x", padx=15, pady=10, ipady=15)

        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
            ["="]
        ]

        for row_index, row in enumerate(buttons):
            button_frame.grid_rowconfigure(row_index, weight=1)

            for col_index, text in enumerate(row):
                button_frame.grid_columnconfigure(col_index, weight=1)

                btn = tk.Button(
                    button_frame,
                    text=text,
                    font=("Segoe UI", 18, "bold"),
                    bd=0,
                    bg="#333333",
                    fg="white",
                    activebackground="#555555",
                    activeforeground="white",
                    command=lambda value=text: self.button_click(value)
                )

                if text == "=":
                    btn.grid(
                        row=row_index,
                        column=0,
                        columnspan=4,
                        sticky="nsew",
                        padx=4,
                        pady=4
                    )
                else:
                    btn.grid(
                        row=row_index,
                        column=col_index,
                        sticky="nsew",
                        padx=4,
                        pady=4
                    )

        footer = tk.Label(
            root,
            text="Made by soobruhdrip",
            font=("Segoe UI", 9),
            bg="#1e1e1e",
            fg="gray"
        )
        footer.pack(pady=8)

        self.root.bind("<Key>", self.key_press)

    def button_click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display()

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.update_display()

        elif value == "=":
            self.calculate()

        else:
            self.expression += value
            self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.update_display()
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def key_press(self, event):
        key = event.keysym

        if key in [
            "0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9"
        ]:
            self.expression += event.char

        elif event.char in "+-*/().%":
            self.expression += event.char

        elif key == "Return":
            self.calculate()
            return

        elif key == "BackSpace":
            self.expression = self.expression[:-1]

        elif key == "Escape":
            self.expression = ""

        else:
            return

        self.update_display()


def main():
    root = tk.Tk()
    ModernCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
