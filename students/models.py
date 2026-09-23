from django.db import models
from accounts.models import User


class SchoolClass(models.Model):
    name = models.CharField(max_length=50)          # e.g. "Grade 5"
    section = models.CharField(max_length=10)        # e.g. "A"
    class_teacher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        limit_choices_to={'role': 'TEACHER'}, related_name='classes_taught'
    )

    def __str__(self):
        return f"{self.name} - {self.section}"


class Student(models.Model):
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("O+", "O+"), ("O-", "O-"), ("AB+", "AB+"), ("AB-", "AB-"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='students')

    parent = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        limit_choices_to={'role': 'PARENT'}, related_name='children'
    )

    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True)
    medical_report = models.TextField(blank=True, help_text="Allergies, conditions, medications, etc.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"