# Capitilize
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.

name_surname = input("enter name and surname")
if len(name_surname) <= 1000:
    name,surname = name_surname.split(" ")
    print(name[0].upper()+name[1:],"",surname[0].upper()+surname[1:])
