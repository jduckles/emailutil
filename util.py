import mimetypes
import smtplib
import getpass
import email
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import local_settings
import jinja2
import csv

# Use Mailgun credentials-
smtp_user = local_settings.smtp_user
smtp_passwd = local_settings.smtp_passwd

server = smtplib.SMTP(local_settings.smtp_host)
server.starttls()
server.login(smtp_user, smtp_passwd)

def send_email(email_to,email_subject,email_body,email_from=local_settings.default_sender):
    """
    Using a pre-rendered body, email
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = email_subject
    msg['From'] = email_from
    msg['To'] = email_to
    msg.attach(MIMEText(email_body, 'html'))
    to_address = email_to
    from_address = email_from
    server.sendmail(from_address, to_address, msg.as_string())

def readtemplate(template):
    with open(template) as fp:
        email_template = fp.read()
    return jinja2.Template(email_template)

def csv2dict(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = next(reader)
        return [dict(zip(header, row)) for row in reader]
