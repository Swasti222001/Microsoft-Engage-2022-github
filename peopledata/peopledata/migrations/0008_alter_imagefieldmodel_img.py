# Generated by Django 4.0 on 2022-05-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopledata', '0007_imagefieldmodel_delete_unknown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefieldmodel',
            name='img',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='unknownimg'),
        ),
    ]