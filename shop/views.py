import eav
from django.shortcuts import render
from django.http import HttpResponse
from eav.models import Attribute,EnumValue,EnumGroup
from shop.models import Product


def add_attribute(request):
    yes = EnumValue.objects.create(value='yes')
    no = EnumValue.objects.create(value='no')
    unkown = EnumValue.objects.create(value='unkown')
    ynu = EnumGroup.objects.create(name='Yes / No / Unkown')
    ynu.enums.add(yes,no,unkown)
    Attribute.objects.create(name = 'Has Fever?',datatype=Attribute.TYPE_ENUM,enum_group=ynu)

    return HttpResponse("Attribute has been added")
