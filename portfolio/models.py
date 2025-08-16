from django.db import models

# Create your models here.
class About(models.Model):
    description = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    role = models.TextField()
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    full_name  = models.CharField(max_length=100,null=True)
    city  = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name 
    

class Skills(models.Model):
    skill1 = models.CharField(max_length=100,null=True)    
    skill2 = models.CharField(max_length=100,null=True)    
    skill3 = models.CharField(max_length=100,null=True)    
    skill4 = models.CharField(max_length=100,null=True)    
    skill5 = models.CharField(max_length=100,null=True)    
    skill6 = models.CharField(max_length=100,null=True)    
    skill7 = models.CharField(max_length=100,null=True)    
    skill8 = models.CharField(max_length=100,null=True)    
    skill9 = models.CharField(max_length=100,null=True)    
    skill10 = models.CharField(max_length=100,null=True) 
    skill11 = models.CharField(max_length=100,null=True) 
    skill12 = models.CharField(max_length=100,null=True) 

    def __str__(self):
        return self.skill1   
    

class Profile(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    resume_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    institution = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    


    def __str__(self):
        return self.degree

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    responsibilities = models.TextField()  # store as plain text or JSON (or use a related model)

    def __str__(self):
        return self.title    


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
