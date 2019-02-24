"""FirstStackSolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pages import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^content-management-solutions$',views.contentmanagemgtsys, name='contentmanagemgtsys'),
    url(r'^services$', views.services, name='services'),
    url(r'^database-app-dev$', views.dbappdev, name='database-app-dev'),
    url(r'^desktop-app-dev$', views.desktopappdev, name='desktop-app-dev'),
    url(r'^mobile-app-design-dev$', views.mobileappdesignanddevelopment, name='mobile-app-design-dev'),
    url(r'^web-design-dev$', views.websitedesignanddevelopment, name='web-design-dev'),
    url(r'^contact-us$', views.contactus, name='contact-us'),
    url(r'^how-we-work$',views.howwework, name='how-we-work'),
    url(r'^e-commerce-solutions$',views.ecommercesol, name='e-commerce-solutions'),
    url(r'^vulnerability-assessment$', views.vulnerability_Scanning, name='vulnerability-assessment'),
    url(r'^penetration-testing$', views.Penetration_Testing, name='penetration-testing'),
    url(r'^security-architecture$', views.security_architecture, name='security-architecture'),
    url(r'^audit-compliance$', views.audit_compliance, name='audit-compliance'),
    url(r'^security-training$', views.security_training, name='security-training'),
    url(r'^risk-assessment$', views.risk_assessment, name='risk-assessment'),
    url(r'^amazon-web-services$', views.aws, name='amazon-web-services'),
    url(r'^cyber-security$',views.cyber_security, name='cyber-security'),
    url(r'^software-development$', views.software_development, name='software-development')
]
