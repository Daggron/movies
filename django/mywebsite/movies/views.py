from django.views import generic
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Movies
from .form import UserForm

class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movies.objects.all()
class DetailsView(generic.DetailView):
    model = Movies
    template_name = 'movies/details.html'
class add_Movies(CreateView):
    model = Movies
    fields = ['movie_title','movie_cast','movie_genre','movie_poster']
class Update_Movies(UpdateView):
    model = Movies
    fields = ['movie_title','movie_cast','movie_genre','movie_poster']
class Delete_Movies(DeleteView):
    model = Movies
    success_url = reverse_lazy('movie:index')

class UserFormView(View):
    form_class= UserForm
    template_name='movies/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})



    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)

            if  user is not None:
                 if  user.is_active:
                     login(request,user)
                     return  redirect('movie:index')
                 else:
                     return render(request,self.template_name,{'form': form})