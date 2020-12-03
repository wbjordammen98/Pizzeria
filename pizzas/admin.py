from django.contrib import admin

# Register your models with the admin site here.

# Imports the models we want to register. 
from .models import Pizza, Topping

# Tells Django to manage our models through the admin site.
# Register a model after you make migrations to the pizzas app via manage.py in the terminal. 
admin.site.register(Pizza)
admin.site.register(Topping)