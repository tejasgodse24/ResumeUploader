from django import forms
from myapp.models import Resume

GENDER_CHOISES = (
    ('Male' , 'Male'),
    ('Female' , 'Female')
)
JOB_LOCATION_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
 ('Banglore', 'Banglore')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOISES, widget=forms.RadioSelect)
    job_location = forms.MultipleChoiceField(choices=JOB_LOCATION_CHOICE, widget=forms.CheckboxSelectMultiple, label="Prefered work location")
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pincode', 'state', 'mobile_no', 'email', 'job_location', 'profile_img', 'resume_file']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            # 'gender' : forms.TextInput(attrs={'class':'form-control'}),
            'locality' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'pincode' : forms.NumberInput(attrs={'class':'form-control'}),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'mobile_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'profile_img' : forms.FileInput(attrs={'class':'form-control'}),
            'resume_file' : forms.FileInput(attrs={'class':'form-control'}),
        }