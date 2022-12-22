# Generated by Django 4.1.4 on 2022-12-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_post_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image_url', models.ImageField(null=True, upload_to='media/post_images')),
                ('github_url', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(null=True, upload_to='media/post_images'),
        ),
    ]