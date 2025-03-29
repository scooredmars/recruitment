from django.shortcuts import render

from .forms import PeselForm


def validate_pesel(pesel):
    if not pesel.isdigit() or len(pesel) != 11:
        return False, "PESEL powinien składać się z 11 cyfr."

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_val = sum(int(pesel[i]) * weights[i] for i in range(10))
    check_digit = (10 - (sum_val % 10)) % 10
    if check_digit != int(pesel[-1]):
        return False, "Błędny numer PESEL."

    # Decoding date of birth
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    if month > 80:
        century = 1800
        month -= 80
    elif month > 60:
        century = 2200
        month -= 60
    elif month > 40:
        century = 2100
        month -= 40
    elif month > 20:
        century = 2000
        month -= 20
    else:
        century = 1900
    full_year = century + year

    # Gender determination: penultimate digit – even for women, odd for men
    gender_digit = int(pesel[9])
    gender = "Kobieta" if gender_digit % 2 == 0 else "Mężczyzna"
    info = f"Data urodzenia: {full_year}-{month:02d}-{day:02d}, Płeć: {gender}"
    return True, info


def pesel_view(request):
    info = None
    valid = None
    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data["pesel"]
            valid, info = validate_pesel(pesel)
    else:
        form = PeselForm()
    return render(
        request,
        "pesel.html",
        {"form": form, "info": info, "valid": valid},
    )
