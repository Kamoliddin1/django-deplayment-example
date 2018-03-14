from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        clean_data = super().clean()
        email = clean_data['email']
        vmail = clean_data['verify']

        if email != vmail:
            raise forms.ValidationError('Make sure emails are not matching')