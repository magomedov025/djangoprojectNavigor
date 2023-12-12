# Generated by Django 4.2.7 on 2023-12-04 21:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='products__images')),
                ('rating', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('educationLocation', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('program', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='educationFormat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productformat'),
        ),
        migrations.AddField(
            model_name='product',
            name='educationTime',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.educationtime'),
        ),
    ]
