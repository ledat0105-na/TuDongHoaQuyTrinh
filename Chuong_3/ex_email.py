import smtplib
from email.mime.text import MIMEText

# Configuration
port = 587
smtp_server = "smtp.gmail.com"
login = "tle723772@gmail.com" 
password = "nhon japa jldw sxfx" 

sender_email = "tle723772@gmail.com"
receiver_email = "lenguyenhai43@gmail.com"

# Plain text content
text = """\
Hi, Hải Lê 
"""

# Create MIMEText object
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

# Send the email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls() 
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')