# Generated by Django 3.1.3 on 2020-11-27 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='学生姓名')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.classes')),
            ],
        ),
    ]
