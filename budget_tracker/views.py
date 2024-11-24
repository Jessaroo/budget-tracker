from django.shortcuts import render
from django.db.models import Sum  # Import Sum for aggregation
from budget.models import Expense  # Import the Expense model

# View for the homepage
def home(request):
    return render(request, 'home.html')

# View for adding a new expense
def add_expense(request):
    if request.method == "POST":
        description = request.POST['description']
        amount = request.POST['amount']
        category = request.POST['category']

        # Create a new Expense object and save it to the database
        new_expense = Expense(description=description, amount=amount, category=category)
        new_expense.save()

        return render(request, 'add_expense.html', {
            'message': f'Expense "{description}" added successfully!'
        })

    return render(request, 'add_expense.html')

# View for the index page (showing all expenses and the summary)
def index(request):
    # Fetch all the expenses from the database, ordered by date
    expenses = Expense.objects.all().order_by('-date')  # Newest expenses appear first

    # Calculate total spending per category
    summary = (
        expenses.values('category')  # Group by category
        .annotate(total_spent=Sum('amount'))  # Sum the amounts for each category
        .order_by('category')  # Optional: Sort by category name
    )

    return render(request, 'index.html', {
        'expenses': expenses,  # Pass the expenses to the template
        'summary': summary  # Pass the summary data to the template
    })


# from django.shortcuts import render
# from django.db.models import Sum  # Import Sum for aggregation
# from budget.models import Expense  # Import the Expense model

# # View for the homepage
# def home(request):
#     return render(request, 'home.html')

# # View for adding a new expense
# def add_expense(request):
#     if request.method == "POST":
#         description = request.POST['description']
#         amount = request.POST['amount']
#         category = request.POST['category']

#         # Create a new Expense object and save it to the database
#         new_expense = Expense(description=description, amount=amount, category=category)
#         new_expense.save()

#         return render(request, 'add_expense.html', {
#             'message': f'Expense "{description}" added successfully!'
#         })

#     return render(request, 'add_expense.html')

# # View for the index page (showing all expenses and the summary)
# def index(request):
#     # Fetch all the expenses from the database, ordered by date
#     expenses = Expense.objects.all().order_by('-date')  # Newest expenses appear first

#     # Calculate total spending per category
#     summary = (
#         expenses.values('category')  # Group by category
#         .annotate(total_spent=Sum('amount'))  # Sum the amounts for each category
#         .order_by('category')  # Optional: Sort by category name
#     )

#     return render(request, 'index.html', {
#         'expenses': expenses,  # Pass the expenses to the template
#         'summary': summary  # Pass the summary data to the template
#     })



# from django.shortcuts import render
# from budget.models import Expense  # Import the Expense model

# # View for the homepage
# def home(request):
#     return render(request, 'home.html')

# # View for adding a new expense
# def add_expense(request):
#     if request.method == "POST":
#         description = request.POST['description']
#         amount = request.POST['amount']
#         category = request.POST['category']

#         # Create a new Expense object and save it to the database
#         new_expense = Expense(description=description, amount=amount, category=category)
#         new_expense.save()

#         return render(request, 'add_expense.html', {
#             'message': f'Expense "{description}" added successfully!'
#         })

#     return render(request, 'add_expense.html')

# # View for the index page (showing all expenses)
# def index(request):
#     # Fetch all the expenses from the database, ordered by date
#     expenses = Expense.objects.all().order_by('-date')  # Newest expenses appear first

#     return render(request, 'index.html', {
#         'expenses': expenses  # Pass the expenses to the template
#     })



# # views.py
# from django.shortcuts import render
# from budget.models import Expense  # Import the Expense model

# # View for the homepage
# def home(request):
#     return render(request, 'home.html')

# # View for adding a new expense
# def add_expense(request):
#     if request.method == "POST":
#         description = request.POST['description']
#         amount = request.POST['amount']
#         category = request.POST['category']

#         # Create a new Expense object and save it to the database
#         new_expense = Expense(description=description, amount=amount, category=category)
#         new_expense.save()

#         return render(request, 'add_expense.html', {
#             'message': f'Expense "{description}" added successfully!'
#         })

#     return render(request, 'add_expense.html')

# # View for the index page (showing all expenses)
# def index(request):
#     # Fetch all the expenses from the database
#     expenses = Expense.objects.all()

#     return render(request, 'index.html', {
#         'expenses': expenses  # Pass the expenses to the template
#     })