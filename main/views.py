from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.
def home(request):
    return render(request,"main/index.html",{})

def faq(request):
    return render(request,"main/faq.html",{})

def register(request):
	if(request.method=='POST'):
		form = RegistrationForm()
		if form.is_valid:
			form.save()
			form = RegistrationForm()
			return render(request,"main/form.html",{'form':form})
		
	else:
		form = RegistrationForm()
		return render(request,"main/form.html",{'form':form})


    