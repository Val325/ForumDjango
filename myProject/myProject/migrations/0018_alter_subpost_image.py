# Generated by Django 4.1.7 on 2023-04-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProject', '0017_alter_subpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
