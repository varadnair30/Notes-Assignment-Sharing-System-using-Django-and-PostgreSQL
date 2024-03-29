from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import *
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
def index(request):
	return render(request,'index.html')
def alogin(request):
    if request.method =='POST':
        User_Name = request.POST['uname']
        Password = request.POST['psw']

        user = auth.authenticate(username=User_Name,password=Password)
        if user is not None:
            auth.login(request, user)
            return redirect("../admin/")
        else:
            return HttpResponse("Invalid User Name or Password")
    else:
        return render(request,'alogin.html')    
def tlogin(request):
    if request.method=="POST":
        uid=request.POST['id']
        uname=request.POST['t_name']
        upasswd=request.POST['Password']
        rs=Teacher.objects.filter(t_name=uname,t_pass=upasswd,id=uid)
        if rs:
            request.session["t_name"]=uname
            for r in rs:
                request.session["id"]=r.id
                request.session["t_name"]=r.t_name
                return redirect('../thome/')
        else:
            return HttpResponse("Invalid User Name or Password")
    else:
        return render(request,'tlogin.html')
def thome(request):
    if request.session.has_key("id"):
        id=request.session["id"]
        rs = Teacher.objects.filter(id=id)
        return render(request,'thome.html',{'rs':rs})
def tupload(request):
    if request.POST:
        by = request.session["t_name"]
        year = request.POST["r2"]
        branch = request.POST["r1"]
        sub_id = request.POST["t1"]
        upload = request.FILES["doc"]
        rs = Student.objects.filter(s_year=year,s_branch=branch)
        if rs:
            mobj = TeacherUpload()
            mobj.send_name = by
            mobj.branch = branch
            mobj.year = year
            mobj.sub_id = sub_id
            mobj.upload_file = upload
            mobj.save()
            return render(request,'tupload.html',{'info':'file uploaded'})
        else:
           return render(request, 'tupload.html', {'info': 'No Student for this year or branch is registered'})
    else:
        return render(request, 'tupload.html')
def tsubmissions(request):
    forr=request.session["t_name"]
    rs=StudentUpload.objects.filter(t_name=forr) 
    return render(request,'tsubmissions.html',{'records':rs})
def tuploaded(request):
    by=request.session["t_name"]
    rs=TeacherUpload.objects.filter(send_name=by)
    return render(request,'teacheroutbox.html',{'records':rs})
def tlogout(request):
    try:
        del request.session["t_name"]
    except KeyError:
        pass
    return redirect('/')
def slogin(request):
    if request.method=="POST":
        uid=request.POST['id']
        uname=request.POST['s_name']
        upasswd=request.POST['Password']
        branch=request.POST['r1']
        year=request.POST['r2']
        rs=Student.objects.filter(id=uid,s_name=uname,s_pass=upasswd,s_branch=branch,s_year=year)
        if rs:
            request.session["s_name"]=uname
            request.session["s_year"]=year
            for r in rs:
                request.session["id"]=r.id
                request.session["s_name"]=r.s_name
                request.session["s_branch"]=r.s_branch
                request.session["s_year"]=r.s_year
                return redirect('../shome/')
        else:
            return HttpResponse("Invalid User Name or Password or year")
    else:
        return render(request,'slogin.html')
def shome(request):
    if request.session.has_key("id"):
        id=request.session["id"]
        rs = Student.objects.filter(id=id)
        return render(request,'shome.html',{'rs':rs})
def supload(request):
    if request.POST:
        by = request.session["s_name"]
        branch = request.session["s_branch"]
        year = request.session["s_year"]
        sub_id = request.POST["t1"]
        upload = request.FILES["doc"]
        try:
            t = Branches.objects.filter(id=sub_id)
            t_name = t[0].teacher_name
        except IndexError:
            return HttpResponse("Unable to Upload")    
        rs = TeacherUpload.objects.filter(sub_id=sub_id,year=year,branch=branch)
        if rs:
            mobj = StudentUpload()
            mobj.send_name = by
            mobj.t_name = t_name
            mobj.branch = branch
            mobj.year = year
            mobj.sub_id = sub_id
            mobj.upload_file = upload
            mobj.save()
            return HttpResponse("File Uploaded")
        else:
            return HttpResponse("Unable to Upload...may be your subject,year or branch not matched")
    else:
        return render(request, 'supload.html')  
def snotes(request):
    rs = TeacherUpload.objects.filter(year=request.session["s_year"],branch=request.session["s_branch"])
    return render(request, 'snotes.html', {'rs':rs})
def suploadedfiles(request):
    by=request.session["s_name"]
    rs=StudentUpload.objects.filter(send_name=by)
    return render(request,'suploadedfiles.html',{'records':rs})
def slogout(request):
    try:
        del request.session["s_name"]
    except KeyError:
        pass
    return redirect('/')
def contact(request):
	return render(request,'contact.html')