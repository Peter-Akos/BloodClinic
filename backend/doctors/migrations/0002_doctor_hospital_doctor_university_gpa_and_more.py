# Generated by Django 4.1.7 on 2023-03-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(default='Unemployed', max_length=30),
        ),
        migrations.AddField(
            model_name='doctor',
            name='university_gpa',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='Missing name', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='title',
            field=models.CharField(default='Missing Title', max_length=30),
        ),
    ]
