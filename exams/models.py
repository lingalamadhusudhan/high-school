from django.db import models
from students.models import Student
from homework.models import Subject


class Exam(models.Model):
    name = models.CharField(max_length=100)   # e.g. "Mid-term 2026"
    date = models.DateField()

    def __str__(self):
        return self.name


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks_obtained}/{self.max_marks}"


class MonthlyPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='monthly_performance')
    month = models.DateField(help_text="Use the 1st of the month, e.g. 2026-09-01")
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.month.strftime('%B %Y')}"