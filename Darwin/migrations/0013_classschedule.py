# Generated by Django 2.0.6 on 2018-07-13 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Darwin', '0012_student_fee_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(choices=[('pre-nursery', 'pre-nursery'), ('nursery', 'nursery'), ('kinder-garten', 'kinder-garten'), ('Grade - 1', 'Grade - 1'), ('Grade - 2', 'Grade - 2'), ('Grade - 3', 'Grade - 3'), ('Grade - 4', 'Grade - 4'), ('Grade - 5', 'Grade - 5'), ('Grade - 6', 'Grade - 6'), ('Grade - 7', 'Grade - 7'), ('Grade - 8', 'Grade - 8'), ('Grade - 9', 'Grade - 9'), ('Grade - X', 'Grade - X'), ('Grade - XI', 'Grade - XI'), ('Grade - XII', 'Grade - XII'), ('none', 'none')], default='none', max_length=30)),
                ('time', models.TimeField()),
                ('monday', models.CharField(max_length=50)),
                ('tuesday', models.CharField(max_length=50)),
                ('wednesday', models.CharField(max_length=50)),
                ('thursday', models.CharField(max_length=50)),
                ('friday', models.CharField(max_length=50)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Darwin.Teacher')),
            ],
        ),
    ]
