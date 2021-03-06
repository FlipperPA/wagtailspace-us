# Generated by Django 2.0.4 on 2018-04-28 13:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ('date', 'start_time'),
            },
        ),
        migrations.CreateModel(
            name='EventDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='ExperienceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field')], max_length=16, verbose_name='field type')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('from_address', models.CharField(blank=True, max_length=255, verbose_name='from address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.core.fields.RichTextField(blank=True)),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('intro_intro', models.TextField(blank=True)),
                ('intro_content', wagtail.core.fields.RichTextField(blank=True)),
                ('talks_sprint_title', models.CharField(blank=True, max_length=255)),
                ('talks_content', wagtail.core.fields.RichTextField(blank=True)),
                ('sprint_content', wagtail.core.fields.RichTextField(blank=True)),
                ('schedule_title', models.CharField(blank=True, max_length=255)),
                ('schedule_content', wagtail.core.fields.RichTextField(blank=True)),
                ('location_facilities_title', models.CharField(blank=True, max_length=255)),
                ('location_content', wagtail.core.fields.RichTextField(blank=True)),
                ('facilities_content', wagtail.core.fields.RichTextField(blank=True)),
                ('travel_hotels_title', models.CharField(blank=True, max_length=255)),
                ('hotels_content', wagtail.core.fields.RichTextField(blank=True)),
                ('travel_content', wagtail.core.fields.RichTextField(blank=True)),
                ('signup_title', models.CharField(blank=True, max_length=255)),
                ('signup_content', wagtail.core.fields.RichTextField(blank=True)),
                ('signup_button_title', models.CharField(blank=True, max_length=100)),
                ('attendees_title', models.CharField(blank=True, max_length=255)),
                ('attendees_content', wagtail.core.fields.RichTextField(blank=True)),
                ('sponsors_title', models.CharField(blank=True, max_length=255)),
                ('sponsors_content', wagtail.core.fields.RichTextField(blank=True)),
                ('house_rules_title', models.CharField(blank=True, max_length=255)),
                ('house_rules_content', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('github_nickname', models.CharField(max_length=255, verbose_name='Github nickname')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('food_allergies', models.CharField(blank=True, max_length=255, verbose_name='Food allergies')),
                ('shirt_size', models.CharField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('noshirt', "I don't want a shirt")], max_length=255, verbose_name='Shirt size')),
                ('give_a_talk', models.BooleanField(default=False, verbose_name='I would like to give a talk on Friday')),
                ('talk_title', models.CharField(blank=True, max_length=1000, verbose_name='Talk subject')),
                ('comments', models.TextField(blank=True, verbose_name='Comments')),
                ('dates', models.ManyToManyField(to='home.EventDate')),
                ('roles', models.ManyToManyField(to='home.ExperienceOption')),
            ],
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.FormPage'),
        ),
        migrations.AddField(
            model_name='dayschedule',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeslots', to='home.EventDate'),
        ),
    ]
