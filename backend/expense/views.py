from django.shortcuts import render
from .models import Expense, Category
from rest_framework import generics
from .models import Expense, Category
from .serializer import ExpenseSerializer, CategorySerializer

# Create your views here.
# EXPENSES
#CREATE & LIST ALL
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
#UPDATE, DELETE & SEARCH BY ID
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    def expense_detail(request, pk):
    # Your logic to retrieve the expense object based on the captured pk (ID)
        expense = Expense.objects.get(pk=pk)
    # ... rest of your view logic to handle the retrieved expense
        return render(request, 'templates/expense_detail.html', {'expense': expense})

# CATEGORY
#CREATE & LIST ALL
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#UPDATE, DELETE & SEARCH BY ID
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def category_detail(request, pk):
    # Your logic to retrieve the expense object based on the captured pk (ID)
        category = Category.objects.get(pk=pk)
    # ... rest of your view logic to handle the retrieved expense
        return render(request, 'templates/expense_detail.html', {'category': category})