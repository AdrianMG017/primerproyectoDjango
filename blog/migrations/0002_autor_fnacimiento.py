# Generated by Django 5.1.3 on 2024-12-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fnacimiento',
            field=models.DateField(null=True),
        ),
    ]