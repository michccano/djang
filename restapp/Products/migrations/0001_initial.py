# Generated by Django 3.0.8 on 2020-07-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('descriptions', models.TextField(blank=True, default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
