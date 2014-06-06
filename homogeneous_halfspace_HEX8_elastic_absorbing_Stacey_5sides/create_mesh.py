#!python
#!/usr/bin/env python

# "create_mesh.py" is a script that generates mesh specific to homogenous halfspace example
# i.e., a uniform mesh of 134 km x 134 km x 60 km with an element size 3.75 km.
# It is not applicable to other examples.

import cubit
import boundary_definition
import cubit2specfem3d

import os
import sys

cubit.cmd('reset')
cubit.cmd('brick x 67000 y 134000 z 60000')
cubit.cmd('volume 1 move x 33500 y 67000 z -30000')
cubit.cmd('brick x 67000 y 134000 z 60000')
cubit.cmd('volume 2 move x 100500 y 67000 z -30000')
cubit.cmd('merge all')

# Meshing the volumes
elementsize = 3000.0


cubit.cmd('volume 1 size '+str(elementsize))
cubit.cmd('volume 2 size '+str(elementsize))
cubit.cmd('mesh volume 1 2')


from geocubitlib import boundary_definition,exportlib

boundary_definition.define_bc(parallel=True)

exportlib.collect(outdir='MESH/')
exportlib.e2SEM(outdir='MESH/')

