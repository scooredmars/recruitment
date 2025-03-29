import random

from django.shortcuts import redirect, render

from .forms import UploadFileForm


def scramble_word(word):
    if len(word) <= 3:
        return word
    # We keep the first and last letters, mix the middle letters
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + "".join(middle) + word[-1]


def scramble_text(text):
    words = text.split()
    scrambled_words = [scramble_word(word) for word in words]
    return " ".join(scrambled_words)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            text = file.read().decode("utf-8")
            scrambled = scramble_text(text)
            # We store the result in the session or pass it directly to the template
            request.session["scrambled_text"] = scrambled
            return redirect("text_processor:result")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def result(request):
    scrambled_text = request.session.get("scrambled_text", "")
    return render(request, "result.html", {"scrambled_text": scrambled_text})
