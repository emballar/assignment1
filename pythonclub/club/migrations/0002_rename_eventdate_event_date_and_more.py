# Generated by Django 4.0.3 on 2022-04-26 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventdate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventdescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventlocation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventtime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventtitle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventuserid',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingagenda',
            new_name='agenda',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetinglocation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingdate',
            new_name='meeting_date',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingtime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingtitle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='meetingattendance',
            new_name='attendance',
        ),
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='meetingid',
            new_name='meeting_id',
        ),
        migrations.RenameField(
            model_name='meetingminutes',
            old_name='meetingminutes',
            new_name='minutes',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resourcedateentered',
            new_name='date_entered',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resourcedescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resourcename',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resourcetype',
            new_name='resource_type',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resourceurl',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='resourceuserid',
            new_name='user_id',
        ),
    ]
