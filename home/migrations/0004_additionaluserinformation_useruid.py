# Generated by Django 5.0.2 on 2024-03-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaluserinformation',
            name='userUID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
