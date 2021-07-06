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

# random numbers
kf = 1e-5
kr = 2e-4


# the BAX, binding sites, diff site states
# shell setup for future initiations of the BAX
# the tail hooks into the MOM, mitochondrial outer membrane
Monomer('BAX', ['t1', 't2', 'bh3', 'tag', 'tail'], {'t1' : ['actv', 'inactv']}, {'t2' : ['actv', 'inactv']}, 
        {'bh3' : ['bound', 'unbound']}, {'tag' : ['taken', 'untaken']}, {'tail' : ['mom_hooked', 'cyto_float']} )  

# temporary intervening-shuttling
## figure 2 of Moldoveanu
Monomer('BCL-XL', ['bh3'], {'bh3' : ['bound', 'unbound']} )
# UBIT gives a tag of death
Monomer('UBIT', ['death_tag'], {'death_tag' : ['given', 'ungiven']} )  

## BEFORE entering the MITO
# rule for retrotranslocation, reversible
# Moldoveanu: 
"""BAX exists in a dynamic equilibrium shuttling
between the mitochondria and cytosol, a process
termed retrotranslocation (Edlich et al. 2011). In
nonapoptotic cells, this equilibrium is weighted
such that BAX is primarily cytosolic.
"""
# BAX, ubiquitin , BCL-xL
##  BAX + Ub <--> BAX:Ub   (tagged)
##  BAX:Ub + BCL-xL <--> (BAX:Ub):BCL-xL  (shuttle from mito)
##  (BAX:Ub):BCL-xL <--> BAX + Ub + BCL-xL  (disassociation)

Rule('BAX_death_tag', BAX(tag='untaken', tail='cyto_float', bh3='unbound') + UBIT(death_tag='ungiven') | 
          BAX(tag='taken') % UBIT(death_tag='given'), kf, kr)

# can we write more than two things being bound?
# need to rewrite -tail and -bh3 state for BAX??
Rule('BCL_XL_chaperoning_BAX', BAX(tag='taken', bh3='unbound') % UBIT(death_tag='given') + BCL-XL(bh3='unbound') |
          BAX(tag='taken', bh3='bound') % UBIT(death_tag='given') % BCL=XL(bh3='bound'), kf, kr)

# disassociate rule, BAX released to free cytosol
Rule('Unchaperone_BAX', BAX(tag='taken', bh3='bound') % UBIT(death_tag='given') % BCL-XL(bh3='bound') |
         BAX(tag='untaken', bh3='unbound') + UBIT(death_tag='ungiven') + BCL-XL(bh3='unbound') )

     
     
## "All BCL-2 family proteins contain a BH3 domain; one of four
## BH domainsinvolved in interactions between these proteins"
#### 2018 - Kale - dance towards death  
#### https://www.nature.com/articles/cdd2017186.pdf

# guardians - anti-apoptotic
# BCL-2, BCL-XL, BCL-W, MCL-1, BFL-1/A1

# attackers - pro-apoptotic pore-formers
# BAX, BAK, BOK

# attackers - pro-apoptotic "BH3-only proteins"
# BAD, BID, BIK, BIM, BMF, HRK, NOXA, PUMA, 'etc'




# how program 'under stress conditions' ... that cause conformation change, 
# ... ... the conf-change that thus causes movement (translocation) to mito-memb
# https://www.uniprot.org/uniprot/Q07812

# default is no-bax
# no-bax always when bax NOT activated
Mitochondria('MOM', ['pore1', 'pore2', 'pore3'], 
             {'pore1' : ['mono-bax', 'di-bax', 'multi-bax', 'no-bax']},
             {'pore2' : ['mono-bax', 'di-bax', 'multi-bax', 'no-bax']}
             {'pore3' : ['mono-bax', 'di-bax', 'multi-bax', 'no-bax']} )

## pending - Monomer('P53', [] )
