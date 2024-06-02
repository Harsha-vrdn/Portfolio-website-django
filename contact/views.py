from django.shortcuts import render
from .models import Contactus
from django.conf import settings

def contact_us(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        subject = request.POST["subject"]

        contact = Contactus(name=name, phone=phone, email=email, subject=subject)
        contact.save()

        # Path to the attachment (optional)
        attachment_path = 'static/pdf/Harsha_resume.pdf'  # Update this if needed

        # Send emails to user and admin
        admin_email = settings.EMAIL_HOST_USER
        contact.notify_admin_and_user(admin_email, attachment_path)

    return render(request, "contact.html")
