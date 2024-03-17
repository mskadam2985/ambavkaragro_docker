from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

from .models import *  

# Create your views here.
def home(request):
    return render(request, 'web/home.html')


def about(request):
    return render(request,'web/about.html')

def vision(request):
    return render(request, 'web/vision.html')

def mission(request):
    return render(request, 'web/mission.html')

def corevalue(request):
    return render(request, 'web/corevalue.html')

def brands(request):
    return render(request, 'web/brands.html')

def services(request):
    return render(request, 'web/services.html')

def products(request):
    return render(request, 'web/products.html')

def testimonial(request):
    
    testimonials = Testimonial.objects.all()

    context = {'testimonials': testimonials}
    return render(request, 'web/testimonials.html', context)

def contact(request):
    if request.method == 'POST':
        m_f_name = request.POST.get('fname')
        m_l_name = request.POST.get('lname')
        m_email = request.POST.get('email') 
        m_tel = request.POST.get('tel') 
        m_message = request.POST.get('message') 

        data = {
            'f_name': m_f_name,
            'l_name': m_l_name,
            'email': m_email,
            'tel' : m_tel,
            'message': m_message 
        }

        #print(data)

        message = '''
        New Message: {}
        
        From: {}
        
        '''.format(data['message'], data['email'])

        

        send_mail(
            data['f_name'], # subject
            message, # message
            m_email, # from email
            ['ambavkaragro@gmail.com'] # to email
        )
    return render(request, 'web/contact.html', {})