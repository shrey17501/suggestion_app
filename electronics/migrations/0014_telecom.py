# Generated by Django 4.0.8 on 2023-11-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0013_movietheater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telecom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_type', models.CharField(max_length=50, null=True)),
                ('store_name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('operating_time', models.CharField(max_length=100, null=True)),
                ('lat', models.CharField(max_length=30, null=True)),
                ('lon', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('brand_name', models.CharField(max_length=50, null=True)),
                ('pincode', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
