# Generated by Django 5.1.3 on 2024-12-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_autor_fnacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='fnacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
