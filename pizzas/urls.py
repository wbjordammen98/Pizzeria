# Defines URL patterns for the Pizzas app. 

# Import the path function in order to map URLs to views. 
from django.urls import path

# Import the views module from the same directory as the current urls.py file. 
from . import views

# This variable helps Django distinguish this urls.py file from the files of the same name in other apps within the project. 
app_name = 'pizzas'

# This variable is a list of individual pages that can be requested from the pizzas app. 
urlpatterns = [
    # Home page
    # First argument is a string that helps django route to the current request properly. 
    # Second argument specifies which function to call in views.py. 
    # Third argument provides the name 'index' for this url pattern so we can refer to it in other code sections.  
    path('', views.index, name='index'),
    # Page that shows all pizzas.
    # Adds pizzas into the string argument used for the home page url. 
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza.
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    # Page for adding a comment on a pizza page.
    path('comment/<int:pizza_id>/',views.comment,name='comment'),
]