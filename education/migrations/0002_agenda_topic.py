# Generated by Django 4.2.3 on 2023-07-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='topic',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]