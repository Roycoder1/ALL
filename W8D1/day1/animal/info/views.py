from django.shortcuts import render
import json
# Create your views here.
def index(request):
    animals =  {
    "animals": [
            {
                "id" :1,
                "name": "Dog",
                "legs": 4,
                "weight": 5.67,
                "height":4.2,
                "speed": 34,
                "family": 2
            },
            {
                "id": 2,
                "name": "Domestic Cat",
                "legs": 2,
                "weight": 5.67,
                "height":4.2,
                "speed": 34,
                "family": 1
            },
            {
                "id": 3,
                "name": "Panther",
                "legs": 2,
                "weight": 5.67,
                "height":4.2,
                "speed": 34,
                "family": 1 
            }
        ],
        "families": [
            {
                "id": 1,
                "name": "Felidae"
            },
            {
                "id": 2,
                "name": "Caninae"
            }
        ]
    }
    return render(request,'index.html', {'animal': animals ,'family': 'families'})

# correction:

# with open('info/data.json','r') as f :
#     data = json.load(f)

# animals = data['animals']
# families = data [ 'families']

# def show_family(request,id):
#     family_selected = None

#     for family in families:
#         if family['id']==id :
#             family_selected = family
#     return render(request,'index.html',{'family':family_selected})

# def animal(request):
#     return render (request , '')