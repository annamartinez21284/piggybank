from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
import json
import os
from .helpers import *
from dotenv import load_dotenv
from .models import *
from urllib.parse import urlencode

load_dotenv()

base_url = 'https://api-sandbox.starlingbank.com'

def index(request):
  request.session.clear()
  context = {"customers": Customer.objects.all()}
  return render(request, "starling/index.html", context)


def customer_info(request, customer_id=None):

  if customer_id is None: #request.session["customer_id"]
    customer = Customer.objects.get(customer_id=request.POST.get("customer", False))
    customer_id = customer.customer_id
    request.session["customer_id"] = customer_id
  else:
    # customer_id = request.session["customer_id"]
    customer = Customer.objects.get(customer_id=customer_id)

  print('CUSTOMER ISSSSS', customer)
  # only GBP accounts, in this app simplification: only 1 acct per customer, acct in GBP
  account = Account.objects.filter(accountholder=customer_id, currency="GBP")
  accountUid = account[0].accountUid
  request.session["accountUid"] = accountUid
  print("ACCOUNTUID", accountUid)

  # Get customer's savings goals if any
  url_1 = base_url + "/api/v2/account/"+accountUid+"/savings-goals"
  headers = get_headers(customer.refresh_token)
  request.session["headers"] = headers
  res_1 = requests.get(url_1, headers=headers)

  if res_1.status_code != 200:
    raise Exception("ERROR: API request unsuccessful.")

  # Get customer's GBP acct balance
  url_2 = base_url + "/api/v2/accounts/"+accountUid+"/balance"
  res_2 = requests.get(url_2, headers=headers)

  if res_2.status_code != 200:
    raise Exception("ERROR: API GET request unsuccessful.")

  savingsGoalList = res_1.json()["savingsGoalList"] # this is a list of dicts
  context = {"customer": customer, "balance": res_2.json()["effectiveBalance"]} # this is a dict
  contextWithSavings = {"context": context, "savingsGoalList": savingsGoalList}

  print("CONTEXT WITH SAVINGS", contextWithSavings)
  # if customer has no goals
  if not savingsGoalList:
    # redirect to create savings goal & from there to view all goals
    print(savingsGoalList) #[]
    return render(request, "starling/show_details.html", contextWithSavings)
  #elif goals exist, show all goals

  return render(request, "starling/show_details.html", contextWithSavings)

def create_goal(request):
  goal_name = request.POST["goalName"]
  goal = request.POST["goal"].strip("£").replace(".", "").replace(",", "")
  goal = int(goal)
  print("GOAL NAME: ", goal_name)
  print("GOAL: ", goal)

  accountUid = request.session["accountUid"]
  url = base_url + "/api/v2/account/"+accountUid+"/savings-goals"
  headers = request.session["headers"]
  json = {"name": goal_name,"currency": "GBP","target": {"currency": "GBP", "minorUnits": goal}}
  res = requests.put(url, headers=headers, json=json)
  print(res.json())
  if res.status_code != 200 and res.status_code != 204:
    raise Exception("ERROR: API PUT request unsuccessful.")

  customer_id = request.session["customer_id"]

  return redirect('customer_info_id', customer_id= customer_id)

def delete(request, savingsGoalUid):
    accountUid = request.session["accountUid"]
    customer_id = request.session["customer_id"]

    url = f"{base_url}/api/v2/account/{accountUid}/savings-goals/{savingsGoalUid}"

    customer = Customer.objects.get(customer_id=customer_id)
    headers = get_headers(customer.refresh_token)
    res = requests.delete(url, headers=headers)

    return redirect('customer_info_id', customer_id= customer_id)
