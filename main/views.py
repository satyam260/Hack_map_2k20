from django.shortcuts import render
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import Register
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"main/index.html",{})

def faq(request):
    return render(request,"main/faq.html",{})

def register1(request):
	if(request.method=='POST'):
		form = RegistrationForm()
		if form.is_valid():
			form.clean()
			form.save()
			return render(request,"main/form.html",{'form':form})
		else:
			print("Errors " ,form.errors)
			print("HAS ERROR : ",form.has_error)
			return render(request,"main/failed.html",{'form':form})
		
	else:
		form = RegistrationForm()
		return render(request,"main/form.html",{'form':form})


class register(CreateView):
	model = Register
	fields = ['teamName', 'emailAddress', 'github_username', 'project_repo_name', 'teamSize', 'userDetail1', 'userDetail2', 'userDetail3','fieldProject', 'title', 'synopsis']
	context_object_name = 'form'
	template_name = 'main/form.html'
	def get_success_url(self):
		messages.success(self.request,"Form Submitted SuccessFully!")
		return reverse('register')
	