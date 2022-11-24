# Generated by Django 4.1 on 2022-08-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('real_estate_agency', models.CharField(max_length=20)),
                ('order_description', models.TextField(max_length=255)),
                ('company', models.CharField(max_length=20)),
                ('deadline', models.DateField()),
            ],
        ),
    ]