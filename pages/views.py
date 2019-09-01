from django.shortcuts import render

from django.urls import reverse

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'index.html', context=None)


def about(request):
    return render(request, 'about.html', context=None)


def contentmanagemgtsys(request):
    return render(request, 'contentManagementSolutions.html', context=None)

def services(request):
    return render(request, 'services.html', context=None)


def dbappdev(request):
    return render(request,'DatabaseApplicationDevelopment.html', context=None)

def desktopappdev(request):
    return render(request, 'DesktopApplicationDevelopment.html', context=None)


def mobileappdesignanddevelopment(request):
    return render(request, 'MobileAppDesignAndDevelopment.html', context=None)


def websitedesignanddevelopment(request):
    return render(request, 'WebDesignAndDevelopment.html', context=None)


def ecommercesol(request):
    return render(request, 'eCommerceWebsiteSolutions.html', context=None)


def contactus(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    from_email = request.POST.get('from_email')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['martins.okuonghae@gmail.com'], fail_silently=False)
            return HttpResponseRedirect(reverse('contact-us'))
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request, 'contactUs.html', context=None)


def howwework(request):
    return render(request, 'HowWeWork.html', context=None)


def vulnerability_Scanning(request):
    return render(request, 'VulnerabilityAssessment.html', context=None)


def Penetration_Testing(request):
    return render(request, 'PenetrationTesting.html', context=None)

def risk_assessment(request):
    return render(request, 'RiskAssessment.html', context=None)


def security_architecture(request):
    return render(request, 'SecurityArchitecture.html', context=None)


def security_training(request):
    return render(request, 'SecurityTraining.html', context=None)


def audit_compliance(request):
    return render(request, 'AuditCompliance.html', context=None)


def aws(request):
    return render(request, 'AmazonWebServices.html', context=None)


def cyber_security(request):
    return  render(request, 'CyberSecurity.html', context=None)


def software_development(request):
    return render(request, 'SoftwareDevelopment.html', context=None)



