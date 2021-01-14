from django.shortcuts import HttpResponse,render

from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    #number = 50
    #return render(request,'index.html',{"my_num":number})
    #name = "Michael"
    nums = [1,2,3,4,5]
    return render(request,'index.html',{"my_list":nums})

def about_me(request):
    return render(request,'about_me.html',{})

def eda(request):
    return render(request,'eda.html',{})

# def coffee_view(request):
#     coffee_all = Coffee.objects.all()
#     return render(request, 'coffee.html', {"coffee_list":coffee_all})

def coffee_view(request):
    http_method_names = ['get', 'post', 'put', 'delete']
    # 만약 request가 POST라면:
        # POST를 바탕으로 Form 을 완성하고
        # Form이 유효하면 -> 저장
    if request.POST.get("_method") == "post":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    elif request.POST.get("_method") == "put":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            row = Coffee.objects.get(id=request.POST.get('id'))
            row.name = request.POST.get('name')
            row.price = request.POST.get('price')
            if request.POST.get('is_ice') == 'false':
                row.is_ice = False
            else:
                row.is_ice = True
            row.stock = request.POST.get('stock')
            row.save()
    elif request.POST.get("_method") == "delete":
        row = Coffee.objects.get(id=request.POST.get('id'))
        row.delete()

    coffee_all = Coffee.objects.all()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list":coffee_all, "coffee_form":form})

