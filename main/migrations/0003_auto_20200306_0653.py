# Generated by Django 3.0.3 on 2020-03-06 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200305_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='emailAddress',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='register',
            name='fieldProject',
            field=models.CharField(max_length=30, verbose_name='Field of Project'),
        ),
        migrations.AlterField(
            model_name='register',
            name='github_username',
            field=models.CharField(max_length=150, verbose_name='GitHub Username'),
        ),
        migrations.AlterField(
            model_name='register',
            name='project_repo_name',
            field=models.CharField(max_length=150, verbose_name='Project Repository Name'),
        ),
        migrations.AlterField(
            model_name='register',
            name='synopsis',
            field=models.TextField(verbose_name='Synopsis of Project'),
        ),
        migrations.AlterField(
            model_name='register',
            name='teamName',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Team Name'),
        ),
        migrations.AlterField(
            model_name='register',
            name='teamSize',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1, verbose_name='Team Size'),
        ),
        migrations.AlterField(
            model_name='register',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title of Project'),
        ),
        migrations.AlterField(
            model_name='register',
            name='userDetail1',
            field=models.CharField(max_length=150, verbose_name='User 1 Name'),
        ),
        migrations.AlterField(
            model_name='register',
            name='userDetail2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='User 2 name'),
        ),
        migrations.AlterField(
            model_name='register',
            name='userDetail3',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='User 3 name'),
        ),
    ]