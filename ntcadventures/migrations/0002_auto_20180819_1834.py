# Generated by Django 2.0.5 on 2018-08-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntcadventures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
