import json
from django.shortcuts import render
from django.http import HttpResponse
from polls.db.oracle import lista

def index(request):
    return HttpResponse(json.dumps(lista))
# si renderizas lista normal te devuelve igual una lista de python
# pero yo lo parsie a un json pq si por tanto este views.py es un json consumible
# https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html