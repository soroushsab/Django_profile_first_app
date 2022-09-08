from django.shortcuts import render
from index.models import Skills,Educations,ContactMe,Content,Experience,Languages

def index(request):
    content = Content.objects.all()
    education = Educations.objects.order_by('-start')
    experienc = Experience.objects.order_by('-start')
    skill = Skills.objects.all()
    language = Languages.objects.all()
    index_dic = {
        'info': {
            'title':content[0].Firstname +' ' + content[0].Lastname,
            'Firstname':content[0].Firstname,
            'Lastname':content[0].Lastname,
            'Contactnumber':content[0].Contactnumber,
            'Email':content[0].Email,
            'LinkedIn':content[0].LinkedIn,
            'GitHub':content[0].GitHub,
            'Profile_description':content[0].Profile_description,
        },
        'educations':
            education,
        'experience':
            experienc,
        'languages':
            language,
        'skills':
            skill,
    }
    return render(request,'index/index.html',context=index_dic)
def login(request):
    login_dic = {

    }
    return render(request,'index/login.html',context=login_dic)
def contactme(request):
    contactme_dic = {

    }
    return render(request,'index/contactme.html',context=contactme_dic)
def dashboard(request):
    dashboard_dic = {
        'title':'sina',
        'loc':'London',
    }
    return render(request,'index/dashboard.html',context=dashboard_dic)