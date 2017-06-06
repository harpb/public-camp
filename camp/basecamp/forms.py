
from django import forms

from camp.basecamp.models import Camp


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

        if end_date < start_date:
            raise forms.ValidationError('Camp must end after it starts.')

        return cleaned_data
