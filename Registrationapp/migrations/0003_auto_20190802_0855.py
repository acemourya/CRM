# Generated by Django 2.2.3 on 2019-08-02 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrationapp', '0002_auto_20190801_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='FirstName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='LastName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Postion',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterModelTable(
            name='registration',
            table='Registration',
        ),
    ]
