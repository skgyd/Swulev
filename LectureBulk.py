import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swulev.settings')
django.setup()

from swuapp.models import Lecture

f = open('lecture.csv', 'r')
info = []

rdr = csv.reader(f)
for row in rdr:
    lectureid, lecturename, semester, professor = row
    tuple = (lectureid, lecturename, semester, professor)
    info.append(tuple)
f.close()

instances = []
for (lectureid, lecturename, semester, professor) in info:
    instances.append(Lecture(lectureid=lectureid, lecturename=lecturename, semester=semester, professor=professor))

Lecture.objects.bulk_create(instances)
