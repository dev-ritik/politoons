# Generated by Django 2.1.4 on 2018-12-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Politoon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(max_length=8)),
                ('area', models.CharField(default=' ', help_text='Area of influence', max_length=200)),
                ('party', models.CharField(help_text='Political party', max_length=200)),
                ('majorRole', models.CharField(help_text='major role today', max_length=200)),
                ('date', models.DateTimeField()),
                ('placeOfBirth', models.CharField(default=' ', help_text='Enter the place of birth', max_length=80)),
                ('imageUrl', models.URLField()),
            ],
            options={
                'ordering': ['dob'],
            },
        ),
        migrations.DeleteModel(
            name='Politoons',
        ),
    ]
