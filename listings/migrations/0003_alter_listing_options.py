# Generated by Django 4.2.5 on 2023-09-19 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_options_alter_listing_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['is_sold', '-created_at']},
        ),
    ]
