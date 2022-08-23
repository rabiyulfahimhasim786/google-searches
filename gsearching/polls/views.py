from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from googlesearch import search

# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render
from .models import MyModel
from .forms import MyForm

def index(request):
    return HttpResponse("Hello, world.")

def getting(request):
    books = MyModel.objects.all()
    return render(request, 'get.html', {'books': books})

def my_form(request):
  if request.method == "POST":
    title = request.POST.get('name')
    website = request.POST.get('web')
    #print(title)
    #print(website)
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    #website = # need a exact site name including /
    # to search
    query = title#"geeksforgeeks" # keyword
    #rank, rank_list = 1, ""
    squares = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        #print(j)
        squares.append(j)
    #print(squares)
# app.py

#streaming = ['netflix', 'hulu', 'disney+', 'appletv+']
    streaming = squares
    index = streaming.index(website)
    ranking = index+1
    print('The rank of your site is:', ranking)#index+1)
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'index.html', {'form': form})

#def saveCriteria(request):
 ##   context = {}
 #   if request.method == "POST":
 #       title = request.POST.get('quantity')
 #       print(title)
 #   return render(request, "home.html", context)