from django.db import models

# Create your models here.
class Register(models.Model):
	#id_1=models.UUIDField(default=uuid.uuid4, editable=True)
	CHOICES=(
		(1,'1'),
		(2,'2'),
		(3,'3'),
		)
	teamName=models.CharField(primary_key=True,max_length=100, null=False, blank=False,verbose_name="Team Name")
	emailAddress=models.EmailField(null=False,verbose_name="Email Address")
	github_username=models.CharField(max_length=150, null=False, blank=False,verbose_name="GitHub Username")
	project_repo_name=models.CharField(max_length=150, null=False, blank=False,verbose_name="Project Repository Name")
	teamSize=models.IntegerField(choices=CHOICES,null=False,default=1,verbose_name="Team Size")
	userDetail1=models.CharField(max_length=150, null=False, blank=False,verbose_name="User 1 Name")
	userDetail2=models.CharField(max_length=150,blank=True,null=True,verbose_name="User 2 name")
	userDetail3=models.CharField(max_length=150,blank=True,null=True,verbose_name="User 3 name")
	fieldProject=models.CharField(max_length=30,null=False, blank=False,verbose_name="Field of Project")
	title=models.CharField(max_length=50,null=False, blank=False,verbose_name="Title of Project")
	synopsis=models.TextField(null=False, blank=False,verbose_name="Synopsis of Project")
