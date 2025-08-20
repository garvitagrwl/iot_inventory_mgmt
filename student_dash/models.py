from django.db import models
from base.models import Student, Component

# Create your models here.
class StudentIssueLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # studentid = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="sid_fromtable",
    #                               null=True)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity_issued = models.PositiveIntegerField()
    form_date = models.DateField(null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    STUDENT_STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
        ('Rejectedbyteacher','Rejectedbyteacher')
    ]
    status_from_student = models.CharField(
        max_length=20,
        choices=STUDENT_STATUS_CHOICES,
        blank=True,
        null=True
    )

    TEACHER_STATUS_CHOICES = [ 
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Returned', 'Returned'),
    ]
    status_from_teacher = models.CharField(
        max_length=20,
        choices=TEACHER_STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.student.full_name} - {self.component.name}"

    
    
