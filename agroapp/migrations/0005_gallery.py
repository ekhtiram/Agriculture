# Generated by Django 2.0.7 on 2020-08-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroapp', '0004_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('altbaslik', models.CharField(max_length=100)),
                ('resim', models.FileField(null=True, upload_to='documents/')),
            ],
        ),
    ]