from django.shortcuts import render, redirect

# Import the model associated with the data it needs.
from .models import Pizza

# Import the form associated with the comment insertion form. 
from .forms import CommentForm

# Create your views here.
def index(request):
    # The home page for the pizzas app. 
    return render(request, 'pizzas/index.html')

def pizzas(request):
    # Shows all pizzas.

    # Queries the database by asking for the Pizza objects, sorted by the date_added attribute, storing the resulting queryset in pizzas. 
    pizzas = Pizza.objects.order_by('date_added')

    # This is a dictionary in which the keys are names we'll use in the template to access the data, and the values are the data we need to 
    # send to the template.
    context = {'pizzas':pizzas}

    # To build a page that uses data, pass the context variable to render, as well as the request object and the path to the template. 
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    # Show a single pizza and all its toppings.

    # Use get() to retrieve the pizza, just like in the Django shell. 
    pizza = Pizza.objects.get(id=pizza_id)

    # Gets the toppings associated with this pizza, and orders it according to date_added.
    toppings = pizza.topping_set.order_by('date_added')

    # Stores the pizza and toppings in the context dictionary.
    context = {'pizza':pizza, 'toppings':toppings}

    # Sends the context to the template pizza.html.
    return render(request,'pizzas/pizza.html', context)

def comment(request,pizza_id):
    # Add a comment for the pizza page.

    # Attribute uses the pizza_id to get the correct pizza.
    pizza = Pizza.objects.get(id=pizza_id)

    # Checks whether the request method is POST or GET. 
    # The if block executes if it's a GET request and creates an instance of CommentForm. 
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()

    else:
        # POST data submitted; process data. 
        form = CommentForm(data=request.POST)

        if form.is_valid():
            # This attribute tells django to create a comment object and assign it to comment without saving it to the database. 
            comment = form.save(commit=False)
            # Set the pizza attribute of comment to the pizza we pulled from the database at the beginning of the function. 
            comment.pizza = pizza
            comment.save()

            # This renders the pizza page the user made comments on, and they should see their comment on the pizza page.
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    # Display a blank or invalid form. 
    context = {'pizza':pizza,'form':form}
    return render(request,'pizzas/comment.html',context)