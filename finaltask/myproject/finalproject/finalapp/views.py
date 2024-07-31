from django.shortcuts import render,redirect, get_object_or_404
from .forms import Createuser,LoginForm,CreateMovieForm,UpdateMovieForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib import messages 

from django.contrib.auth.decorators import login_required



from .forms import ReviewForm

from . models import Movie,Review
# Create your views here.
#home page
def home(request):
    return render(request,'finalapp/index.html')


# register

def registration(request):
    form=Createuser()

    if request.method =='POST':
        form=Createuser(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my-login') 


    context={'form':form}

    return render(request,'finalapp/register.html',context=context)        

#login 

def my_login(request):
    form=LoginForm()

    if request.method=='POST':
        
        form=LoginForm(request,data=request.POST)


        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

           

            if user is not None:

              auth.login(request,user)

              return redirect('dashboard')


    context={'form':form}

    return render (request,'finalapp/login.html',context=context)
     

# Dashboard

@login_required(login_url='my-login')

def dashboard(request):
    
    my_movie=Movie.objects.all()
    context={'movies':my_movie} 
    return render(request,'finalapp/dashboard.html',context=context)



#add movies

@login_required(login_url='my-login')

def create_movie(request):
    form=CreateMovieForm()

    if request.method == "POST":

        form = CreateMovieForm(request.POST, request.FILES)

        if form.is_valid():
            movie = form.save(commit=False)

            movie.user = request.user

            form.save()

            messages.success(request, "Your movie is added!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'finalapp/addmovies.html', context=context)


       

#fields include movie title, poster, description, release date, actors,
#category and a YouTube trailer link.


#update movie








@login_required(login_url='my-login')
def details(request,movie_id):
    data= Movie.objects.get(id=movie_id)
    return render(request,'finalapp/details.html',{'data':data})




@login_required(login_url='my-login')
def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if movie.user != request.user:
        return HttpResponseForbidden("")

    if request.method == 'POST':
        form = UpdateMovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = UpdateMovieForm(instance=movie)

        return render(request, 'finalapp/edit.html', {'form': form, 'movie': movie})


@login_required(login_url='my-login')

def delete(request, id):
    movie = get_object_or_404(Movie, id=id)

    if movie.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this movie.")

    if request.method == 'POST':
        movie.delete()
        return redirect("dashboard")
    return render(request, 'finalapp/delete.html')


#Reviews

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
        else:
            # Debugging: print form errors to the console
            print("Form errors:", form.errors)
    else:
        form = ReviewForm(instance=movie)
    print("Form:", form)   

    
    print("Form being passed to the template:", form)
    return render(request, 'finalapp/details.html', {'movie': movie, 'reviews': reviews, 'form': form})





















# logout

def user_logout(request):
    
    auth.logout(request)
    return redirect('my-login')
