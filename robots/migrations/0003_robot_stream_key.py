# Generated by Django 3.0.7 on 2020-06-23 07:58

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0002_auto_20200622_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='stream_key',
            field=django_cryptography.fields.encrypt(models.CharField(default='', max_length=300, verbose_name='Websocket消息密钥')),
            preserve_default=False,
        ),
    ]