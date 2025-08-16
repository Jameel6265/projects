from django.shortcuts import render, redirect
from .models import About,Skills,Profile,Education,Experience, Contact
from .forms import ContactForm
from django.contrib import messages
import logging
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    import logging
    logger = logging.getLogger('TESTING')
    
    about = About.objects.first()
    skills = Skills.objects.first()
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('id')
    experiences = profile.experiences.all().order_by('id')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact.save()
            send_mail(
                subject=f"New Contact: {form.cleaned_data['subject']}",
                message=f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['abdulhameed5122000@gmail.com'],  # <- Change to your email
                fail_silently=False,
            )
            logger.debug("Form submitted successfully and email sent.")
            messages.success(request, "Email Sent! Thank you for contacting me! I’ll get back to you soon.")
            return redirect('home')
        else:
            logger.debug('Form Validation Failure')
            messages.error(request, "Oops! Something went wrong. Please correct the form and try again.")


        return render(request, 'portfolio/index.html', {
            'form': form,
            # 'name': name,
            # 'email': email,
            # 'subject': subject,
            # 'message': message,
            'about': about,
            'skills': skills,
            'profile': profile,
            'education': education,
            'experience': experiences
        })

    else:
        form = ContactForm()

    return render(request, 'portfolio/index.html', {
        'form': form,
        'about': about,
        'skills': skills,
        'profile': profile,
        'education': education,
        'experience': experiences
    })

