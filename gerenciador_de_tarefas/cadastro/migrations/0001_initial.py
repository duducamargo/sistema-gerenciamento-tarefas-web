# Generated by Django 5.1.1 on 2024-09-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('ultimo_nome', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
