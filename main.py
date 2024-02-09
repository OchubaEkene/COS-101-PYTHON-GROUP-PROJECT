import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


# Function the display the current question and its answer choices
def show_question():
    # Get the current question from quiz_data
    question = quiz_data[current_question]

    # Update the question from quiz_data
    qs_label.config(text=question["question"])

    # Get answer choices for the current question
    choices = question["choices"]
    # Update the text of each choice button with the answer choices
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    # Reset feedback label and disable the "Next" button
    feedback_label.config(text="")
    next_btn.config(state="disabled")


# Function the check the selected answer, update the score, and give feedback.
def check_answer(choice):
    # Get the current question from quiz_data
    question = quiz_data[current_question]
    # Get the selected choice from the button that was clicked
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice is correct
    if selected_choice == question["answer"]:
        global score
        # Update the score and display feedback for correct answer
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        # Display feedback for incorrect answer
        feedback_label.config(text="Incorrect!", foreground="red")

    # Disable all choice buttons and enable the "Next" button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to Restart the Quiz
def restart_quiz():
    global current_question, score
    # Reset current_question and score
    current_question = 0
    score = 0
    # Update the score label
    score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))

    # Enable all choice buttons
    for button in choice_btns:
        button.config(state="normal")

    # Display the first question
    show_question()

# Function to move on to the next question or end the quiz if the questions have finished
def next_question():
    global current_question
    # Move to the next question
    current_question += 1

    # Check if there are more questions
    if current_question < len(quiz_data):
        # Display the next question
        show_question()
    else:
        # Display a message box with the final score and exit the application
        messagebox.showinfo("QUIZ COMPLETED",
                            "QUIZ COMPLETED! Final Score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Creating the Tkinter window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x650")
# Apply a flatly theme using ttkbootstrap
style = Style(theme="flatly")
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))
# Create and configure labels, buttons, and other UI elements
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=10)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

score = 0
score_label = ttk.Label(
    root,
    text="Score:0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)

score_label.pack(pady=0)
# Next Button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Restart Button
restart_btn = ttk.Button(
    root,
    text="Restart Quiz",
    command=restart_quiz
)

restart_btn.pack(pady=20)

current_question = 0

# Display the first question
show_question()

# Run the Tkinter event loop
root.mainloop()
