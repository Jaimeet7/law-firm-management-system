from django.db import models

case_types = [
    ('criminal','CRIMINAL'),
    ('divorce','DIVORCE'),
    ('consumer','CONSUMER'),
    ('civil','CIVIL'),
    ('bankruptcy','BANKRUPTCY'),
    ('environmental','ENVIRONMENTAL'),
    ('other','OTHER')
]


class LawyerDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    years_of_experience = models.IntegerField()
    specialization = models.CharField(max_length=100)
    Total_cases = models.IntegerField()
    Description = models.TextField()
    lawyer_img = models.ImageField(upload_to='lawyer_img/',blank=True,null=True)

class CaseDetail(models.Model):
    case_title = models.CharField(max_length=100)
    case_description = models.CharField(max_length=500)
    case_img = models.ImageField(upload_to="case_img/",blank=True,null=True)

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100,choices=case_types,default="criminal")
    description = models.TextField()
    document = models.ImageField(upload_to="enq_docs/",blank=True,null=True)

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100,choices=case_types,default="criminal")
    description = models.CharField(max_length=100)
    case_doc = models.ImageField(upload_to='appointmentimg/',blank=True,null=True)
    no_of_hearings = models.IntegerField()
    court_name = models.CharField(max_length=100)
    fees = models.IntegerField(default=500)