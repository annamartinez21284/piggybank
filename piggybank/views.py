from django.shortcuts import render
import requests
import json
import os
from .helpers import *
from dotenv import load_dotenv
from .models import *

load_dotenv()
#https://developer.starlingbank.com/docs
#sguid1 = 'd37c59e9-e8c5-40a8-b87e-cdb5e25cae98'

base_url = 'https://api-sandbox.starlingbank.com/'

# Create your views here.
def index(request):

  context = {"customers": Customer.objects.all()}

  return render(request, "starling/index.html", context)
