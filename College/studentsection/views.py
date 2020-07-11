from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import student,UserProfile,Profile
from django.contrib.auth import authenticate,login,logout
from .forms import Userupdateform,ProfileUpdateform
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User



def college(request):
	return render(request,'studentsection/college.html')


def Home(request):
	return render(request,'studentsection/Home.html')
# Create your views here.
def Add(request):
	if request.method=='POST':
		b=request.POST
		c=student(Name=b.get('name'),
				 Roll_Number=b.get('roll'),
				 Email=b.get('mail'),
				 College=b.get('college'),
				 passedout_year=b.get('passout'),
				 course_name=b.get('course'),
				 course_fee=b.get('fees'),
				 Institute_area=b.get('location'),
				 Fieles=request.FILES['pdf'],
				 Image=request.FILES['pic'],

				 )
		#uploaded_file=request.FILES['pdf']
		#fs=FileSystemStorage()
		#name=fs.save(uploaded_file.name,uploaded_file)


		c.save()
	return render(request,'studentsection/add.html')
	
def display(request):
	b=student.objects.all()
	return render(request,'studentsection/display.html',{'d':b})
def delete(request,pk):
	k=student.objects.get(pk=pk)
	if request.method=='POST':
		d=request.POST
		k.delete()
		return redirect (display)

	return render(request,'studentsection/delete.html',{'data':k})

def Update(request,pk):
	h=student.objects.get(Name=pk)
	if request.method=='POST':
		g=request.POST
		h.Name=g.get('name')
		h.Email=g.get('email')
		h.passedout_yeat=g.get('pass')
		h.course_name=g.get('course')
		h.course_fee=g.get('fee')
		h.save()
		return redirect(display)
	return render(request,'studentsection/update.html',{'data':h})

def search(request):
	if request.method=='POST':
		k=request.POST
		Name=k.get('name')
		getdata=student.objects.filter(Name=Name)
		return render(request,"studentsection/search.html",{'data':getdata})

	return render(request,"studentsection/search.html")


def register(request):
	if request.method=='POST':
		d=request.POST
		if d.get("sub"):
			c=UserProfile.objects.create_user(
				username = d.get('uname'),
				password = d.get('pswd'),
				email = d.get('email'),
				)
			return render(request,"studentsection/Mainpage.html",{"msg":"User Created Successfully!. Please Login"})

	return render(request,'studentsection/registration.html')
	

def Elogin(request):
	if request.method=='POST':
		d=request.POST
		if d.get("login"):
			user = authenticate(
				username=d.get("uname"),
				password=d.get("pswd")
				)
			if user:
				login(request,user)
				return redirect(Home)
			else:
				return render(request,"studentsection/login.html",{"msg":"Login failed."})

	return render(request,'studentsection/login.html')

def Elogout(request):
	logout(request)
	return redirect(Main)

def Main(request):
	return render(request,'studentsection/Mainpage.html')

#@login_required
def profile(request):
	if request.method=='POST':
		u_form=Userupdateform(request.POST,instance=request.user)

		p_form=ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()

			messages.success(request,f'Updated Successfully')

			return redirect(profile)
	else:
		u_form=Userupdateform(instance=request.user)
		p_form=ProfileUpdateform(instance=request.user.profile)
	
	context={'u_form':u_form,
			'p_form':p_form
			}
			
	return render(request,'studentsection/profile.html',context)