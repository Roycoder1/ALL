# Generated by Django 4.1 on 2022-08-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0002_todo_category_alter_todo_date_completion_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="todo", name="category",),
    ]
