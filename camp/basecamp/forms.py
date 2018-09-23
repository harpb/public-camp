
from django import forms

from camp.basecamp.models import Camp, Activity, ActivityAttendee, Attendee


class CampAdminForm(forms.ModelForm):
    '''
    Form for Camp admin
    '''
    class Meta:
        model = Camp
        fields = '__all__'

    def clean(self):
        '''
        Basic form validation that ensures the camp ends after it starts
        '''
        cleaned_data = super(CampAdminForm, self).clean()
        start_date = cleaned_data.get('start_at')
        end_date = cleaned_data.get('end_at')

        if end_date <= start_date:
            raise forms.ValidationError('Camp must end after it starts.')

        return cleaned_data


class ActivityAdminForm(forms.ModelForm):
    '''
    Form for Camp admin
    '''
    class Meta:
        model = Activity
        fields = '__all__'

    def clean(self):
        '''
        Basic form validation that ensures the activity ends after it starts
        '''
        cleaned_data = super(ActivityAdminForm, self).clean()
        start_date = cleaned_data.get('start_at')
        end_date = cleaned_data.get('end_at')

        if end_date <= start_date:
            raise forms.ValidationError('Activity must end after it starts.')

        if 'counselor' in cleaned_data:
            camp = cleaned_data['counselor'].camp
            if start_date < camp.start_at:
                raise forms.ValidationError('Activity must start after camp starts.')
            if camp.end_at < end_date:
                raise forms.ValidationError('Activity must end before camp ends.')

        return cleaned_data

    def save(self, commit=True):
        instance = super(ActivityAdminForm, self).save(commit=commit)
        instance.save()

        if instance.name == 'All-hands Meeting':
            # Automagically add all of the campers to the activity
            for attendee in instance.counselor.camp.attendees.all():
                if attendee.role == Attendee.ROLE_COUNSELOR:
                    continue

                ActivityAttendee.objects.create(
                    activity=instance,
                    attendee=attendee
                )

        return instance