# Generated by Django 2.2.2 on 2019-07-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsection', '0009_remove_student_fieles'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Fieles',
            field=models.FileField(null=True, upload_to='profile/pdfs/'),
        ),
    ]
