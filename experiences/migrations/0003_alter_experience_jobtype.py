# Generated by Django 5.0.4 on 2024-04-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_experience_jobtype_alter_experience_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='jobType',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
