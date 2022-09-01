from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import os
def index(request):
    return HttpResponse("Hello, world!")

from .models import Document
def home(request):
    documents = Document.objects.all()
    rank = Document.objects.latest('id')
    print(rank)
    return render(request, 'home.html', { 'documents': documents })


from django.shortcuts import render
from django.shortcuts import render
from mysite import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

from .forms import DocumentForm
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


cx = 'google_cx'
key = 'googlecse_key'

import advertools as adv
import pandas as pd
pd.options.display.max_columns = None
import urllib.request
import requests
import csv
def uploadings(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        df=pd.read_csv('.'+uploaded_file_url)
        z=list(df['keyword'])
        y=list(df['url'])
        print(y[0])
        print(z)
        search = adv.serp_goog(q=z, cx=cx, key=key)
        search.to_csv('./media/input/input.csv')
        df1 = pd.read_csv('./media/input/input.csv', index_col=[0])
	    #df2 = df1[df1['displayLink']== 'www.desss.com']
        df2 = df1[df1['displayLink']== y[0]]
        df2.to_csv('./media/output/output.csv')
	    #return HttpResponse("Hello, world!")
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')