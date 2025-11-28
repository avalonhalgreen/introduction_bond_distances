#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ase import Atoms

atoms = Atoms('H2O', positions=[(0, 0, 1), (0, 1, 0), (0, 0, 0)])

for atom in atoms:
    atom_1 = atom
    position_1 = atom.position
    for atom in atoms:
        atom_2 = atom
        if atom_2.index > atom_1.index: 
            position_2 = atom.position
            sq_vector = (position_1 - position_2)**2
            distance = (sq_vector[0] + sq_vector[1] + sq_vector[2])**0.5
            print(atom_1.symbol, atom_1.index, "-", atom_2.symbol, atom_2.index, "distance = ", distance)

# this finds all distance, how to refine to just distances of bonded atoms? 

print ("testing function..")

def find_bond_length (atom_a, atom_b):
    pos_a = atom_a.position
    pos_b = atom_b.position
    sq_vector = (pos_a - pos_b)**2
    distance = (sq_vector[0] + sq_vector[1] + sq_vector[2])**0.5
    print(atom_a.symbol, atom_a.index, "-", atom_b.symbol, atom_b.index, "distance = ", distance)

find_bond_length(atoms[0], atoms[1])
# should find the H-H distance 

