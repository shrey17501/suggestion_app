# Generated by Django 4.0.8 on 2023-11-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=600, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('open', models.CharField(max_length=400, null=True)),
                ('lat', models.CharField(max_length=30, null=True)),
                ('lag', models.CharField(max_length=30, null=True)),
                ('pincode', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('pageno', models.CharField(max_length=100, null=True)),
                ('brand_logo', models.CharField(max_length=100, null=True)),
                ('new_lat', models.CharField(max_length=30, null=True)),
                ('new_lon', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
