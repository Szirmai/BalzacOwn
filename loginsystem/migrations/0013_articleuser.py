# Generated by Django 4.1.7 on 2023-05-11 18:00

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginsystem', '0012_delete_articleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(max_length=1000000, null=True)),
                ('indeximg', models.ImageField(default='images/home9.jpg', upload_to='images/')),
                ('category', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
