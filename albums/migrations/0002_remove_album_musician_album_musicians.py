# Generated by Django 5.0.6 on 2024-06-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musician',
        ),
        migrations.AddField(
            model_name='album',
            name='musicians',
            field=models.ManyToManyField(to='musicians.musician'),
        ),
    ]
