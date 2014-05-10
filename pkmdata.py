#!/bin/python3
import csv
"""reader = csv.reader(open('pokemon.csv'), delimiter=',')
for row in reader:
    print (row)"""
from csv import DictReader
reader = DictReader(open('pokemon.csv','r'),("species_id","identifier"))

list_of_pkmn = []
for i in reader:
    list_of_pkmn.append(i)

pokedex = {}
for i in list_of_pkmn:
    pokedex[i["species_id"]]=i["identifier"] # data['1'] gives 'bulbasaur', etc.

reader = DictReader(open('abilities.csv','r'),("id","identifier"))

list_of_abilities = []
for i in reader:
    list_of_abilities.append(i)

abilitydex = {}
for i in list_of_abilities:
    abilitydex[i["id"]]=i["identifier"]
