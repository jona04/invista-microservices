# Generated by Django 4.1.2 on 2022-11-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_entradachapa_created_at_entradachapa_data_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="entradachapa",
            name="observacao",
            field=models.TextField(null=True),
        ),
    ]
