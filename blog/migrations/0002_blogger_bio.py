# Generated by Django 2.1.7 on 2019-03-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='bio',
            field=models.TextField(default='This is where my bio should be', help_text='Enter a brief bio', max_length=1000),
            preserve_default=False,
        ),
    ]
