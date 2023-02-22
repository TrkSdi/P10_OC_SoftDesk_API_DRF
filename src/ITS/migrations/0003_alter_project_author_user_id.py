# Generated by Django 4.1.7 on 2023-02-22 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ITS', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author_user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]