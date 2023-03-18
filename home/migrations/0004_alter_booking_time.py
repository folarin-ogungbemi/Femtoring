# Generated by Django 4.1.7 on 2023-03-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_mentorsprofile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:30'), ('20:00', '20:00'), ('20:30', '20:30')], default='17:30'),
        ),
    ]
