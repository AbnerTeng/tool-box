"""
Sender
"""
import os
from typing import List, Tuple
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from .constants import INTERVIEW


class AutoMailSender:
    """
    Class for AutoMailSender
    """
    def __init__(
        self, event: str, path: str,
        yourmail: str, yourpassword: str
    ) -> None:
        self.event = event
        self.path = path
        self.yourmail = yourmail
        self.yourpassword = yourpassword

    def get_data(self) -> Tuple:
        """
        You can customize ouptut lists, maybe time, link, etc.
        """
        if self.event == 'personal_interview':
            with open(f'{self.path}', 'r', encoding='utf-8') as file:
                data = file.readlines()
                data = [i.strip().split(',') for i in data]
                date  = [i[2] for i in data]
                __time__ = [i[3] for i in data]
                name = [i[1] for i in data]
                mt_link = [i[4] for i in data]
                email = [i[0] for i in data]

        return date, __time__, name, mt_link, email

    def send_mail(
        self,
        col1: List[str],
        col2: List[str],
        col3: List[str],
        col4: List[str],
        col5: List[str]
    ) -> None:
        """
        execute this function to send mail by smtplib
        
        Parameters
        ----------
        | date | time | name | mt_link | email |
        """
        for idx, _ in enumerate(col1):
            with open(f'{os.getcwd()}/content/{self.event}.html', 'r', encoding = 'utf-8') as html:
                soup = BeautifulSoup(html, 'html.parser')
                soup.find('p', id = 'name').string = f'{col3[idx]} 同學您好，'
                soup.find(
                    'ol', id = 'info'
                ).find(
                    'li', id = 'time'
                ).find(
                    'span', style='color: red;'
                ).string = col1[idx] + ' ' + col2[idx]
                soup.find(
                    'ol', id = 'info'
                ).find(
                    'li', id = 'link'
                ).find('a')['href'] = col4[idx]
                soup.find(
                    'ol', id = 'info'
                ).find(
                    'li', id = 'itv_link'
                ).find('a')['href'] = INTERVIEW

            content = MIMEMultipart()
            content['subject'] = f'第五屆 NTUDAC 社員招募 | 個人面試時間通知_{col3[idx]} 同學'
            content['from'] = self.yourmail
            content['to'] = col5[idx]
            content.attach(MIMEText(soup, 'html'))
            with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
                try:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(self.yourmail, self.yourpassword)
                    smtp.send_message(content)
                    print(f'{col3[idx]}: Success')
                    time.sleep(3)
                except ValueError as exc:
                    print(f'Error message: {exc}')
