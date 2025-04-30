import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is a test email from Python.")
msg["Subject"] = "Hello from Python"
msg["From"] = "you@example.com"
msg["To"] = "friend@example.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("you@example.com", "your-password")
    server.send_message(msg)