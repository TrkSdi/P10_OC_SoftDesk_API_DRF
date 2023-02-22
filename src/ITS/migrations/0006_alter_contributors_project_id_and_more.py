# Generated by Django 4.1.7 on 2023-02-22 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ITS', '0005_alter_issues_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributors',
            name='project_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ITS.project'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
