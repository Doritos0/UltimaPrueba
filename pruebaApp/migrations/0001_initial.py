# Generated by Django 4.1.6 on 2023-06-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nom_prod', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
