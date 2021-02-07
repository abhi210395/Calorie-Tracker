from django.shortcuts import render,redirect
from .models import Food,Consume

# Create your views here.

def index(request):

    #To check incoming request is POST
    if request.method == "POST":
        #To get the text from the input selected
        food_consumed = request.POST["food_consumed"]
        #To fetch the data based on name
        consume = Food.objects.get(name=food_consumed)
        #To get the user logged in 
        user = request.user
        #Object creation
        consume = Consume(user=user,food_consumed=consume)
        #To save the object
        consume.save()
        foods =Food.objects.all()#To fetch all the objects 
    else:
        foods =Food.objects.all()#To display list of food items
    consumed_food = Consume.objects.filter(user=request.user)#To show the consumed food 
    return render(request,"calorie/index.html",{"foods":foods,"consumed_food": consumed_food})


def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if (request.method == "POST"):
        consumed_food.delete()
        return redirect("/")
    return render(request,'calorie/delete.html')