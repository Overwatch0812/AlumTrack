
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Event,New,Blog,Contact
from accounts.models import CustomUser
from django.db.models import Q
from django.http import HttpResponse
from django.core.mail import send_mail,mail_admins

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def events(request):
    events=Event.objects.all()
    return render(request, 'events.html',{'events':events})

@login_required
def blog(request):
    blogs=Blog.objects.all()
    news=New.objects.all()
    return render(request,'blog.html',{'blogs':blogs,'news':news})

@login_required
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        mail=request.POST['mail']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact()
        contact.name=name
        contact.mail=mail
        contact.subject=subject
        contact.message=message
        contact.save()

        return redirect('/home')
    else:   
        return render(request,'contact.html')

@login_required
def findalumni(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.all()
        return render(request, 'display.html', {'user': user})

@login_required
def searchalumni(request):
    if request.method=='POST':
        search=request.POST['search']
        user=CustomUser.objects.filter(Q(name__icontains=search)|Q(graduation_year__icontains=search)| Q(course_name__icontains=search) )
        return render(request,'search.html',{'search':search,'user':user})
    else:
        return render(request,'search.html')

@login_required
def profile(request):
    if request.user.is_authenticated:
       return render(request,'profile.html')


@login_required
def edit_profile(request):
    if request.method=='POST':
        if 'img' in request.FILES:
            name = request.POST['name']
            email = request.POST['email']
            graduation_year = request.POST['graduation_year']
            course_name = request.POST['course_name']
            GR_number = request.POST['GR_number']
            contact_num=request.POST['contact_num']
            current_location=request.POST['current_location']
            current_job_designation=request.POST['current_job_designation']
            img=request.FILES['img']
           
            user=CustomUser.objects.get(id=request.user.id)
            user.name=name
            user.email=email
            user.graduation_year=graduation_year
            user.course_name=course_name
            user.GR_number=GR_number
            user.contact_num=contact_num
            user.current_location=current_location
            user.current_job_designation=current_job_designation
            user.img=img
           
            user.save()
            return redirect('/home')
            
        elif 'doc' in request.FILES:
            name = request.POST['name']
            email = request.POST['email']
            graduation_year = request.POST['graduation_year']
            course_name = request.POST['course_name']
            GR_number = request.POST['GR_number']
            contact_num=request.POST['contact_num']
            current_location=request.POST['current_location']
            current_job_designation=request.POST['current_job_designation']
            docs=request.FILES['doc']
            
           
            user=CustomUser.objects.get(id=request.user.id)
            user.name=name
            user.email=email
            user.graduation_year=graduation_year
            user.course_name=course_name
            user.GR_number=GR_number
            user.contact_num=contact_num
            user.current_location=current_location
            user.current_job_designation=current_job_designation
            user.documents=docs
           
            user.save()
            return redirect('/home')
        else:   
            name = request.POST['name']
            email = request.POST['email']
            graduation_year = request.POST['graduation_year']
            course_name = request.POST['course_name']
            GR_number = request.POST['GR_number']
            contact_num=request.POST['contact_num']
            current_location=request.POST['current_location']
            current_job_designation=request.POST['current_job_designation']
            
            

            user=CustomUser.objects.get(id=request.user.id)
            user.name=name
            user.email=email
            user.graduation_year=graduation_year
            user.course_name=course_name
            user.GR_number=GR_number
            user.contact_num=contact_num
            user.current_location=current_location
            user.current_job_designation=current_job_designation
            user.save()
            return redirect('/home')          
    else:
        return render(request,'edit_profile.html')


@login_required
def userdetail(request,id):
    if request.user.is_authenticated:
        user=CustomUser.objects.get(id=id)
        user1=CustomUser.objects.get(id=request.user.id)
        return render(request,'userdetail.html',{'user':user,'current_user':user1})