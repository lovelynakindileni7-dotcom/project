from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    matric_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    study_time = models.IntegerField()
    absences = models.IntegerField()
    failures = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    G1 = models.FloatField()
    G2 = models.FloatField()

    predicted_G3 = models.FloatField()
    risk_level = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.predicted_G3}"