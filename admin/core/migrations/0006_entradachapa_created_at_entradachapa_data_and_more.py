# Generated by Django 4.1.2 on 2022-11-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_saidachapa_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="entradachapa",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="entradachapa",
            name="data",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="saidachapa",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="saidachapa",
            name="data",
            field=models.DateTimeField(null=True),
        ),
    ]
