from django.shortcuts import render

# View for the homepage
def home(request):
    return render(request, 'home.html')

# View for adding a new expense
def add_expense(request):
    if request.method == "POST":
        # Here you would handle the form submission to add the expense to the database
        description = request.POST['description']
        amount = request.POST['amount']
        category = request.POST['category']

        # Add logic to save this data in the database (e.g., create a new Expense object)
        return render(request, 'add_expense.html', {
            'message': f'Expense "{description}" added successfully!'
        })

    # GET request: show the form to add a new expense
    return render(request, 'add_expense.html')

# View for the index page (this could be a summary of expenses, for example)
def index(request):
    return render(request, 'index.html')