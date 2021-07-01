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

Model()

# the BAX, binding sites, diff site states
# shell setup for future initiations of the BAX
Monomer('BAX', ['t1', 't2'], {'t1' : ['actv', 'inactv']}, {'t2' : ['actv', 'inactv']} )  

# how program 'under stress conditions' ... that cause conformation change, 
# ... ... the conf-change that thus causes movement (translocation) to mito-memb
# https://www.uniprot.org/uniprot/Q07812




