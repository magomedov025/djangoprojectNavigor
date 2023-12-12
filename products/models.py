from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from teacher.models import EducationTeacher

class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категории'
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



class ProductFormat(models.Model):
    class Meta:
        verbose_name = 'Формат продукта'
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class EducationTime(models.Model):
    class Meta:
        verbose_name = 'Продолжительность курса'
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class EducationTrans(models.Model):
    class Meta:
        verbose_name = 'Сложность курса'
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class EducationOneLesson(models.Model):
    class Meta:
        verbose_name = 'Продолжительность одного урока'
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=0)
    image = models.ImageField(upload_to='products__images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    rating = models.PositiveIntegerField(default=0, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    educationTime = models.ForeignKey(to=EducationTime, on_delete=models.PROTECT, blank=True)
    educationLocation = models.CharField(max_length=256, blank=True)
    educationFormat = models.ForeignKey(to=ProductFormat, on_delete=models.PROTECT)
    productUrl = models.TextField(blank=True)
    educationTeacher = models.ForeignKey(to=EducationTeacher, on_delete=models.PROTECT)
    timeLesson = models.ForeignKey(to=EducationOneLesson, on_delete=models.PROTECT, blank=True)
    transEducation = models.ForeignKey(to=EducationTrans, on_delete=models.PROTECT, blank=True)



    def __str__(self):
        return self.name

class ProgrammProduct(models.Model):
    class Meta:
        verbose_name = 'Программа продукта'
    name = models.CharField(max_length=256)
    program = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)



    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'


