from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        email = self.cleaned_data.get('email')
        vmail = self.cleaned_data.get('verify')

        if email != vmail:
            raise forms.ValidationError('Make sure emails are not matching')
