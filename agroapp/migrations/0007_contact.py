# Generated by Django 2.0.7 on 2020-08-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroapp', '0006_auto_20200807_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adsoyad', models.CharField(help_text='Ad :', max_length=50)),
                ('telefon', models.CharField(help_text='Telefon :', max_length=50)),
                ('eposta', models.CharField(help_text='Eposta :', max_length=50)),
                ('konu', models.CharField(help_text='Konu :', max_length=50)),
                ('mesaj', models.TextField(max_length=700)),
            ],
        ),
    ]