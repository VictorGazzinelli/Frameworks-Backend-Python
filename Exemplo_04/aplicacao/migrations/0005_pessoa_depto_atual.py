# Generated by Django 3.2.3 on 2021-06-27 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0004_departamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='depto_atual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='aplicacao.departamento'),
        ),
    ]