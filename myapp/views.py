from django.shortcuts import render,redirect
from . models import Contact
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	Contact.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		subject=request.POST['subject'],
		message=request.POST['message'],
		)
	msg="contact saved succesfully.will reach you very soon "
	return render(request,'index.html',{'msg':msg})
