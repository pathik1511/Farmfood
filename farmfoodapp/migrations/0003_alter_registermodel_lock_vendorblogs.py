# Generated by Django 4.0.2 on 2022-04-05 07:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmfoodapp', '0002_alter_registermodel_lock_productviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='lock',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 4, 49, 2, 243482)),
        ),
        migrations.CreateModel(
            name='VendorBlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmfoodapp.registermodel')),
            ],
        ),
    ]
