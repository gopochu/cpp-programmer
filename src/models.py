from django.db import models

class History_First(models.Model):
    titleF = models.CharField(max_length=400)
    hero = models.CharField(max_length=1000)

class History_Second(models.Model):
    titleS = models.CharField(max_length=400)
    about = models.CharField(max_length=4000)

class Born(models.Model):
    titleB = models.CharField(max_length=400)
    born = models.CharField(max_length=4000)

class Compatibility(models.Model):
    titleC = models.CharField(max_length=400)
    compatibility = models.CharField(max_length=4000)

class Usage(models.Model):
    titleU = models.CharField(max_length=400)
    usage = models.CharField(max_length=4000)

#====================================================

class DemandHeader(models.Model):
    titleDH = models.CharField(max_length=400)
    demand_header = models.CharField(max_length=500)

class AllSalary(models.Model):
    titleAS = models.CharField(max_length=400)
    all_salary = models.CharField(max_length=4000)

class AllVacancy(models.Model):
    titleAV = models.CharField(max_length=400)
    all_vacancy = models.CharField(max_length=4000)

class CppSalary(models.Model):
    titleCS = models.CharField(max_length=400)
    cpp_salary = models.CharField(max_length=4000)

class CppVacancy(models.Model):
    titleCV = models.CharField(max_length=400)
    cpp_vacancy = models.CharField(max_length=4000)

class AllSalaryImg(models.Model):
    all_salary_img = models.ImageField()

#<-- images -->

class Image(models.Model):
    title = models.CharField(max_length=200)
    imageAS = models.ImageField(blank=True, upload_to='images')
    imageAV = models.ImageField(blank=True, upload_to='images')
    imageCS = models.ImageField(blank=True, upload_to='images')
    imageCV = models.ImageField(blank=True, upload_to='images')
    def __str__(self):
        return self.title

#<--//images -->

class GeographyHeader(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)

class CitySalary(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)

class VacancyRate(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)

class CitySalaryCpp(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)

class VacancyRateCpp(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)


class Graphs(models.Model):
    graphsCS = models.ImageField(blank=True, upload_to='images')
    graphsVR = models.ImageField(blank=True, upload_to='images')
    graphsCSC = models.ImageField(blank=True, upload_to='images')
    graphsVRC = models.ImageField(blank=True, upload_to='images')

class BestSkills(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)
    table = models.CharField(max_length=15000)


class BestSkillsCpp(models.Model):
    title = models.CharField(max_length=400)
    text = models.CharField(max_length=4000)
    table = models.TextField(max_length=15000)