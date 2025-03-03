# Generated by Django 4.2.3 on 2023-07-13 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.task_category')),
            ],
        ),
    ]
