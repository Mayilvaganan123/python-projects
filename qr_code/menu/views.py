from django.shortcuts import render
from .models import FoodItems
from django.http import JsonResponse
from django.utils import timezone


orders= []
def submit_order(request):
    if request.method=="POST":
        table_no = request.POST['table_no']
        food_list = request.POST['food_list']
        Created_at = timezone.now()
        orders.append({'table':table_no, "order":food_list,'Created_at':Created_at})
        return JsonResponse({"success":True})
        
def Dashboard(request):
    return render(request,'Dashboard.html',{'orders':orders})

def menu_view(request):
    selected_category = request.GET.get("category", "")

    categories = FoodItems.objects.values_list("category", flat=True).distinct()

    if selected_category:
        items = FoodItems.objects.filter(category=selected_category)
    else:
        items = FoodItems.objects.all()

    return render(request, "menu.html", {
        "items": items,               # used for displaying menu cards + ordering
        "categories": categories,     # used for dropdown
        "selected_category": selected_category
    })



