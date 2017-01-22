from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .analyse.Detection_type import Type_Donnees
# Imaginary function to handle an uploaded file.


def handle_uploaded_file(f):
    data = ""
    with open('uploaded.data', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            data = data + chunk.decode(encoding='UTF-8')
        Type_Donnees(data)

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return render(request, 'polls/index.html', {'form': form, 'done': True})
    else:
        form = UploadFileForm()
    return render(request, 'polls/index.html', {'form': form})
