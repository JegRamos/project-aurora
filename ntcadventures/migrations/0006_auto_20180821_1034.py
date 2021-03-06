# Generated by Django 2.0.5 on 2018-08-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntcadventures', '0005_auto_20180820_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='overtime',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.PROTECT, to='ntcadventures.OvertimeRequest'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='supervisor',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='ntcadventures.Supervisor'),
        ),
    ]
