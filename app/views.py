from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import csv
from app.models import *

def insert_bank(request):
    with open('C:\\Users\\jmadh\\OneDrive\\Desktop\\django projects\\madhan\\Scripts\\project39\\app\\bank.csv') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data inserted successfully')

def insert_branch(request):
    with open('C:\\Users\\jmadh\\OneDrive\\Desktop\\django projects\\madhan\\Scripts\\project39\\app\\branch1.csv') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                add=i[3]
                con=i[4]
                cty=i[5]
                drst=i[6]
                st=i[7]
                DBO=Branch(bank_name=BO[0],IFSC=ifs,branch=br,address=add,contact=con,city=cty,District=drst,State=st)
                DBO.save()
    return HttpResponse('Branch data inserted successfully')