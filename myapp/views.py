from django.shortcuts import render,redirect
from . models import Contact
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'index.html')

def single(request):
	return render(request, 'index.html')

def contact(request):
	if request.method == 'POST':
		Contact.objects.create(
			name=request.POST.get('name', ''),
			email=request.POST.get('email', ''),
			subject=request.POST.get('subject', ''),
			message=request.POST.get('message', ''),
		)
		msg = "Contact saved successfully. I will reach out to you very soon."
		return render(request, 'index.html', {'msg': msg})
	return redirect('index')
