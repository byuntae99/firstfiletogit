from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver






# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Student") )
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




class Status(models.Model):
    status=models.CharField(max_length=50)
    objects = models.Manager()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    email=models.EmailField()
    rollnumber=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    address = models.TextField(max_length=250)
    objects = models.Manager()



class LeaveReportStudent(models.Model):
    LEAVE_CHOICES= [
    ('Leave', 'Leave'),
    ('Emergency Leave', 'Emergency Leave'),
    ('OD', 'OD'),
    ('Study Leave', 'Study Leave'),
    ]
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_types=models.CharField(choices=LEAVE_CHOICES, default='Leave',max_length=100)
    from_leave_date = models.CharField(max_length=255)
    to_leave_date = models.CharField(max_length=255)   
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()




class Courseregister(models.Model):
    id = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Students, on_delete=models.CASCADE)
    Stafff=models.CharField(max_length=100)
    Coursee=models.CharField(max_length=100)
    timess=models.CharField(max_length=100)



#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Students.objects.create(admin=instance, address="",email='', password="",gender="")
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.students.save()
   
    


