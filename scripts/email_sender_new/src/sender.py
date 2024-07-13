"""
Sender
"""
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from bs4 import BeautifulSoup


class AutoMailSender:
    """
    Class for AutoMailSender
    """
    def __init__(
        self,
        event: str,
        path: str,
        link: str,
        subject: str,
        yourmail: str,
        yourpassword: str
    ) -> None:
        self.event = event
        self.path = path
        self.link = link
        self.subject = subject
        self.yourmail = yourmail
        self.yourpassword = yourpassword
        self.event_mapper = {
            "Member Recruiting": "memrecruit",
            "Director Recruiting": "dirrecruit",
            "Corporate Visiting": "corpvisit",
        }

    def get_data(self) -> pd.DataFrame:
        """
        You can customize ouptut lists, maybe time, link, etc.
        """
        data = pd.read_csv(self.path)
        return data

    def send_mail(
        self,
        infos: pd.DataFrame
    ) -> None:
        """
        execute this function to send mail by smtplib
        
        Args:
            Changed based on your input .csv file
        """
        for i in range(len(infos)):
            with open(
                f"content/{self.event_mapper[self.event]}.html", 'r', encoding="utf-8"
            ) as html:
                soup = BeautifulSoup(html, "html.parser")
                soup.find('p', id="name").string = f"{infos['name'][i]} 同學您好，"
                soup.find(
                    "ol", id="info"
                ).find(
                    "li", id="time"
                ).find(
                    "span", style="color: red;"
                ).string = infos["date"][i] + " " + infos["time"][i]
                soup.find(
                    "ol", id="info"
                ).find(
                    "li", id="link"
                ).find("a")["href"] = infos["mt_link"][i]
                soup.find(
                    "ol", id="info"
                ).find(
                    "li", id="itv_link"
                ).find("a")["href"] = self.link

            content = MIMEMultipart()

            if self.event.split(" ")[-1] == "Recruiting":
                content["subject"] = f"{self.subject}_{infos['name'][i]} 同學"
            else:
                content["subject"] = f"{self.subject}"

            content["from"] = self.yourmail
            content["to"] = infos["email"][i]
            content.attach(MIMEText(soup, "html"))

            with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
                try:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(self.yourmail, self.yourpassword)
                    smtp.send_message(content)
                    print(f'{infos["name"][i]} Status: Success')
                    time.sleep(3)

                except Exception as exc:
                    print(f"Error message: {exc}")
                    print(f'{infos["name"][i]} Status: Failed')
