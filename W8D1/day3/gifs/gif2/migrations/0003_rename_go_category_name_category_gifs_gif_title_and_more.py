# Generated by Django 4.1 on 2022-08-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gif2", "0002_remove_category_gifs_category_go"),
    ]

    operations = [
        migrations.RenameField(model_name="category", old_name="go", new_name="name",),
        migrations.AddField(
            model_name="category",
            name="gifs",
            field=models.ManyToManyField(to="gif2.gif"),
        ),
        migrations.AddField(
            model_name="gif",
            name="title",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gif",
            name="uploader_name",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="gif",
            name="url",
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
