# Generated by Django 4.1.1 on 2022-12-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(upload_to='autor'),
        ),
    ]