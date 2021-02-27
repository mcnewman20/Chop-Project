from django import forms


class SampleCodeForm(forms.Form):
    sample_code = forms.CharField(label='Enter the code of the sample you want to see:', max_length=100, required=False)


class UseSampleCodeForm(forms.Form):
    sample_code = forms.CharField(label='Enter the code of the sample you want to use:', max_length=100, required=False)
    use_sample_code = forms.IntegerField(label='Enter the amount of the above sample you want to use:', required=False)