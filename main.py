from tkinter import *
import smtplib

window = Tk()
window.title('Email')

def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username == "" or password == "" or to == "" or subject == "" or body == "":
            notif.config(text='All fields required!', fg='red')
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('SMTP.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, finalMessage)
            notif.config(text='Email has been sent', fg='green')
    except:
        notif.config(text='Error sending email', fg='red')

def reset():
    usernameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    receiverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    bodyEntry.delete(0, 'end')

Label(window, text='Use the form below to send an email', font=('Calibri', 11)).grid(row=1, sticky=W, padx=5)
Label(window, text='Email', font=('Calibri', 11)).grid(row=2, sticky=W, padx=5)
Label(window, text='Password', font=('Calibri', 11)).grid(row=3, sticky=W, padx=5)
Label(window, text='To', font=('Calibri', 11)).grid(row=4, sticky=W, padx=5)
Label(window, text='Subject', font=('Calibri', 11)).grid(row=5, sticky=W, padx=5)
Label(window, text='Body', font=('Calibri', 11)).grid(row=6, sticky=W, padx=5)

notif = Label(window, text='', font=('Calibri', 11))
notif.grid(row=7, sticky=S, padx=5)

temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

usernameEntry = Entry(window, textvariable=temp_username)
usernameEntry.grid(row=2, column=0)
passwordEntry = Entry(window, show='*', textvariable=temp_password)
passwordEntry.grid(row=3, column=0)
receiverEntry = Entry(window, textvariable=temp_receiver)
receiverEntry.grid(row=4, column=0)
subjectEntry = Entry(window, textvariable=temp_subject)
subjectEntry.grid(row=5, column=0)
bodyEntry = Entry(window, textvariable=temp_body)
bodyEntry.grid(row=6, column=0)

Button(window, text='Send', command=send).grid(row=7, sticky=W, pady=15, padx=5)
Button(window, text='Reset', command=reset).grid(row=7, sticky=W, pady=45, padx=45)

window.mainloop()