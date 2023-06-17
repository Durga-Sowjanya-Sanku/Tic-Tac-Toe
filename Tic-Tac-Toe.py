from tkinter import *


class Board:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("320x400")
        self.window.title("Tic-Tac-Toe")

        self.buttons = []
        self.current_player = "X"

        # Adding 9 Buttons
        for row in range(0, 3):
            for col in range(0, 3):
                button = Button(self.window, text="", width=3, height=1,
                                font=("bold", 36),
                                fg="black",
                                bg="lightpink",
                                command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)  # Add button to the list

        self.turn_label = Label(self.window, text="It's X's Turn", font=("bold", 28))
        self.turn_label.place(x=70, y=320)

        self.window.mainloop()

    def button_click(self, row, col):
        button_index = row * 3 + col
        button = self.buttons[button_index]
        if button["text"] == "":
            button["text"] = self.current_player
            button["state"] = "disabled"
            if self.current_player == "X":
                self.current_player = "O"
                self.turn_label["text"] = "It's O's Turn"
            else:
                self.current_player = "X"
                self.turn_label["text"] = "It's X's Turn"
            self.check_winner()

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        # Check if any player has won
        for combination in winning_combinations:
            a, b, c = combination
            if (
                self.buttons[a]["text"] == self.buttons[b]["text"] == self.buttons[c]["text"]
                and self.buttons[a]["text"] != ""
            ):
                winner = self.buttons[a]["text"]
                self.turn_label["text"] = f"{winner} won!"
                self.disable_buttons()
                return

        # Check for a tie
        if all(button["text"] != "" for button in self.buttons):
            self.turn_label["text"] = "Game Tied!"
            self.disable_buttons()

    def disable_buttons(self):
        for button in self.buttons:
            button["state"] = "disabled"


B = Board()
