# Generated by Django 4.0 on 2022-05-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopledata', '0008_alter_imagefieldmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefieldmodel',
            name='img',
            field=models.TextField(null=True),
        ),
    ]
