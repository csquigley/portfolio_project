# Generated by Django 4.1.4 on 2022-12-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_projectsection_code_snippet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsection',
            name='section_template',
            field=models.CharField(choices=[('CF', 'CONTENT_FULL'), ('IL', 'IMAGE_LEFT'), ('IR', 'IMAGE_RIGHT')], default='CF', max_length=2),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='section_type',
            field=models.CharField(choices=[('opt3', 'code_section'), ('opt5', 'html_section'), ('opt1', 'image_section'), ('opt2', 'text_section'), ('opt4', 'sub_section')], default='opt1', max_length=4),
        ),
    ]