# Generated by Django 3.2.7 on 2021-12-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('status', models.SmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]