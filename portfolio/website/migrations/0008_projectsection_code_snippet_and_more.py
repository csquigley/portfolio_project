# Generated by Django 4.1.4 on 2022-12-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_project_code_snippet_is_html_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsection',
            name='code_snippet',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projectsection',
            name='code_snippet_is_html',
            field=models.BooleanField(default=False, verbose_name='Already HTML?'),
        ),
        migrations.AddField(
            model_name='projectsection',
            name='content_is_html',
            field=models.BooleanField(default=False, verbose_name='Already HTML?'),
        ),
        migrations.AddField(
            model_name='projectsection',
            name='customCSS',
            field=models.FileField(blank=True, upload_to='media/customCSS'),
        ),
        migrations.AddField(
            model_name='projectsection',
            name='use_customCSS',
            field=models.BooleanField(default=False, verbose_name='use custom CSS?'),
        ),
        migrations.AlterField(
            model_name='projectsection',
            name='section_type',
            field=models.CharField(choices=[('opt2', 'text_section'), ('opt1', 'image_section'), ('opt5', 'html_section'), ('opt4', 'sub_section'), ('opt3', 'code_section')], default='opt1', max_length=4),
        ),
    ]