# Generated by Django 4.1.4 on 2022-12-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_projectsection_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
