# Generated by Django 5.0.4 on 2024-05-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(default='Unknown', null=True)),
            ],
        ),
    ]
