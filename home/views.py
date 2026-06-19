import datetime
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    context = {"year": datetime.datetime.now().year}
    return render(request, "home/index.html", context)

def about(request):
    return render(request, "home/about.html")

def projects(request):
    return render(request, 'home/projects.html')

from django.shortcuts import render
def certificates(request):
    certificates = [
        {
            "title": "AI and Python Development",
            "issuer": "Elevate Tech",
            "date": "February 4 - March 11, 2026",
            "description": "Completed a 120-hour intensive development track. Designed and engineered an AI Chatbot and an Face Recognition System utilizing Python.",
            "tags": ["Python", "AI Chatbot", "Face Recognition System", "CV", "Software Development"],
            "image":"certificates/elevatetech.png"
        },
        {
            "title": "Software Testing Fundamentals: Performance Testing & BDD",
            "issuer": "NIC College Ambassador Program × Code for Change",
            "date": "May 5, 2026",
            "description": "Completed foundational training in software quality assurance, focusing on Behavior-Driven Development (BDD) methodologies and performance testing principles to ensure software reliability and scalability.",
            "tags": ["Software Testing", "Performance Testing", "BDD", "Quality Assurance", "Agile Methodologies"],
            "image": "certificates/testing.png"
        },
        {
            "title": "3-Day AI and Robotics Bootcamp",
            "issuer": "Infomax College of IT and Management",
            "date": "July 14 - July 18, 2025",
            "description": "Hands-on technical bootcamp involving the end-to-end assembly, calibration, and logic programming of an autonomous Obstacle Avoiding Robot.",
            "tags": ["Robotics", "Obstacle Avoiding Robot", "Arduino", "Sensors", "Bootcamp"],
            "image": "certificates/robotics.png"
        },
        {
            "title": "Project Showcase at Provincial Ideathon (Gandaki Province) - CodeFest 2024",
            "issuer": "Code for Change",
            "date": "2024",
            "description": "Built and showcased 'Smart Traffic Light Automation System', an automated system designed to optimize traffic flow and reduce urban congestion during Nepal's major provincial hackathon.",
            "tags": ["Smart Traffic Light", "Smart City", "Automation", "Hackathon", "Project Showcase"],
            "image": "certificates/codefest.png",
        },
        {
            "title": "Science Exhibition 2024 (Grade XI - XII Category)",
            "issuer": "SOS Children's Villages / SOS HGS Gandaki",
            "date": "November 15, 2024",
            "description": "Developed and demonstrated a functional Fire Extinguishing Robot equipped with flame sensors and an automated suppression mechanism to combat fire hazards.",
            "tags": ["Fire Extinguishing Robot", "Hardware Engineering", "Automation", "Science Exhibition"],
            "image": "certificates/exibition.png"
        },
        {
            "title": "PEA Engineering & IT Quiz - 2081 B.S.",
            "issuer": "PEA Association & Pokhara Engineering College",
            "date": "2081 B.S.",
            "description": "Represented SOS Hermann Gmeiner Secondary School Gandaki as an active participant in the National Level Engineering & IT Quiz program designed for +2 Science studying students.",
            "tags": ["Quiz Competition", "Engineering", "IT", "Science"],
            "image": "certificates/pea.png"
        },
        {
            "title": "Certificate of Appreciation (Sports Volunteer Segment Summary)",
            "issuer": "SOS Children's Villages",
            "date": "January 2 -January 4, 2024",
            "description": "A close-up segment of the appreciation certificate earned for handling event logistics and support arrangements during the educational institution's major sports gatherings.",
            "tags": ["Volunteer", "Appreciation", "Leadership"],
            "image": "certificates/volunteer.png"
        }
    ]
    return render(request, "home/certificates.html", {"certificates": certificates})


def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves to database
            success = True
            form = ContactForm()  # clear the form
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form, 'success': success})
