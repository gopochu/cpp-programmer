from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import History_First, History_Second, Born, Compatibility, Usage, DemandHeader, AllSalary, AllVacancy, CppSalary, CppVacancy, Image

def index(request):
    return render(request, "index.html")


def demand(request):
    return render(request, "demand.html")


def contact(request):
    return HttpResponse('Контакты')

# <!-- index -->

# получение данных из бд
def index(request):
    hero = History_First.objects.all()
    about = History_Second.objects.all()
    born = Born.objects.all()
    compatibility = Compatibility.objects.all()
    usage = Usage.objects.all()
    return render(request, "index.html", {"hero": hero, "about": about, "born": born, "compatibility": compatibility, "usage": usage})



# <!--//index -->
# <!-- demand -->
def demand(request):
    demand_header = DemandHeader.objects.all()
    all_salary = AllSalary.objects.all()
    all_vacancy = AllVacancy.objects.all()
    cpp_salary = CppSalary.objects.all()
    cpp_vacancy = CppVacancy.objects.all()
    image = Image.objects.all()
    return render(request, "demand.html", {"demand_header": demand_header, "all_salary": all_salary, "all_vacancy": all_vacancy, "cpp_salary": cpp_salary, "cpp_vacancy": cpp_vacancy, 'image': image})

# <!--//demand -->



# def image_upload_view(request):
#     """Process images uploaded by users"""
#     image = Image
#     return render(request, 'demand.html', {'image': image})
