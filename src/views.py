from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import History_First, History_Second, Born, Compatibility, Usage, DemandHeader, AllSalary, AllVacancy, CppSalary, CppVacancy, Image, Graphs, CitySalary, VacancyRate, CitySalaryCpp, VacancyRateCpp, GeographyHeader, BestSkills, BestSkillsCpp

def index(request):
    return render(request, "index.html")


def demand(request):
    return render(request, "demand.html")


def geography(request):
    return render(request, 'geography.html')

def skills(request):
    return render(request, 'skills.html')

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

def geography(request):
    geography_header = GeographyHeader.objects.all()
    city_salary = CitySalary.objects.all()
    vacancy_rate = VacancyRate.objects.all()
    city_salary_cpp = CitySalaryCpp.objects.all()
    vacancy_rate_cpp = VacancyRateCpp.objects.all()
    graphs = Graphs.objects.all()
    return render(request, "geography.html", {"geography_header": geography_header, "city_salary": city_salary, "vacancy_rate": vacancy_rate, "city_salary_cpp": city_salary_cpp, "vacancy_rate_cpp": vacancy_rate_cpp, "graphs": graphs})

def skills(request):
    best_skills = BestSkills.objects.all()
    best_skills_cpp = BestSkillsCpp.objects.all()
    return render(request, "skills.html", {"best_skills": best_skills, "best_skills_cpp": best_skills_cpp})