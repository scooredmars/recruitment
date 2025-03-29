from django import forms


class PeselForm(forms.Form):
    pesel = forms.CharField(
        label="Podaj numer PESEL",
        max_length=11,
        min_length=11,
        help_text="Numer PESEL powinien składać się z 11 cyfr.",
    )
