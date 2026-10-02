from django import forms
from.models import Job,CompanyProfile,StudentProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields = [
            'title',
            'description',
            'location',
            'salary',
            'job_type',
            'skills_required',
            'last_date',
        ]


        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'skills_required': forms.Textarea(attrs={'rows': 3}),
        }





class CompanyRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    company_name=forms.CharField(max_length=100)
    website = forms.URLField(required=False)
    location = forms.CharField( max_length=100)
    description = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
            
            )





class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields ={
            'username',
            'email',
            'password1',
            'password2',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.order_fields([
            'username',
            'email',
            'password1',
            'password2',
        ])




class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = {
            'phone',
            'profile_image',
            'education',
            'skills',
            'resume',
            'location',
            'bio',
        }
        widgets = {
                                'skills': forms.Textarea(attrs={'rows': 3}),
                                'bio': forms.Textarea(attrs={'rows': 3}),
                            }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
            self.order_fields([
                'phone',
                'education',
                'skills',
                'location',
                'bio',
                'profile_image',
                'reusme',
            ])





class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = [
            'company_name',
            'logo',
            'website',
            'location',
            'description',
        ]

        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 4}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.order_fields([
            'company_name',
            'logo',
            'website',
            'location',
            'description',
        ])

            