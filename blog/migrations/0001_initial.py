# Generated by Django 2.1.5 on 2021-07-17 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tophead', models.TextField(max_length=100)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blogimage', models.ImageField(upload_to='images/')),
                ('blogtext', models.TextField(max_length=200)),
            ],
        ),
    ]
