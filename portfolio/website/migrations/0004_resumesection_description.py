# Generated by Django 4.1.4 on 2022-12-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_resumesection_resume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumesection',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
