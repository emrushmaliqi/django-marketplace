# Generated by Django 4.2.5 on 2023-09-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='seller_message',
            field=models.BooleanField(default=False),
        ),
    ]
