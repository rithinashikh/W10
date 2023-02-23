# Generated by Django 4.1.4 on 2023-02-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50, unique=True)),
                ('uemail', models.CharField(max_length=50)),
                ('uphone', models.BigIntegerField(default=None)),
                ('upassword', models.CharField(max_length=50)),
                ('uactive', models.BooleanField(default=True)),
            ],
        ),
    ]
