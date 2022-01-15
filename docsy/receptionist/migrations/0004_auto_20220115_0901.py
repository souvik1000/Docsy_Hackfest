# Generated by Django 3.2.11 on 2022-01-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0003_auto_20220113_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagingexam',
            name='imaging_document',
            field=models.FileField(null=True, upload_to='dianosis_image/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='labreport',
            name='lab_document',
            field=models.FileField(null=True, upload_to='dianosis_image/', verbose_name=''),
        ),
    ]