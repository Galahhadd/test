# Generated by Django 5.1.2 on 2024-10-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_of_experience', models.PositiveIntegerField()),
                ('breed', models.CharField(max_length=100)),
                ('salart', models.PositiveIntegerField()),
            ],
        ),
    ]
