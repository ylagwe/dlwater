from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home(request):
    return render(request, 'water/home.html')

def products(request):
    return render(request, 'water/products.html')

def shop(request):
    return render(request, 'water/shop.html')

def about(request):
    return render(request, 'water/about.html')

def contact(request):
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        phone   = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        msg     = request.POST.get('message', '').strip()

        # Save to database
        ContactMessage.objects.create(
            name=name, email=email, phone=phone,
            subject=subject, message=msg
        )

        # Send email to business
        email_body = f"""
New enquiry from D & L Water Solutions website
================================================

Name    : {name}
Email   : {email}
Phone   : {phone or 'Not provided'}
Subject : {subject}

Message:
{msg}

================================================
This message was submitted via dlwatersolutions.com contact form.
        """.strip()

        try:
            send_mail(
                subject=f'[Website Enquiry] {subject} — {name}',
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception:
            pass  # Still show success even if email fails (saved to DB)

        messages.success(request, f'Thank you {name}! Your message has been sent. We will get back to you shortly.')
        return redirect('contact')

    return render(request, 'water/contact.html')
