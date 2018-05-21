from django import forms


class PlaylistForm(forms.Form):
    name = forms.CharField(label="Nom de la playlist", )

    def clean_name(self):
        return self.cleaned_data['name']