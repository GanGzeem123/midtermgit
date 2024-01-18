# Generated by Django 4.2.9 on 2024-01-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_app', '0002_tool_tooltype_delete_employee_tool_drug_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user', models.AutoField(primary_key=True, serialize=False)),
                ('user_firstname', models.CharField(max_length=50)),
                ('user_lastname', models.CharField(max_length=50)),
                ('user_gender', models.CharField(max_length=10)),
                ('user_tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='tool',
        ),
        migrations.DeleteModel(
            name='tooltype',
        ),
    ]
