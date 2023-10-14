from django import forms
from .models import Client, Branch, Area , Material


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','age','gender','mail_id','address','phone_number','dob','branch','area','account','materials'] 

    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].queryset = Area.objects.none()

        if 'branch' in self.data:
            try:
                branch_id = int(self.data.get('branch'))
                self.fields['area'].queryset = Area.objects.filter(branch_id=branch_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['area'].queryset = self.instance.branch.area_set.order_by('name')