from django.db import models
import ssl
from email.message import EmailMessage
from mimetypes import guess_type
import smtplib
from django.conf import settings

class Contactus(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.TextField()
    timeStamp = models.DateField(auto_now_add=True, blank=True)

    def create_email(self, email_sender, email_password, recipient, subject, body, attachment_path=None):
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = recipient
        em['Subject'] = subject
        em.set_content(body)

        if attachment_path:
            file_name = attachment_path.split('/')[-1]
            mime_type, encoding = guess_type(file_name)
            if mime_type:
                app_type, sub_type = mime_type.split("/")
                with open(attachment_path, 'rb') as f:
                    file_data = f.read()
                em.add_attachment(file_data, maintype=app_type, subtype=sub_type, filename=file_name)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, recipient, em.as_string())

    def send_email(self, recipient, subject, body, attachment_path=None):
        email_sender = settings.EMAIL_HOST_USER
        email_password = settings.EMAIL_HOST_PASSWORD
        self.create_email(email_sender, email_password, recipient, subject, body, attachment_path)

    def notify_admin_and_user(self, admin_email, attachment_path=None):
        email_sender = settings.EMAIL_HOST_USER
        email_password = settings.EMAIL_HOST_PASSWORD

        # Email to the user
        user_subject = 'Regarding Your Contact Request'
        user_body = f'Hello {self.name},\n\nThank you for reaching out to us. We will get back to you shortly.\n\nBest regards,\nYour Company'
        self.send_email(self.email, user_subject, user_body, attachment_path)

        # Email to the admin
        admin_subject = f'New Contact Request from {self.name}'
        admin_body = f'You have received a new contact request.\n\nName: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nSubject: {self.subject}'
        self.send_email(admin_email, admin_subject, admin_body, attachment_path)
