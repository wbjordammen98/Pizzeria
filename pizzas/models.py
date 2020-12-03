from django.db import models

# Create your models here.
class Pizza(models.Model):
    # A pizza option for the pizzeria.

    # Use CharField for storing a small amount of text.
    text = models.CharField(max_length=200)

    # Tells Django to automatically set this attribute to the current date and time when a user creates a new pizza.
    date_added = models.DateTimeField(auto_now_add=True)

    # Method to return the string stored in the text attribute. 
    def __str__(self):
        # Return a string representation of the model.
        return self.text

class Topping(models.Model):
    # Toppings for the pizza options listed. 

    # The first attribute, Pizza, is a Foregin Key reference, which references another record in the database, connecting each topping to a specific pizza. 
    # The on-delete argument tells Django that when a pizza is deleted, all toppings associated with that pizza. 
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)

    # Attribute defines an instance of TextField, which doesn't require a size limit. 
    text = models.TextField()

    # This attribute allows to present toppings in the order they were created to place a timestamp next to each topping. 
    date_added = models.DateTimeField(auto_now_add=True) 

    # This class holds extra information for managing a model. For this one, it sets a special attribute telling Django to use 'toppings' to refer to more than one topping.
    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        # Return a string representation of the model of only the first 50 characters of a text.
        return f"{self.text[:50]}..."