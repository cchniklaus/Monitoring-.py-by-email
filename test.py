# coding=iso-8859-1
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import sys

def send_email(from_email: str, password: str, subject: str, body: str, to_email: str="your_email@example.com") -> None:
    """
    send email
    :param from_email: sender email address
    :param password: sender email password
    :param subject: email subject
    :param body: email body
    :param to_email: recipient email address
    :return None
    """
    # create message object instance
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # add body to email
    msg.attach(MIMEText(body, "plain"))

    try:
        # qq mail server
        server = smtplib.SMTP("smtp.qq.com", 587)
        server.starttls()
        server.login(from_email, password) 
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("email sent successfully!")
    except Exception as e:
        print(f"email sent failed：{e}")
        
        


def main(sender_email: str, sender_password: str, recipient_email: str) -> None:
    try:
        # your codes
        print("The program has started running...")
        ################## input your codes here ##################
        time.sleep(5)  
        result = 10 / 0
        ################################################
        print("The program has finished...")
        message = "The program has finished running successfully!"
        send_email(from_email=sender_email, password=sender_password, subject="Program Runtime Notification",
                   body=message, to_email=recipient_email)

    except Exception as e:
        # Catch the exception and send an email notification
        error_message = f"The program encountered an error! Error message:{e}"
        print(error_message)
        send_email(from_email=sender_email, password=sender_password, subject="Program Runtime Error Notification",
                   body=error_message, to_email=recipient_email)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError("Usage: python test.py sender_email sender_password recipient_email")
        #print("Usage: python test.py sender_email sender_password recipient_email")
        #sys.exit(1)
    else:
        sender_email = sys.argv[1]
        sender_password = sys.argv[2]
        recipient_email = sys.argv[3]
        main(sender_email=sender_email, sender_password=sender_password, recipient_email=recipient_email)


