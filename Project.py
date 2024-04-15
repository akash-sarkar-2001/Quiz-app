import tkinter as tkr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def check_answer():
    global i, num_correct
    user_answer = textbox.get().strip()
    correct_answer = answers[i].strip()
    if user_answer.lower() == correct_answer.lower():
        l2.config(text="Correct!")
        num_correct += 1
        write_result(user_answer, "Correct")
    else:
        l2.config(text="Incorrect.")
        write_result(user_answer, "Incorrect")
    check_button.config(state=tkr.DISABLED)
    next_button.config(state=tkr.NORMAL)

def next_question():
    global i
    i += 1
    if i < len(questions):
        l1.config(text=questions[i])
        textbox.delete(0, tkr.END)
        l2.config(text="")
        check_button.config(state=tkr.NORMAL)
        next_button.config(state=tkr.DISABLED)
    else:
        show_results()

def show_results():
    global num_correct
    num_questions = len(questions)
    score = round(num_correct / num_questions * 100, 2)
    message = f"You answered {num_correct} out of {num_questions} questions correctly.\nYour score is {score}%."
    l1.config(text=message)
    textbox.pack_forget()
    check_button.pack_forget()
    l2.pack_forget()
    next_button.destroy()

    f=open("results.txt", "w")     #result will be printed on results.txt file
    f.write(f"Number of correct answers: {num_correct}\n")
    f.write(f"Total questions: {num_questions}\n")
    f.write(f"Score: {score}%\n")
    send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)
    

    
def write_result(answer, status):
    f=open("resultswithQuestions.txt", "a")  #It will print questions with answers and results
    f.write(f"Question: {questions[i]}\n")
    f.write(f"User Answer: {answer}\n")
    f.write(f"Status: {status}\n\n")

with open("questions.txt", "r") as f:      #The question format should be, odd lines will contain questions and even lines will contain answers
    lines = f.readlines()
    questions = [i.strip() for i in lines[::2]]
    answers = [i.strip() for i in lines[1::2]] 
    
    

    
def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    # Set up the SMTP connection
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = sender_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, sender_password)
    except Exception as e:
        print("Failed to connect to the SMTP server.")
        print(str(e))
        return

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Add the body text to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the file
    attachment = open(attachment_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
    message.attach(part)

    # Send the email
    try:
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(str(e))

    # Close the connection
    server.quit()

questions_file = "location of questions.txt"
results_file = "location of results.txt"

# Usage example
sender_email = 'sender@gmail.com'
sender_password = 'created_by_google'  #You have to create an app password for this on google account
recipient_email = 'receiver@gmail.com'
subject = 'Email Subject'
body = 'This is the body of the email.'
attachment_path = results_file

i = 0
num_correct = 0

root = tkr.Tk()
root.title("Quiz App")
root.geometry("500x400")
root.configure(bg="light blue")

l1 = tkr.Label(root, text=questions[i])
l1.configure(bg="light blue")
l1.pack()

textbox = tkr.Entry(root)
textbox.pack()

check_button = tkr.Button(root, text="Check Answer", command=check_answer)
check_button.configure(bg="light blue")
check_button.pack()

l2= tkr.Label(root, text="")
l2.configure(bg="light blue")
l2.pack()

next_button = tkr.Button(root, text="Next", command=next_question, state=tkr.DISABLED)
next_button.configure(bg="light blue")
next_button.pack()

root.mainloop()