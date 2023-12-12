from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class EducationTeacher(models.Model):
    class Meta:
        verbose_name = 'Учитель'
    name = models.CharField(max_length=128, unique=True)
    age = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(80)])
    ageEducation = models.DecimalField(max_digits=2, decimal_places=0, validators=[MinValueValidator(1), MaxValueValidator(40)])
    imageTeacher = models.ImageField(upload_to='avatar__image', blank=True)


    def __str__(self):
        return self.name