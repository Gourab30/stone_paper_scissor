import tkinter as tk
from tkinter import messagebox
import random

# Dictionaries for mapping
choice_dict = {"Stone": 1, "Paper": 2, "Scissor": 3}
reverse_dict = {1: "Stone", 2: "Paper", 3: "Scissor"}

# Core game logic
def play(user_choice):
    computer_choice = random.choice([1, 2, 3])
    user_value = choice_dict[user_choice]

    result_text = f"Your choice: {user_choice}\nComputer's choice: {reverse_dict[computer_choice]}\n"

    if user_value == computer_choice:
        result = "It's a draw!"
    elif (user_value == 1 and computer_choice == 3) or \
         (user_value == 2 and computer_choice == 1) or \
         (user_value == 3 and computer_choice == 2):
        result = "🎉 You win!"
    else:
        result = "😞 You lose!"

    result_label.config(text=result_text + "\n" + result)

# Create main window
root = tk.Tk()
root.title("Stone Paper Scissor Game")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Stone Paper Scissor", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

for item in ["Stone", "Paper", "Scissor"]:
    tk.Button(button_frame, text=item, font=("Arial", 14), width=10, command=lambda c=item: play(c)).pack(side=tk.LEFT, padx=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="#333")
result_label.pack(pady=20)

# Run the app
root.mainloop()
