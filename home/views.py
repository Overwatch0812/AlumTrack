
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Event,New,Blog
from accounts.models import CustomUser
from django.db.models import Q

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
        name = request.POST['name']
        email = request.POST['email']
        graduation_year = request.POST['graduation_year']
        course_name = request.POST['course_name']
        GR_number = request.POST['GR_number']

        user=CustomUser.objects.get(id=request.user.id)
        user.name=name
        user.email=email
        user.graduation_year=graduation_year
        user.course_name=course_name
        user.GR_number=GR_number
        user.save()

        if 'img' in request.FILES:
            img=request.FILES['img']
            user.img=img
            user.save()
            return redirect('/home')
    else:
        return render(request,'edit_profile.html')


@login_required
def userdetail(request,id):
    if request.user.is_authenticated:
        user=CustomUser.objects.get(id=id)
        return render(request,'userdetail.html',{'user':user})