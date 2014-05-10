#!/bin/python3
import struct
from pkmdata import pokedex
from pkmdata import abilitydex
import csv

# When reading a binary file, always add a 'b' to the file open mode
with open('charmander_scratch_bin.pkm', 'rb') as f:
    f.seek(0)
    bytes = f.read(4)
    PID = ( bytes[3] << 24 ) + ( bytes[2] << 16 ) + \
          ( bytes[1] << 8  ) + ( bytes[0] << 0  )
    f.seek(0x38)
    bytes = f.read(4)
    IVs = ( bytes[3] << 24 ) + ( bytes[2] << 16 ) + \
          ( bytes[1] << 8  ) + ( bytes[0] << 0  )
    HP = IVs % 32
    IVs >>= 5;
    Atk = IVs % 32
    IVs >>= 5;
    Def = IVs % 32
    IVs >>= 5;
    Spe = IVs % 32
    IVs >>= 5;
    SpA = IVs % 32
    IVs >>= 5;
    SpD = IVs % 32
    IVs >>= 5;
    IsEgg = IVs %2;
    IsNick = IVs / 2;
    f.seek(8)
    bytes = f.read(2)
    DexNo = ( bytes[1] << 8 ) + bytes[0]
    DexName = pokedex[str(DexNo)].capitalize()
    f.seek(0x15)
    bytes = f.read(1)
    AbilityNo = bytes[0]
    Ability = abilitydex[str(AbilityNo)].capitalize()
f.close()

""" Display Data Stuffs """
print("#" + str(DexNo) + ": " + DexName)
print("PID: " + hex(PID).upper() + " / " + str(PID))
print( str(HP) + " HP / " + str(Atk) + " Atk / " + str(Def) + \
       " Def / " + str(SpA) + " SpA / " + str(SpD) + " SpD / " \
       + str(Spe) + " Spe")
print( "Is Egg: " + str(bool(IsEgg)) )
print( "Is Nicknamed: " + str(bool(IsNick)) )
print( "Ability: " + Ability )
