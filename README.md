# Quiz App

A simple Python-based quiz application with a graphical user interface (GUI) that allows users to answer a series of questions, get instant feedback, and view their final score. User responses and results are saved to files for later review.

## Features

- Presents a series of quiz questions in a graphical window
- Checks user answers in real time and provides immediate feedback (correct/incorrect)
- Tracks the number of correct responses and calculates the final score
- Saves a summary of results (`results.txt`) and detailed responses (`resultswithQuestions.txt`)
- Automatically sends the results file via email upon completion

## Example Questions

Some sample questions included:
- What is the capital of France?
- Who is the current President of the United States?
- What is the largest planet in our solar system?
- How many minutes are in a full week?
- What country drinks the most coffee per capita?

## Technologies Used

- Python
- Tkinter (for GUI)
- Standard Python libraries (for file I/O and email sending)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/akash-sarkar-2001/Quiz-app.git
   cd Quiz-app
   ```

2. **Install Python (if not already installed):**
   
   Ensure you have Python 3.x installed on your system.

3. **Run the Application:**

   ```bash
   python Project.py
   ```

   This will launch the GUI window for the quiz.

## File Structure

- `Project.py`: Main source code for the quiz app.
- `questions.txt`: List of questions and correct answers.
- `results.txt`: Summary of user's quiz performance.
- `resultswithQuestions.txt`: Detailed log of each question, user answer, and correctness.

## How It Works

- The quiz loads questions from `questions.txt`.
- The user enters answers in a GUI window.
- After each answer, the app provides correctness feedback.
- At the end of the quiz, results are saved and can be automatically emailed.

## License

This project currently does not specify a license.
