## descriptive text from Panda 2020 apoptosis review article
## https://ejmcm.com/article_3657.html
## layout helped by https://github.com/LoLab-VU/pysb/blob/master/pysb/examples/bax_pore.py

## hax is like an ax, and like hacking the cell
##  ...  or are we hacking bax

from __future__ import print_function
from pysb import *

##  *+* operator to represent complexation
##  *|* operator to represent backward/forward reaction
##  *>>* operator to represent forward-only reaction
##  *%* operator to represent a binding interaction between two species

Model('your_cell')

# the BAX, binding sites, diff site states
# shell setup for future initiations of the BAX
# the tail hooks into the MOM, mitochondrial outer membrane
Monomer('BAX', ['t1', 't2', 'tail'], {'t1' : ['actv', 'inactv']}, {'t2' : ['actv', 'inactv']}, {'tail' : ['mom_hooked', 'cyto_float']} )  

# how program 'under stress conditions' ... that cause conformation change, 
# ... ... the conf-change that thus causes movement (translocation) to mito-memb
# https://www.uniprot.org/uniprot/Q07812

# default is no-bax
# no-bax always when bax NOT activated
Mitochondria('MOM', ['pore1', 'pore2', 'pore3'], 
             {'pore1' : ['mono-bax', 'di-bax', 'multi-bax', 'no-bax']},
             {'pore2' : ['mono-bax', 'di-bax', 'multi-bax', 'no-bax']}
             {'pore3' : ['mono-bax', 'di-bax', 'multi-bax', 'no-bax']} )




