from django.contrib import admin

from products.models import (ProductCategory, Product, EducationTime, ProgrammProduct, ProductFormat, EducationOneLesson, EducationTrans)

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(EducationTime)
admin.site.register(ProgrammProduct)
admin.site.register(ProductFormat)
admin.site.register(EducationOneLesson)
admin.site.register(EducationTrans)


