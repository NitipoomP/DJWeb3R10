from django.db import models
from django.db import models

class Mproduct:
    def __init__(self, id, name, brand, price, amount,  made, total, discount, net):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.amount = amount
        self.made = made
        self.total = total
        self.discount = discount
        self.net = net

    def getInfo(self):
        return "ID: {0}, Name: {1}, Brand: {2}, Price: {3}, Net: {4}"\
            .format(self.id, self.name, self.brand, self.price, self.net, self.made)


class Category(models.Model):
    name =models.CharField(max_length=50, default="")
    desc =models.CharField(max_length=200, default="")

    def __str__(self):
        return str(self.id) + " : " + self.name + " : " + self.desc

class Product(models.Model):
    pid = models.CharField(max_length=13, primary_key=True, default="")
    name = models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=30, default="")
    price = models.FloatField(default=0.00)
    net = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.pid + " : " + self.name + " : " + self.brand + " : " + str(self.price) + " : " + \
               str(self.net) + " : " + self.category.name

import datetime
class Employee(models.Model):
    eid = models.CharField(max_length=13, default="")
    name = models.CharField(max_length=35, default="")
    surname = models.CharField(max_length=35, default="")
    address = models.CharField(max_length=200, default="")
    gender = models.BooleanField(default=True)
    birthdate = models.DateField(default=datetime.date.today())
    salary = models.FloatField(default=0.00)