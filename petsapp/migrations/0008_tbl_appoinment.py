# Generated by Django 5.0.6 on 2024-05-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsapp', '0007_tbl_dr'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('age', models.IntegerField(null=True)),
                ('birthdate', models.IntegerField(null=True)),
                ('symptoms', models.CharField(max_length=20, null=True)),
                ('district', models.CharField(max_length=20, null=True)),
                ('place', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
