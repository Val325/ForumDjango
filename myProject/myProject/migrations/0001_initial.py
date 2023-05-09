# Generated by Django 4.2.1 on 2023-05-09 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='textData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textdata', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='SubPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('textdata', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subpost', to='myProject.textdata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'subpost',
            },
        ),
    ]