# Generated by Django 2.0.5 on 2018-08-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntcadventures', '0003_auto_20180819_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='entry_pics'),
        ),
    ]
