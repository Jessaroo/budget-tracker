from collections import defaultdict
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib import messages
from budget.models import Expense

# View for the homepage
def home(request):
    return render(request, 'home.html')

# View for adding a new expense
def add_expense(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        category = request.POST.get('category')

        # Basic validation to ensure fields are not empty
        if not description or not amount or not category:
            messages.error(request, "All fields are required!")
            return redirect('add_expense')

        # Create a new Expense object and save it to the database
        new_expense = Expense(description=description, amount=amount, category=category)
        new_expense.save()

        # Add a success message
        messages.success(request, f'Expense "{description}" added successfully!')

        # Redirect to the index page after adding the expense
        return redirect('index')

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
    
    # Group expenses by year and month
    grouped_expenses = defaultdict(list)
    for expense in expenses:
        key = (expense.date.year, expense.date.month)
        grouped_expenses[key].append(expense)

    # Sort grouped data by year and month (descending order)
    sorted_expenses = sorted(grouped_expenses.items(), key=lambda x: x[0], reverse=True)

    # Format the year and month as "Month Year"
    formatted_expenses = []
    for (year, month), expense_list in sorted_expenses:
        formatted_month_year = f"{expense_list[0].date.strftime('%B')} {year}"
        formatted_expenses.append((formatted_month_year, expense_list))

    return render(request, 'index.html', {
        'expenses': expenses,  # Pass the expenses to the template
        'summary': summary,  # Pass the summary data to the template
        'grouped_expenses': formatted_expenses,  # Pass the formatted expenses data to the template
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