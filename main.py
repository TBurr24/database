# Main Quiz App GUI
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = None  # To store the user's selected answer

    def check_answer(self):
        """Check if the user's answer is correct."""
        return self.user_answer == self.correct_answer

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.course = tk.StringVar()
        self.questions = []
        self.current_question_index = 0
        self.score = 0

        # Category Selection Window
        self.create_category_window()

    def create_category_window(self):
        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack(padx=10, pady=10)

        tk.Label(self.category_frame, text="Select a Category").pack(pady=5)
        self.course_selector = ttk.Combobox(self.category_frame, textvariable=self.course)
        self.course_selector['values'] = ["DS3810", "DS3860", "BMGT3510", "DS3850"]
        self.course_selector.pack()

        start_button = tk.Button(self.category_frame, text="Start Quiz Now", command=self.start_quiz)
        start_button.pack(pady=10)

    def start_quiz(self):
        selected_course = self.course.get()
        if selected_course:
            self.questions = get_questions(selected_course)
            if len(self.questions) >= 10:  # Ensure there are enough questions
                self.category_frame.destroy()
                self.create_quiz_window()
            else:
                messagebox.showerror("Error", "Not enough questions available in this category.")
        else:
            messagebox.showwarning("Select Category", "Please select a category to continue.")

    def create_quiz_window(self):
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack(padx=10, pady=10)

        self.question_label = tk.Label(self.quiz_frame, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.options = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.quiz_frame, text="", variable=self.options, value=str(i))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        self.feedback_label = tk.Label(self.quiz_frame, text="", fg="blue")
        self.feedback_label.pack(pady=5)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question.question_text)

        for i, option in enumerate(question.options):
            self.option_buttons[i].config(text=option)

        self.options.set(None)
        self.feedback_label.config(text="")

    def submit_answer(self):
        selected_index = self.options.get()
        if selected_index is None:
            messagebox.showwarning("No Answer", "Please select an answer before submitting.")
            return

        # Set the user's answer in the Question instance
        current_question = self.questions[self.current_question_index]
        current_question.user_answer = current_question.options[int(selected_index)]

        # Check if the answer is correct
        if current_question.check_answer():
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer was: {current_question.correct_answer}", fg="red")

        # Proceed to the next question or end the quiz after feedback
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.root.after(1000, self.show_question)  # Wait a moment before showing the next question
        else:
            self.root.after(1000, self.end_quiz)

    def end_quiz(self):
        self.quiz_frame.destroy()
        result_label = tk.Label(self.root, text=f"Quiz Finished! Your score is {self.score}/{len(self.questions)}.")
        result_label.pack(pady=20)
# Function to retrieve questions from the database and convert them to Question instances
def get_questions(course):
        conn = sqlite3.connect('quiz.db')
        c = conn.cursor()
        c.execute(f"SELECT question_text, option_1, option_2, option_3, option_4, correct_answer FROM {course}")
        rows = c.fetchall()
        conn.close()

        # Convert each row into a Question instance
        questions = [Question(row[0], row[1:5], row[5]) for row in rows]
        return questions
    
root = tk.Tk()
app = QuizApp(root)
root.mainloop()