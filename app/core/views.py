from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book, Branch, Inventory

# Home view - list all models
def home(request):
    return render(request, 'core/home.html')

# Book views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        thumbnail_url = request.POST.get('thumbnail_url', '')
        price = request.POST.get('price', None)
        
        book = Book.objects.create(
            Author=author,
            Title=title,
            Description=description,
            ThumbnailUrl=thumbnail_url,
            Price=price if price else None
        )
        messages.success(request, f'Book "{book.Title}" created successfully!')
        return redirect('book_list')
    
    return render(request, 'core/book_form.html', {'action': 'Create'})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.Author = request.POST.get('author')
        book.Title = request.POST.get('title')
        book.Description = request.POST.get('description', '')
        book.ThumbnailUrl = request.POST.get('thumbnail_url', '')
        price = request.POST.get('price', None)
        book.Price = price if price else None
        book.save()
        
        messages.success(request, f'Book "{book.Title}" updated successfully!')
        return redirect('book_list')
    
    return render(request, 'core/book_form.html', {'book': book, 'action': 'Edit'})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        title = book.Title
        book.delete()
        messages.success(request, f'Book "{title}" deleted successfully!')
        return redirect('book_list')
    
    return render(request, 'core/book_confirm_delete.html', {'book': book})

# Branch views
def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'core/branch_list.html', {'branches': branches})

def branch_create(request):
    if request.method == 'POST':
        branch = Branch.objects.create(
            BranchName=request.POST.get('branch_name'),
            Address=request.POST.get('address'),
            City=request.POST.get('city'),
            State=request.POST.get('state'),
            Zip=request.POST.get('zip'),
            Phone=request.POST.get('phone', '')
        )
        messages.success(request, f'Branch "{branch.BranchName}" created successfully!')
        return redirect('branch_list')
    
    return render(request, 'core/branch_form.html', {'action': 'Create'})

def branch_edit(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    
    if request.method == 'POST':
        branch.BranchName = request.POST.get('branch_name')
        branch.Address = request.POST.get('address')
        branch.City = request.POST.get('city')
        branch.State = request.POST.get('state')
        branch.Zip = request.POST.get('zip')
        branch.Phone = request.POST.get('phone', '')
        branch.save()
        
        messages.success(request, f'Branch "{branch.BranchName}" updated successfully!')
        return redirect('branch_list')
    
    return render(request, 'core/branch_form.html', {'branch': branch, 'action': 'Edit'})

def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    
    if request.method == 'POST':
        name = branch.BranchName
        branch.delete()
        messages.success(request, f'Branch "{name}" deleted successfully!')
        return redirect('branch_list')
    
    return render(request, 'core/branch_confirm_delete.html', {'branch': branch})

# Inventory views
def inventory_list(request):
    inventory = Inventory.objects.all().select_related('Book', 'Branch')
    return render(request, 'core/inventory_list.html', {'inventory': inventory})

def inventory_create(request):
    if request.method == 'POST':
        book_id = request.POST.get('book')
        branch_id = request.POST.get('branch')
        quantity = request.POST.get('quantity')
        
        try:
            inventory = Inventory.objects.create(
                Book_id=book_id,
                Branch_id=branch_id,
                Quantity=quantity
            )
            messages.success(request, 'Inventory record created successfully!')
            return redirect('inventory_list')
        except Exception as e:
            messages.error(request, f'Error creating inventory: {str(e)}')
    
    books = Book.objects.all()
    branches = Branch.objects.all()
    return render(request, 'core/inventory_form.html', {
        'books': books, 
        'branches': branches, 
        'action': 'Create'
    })

def inventory_edit(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        inventory.Book_id = request.POST.get('book')
        inventory.Branch_id = request.POST.get('branch')
        inventory.Quantity = request.POST.get('quantity')
        
        try:
            inventory.save()
            messages.success(request, 'Inventory record updated successfully!')
            return redirect('inventory_list')
        except Exception as e:
            messages.error(request, f'Error updating inventory: {str(e)}')
    
    books = Book.objects.all()
    branches = Branch.objects.all()
    return render(request, 'core/inventory_form.html', {
        'inventory': inventory,
        'books': books, 
        'branches': branches, 
        'action': 'Edit'
    })

def inventory_delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        inventory.delete()
        messages.success(request, 'Inventory record deleted successfully!')
        return redirect('inventory_list')
    
    return render(request, 'core/inventory_confirm_delete.html', {'inventory': inventory})