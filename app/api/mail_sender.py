import smtplib
from email.mime.text import MIMEText


def send_mail(content) -> None:
    """
    Send email based on sepcific templates
    """
    msg = MIMEText(
        f"""
        Message from {content['name']} ({content['email']}):
        \n\n Issue type: {content['type_of_issue']}
        \n\n{content['message']}
        """
    )
    msg["Subject"] = f"Contact form with issue: {content['type_of_issue']}"
    msg["From"] = content['email']
    msg["To"] = "abnerteng16@gmail.com"

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as server:
        server.starttls()
        server.login("abnerteng16@gmail.com", "hbry dmcd xloz ahpg")
        server.sendmail(content['email'], "abnerteng16@gmail.com", msg.as_string())
        # server.sendmail("abnerteng16@gmail.com", "abnerteng16@gmail.com", msg.as_string())
