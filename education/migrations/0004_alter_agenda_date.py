# Generated by Django 4.2.3 on 2023-07-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_agenda_time_alter_agenda_evaluator_crutch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]
