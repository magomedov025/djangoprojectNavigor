# Generated by Django 4.2.7 on 2023-12-10 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_timelesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='timeLesson',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.educationonelesson'),
        ),
        migrations.AlterField(
            model_name='product',
            name='transEducation',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.educationtrans'),
        ),
    ]
