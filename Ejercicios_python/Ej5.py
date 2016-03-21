# -*- coding: utf-8 -*-
import time

# 5) Diseñar un presupuesto con una clase ModeloPresupuesto pidiendo los siguientes datos:
# Nombre de la empresa, nombre del cliente, fecha del presupuesto, descripción del
# servicio, importe bruto, fecha de caducidad , iva e importe total

class ModeloPresupuesto(object):
    estimate_ID = 1000;
    def __init__(self, company, customer, service_description, gross_amount, expiry_date, iva, total_amount ):
        self.company = company
        self.customer = customer
        self.estimate_ID = self.estimate_ID
        self.service = service_description
        self.gross_amount = gross_amount
        self.expiry_date = expiry_date
        self.iva = iva
        self.total_amount = total_amount
        self.estimate_ID += 100
        time.sleep(2)
        return

class Menu(object):
    def __init__(self):
        return

    def showMenu(self):
        print("-----------------------------------")
        print("-------Estimate creator v1.0-------")
        print("-----------------------------------")

        company = input("Enter company name: \n")
        customer = input("Enter customer name: \n")
        service_description = input("Enter a short description for service: \n")
        gross_amount = input("Enter the gross amount: \n")
        expiry_date = input("Enter expiry date: \n")
        iva = input("Enter IVA tax: \n")
        total_amount = input("Enter total amount: \n")

        print("--------Calculating Estimate ... -------")
        estimate = ModeloPresupuesto(company,customer,service_description,gross_amount,expiry_date,iva,total_amount)
        print(estimate.__dict__)


menu = Menu()
menu.showMenu()