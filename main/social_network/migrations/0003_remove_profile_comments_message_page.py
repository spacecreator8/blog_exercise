# Generated by Django 4.2.7 on 2023-12-10 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0002_alter_message_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='comments',
        ),
        migrations.AddField(
            model_name='message',
            name='page',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_network.profile'),
        ),
    ]
