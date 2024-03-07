from django.shortcuts import render
from app2.forms import bookform
from app2.models import Movie
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'b':k})
class MovieList(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "b"


# def add(request):
#     if (request.method == "POST"):
#         form = bookform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form = bookform()
#     return render(request, "addpage.html", {'form': form})

class MovieAdd(CreateView):
    model = Movie
    template_name = "addpage.html"
    fields = '__all__'
    success_url = reverse_lazy('movie:home')


# def detail(request, p):
#     k = Movie.objects.get(id=p)
#     return render(request, 'detail.html', {'k': k})

class MovieDetail(DetailView):
    model = Movie
    template_name = "detail.html"
    context_object_name = "k"


# def update(request, p):
#     b = Movie.objects.get(id=p)
#     if (request.method == "POST"):
#         form = bookform(request.POST, request.FILES, instance=b)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form = bookform(instance=b)
#     return render(request, 'update.html', {'form': form})

class MovieUpdate(UpdateView):
    model = Movie
    template_name = "update.html"
    fields = '__all__'
    success_url = reverse_lazy('movie:home')


class MovieDelete(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('movie:home')

# def delete(request, p):
#     b = Movie.objects.get(id=p)
#     b.delete()
#     return home(request)
