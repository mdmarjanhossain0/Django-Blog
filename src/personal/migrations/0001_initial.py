# Generated by Django 2.2.2 on 2021-02-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=61)),
                ('question', models.TextField(max_length=401)),
                ('priority', models.CharField(choices=[{'LOW', 'L'}, {'M', 'MEDIEM'}, {'H', 'HIGH'}], max_length=61)),
            ],
        ),
    ]
