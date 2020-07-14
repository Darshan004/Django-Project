from django.shortcuts import render, redirect
from django.http import HttpResponse
from macd.models import values,values2
import numpy as np
from .forms import InputsForm


def index(request):
    if request.method == 'POST':
        # create new 'values' object
        vals = values()
        vals2 = values2()
        vals.zero = 0
        vals.hocan15 = float(request.POST['hocan15'])
        vals.g1sb015 = float(request.POST['g1sb015'])
        vals.corn15 = float(request.POST['corn15'])
        vals.hsbo15 = float(request.POST['hsbo15'])
        vals.stote_oil_blend15 = vals.g1sb015/(16.5/100)
        vals.chicken_par_fry15 = (
        vals.corn15 - vals.stote_oil_blend15*20/100)/(45/100)
        vals.macd_system_total15 = vals.stote_oil_blend15 + vals.chicken_par_fry15


        vals.hocan16 = float(request.POST['hocan16'])
        vals.g1sb016 = float(request.POST['g1sb016'])
        vals.corn16 = float(request.POST['corn16'])
        vals.hsbo16 = float(request.POST['hsbo16'])
        vals.stote_oil_blend16 = vals.g1sb016/(16.5/100)
        vals.chicken_par_fry16 = (vals.corn16 - (vals.stote_oil_blend16*20/100))/(45/100)
        vals.macd_system_total16 = vals.stote_oil_blend16 + vals.chicken_par_fry16

        vals.hocan17 = float(request.POST['hocan17'])
        vals.g1sb017 = float(request.POST['g1sb017'])
        vals.corn17 = float(request.POST['corn17'])
        vals.hsbo17 = float(request.POST['hsbo17'])
        vals.stote_oil_blend17 = vals.g1sb017/(16.5/100)
        vals.chicken_par_fry17 = (vals.corn17 - (vals.stote_oil_blend17*20/100))/(45/100)
        vals.macd_system_total17 = vals.stote_oil_blend17 + vals.chicken_par_fry17

        vals.hocan18 = float(request.POST['hocan18'])
        vals.g1sb018 = float(request.POST['g1sb018'])
        vals.corn18 = float(request.POST['corn18'])
        vals.hsbo18 = float(request.POST['hsbo18'])
        vals.stote_oil_blend18 = vals.g1sb018/(16.5/100)
        vals.chicken_par_fry18 = (vals.corn18 - (vals.stote_oil_blend18*20/100))/(45/100)
        vals.macd_system_total18 = vals.stote_oil_blend18 + vals.chicken_par_fry18

        vals.hocan19 = float(request.POST['hocan19'])
        vals.g1sb019 = float(request.POST['g1sb019'])
        vals.corn19 = float(request.POST['corn19'])
        vals.hsbo19 = float(request.POST['hsbo19'])
        vals.stote_oil_blend19 = vals.g1sb019/(16.5/100)
        vals.chicken_par_fry19 = (vals.corn19 - (vals.stote_oil_blend19*20/100))/(45/100)
        vals.macd_system_total19 = vals.stote_oil_blend19 + vals.chicken_par_fry19

        vals.hocan20 = float(request.POST['hocan20'])
        vals.g1sb020 = float(request.POST['g1sb020'])
        vals.corn20 = float(request.POST['corn20'])
        vals.hsbo20 = float(request.POST['hsbo20'])
        vals.stote_oil_blend20 = vals.g1sb020/(16.5/100)
        vals.chicken_par_fry20 = (vals.corn20 - (vals.stote_oil_blend20*20/100))/(45/100)
        vals.macd_system_total20 = vals.stote_oil_blend20 + vals.chicken_par_fry20

        vals.hocan21 = float(request.POST['hocan21'])
        vals.g1sb021 = float(request.POST['g1sb021'])
        vals.corn21 = float(request.POST['corn21'])
        vals.hsbo21 = float(request.POST['hsbo21'])
        vals.stote_oil_blend21 = vals.g1sb021/(16.5/100)
        vals.chicken_par_fry21 = (vals.corn21 - (vals.stote_oil_blend21*20/100))/(45/100)
        vals.macd_system_total21 = vals.stote_oil_blend21 + vals.chicken_par_fry21

        vals.hocan22 = float(request.POST['hocan22'])
        vals.g1sb022 = float(request.POST['g1sb022'])
        vals.corn22 = float(request.POST['corn22'])
        vals.hsbo22 = float(request.POST['hsbo22'])
        vals.stote_oil_blend22 = vals.g1sb022/(16.5/100)
        vals.chicken_par_fry22 = (vals.corn22 - (vals.stote_oil_blend22*20/100))/(45/100)
        vals.macd_system_total22 = vals.stote_oil_blend22 + vals.chicken_par_fry22

        vals.hocan23 = float(request.POST['hocan23'])
        vals.g1sb023 = float(request.POST['g1sb023'])
        vals.corn23 = float(request.POST['corn23'])
        vals.hsbo23 = float(request.POST['hsbo23'])
        vals.stote_oil_blend23 = vals.g1sb023/(16.5/100)
        vals.chicken_par_fry23 = (vals.corn23 - (vals.stote_oil_blend23*20/100))/(45/100)
        vals.macd_system_total23 = vals.stote_oil_blend23 + vals.chicken_par_fry23

        vals.hocan24 = float(request.POST['hocan24'])
        vals.g1sb024 = float(request.POST['g1sb024'])
        vals.corn24 = float(request.POST['corn24'])
        vals.hsbo24 = float(request.POST['hsbo24'])
        vals.stote_oil_blend24 = vals.g1sb024/(16.5/100)
        vals.chicken_par_fry24 = (vals.corn24 - (vals.stote_oil_blend24*20/100))/(45/100)
        vals.macd_system_total24 = vals.stote_oil_blend24 + vals.chicken_par_fry24

        vals.rhpko15 = float(request.POST['rhpko15'])
        vals.rhpkol15 = float(request.POST['rhpkol15'])
        vals.rhpkst15 = float(request.POST['rhpkst15'])
        vals.shortening15 = float(request.POST['shortening15'])
        vals.rhpo15 = float(request.POST['rhpo15'])
        vals.rpst15 = float(request.POST['rpst15'])
        vals.rhpst15 = float(request.POST['rhpst15'])
        vals.rhcno15 = float(request.POST['rhcno15'])
        vals.rcno15 = float(request.POST['rcno15'])
        vals.rpko15 = float(request.POST['rpko15'])
        vals.subtotal15 =( vals.rhpko15 + vals.rhpkol15 + vals.rhpkst15 + vals.shortening15 + vals.rhpo15 + vals.rpst15 + 
                        vals.rhpst15 + vals.rhcno15 + vals.rcno15 + vals.rpko15 )

        vals.rhpko16 = float(request.POST['rhpko16'])
        vals.rhpkol16 = float(request.POST['rhpkol16'])
        vals.rhpkst16 = float(request.POST['rhpkst16'])
        vals.shortening16 = float(request.POST['shortening16'])
        vals.rhpo16 = float(request.POST['rhpo16'])
        vals.rpst16 = float(request.POST['rpst16'])
        vals.rhpst16 = float(request.POST['rhpst16'])
        vals.rhcno16 = float(request.POST['rhcno16'])
        vals.rcno16 = float(request.POST['rcno16'])
        vals.rpko16 = float(request.POST['rpko16'])
        vals.subtotal16 =( vals.rhpko16 + vals.rhpkol16 + vals.rhpkst16 + vals.shortening16 + vals.rhpo16 + vals.rpst16 + 
                        vals.rhpst16 + vals.rhcno16 + vals.rcno16 + vals.rpko16 )
                            
        vals.rhpko17 = float(request.POST['rhpko17'])
        vals.rhpkol17 = float(request.POST['rhpkol17'])
        vals.rhpkst17 = float(request.POST['rhpkst17'])
        vals.shortening17 = float(request.POST['shortening17'])
        vals.rhpo17 = float(request.POST['rhpo17'])
        vals.rpst17 = float(request.POST['rpst17'])
        vals.rhpst17 = float(request.POST['rhpst17'])
        vals.rhcno17 = float(request.POST['rhcno17'])
        vals.rcno17 = float(request.POST['rcno17'])
        vals.rpko17 = float(request.POST['rpko17'])
        vals.subtotal17 =( vals.rhpko17 + vals.rhpkol17 + vals.rhpkst17 + vals.shortening17 + vals.rhpo17 + vals.rpst17 + 
                        vals.rhpst17 + vals.rhcno17 + vals.rcno17 + vals.rpko17 )                    

        vals.rhpko18 = float(request.POST['rhpko18'])
        vals.rhpkol18 = float(request.POST['rhpkol18'])
        vals.rhpkst18 = float(request.POST['rhpkst18'])
        vals.shortening18 = float(request.POST['shortening18'])
        vals.rhpo18 = float(request.POST['rhpo18'])
        vals.rpst18 = float(request.POST['rpst18'])
        vals.rhpst18 = float(request.POST['rhpst18'])
        vals.rhcno18 = float(request.POST['rhcno18'])
        vals.rcno18 = float(request.POST['rcno18'])
        vals.rpko18 = float(request.POST['rpko18'])
        vals.subtotal18 =( vals.rhpko18 + vals.rhpkol18 + vals.rhpkst18 + vals.shortening18 + vals.rhpo18 + vals.rpst18 + 
                        vals.rhpst18 + vals.rhcno18 + vals.rcno18 + vals.rpko18 )

        vals.rhpko19 = float(request.POST['rhpko19'])
        vals.rhpkol19 = float(request.POST['rhpkol19'])
        vals.rhpkst19 = float(request.POST['rhpkst19'])
        vals.shortening19 = float(request.POST['shortening19'])
        vals.rhpo19 = float(request.POST['rhpo19'])
        vals.rpst19 = float(request.POST['rpst19'])
        vals.rhpst19 = float(request.POST['rhpst19'])
        vals.rhcno19 = float(request.POST['rhcno19'])
        vals.rcno19 = float(request.POST['rcno19'])
        vals.rpko19 = float(request.POST['rpko19'])
        vals.subtotal19 =( vals.rhpko19 + vals.rhpkol19 + vals.rhpkst19 + vals.shortening19 + vals.rhpo19 + vals.rpst19 + 
                        vals.rhpst19 + vals.rhcno19 + vals.rcno19 + vals.rpko19 )

        vals.rhpko20 = float(request.POST['rhpko20'])
        vals.rhpkol20 = float(request.POST['rhpkol20'])
        vals.rhpkst20 = float(request.POST['rhpkst20'])
        vals.shortening20 = float(request.POST['shortening20'])
        vals.rhpo20 = float(request.POST['rhpo20'])
        vals.rpst20 = float(request.POST['rpst20'])
        vals.rhpst20 = float(request.POST['rhpst20'])
        vals.rhcno20 = float(request.POST['rhcno20'])
        vals.rcno20 = float(request.POST['rcno20'])
        vals.rpko20 = float(request.POST['rpko20'])
        vals.subtotal20 =( vals.rhpko20 + vals.rhpkol20 + vals.rhpkst20 + vals.shortening20 + vals.rhpo20 + vals.rpst20 + 
                        vals.rhpst20 + vals.rhcno20 + vals.rcno20 + vals.rpko20 )

        vals.rhpko21 = float(request.POST['rhpko21'])
        vals.rhpkol21 = float(request.POST['rhpkol21'])
        vals.rhpkst21 = float(request.POST['rhpkst21'])
        vals.shortening21 = float(request.POST['shortening21'])
        vals.rhpo21 = float(request.POST['rhpo21'])
        vals.rpst21 = float(request.POST['rpst21'])
        vals.rhpst21 = float(request.POST['rhpst21'])
        vals.rhcno21 = float(request.POST['rhcno21'])
        vals.rcno21 = float(request.POST['rcno21'])
        vals.rpko21 = float(request.POST['rpko21'])
        vals.subtotal21 =( vals.rhpko21 + vals.rhpkol21 + vals.rhpkst21 + vals.shortening21 + vals.rhpo21 + vals.rpst21 + 
                        vals.rhpst21 + vals.rhcno21 + vals.rcno21 + vals.rpko21 )

        vals.rhpko22 = float(request.POST['rhpko22'])
        vals.rhpkol22 = float(request.POST['rhpkol22'])
        vals.rhpkst22 = float(request.POST['rhpkst22'])
        vals.shortening22 = float(request.POST['shortening22'])
        vals.rhpo22 = float(request.POST['rhpo22'])
        vals.rpst22 = float(request.POST['rpst22'])
        vals.rhpst22 = float(request.POST['rhpst22'])
        vals.rhcno22 = float(request.POST['rhcno22'])
        vals.rcno22 = float(request.POST['rcno22'])
        vals.rpko22 = float(request.POST['rpko22'])
        vals.subtotal22 =( vals.rhpko22 + vals.rhpkol22 + vals.rhpkst22 + vals.shortening22 + vals.rhpo22 + vals.rpst22 + 
                        vals.rhpst22 + vals.rhcno22 + vals.rcno22 + vals.rpko22 )

        vals.rhpko23 = float(request.POST['rhpko23'])
        vals.rhpkol23 = float(request.POST['rhpkol23'])
        vals.rhpkst23 = float(request.POST['rhpkst23'])
        vals.shortening23 = float(request.POST['shortening23'])
        vals.rhpo23 = float(request.POST['rhpo23'])
        vals.rpst23 = float(request.POST['rpst23'])
        vals.rhpst23 = float(request.POST['rhpst23'])
        vals.rhcno23 = float(request.POST['rhcno23'])
        vals.rcno23 = float(request.POST['rcno23'])
        vals.rpko23 = float(request.POST['rpko23'])
        vals.subtotal23 =( vals.rhpko23 + vals.rhpkol23 + vals.rhpkst23 + vals.shortening23 + vals.rhpo23 + vals.rpst23 + 
                        vals.rhpst23 + vals.rhcno23 + vals.rcno23 + vals.rpko23 )

        vals.rhpko24 = float(request.POST['rhpko24'])
        vals.rhpkol24 = float(request.POST['rhpkol24'])
        vals.rhpkst24 = float(request.POST['rhpkst24'])
        vals.shortening24 = float(request.POST['shortening24'])
        vals.rhpo24 = float(request.POST['rhpo24'])
        vals.rpst24 = float(request.POST['rpst24'])
        vals.rhpst24 = float(request.POST['rhpst24'])
        vals.rhcno24 = float(request.POST['rhcno24'])
        vals.rcno24 = float(request.POST['rcno24'])
        vals.rpko24 = float(request.POST['rpko24'])
        vals.subtotal24 =( vals.rhpko24 + vals.rhpkol24 + vals.rhpkst24 + vals.shortening24 + vals.rhpo24 + vals.rpst24 + 
                        vals.rhpst24 + vals.rhcno24 + vals.rcno24 + vals.rpko24 )

        vals.apshortening15 = float(request.POST['apshortening15'])
        vals.rhpoc15 = float(request.POST['rhpoc15'])
        vals.rhsbo15 = float(request.POST['rhsbo15'])
        vals.subtotal_15 = vals.apshortening15 + vals.rhsbo15 + vals.rhpoc15
        vals.sf_total15 = vals.subtotal_15 + vals.subtotal15

        vals.apshortening16 = float(request.POST['apshortening16'])
        vals.rhpoc16 = float(request.POST['rhpoc16'])
        vals.rhsbo16 = float(request.POST['rhsbo16'])
        vals.subtotal_16 = vals.apshortening16 + vals.rhsbo16 + vals.rhpoc16
        vals.sf_total16 = vals.subtotal_16 + vals.subtotal16

        vals.apshortening17 = float(request.POST['apshortening17'])
        vals.rhpoc17 = float(request.POST['rhpoc17'])
        vals.rhsbo17 = float(request.POST['rhsbo17'])
        vals.subtotal_17 = vals.apshortening17 + vals.rhsbo17 + vals.rhpoc17
        vals.sf_total17 = vals.subtotal_17 + vals.subtotal17

        vals.apshortening18 = float(request.POST['apshortening18'])
        vals.rhpoc18 = float(request.POST['rhpoc18'])
        vals.rhsbo18 = float(request.POST['rhsbo18'])
        vals.subtotal_18 = vals.apshortening18 + vals.rhsbo18 + vals.rhpoc18
        vals.sf_total18 = vals.subtotal_18 + vals.subtotal18

        vals.apshortening19 = float(request.POST['apshortening19'])
        vals.rhpoc19 = float(request.POST['rhpoc19'])
        vals.rhsbo19 = float(request.POST['rhsbo19'])
        vals.subtotal_19 = vals.apshortening19 + vals.rhsbo19 + vals.rhpoc19
        vals.sf_total19 = vals.subtotal_19 + vals.subtotal19

        vals.apshortening20 = float(request.POST['apshortening20'])
        vals.rhpoc20 = float(request.POST['rhpoc20'])
        vals.rhsbo20 = float(request.POST['rhsbo20'])
        vals.subtotal_20 = vals.apshortening20 + vals.rhsbo20 + vals.rhpoc20
        vals.sf_total20 = vals.subtotal_20 + vals.subtotal20

        vals.apshortening21 = float(request.POST['apshortening21'])
        vals.rhpoc21 = float(request.POST['rhpoc21'])
        vals.rhsbo21 = float(request.POST['rhsbo21'])
        vals.subtotal_21 = vals.apshortening21 + vals.rhsbo21 + vals.rhpoc21
        vals.sf_total21 = vals.subtotal_21 + vals.subtotal21

        vals.apshortening22 = float(request.POST['apshortening22'])
        vals.rhpoc22 = float(request.POST['rhpoc22'])
        vals.rhsbo22 = float(request.POST['rhsbo22'])
        vals.subtotal_22 = vals.apshortening22 + vals.rhsbo22 + vals.rhpoc22
        vals.sf_total22 = vals.subtotal_22 + vals.subtotal22

        vals.apshortening23 = float(request.POST['apshortening23'])
        vals.rhpoc23 = float(request.POST['rhpoc23'])
        vals.rhsbo23 = float(request.POST['rhsbo23'])
        vals.subtotal_23 = vals.apshortening23 + vals.rhsbo23 + vals.rhpoc23
        vals.sf_total23 = vals.subtotal_23 + vals.subtotal23

        vals.apshortening24 = float(request.POST['apshortening24'])
        vals.rhpoc24 = float(request.POST['rhpoc24'])
        vals.rhsbo24 = float(request.POST['rhsbo24'])
        vals.subtotal_24 = vals.apshortening24 + vals.rhsbo24 + vals.rhpoc24
        vals.sf_total24 = vals.subtotal_24 + vals.subtotal24

        vals.g1sbo15 = float(request.POST['g1sbo15'])
        vals.blendedoil15 = float(request.POST['blendedoil15'])
        vals.rol15 = float(request.POST['rol15'])
        vals.spmf15 = float(request.POST['spmf15'])
        vals.mpbtotal15 = vals.g1sbo15 + vals.blendedoil15 + vals.rol15 + vals.spmf15

        vals.g1sbo16 = float(request.POST['g1sbo16'])
        vals.blendedoil16 = float(request.POST['blendedoil16'])
        vals.rol16 = float(request.POST['rol16'])
        vals.spmf16 = float(request.POST['spmf16'])
        vals.mpbtotal16 = vals.g1sbo16 + vals.blendedoil16 + vals.rol16 + vals.spmf16

        vals.g1sbo17 = float(request.POST['g1sbo17'])
        vals.blendedoil17 = float(request.POST['blendedoil17'])
        vals.rol17 = float(request.POST['rol17'])
        vals.spmf17 = float(request.POST['spmf17'])
        vals.mpbtotal17 = vals.g1sbo17 + vals.blendedoil17 + vals.rol17 + vals.spmf17

        vals.g1sbo18 = float(request.POST['g1sbo18'])
        vals.blendedoil18 = float(request.POST['blendedoil18'])
        vals.rol18 = float(request.POST['rol18'])
        vals.spmf18 = float(request.POST['spmf18'])
        vals.mpbtotal18 = vals.g1sbo18 + vals.blendedoil18 + vals.rol18 + vals.spmf18

        vals.g1sbo19 = float(request.POST['g1sbo19'])
        vals.blendedoil19 = float(request.POST['blendedoil19'])
        vals.rol19 = float(request.POST['rol19'])
        vals.spmf19 = float(request.POST['spmf19'])
        vals.mpbtotal19 = vals.g1sbo19 + vals.blendedoil19 + vals.rol19 + vals.spmf19

        vals.g1sbo20 = float(request.POST['g1sbo20'])
        vals.blendedoil20 = float(request.POST['blendedoil20'])
        vals.rol20 = float(request.POST['rol20'])
        vals.spmf20 = float(request.POST['spmf20'])
        vals.mpbtotal20 = vals.g1sbo20 + vals.blendedoil20 + vals.rol20 + vals.spmf20

        vals.g1sbo21 = float(request.POST['g1sbo21'])
        vals.blendedoil21 = float(request.POST['blendedoil21'])
        vals.rol21 = float(request.POST['rol21'])
        vals.spmf21 = float(request.POST['spmf21'])
        vals.mpbtotal21 = vals.g1sbo21 + vals.blendedoil21 + vals.rol21 + vals.spmf21

        vals.g1sbo22 = float(request.POST['g1sbo22'])
        vals.blendedoil22 = float(request.POST['blendedoil22'])
        vals.rol22 = float(request.POST['rol22'])
        vals.spmf22 = float(request.POST['spmf22'])
        vals.mpbtotal22 = vals.g1sbo22 + vals.blendedoil22 + vals.rol22 + vals.spmf22

        vals.g1sbo23 = float(request.POST['g1sbo23'])
        vals.blendedoil23 = float(request.POST['blendedoil23'])
        vals.rol23 = float(request.POST['rol23'])
        vals.spmf23 = float(request.POST['spmf23'])
        vals.mpbtotal23 = vals.g1sbo23 + vals.blendedoil23 + vals.rol23 + vals.spmf23

        vals.g1sbo24 = float(request.POST['g1sbo24'])
        vals.blendedoil24 = float(request.POST['blendedoil24'])
        vals.rol24 = float(request.POST['rol24'])
        vals.spmf24 = float(request.POST['spmf24'])
        vals.mpbtotal24 = vals.g1sbo24 + vals.blendedoil24 + vals.rol24 + vals.spmf24

        vals.g1sbo1_15 = float(request.POST['g1sbo1_15'])
        vals.g1sbo2_15 = float(request.POST['g1sbo2_15'])
        vals.g1sbo3_15 = float(request.POST['g1sbo3_15'])
        vals.g1sbo4_15 = float(request.POST['g1sbo4_15'])
        vals.blendedoil1_15 = float(request.POST['blendedoil1_15'])
        vals.blendedoil2_15 = float(request.POST['blendedoil2_15'])
        vals.blendedoil3_15 = float(request.POST['blendedoil3_15'])
        vals.blendedoil4_15 = float(request.POST['blendedoil4_15'])
        vals.superolein1_15 = float(request.POST['superolein1_15'])
        vals.superolein2_15 = float(request.POST['superolein2_15'])
        vals.superolein3_15 = float(request.POST['superolein3_15'])
        vals.superolein4_15 = float(request.POST['superolein4_15'])
        vals.mpptotal15 = (vals.g1sbo1_15 + vals.g1sbo2_15 + vals.g1sbo3_15 + vals.g1sbo4_15 +
                                vals.blendedoil1_15 + vals.blendedoil2_15 + vals.blendedoil3_15 + vals.blendedoil4_15 +  
                                    vals.superolein1_15 + vals.superolein2_15 + vals.superolein3_15 + vals.superolein4_15)

        vals.g1sbo1_16 = float(request.POST['g1sbo1_16'])
        vals.g1sbo2_16 = float(request.POST['g1sbo2_16'])
        vals.g1sbo3_16 = float(request.POST['g1sbo3_16'])
        vals.g1sbo4_16 = float(request.POST['g1sbo4_16'])
        vals.blendedoil1_16 = float(request.POST['blendedoil1_16'])
        vals.blendedoil2_16 = float(request.POST['blendedoil2_16'])
        vals.blendedoil3_16 = float(request.POST['blendedoil3_16'])
        vals.blendedoil4_16 = float(request.POST['blendedoil4_16'])
        vals.superolein1_16 = float(request.POST['superolein1_16'])
        vals.superolein2_16 = float(request.POST['superolein2_16'])
        vals.superolein3_16 = float(request.POST['superolein3_16'])
        vals.superolein4_16 = float(request.POST['superolein4_16'])
        vals.mpptotal16 =( vals.g1sbo1_16 + vals.g1sbo2_16 + vals.g1sbo3_16 + vals.g1sbo4_16 +
                                vals.blendedoil1_16 + vals.blendedoil2_16 + vals.blendedoil3_16 + vals.blendedoil4_16 +  
                                    vals.superolein1_16 + vals.superolein2_16 + vals.superolein3_16 + vals.superolein4_16 )

        vals.g1sbo1_17 = float(request.POST['g1sbo1_17'])
        vals.g1sbo2_17 = float(request.POST['g1sbo2_17'])
        vals.g1sbo3_17 = float(request.POST['g1sbo3_17'])
        vals.g1sbo4_17 = float(request.POST['g1sbo4_17'])
        vals.blendedoil1_17 = float(request.POST['blendedoil1_17'])
        vals.blendedoil2_17 = float(request.POST['blendedoil2_17'])
        vals.blendedoil3_17 = float(request.POST['blendedoil3_17'])
        vals.blendedoil4_17 = float(request.POST['blendedoil4_17'])
        vals.superolein1_17 = float(request.POST['superolein1_17'])
        vals.superolein2_17 = float(request.POST['superolein2_17'])
        vals.superolein3_17 = float(request.POST['superolein3_17'])
        vals.superolein4_17 = float(request.POST['superolein4_17'])
        vals.mpptotal17 = (vals.g1sbo1_17 + vals.g1sbo2_17 + vals.g1sbo3_17 + vals.g1sbo4_17 +
                                vals.blendedoil1_17 + vals.blendedoil2_17 + vals.blendedoil3_17 + vals.blendedoil4_17 +  
                                    vals.superolein1_17 + vals.superolein2_17 + vals.superolein3_17 + vals.superolein4_17)

        vals.g1sbo1_18 = float(request.POST['g1sbo1_18'])
        vals.g1sbo2_18 = float(request.POST['g1sbo2_18'])
        vals.g1sbo3_18 = float(request.POST['g1sbo3_18'])
        vals.g1sbo4_18 = float(request.POST['g1sbo4_18'])
        vals.blendedoil1_18 = float(request.POST['blendedoil1_18'])
        vals.blendedoil2_18 = float(request.POST['blendedoil2_18'])
        vals.blendedoil3_18 = float(request.POST['blendedoil3_18'])
        vals.blendedoil4_18 = float(request.POST['blendedoil4_18'])
        vals.superolein1_18 = float(request.POST['superolein1_18'])
        vals.superolein2_18 = float(request.POST['superolein2_18'])
        vals.superolein3_18 = float(request.POST['superolein3_18'])
        vals.superolein4_18 = float(request.POST['superolein4_18'])
        vals.mpptotal18 =( vals.g1sbo1_18 + vals.g1sbo2_18 + vals.g1sbo3_18 + vals.g1sbo4_18 +
                                vals.blendedoil1_18 + vals.blendedoil2_18 + vals.blendedoil3_18 + vals.blendedoil4_18 +  
                                    vals.superolein1_18 + vals.superolein2_18 + vals.superolein3_18 + vals.superolein4_18)

        vals.g1sbo1_19 = float(request.POST['g1sbo1_19'])
        vals.g1sbo2_19 = float(request.POST['g1sbo2_19'])
        vals.g1sbo3_19 = float(request.POST['g1sbo3_19'])
        vals.g1sbo4_19 = float(request.POST['g1sbo4_19'])
        vals.blendedoil1_19 = float(request.POST['blendedoil1_19'])
        vals.blendedoil2_19 = float(request.POST['blendedoil2_19'])
        vals.blendedoil3_19 = float(request.POST['blendedoil3_19'])
        vals.blendedoil4_19 = float(request.POST['blendedoil4_19'])
        vals.superolein1_19 = float(request.POST['superolein1_19'])
        vals.superolein2_19 = float(request.POST['superolein2_19'])
        vals.superolein3_19 = float(request.POST['superolein3_19'])
        vals.superolein4_19 = float(request.POST['superolein4_19'])
        vals.mpptotal19 = (vals.g1sbo1_19 + vals.g1sbo2_19 + vals.g1sbo3_19 + vals.g1sbo4_19 +
                                vals.blendedoil1_19 + vals.blendedoil2_19 + vals.blendedoil3_19 + vals.blendedoil4_19 +  
                                    vals.superolein1_19 + vals.superolein2_19 + vals.superolein3_19 + vals.superolein4_19)

        vals.g1sbo1_20 = float(request.POST['g1sbo1_20'])
        vals.g1sbo2_20 = float(request.POST['g1sbo2_20'])
        vals.g1sbo3_20 = float(request.POST['g1sbo3_20'])
        vals.g1sbo4_20 = float(request.POST['g1sbo4_20'])
        vals.blendedoil1_20 = float(request.POST['blendedoil1_20'])
        vals.blendedoil2_20 = float(request.POST['blendedoil2_20'])
        vals.blendedoil3_20 = float(request.POST['blendedoil3_20'])
        vals.blendedoil4_20 = float(request.POST['blendedoil4_20'])
        vals.superolein1_20 = float(request.POST['superolein1_20'])
        vals.superolein2_20 = float(request.POST['superolein2_20'])
        vals.superolein3_20 = float(request.POST['superolein3_20'])
        vals.superolein4_20 = float(request.POST['superolein4_20'])
        vals.mpptotal20 = (vals.g1sbo1_20 + vals.g1sbo2_20 + vals.g1sbo3_20 + vals.g1sbo4_20 +
                                vals.blendedoil1_20 + vals.blendedoil2_20 + vals.blendedoil3_20 + vals.blendedoil4_20 +  
                                    vals.superolein1_20 + vals.superolein2_20 + vals.superolein3_20 + vals.superolein4_20)

        vals.g1sbo1_21 = float(request.POST['g1sbo1_21'])
        vals.g1sbo2_21 = float(request.POST['g1sbo2_21'])
        vals.g1sbo3_21 = float(request.POST['g1sbo3_21'])
        vals.g1sbo4_21 = float(request.POST['g1sbo4_21'])
        vals.blendedoil1_21 = float(request.POST['blendedoil1_21'])
        vals.blendedoil2_21 = float(request.POST['blendedoil2_21'])
        vals.blendedoil3_21 = float(request.POST['blendedoil3_21'])
        vals.blendedoil4_21 = float(request.POST['blendedoil4_21'])
        vals.superolein1_21 = float(request.POST['superolein1_21'])
        vals.superolein2_21 = float(request.POST['superolein2_21'])
        vals.superolein3_21 = float(request.POST['superolein3_21'])
        vals.superolein4_21 = float(request.POST['superolein4_21'])
        vals.mpptotal21 = (vals.g1sbo1_21 + vals.g1sbo2_21 + vals.g1sbo3_21 + vals.g1sbo4_21 +
                                vals.blendedoil1_21 + vals.blendedoil2_21 + vals.blendedoil3_21 + vals.blendedoil4_21 +  
                                    vals.superolein1_21 + vals.superolein2_21 + vals.superolein3_21 + vals.superolein4_21)

        vals.g1sbo1_22 = float(request.POST['g1sbo1_22'])
        vals.g1sbo2_22 = float(request.POST['g1sbo2_22'])
        vals.g1sbo3_22 = float(request.POST['g1sbo3_22'])
        vals.g1sbo4_22 = float(request.POST['g1sbo4_22'])
        vals.blendedoil1_22 = float(request.POST['blendedoil1_22'])
        vals.blendedoil2_22 = float(request.POST['blendedoil2_22'])
        vals.blendedoil3_22 = float(request.POST['blendedoil3_22'])
        vals.blendedoil4_22 = float(request.POST['blendedoil4_22'])
        vals.superolein1_22 = float(request.POST['superolein1_22'])
        vals.superolein2_22 = float(request.POST['superolein2_22'])
        vals.superolein3_22 = float(request.POST['superolein3_22'])
        vals.superolein4_22 = float(request.POST['superolein4_22'])
        vals.mpptotal22 = (vals.g1sbo1_22 + vals.g1sbo2_22 + vals.g1sbo3_22 + vals.g1sbo4_22 +
                                vals.blendedoil1_22 + vals.blendedoil2_22 + vals.blendedoil3_22 + vals.blendedoil4_22 +  
                                    vals.superolein1_22 + vals.superolein2_22 + vals.superolein3_22 + vals.superolein4_22)

        vals.g1sbo1_23 = float(request.POST['g1sbo1_23'])
        vals.g1sbo2_23 = float(request.POST['g1sbo2_23'])
        vals.g1sbo3_23 = float(request.POST['g1sbo3_23'])
        vals.g1sbo4_23 = float(request.POST['g1sbo4_23'])
        vals.blendedoil1_23 = float(request.POST['blendedoil1_23'])
        vals.blendedoil2_23 = float(request.POST['blendedoil2_23'])
        vals.blendedoil3_23 = float(request.POST['blendedoil3_23'])
        vals.blendedoil4_23 = float(request.POST['blendedoil4_23'])
        vals.superolein1_23 = float(request.POST['superolein1_23'])
        vals.superolein2_23 = float(request.POST['superolein2_23'])
        vals.superolein3_23 = float(request.POST['superolein3_23'])
        vals.superolein4_23 = float(request.POST['superolein4_23'])
        vals.mpptotal23 = (vals.g1sbo1_23 + vals.g1sbo2_23 + vals.g1sbo3_23 + vals.g1sbo4_23 +
                                vals.blendedoil1_23 + vals.blendedoil2_23 + vals.blendedoil3_23 + vals.blendedoil4_23 +  
                                    vals.superolein1_23 + vals.superolein2_23 + vals.superolein3_23 + vals.superolein4_23)

        vals.g1sbo1_24 = float(request.POST['g1sbo1_24'])
        vals.g1sbo2_24 = float(request.POST['g1sbo2_24'])
        vals.g1sbo3_24 = float(request.POST['g1sbo3_24'])
        vals.g1sbo4_24 = float(request.POST['g1sbo4_24'])
        vals.blendedoil1_24 = float(request.POST['blendedoil1_24'])
        vals.blendedoil2_24 = float(request.POST['blendedoil2_24'])
        vals.blendedoil3_24 = float(request.POST['blendedoil3_24'])
        vals.blendedoil4_24 = float(request.POST['blendedoil4_24'])
        vals.superolein1_24 = float(request.POST['superolein1_24'])
        vals.superolein2_24 = float(request.POST['superolein2_24'])
        vals.superolein3_24 = float(request.POST['superolein3_24'])
        vals.superolein4_24 = float(request.POST['superolein4_24'])
        vals.mpptotal24 = (vals.g1sbo1_24 + vals.g1sbo2_24 + vals.g1sbo3_24 + vals.g1sbo4_24 +
                                vals.blendedoil1_24 + vals.blendedoil2_24 + vals.blendedoil3_24 + vals.blendedoil4_24 +  
                                    vals.superolein1_24 + vals.superolein2_24 + vals.superolein3_24 + vals.superolein4_24)


        vals.ls15 = float(request.POST['ls15'])
        vals.nis15 = float(request.POST['nis15'])
        vals.nim15 = float(request.POST['nim15'])
        vals.is15 = float(request.POST['is15'])
        vals.im15 = float(request.POST['im15'])
        vals.asm15 = float(request.POST['asm15'])
        vals.bot15 = vals.ls15 + vals.nis15 + vals.nim15 + vals.is15 + vals.im15 + vals.asm15

        vals.ls16 = float(request.POST['ls16'])
        vals.nis16 = float(request.POST['nis16'])
        vals.nim16 = float(request.POST['nim16'])
        vals.is16 = float(request.POST['is16'])
        vals.im16 = float(request.POST['im16'])
        vals.asm16 = float(request.POST['asm16'])
        vals.bot16 = vals.ls16 + vals.nis16 + vals.nim16 + vals.is16 + vals.im16 + vals.asm16

        vals.ls17 = float(request.POST['ls17'])
        vals.nis17 = float(request.POST['nis17'])
        vals.nim17 = float(request.POST['nim17'])
        vals.is17 = float(request.POST['is17'])
        vals.im17 = float(request.POST['im17'])
        vals.asm17 = float(request.POST['asm17'])
        vals.bot17 = vals.ls17 + vals.nis17 + vals.nim17 + vals.is17 + vals.im17 + vals.asm17

        vals.ls18 = float(request.POST['ls18'])
        vals.nis18 = float(request.POST['nis18'])
        vals.nim18 = float(request.POST['nim18'])
        vals.is18 = float(request.POST['is18'])
        vals.im18 = float(request.POST['im18'])
        vals.asm18 = float(request.POST['asm18'])
        vals.bot18 = vals.ls18 + vals.nis18 + vals.nim18 + vals.is18 + vals.im18 + vals.asm18

        vals.ls19 = float(request.POST['ls19'])
        vals.nis19 = float(request.POST['nis19'])
        vals.nim19 = float(request.POST['nim19'])
        vals.is19 = float(request.POST['is19'])
        vals.im19 = float(request.POST['im19'])
        vals.asm19 = float(request.POST['asm19'])
        vals.bot19 = vals.ls19 + vals.nis19 + vals.nim19 + vals.is19 + vals.im19 + vals.asm19

        vals.ls20 = float(request.POST['ls20'])
        vals.nis20 = float(request.POST['nis20'])
        vals.nim20 = float(request.POST['nim20'])
        vals.is20 = float(request.POST['is20'])
        vals.im20 = float(request.POST['im20'])
        vals.asm20 = float(request.POST['asm20'])
        vals.bot20 = vals.ls20 + vals.nis20 + vals.nim20 + vals.is20 + vals.im20 + vals.asm20

        vals.ls21 = float(request.POST['ls21'])
        vals.nis21 = float(request.POST['nis21'])
        vals.nim21 = float(request.POST['nim21'])
        vals.is21 = float(request.POST['is21'])
        vals.im21 = float(request.POST['im21'])
        vals.asm21 = float(request.POST['asm21'])
        vals.bot21 = vals.ls21 + vals.nis21 + vals.nim21 + vals.is21 + vals.im21 + vals.asm21

        vals.ls22 = float(request.POST['ls22'])
        vals.nis22 = float(request.POST['nis22'])
        vals.nim22 = float(request.POST['nim22'])
        vals.is22 = float(request.POST['is22'])
        vals.im22 = float(request.POST['im22'])
        vals.asm22 = float(request.POST['asm22'])
        vals.bot22 = vals.ls22 + vals.nis22 + vals.nim22 + vals.is22 + vals.im22 + vals.asm22

        vals.ls23 = float(request.POST['ls23'])
        vals.nis23 = float(request.POST['nis23'])
        vals.nim23 = float(request.POST['nim23'])
        vals.is23 = float(request.POST['is23'])
        vals.im23 = float(request.POST['im23'])
        vals.asm23 = float(request.POST['asm23'])
        vals.bot23 = vals.ls23 + vals.nis23 + vals.nim23 + vals.is23 + vals.im23 + vals.asm23

        vals.ls24 = float(request.POST['ls24'])
        vals.nis24 = float(request.POST['nis24'])
        vals.nim24 = float(request.POST['nim24'])
        vals.is24 = float(request.POST['is24'])
        vals.im24 = float(request.POST['im24'])
        vals.asm24 = float(request.POST['asm24'])
        vals.bot24 = vals.ls24 + vals.nis24 + vals.nim24 + vals.is24 + vals.im24 + vals.asm24

        vals.tvp15 = vals.bot15 + vals.mpptotal15 + vals.mpbtotal15 + vals.sf_total15 + vals.macd_system_total15
        vals.bulk15 = (vals.chicken_par_fry15 + vals.rhpko15 + vals.rhpkol15 + vals.rhpkst15 + vals.shortening15 +
                        vals.rhpo15 + vals.rpst15 + vals.rhpst15 + vals.rhcno15 + vals.rcno15)
        vals.packaged15 = (vals.stote_oil_blend15 + vals.subtotal_15 + vals.ls15 + vals.nim15 + 
                            vals.nis15 + vals.is15 + vals.im15 + vals.asm15)

        vals.tvp16 = vals.bot16 + vals.mpptotal16 + vals.mpbtotal16 + vals.sf_total16 + vals.macd_system_total16
        vals.bulk16 = (vals.chicken_par_fry16 + vals.rhpko16 + vals.rhpkol16 + vals.rhpkst16 + vals.shortening16 +
                        vals.rhpo16 + vals.rpst16 + vals.rhpst16 + vals.rhcno16 + vals.rcno16)
        vals.packaged16 = (vals.stote_oil_blend16 + vals.subtotal_16 + vals.ls16 + vals.nim16 + 
                            vals.nis16 + vals.is16 + vals.im16 + vals.asm16)

        vals.tvp17 = vals.bot17 + vals.mpptotal17 + vals.mpbtotal17 + vals.sf_total17 + vals.macd_system_total17
        vals.bulk17 = (vals.chicken_par_fry17 + vals.rhpko17 + vals.rhpkol17 + vals.rhpkst17 + vals.shortening17 +
                        vals.rhpo17 + vals.rpst17 + vals.rhpst17 + vals.rhcno17 + vals.rcno17)
        vals.packaged17 = (vals.stote_oil_blend17 + vals.subtotal_17 + vals.ls17 + vals.nim17 + 
                            vals.nis17 + vals.is17 + vals.im17 + vals.asm17)

        vals.tvp18 = vals.bot18 + vals.mpptotal18 + vals.mpbtotal18 + vals.sf_total18 + vals.macd_system_total18
        vals.bulk18 = (vals.chicken_par_fry18 + vals.rhpko18 + vals.rhpkol18 + vals.rhpkst18 + vals.shortening18 +
                        vals.rhpo18 + vals.rpst18 + vals.rhpst18 + vals.rhcno18 + vals.rcno18)
        vals.packaged18 = (vals.stote_oil_blend18 + vals.subtotal_18 + vals.ls18 + vals.nim18 + 
                            vals.nis18 + vals.is18 + vals.im18 + vals.asm18)

        vals.tvp19 = vals.bot19 + vals.mpptotal19 + vals.mpbtotal19 + vals.sf_total19 + vals.macd_system_total19
        vals.bulk19 = (vals.chicken_par_fry19 + vals.rhpko19 + vals.rhpkol19 + vals.rhpkst19 + vals.shortening19 +
                        vals.rhpo19 + vals.rpst19 + vals.rhpst19 + vals.rhcno19 + vals.rcno19)
        vals.packaged19 = (vals.stote_oil_blend19 + vals.subtotal_19 + vals.ls19 + vals.nim19 + 
                            vals.nis19 + vals.is19 + vals.im19 + vals.asm19)

        vals.tvp20 = vals.bot20 + vals.mpptotal20 + vals.mpbtotal20 + vals.sf_total20 + vals.macd_system_total20
        vals.bulk20 = (vals.chicken_par_fry20 + vals.rhpko20 + vals.rhpkol20 + vals.rhpkst20 + vals.shortening20 +
                        vals.rhpo20 + vals.rpst20 + vals.rhpst20 + vals.rhcno20 + vals.rcno20)
        vals.packaged20 = (vals.stote_oil_blend20 + vals.subtotal_20 + vals.ls20 + vals.nim20 + 
                            vals.nis20 + vals.is20 + vals.im20 + vals.asm20)

        vals.tvp21 = vals.bot21 + vals.mpptotal21 + vals.mpbtotal21 + vals.sf_total21 + vals.macd_system_total21
        vals.bulk21 = (vals.chicken_par_fry21 + vals.rhpko21 + vals.rhpkol21 + vals.rhpkst21 + vals.shortening21 +
                        vals.rhpo21 + vals.rpst21 + vals.rhpst21 + vals.rhcno21 + vals.rcno21)
        vals.packaged21 = (vals.stote_oil_blend21 + vals.subtotal_21 + vals.ls21 + vals.nim21 + 
                            vals.nis21 + vals.is21 + vals.im21 + vals.asm21)

        vals.tvp22 = vals.bot22 + vals.mpptotal22 + vals.mpbtotal22 + vals.sf_total22 + vals.macd_system_total22
        vals.bulk22 = (vals.chicken_par_fry22 + vals.rhpko22 + vals.rhpkol22 + vals.rhpkst22 + vals.shortening22 +
                        vals.rhpo22 + vals.rpst22 + vals.rhpst22 + vals.rhcno22 + vals.rcno22)
        vals.packaged22 = (vals.stote_oil_blend22 + vals.subtotal_22 + vals.ls22 + vals.nim22 + 
                            vals.nis22 + vals.is22 + vals.im22 + vals.asm22)

        vals.tvp23 = vals.bot23 + vals.mpptotal23 + vals.mpbtotal23 + vals.sf_total23 + vals.macd_system_total23
        vals.bulk23 = (vals.chicken_par_fry23 + vals.rhpko23 + vals.rhpkol23 + vals.rhpkst23 + vals.shortening23 +
                        vals.rhpo23 + vals.rpst23 + vals.rhpst23 + vals.rhcno23 + vals.rcno23)
        vals.packaged23 = (vals.stote_oil_blend23 + vals.subtotal_23 + vals.ls23 + vals.nim23 + 
                            vals.nis23 + vals.is23 + vals.im23 + vals.asm23)

        vals.tvp24 = vals.bot24 + vals.mpptotal24 + vals.mpbtotal24 + vals.sf_total24 + vals.macd_system_total24
        vals.bulk24 = (vals.chicken_par_fry24 + vals.rhpko24 + vals.rhpkol24 + vals.rhpkst24 + vals.shortening24 +
                        vals.rhpo24 + vals.rpst24 + vals.rhpst24 + vals.rhcno24 + vals.rcno24)
        vals.packaged24 = (vals.stote_oil_blend24 + vals.subtotal_24 + vals.ls24 + vals.nim24 + 
                            vals.nis24 + vals.is24 + vals.im24 + vals.asm24)
        
        vals.sob_n15 = (vals.stote_oil_blend15*60/100 + vals.stote_oil_blend15*20/100)/150
        vals.sob_d15 = (vals.stote_oil_blend15*20/100)/150
        vals.sob_fr15 = (vals.stote_oil_blend15*60/100 + vals.stote_oil_blend15*20/100 + vals.stote_oil_blend15*3.5/100)/400
        vals.sob_h15 = (vals.stote_oil_blend15*3.5/100)/50
        vals.sob_perf15 = (vals.stote_oil_blend15/8.6/24/80*100)
        vals.cpf_n15 = (vals.chicken_par_fry15/150)
        vals.cpf_d15 = (vals.chicken_par_fry15*45/100)/150
        vals.cpf_fr15 = (vals.chicken_par_fry15)/400
        vals.cpf_lv15 = (vals.chicken_par_fry15/30)/52

        vals.sob_n16 = (vals.stote_oil_blend16*60/100 + vals.stote_oil_blend16*20/100)/150
        vals.sob_d16 = (vals.stote_oil_blend16*20/100)/150
        vals.sob_fr16 = (vals.stote_oil_blend16*60/100 + vals.stote_oil_blend16*20/100 + vals.stote_oil_blend16*3.5/100)/400
        vals.sob_h16 = (vals.stote_oil_blend16*3.5/100)/50
        vals.sob_perf16 = (vals.stote_oil_blend16/8.6/24/80*100)
        vals.cpf_n16 = (vals.chicken_par_fry16/150)
        vals.cpf_d16 = (vals.chicken_par_fry16*45/100)/150
        vals.cpf_fr16 = (vals.chicken_par_fry16)/400
        vals.cpf_lv16 = (vals.chicken_par_fry16/30)/52

        vals.sob_n17 = (vals.stote_oil_blend17*60/100 + vals.stote_oil_blend17*20/100)/150
        vals.sob_d17 = (vals.stote_oil_blend17*20/100)/150
        vals.sob_fr17 = (vals.stote_oil_blend17*60/100 + vals.stote_oil_blend17*20/100 + vals.stote_oil_blend17*3.5/100)/400
        vals.sob_h17 = (vals.stote_oil_blend17*3.5/100)/50
        vals.sob_perf17 = (vals.stote_oil_blend17/8.6/24/80*100)
        vals.cpf_n17 = (vals.chicken_par_fry17/150)
        vals.cpf_d17 = (vals.chicken_par_fry17*45/100)/150
        vals.cpf_fr17 = (vals.chicken_par_fry17)/400
        vals.cpf_lv17 = (vals.chicken_par_fry17/30)/52

        vals.sob_n18 = (vals.stote_oil_blend18*60/100 + vals.stote_oil_blend18*20/100)/150
        vals.sob_d18 = (vals.stote_oil_blend18*20/100)/150
        vals.sob_fr18 = (vals.stote_oil_blend18*60/100 + vals.stote_oil_blend18*20/100 + vals.stote_oil_blend18*3.5/100)/400
        vals.sob_h18 = (vals.stote_oil_blend18*3.5/100)/50
        vals.sob_perf18 = (vals.stote_oil_blend18/8.6/24/80*100)
        vals.cpf_n18 = (vals.chicken_par_fry18/150)
        vals.cpf_d18 = (vals.chicken_par_fry18*45/100)/150
        vals.cpf_fr18 = (vals.chicken_par_fry18)/400
        vals.cpf_lv18 = (vals.chicken_par_fry18/30)/52

        vals.sob_n19 = (vals.stote_oil_blend19*60/100 + vals.stote_oil_blend19*20/100)/150
        vals.sob_d19 = (vals.stote_oil_blend19*20/100)/150
        vals.sob_fr19 = (vals.stote_oil_blend19*60/100 + vals.stote_oil_blend19*20/100 + vals.stote_oil_blend19*3.5/100)/400
        vals.sob_h19 = (vals.stote_oil_blend19*3.5/100)/50
        vals.sob_perf19 = (vals.stote_oil_blend19/8.6/24/80*100)
        vals.cpf_n19 = (vals.chicken_par_fry19/150)
        vals.cpf_d19 = (vals.chicken_par_fry19*45/100)/150
        vals.cpf_fr19 = (vals.chicken_par_fry19)/400
        vals.cpf_lv19 = (vals.chicken_par_fry19/30)/52

        vals.sob_n20 = (vals.stote_oil_blend20*60/100 + vals.stote_oil_blend20*20/100)/150
        vals.sob_d20 = (vals.stote_oil_blend20*20/100)/150
        vals.sob_fr20 = (vals.stote_oil_blend20*60/100 + vals.stote_oil_blend20*20/100 + vals.stote_oil_blend20*3.5/100)/400
        vals.sob_h20 = (vals.stote_oil_blend20*3.5/100)/50
        vals.sob_perf20 = (vals.stote_oil_blend20/8.6/24/80*100)
        vals.cpf_n20 = (vals.chicken_par_fry20/150)
        vals.cpf_d20 = (vals.chicken_par_fry20*45/100)/150
        vals.cpf_fr20 = (vals.chicken_par_fry20)/400
        vals.cpf_lv20 = (vals.chicken_par_fry20/30)/52

        vals.sob_n21 = (vals.stote_oil_blend21*60/100 + vals.stote_oil_blend21*20/100)/150
        vals.sob_d21 = (vals.stote_oil_blend21*20/100)/150
        vals.sob_fr21 = (vals.stote_oil_blend21*60/100 + vals.stote_oil_blend21*20/100 + vals.stote_oil_blend21*3.5/100)/400
        vals.sob_h21 = (vals.stote_oil_blend21*3.5/100)/50
        vals.sob_perf21 = (vals.stote_oil_blend21/8.6/24/80*100)
        vals.cpf_n21 = (vals.chicken_par_fry21/150)
        vals.cpf_d21 = (vals.chicken_par_fry21*45/100)/150
        vals.cpf_fr21 = (vals.chicken_par_fry21)/400
        vals.cpf_lv21 = (vals.chicken_par_fry21/30)/52

        vals.sob_n22 = (vals.stote_oil_blend22*60/100 + vals.stote_oil_blend22*20/100)/150
        vals.sob_d22 = (vals.stote_oil_blend22*20/100)/150
        vals.sob_fr22 = (vals.stote_oil_blend22*60/100 + vals.stote_oil_blend22*20/100 + vals.stote_oil_blend22*3.5/100)/400
        vals.sob_h22 = (vals.stote_oil_blend22*3.5/100)/50
        vals.sob_perf22 = (vals.stote_oil_blend22/8.6/24/80*100)
        vals.cpf_n22 = (vals.chicken_par_fry22/150)
        vals.cpf_d22 = (vals.chicken_par_fry22*45/100)/150
        vals.cpf_fr22 = (vals.chicken_par_fry22)/400
        vals.cpf_lv22 = (vals.chicken_par_fry22/30)/52

        vals.sob_n23 = (vals.stote_oil_blend23*60/100 + vals.stote_oil_blend23*20/100)/150
        vals.sob_d23 = (vals.stote_oil_blend23*20/100)/150
        vals.sob_fr23 = (vals.stote_oil_blend23*60/100 + vals.stote_oil_blend23*20/100 + vals.stote_oil_blend23*3.5/100)/400
        vals.sob_h23 = (vals.stote_oil_blend23*3.5/100)/50
        vals.sob_perf23 = (vals.stote_oil_blend23/8.6/24/80*100)
        vals.cpf_n23 = (vals.chicken_par_fry23/150)
        vals.cpf_d23 = (vals.chicken_par_fry23*45/100)/150
        vals.cpf_fr23 = (vals.chicken_par_fry23)/400
        vals.cpf_lv23 = (vals.chicken_par_fry23/30)/52

        vals.sob_n24 = (vals.stote_oil_blend24*60/100 + vals.stote_oil_blend24*20/100)/150
        vals.sob_d24 = (vals.stote_oil_blend24*20/100)/150
        vals.sob_fr24 = (vals.stote_oil_blend24*60/100 + vals.stote_oil_blend24*20/100 + vals.stote_oil_blend24*3.5/100)/400
        vals.sob_h24 = (vals.stote_oil_blend24*3.5/100)/50
        vals.sob_perf24 = (vals.stote_oil_blend24/8.6/24/80*100)
        vals.cpf_n24 = (vals.chicken_par_fry24/150)
        vals.cpf_d24 = (vals.chicken_par_fry24*45/100)/150
        vals.cpf_fr24 = (vals.chicken_par_fry24)/400
        vals.cpf_lv24 = (vals.chicken_par_fry24/30)/52

        vals.cbibv15 = float(request.POST['cbibv15'])
        vals.cpetv15 = float(request.POST['cpetv15'])
        vals.cbibv_gsbo15 = vals.cbibv15 * 20/100
        vals.cbibv_blendedoil15 = vals.cbibv15 * 45/100
        vals.cbibv_rol15 = vals.cbibv15 * 15/100
        vals.cbibv_spmf15 = vals.cbibv15 * 20/100
        vals.cpetv_gsbo1_15 = vals.cpetv15 * 2/100
        vals.cpetv_gsbo2_15 = vals.cpetv15 * 12/100
        vals.cpetv_gsbo3_15 = vals.cpetv15 * 3/100
        vals.cpetv_gsbo4_15 = vals.cpetv15 * 15/100
        vals.cpetv_blendedoil1_15 = vals.cpetv15 * 3.3/100
        vals.cpetv_blendedoil2_15 = vals.cpetv15 * 40.3/100
        vals.cpetv_blendedoil3_15 = vals.cpetv15 * 4.5/100
        vals.cpetv_blendedoil4_15 = vals.cpetv15 * 1.8/100
        vals.cpetv_superolein1_15 = vals.cpetv15 * 1.3/100
        vals.cpetv_superolein2_15 = vals.cpetv15 * 13.4/100
        vals.cpetv_superolein3_15 = vals.cpetv15 * 1.5/100
        vals.cpetv_superolein4_15 = vals.cpetv15 * 1.9/100

        vals.cbibv16 = float(request.POST['cbibv16'])
        vals.cpetv16 = float(request.POST['cpetv16'])
        vals.cbibv_gsbo16 = vals.cbibv16 * 20/100
        vals.cbibv_blendedoil16 = vals.cbibv16 * 45/100
        vals.cbibv_rol16 = vals.cbibv16 * 15/100
        vals.cbibv_spmf16 = vals.cbibv16 * 20/100
        vals.cpetv_gsbo1_16 = vals.cpetv16 * 2/100
        vals.cpetv_gsbo2_16 = vals.cpetv16 * 12/100
        vals.cpetv_gsbo3_16 = vals.cpetv16 * 3/100
        vals.cpetv_gsbo4_16 = vals.cpetv16 * 15/100
        vals.cpetv_blendedoil1_16 = vals.cpetv16 * 3.3/100
        vals.cpetv_blendedoil2_16 = vals.cpetv16 * 40.3/100
        vals.cpetv_blendedoil3_16 = vals.cpetv16 * 4.5/100
        vals.cpetv_blendedoil4_16 = vals.cpetv16 * 1.8/100
        vals.cpetv_superolein1_16 = vals.cpetv16 * 1.3/100
        vals.cpetv_superolein2_16 = vals.cpetv16 * 13.4/100
        vals.cpetv_superolein3_16 = vals.cpetv16 * 1.5/100
        vals.cpetv_superolein4_16 = vals.cpetv16 * 1.9/100

        vals.cbibv17 = float(request.POST['cbibv17'])
        vals.cpetv17 = float(request.POST['cpetv17'])
        vals.cbibv_gsbo17 = vals.cbibv17 * 20/100
        vals.cbibv_blendedoil17 = vals.cbibv17 * 45/100
        vals.cbibv_rol17 = vals.cbibv17 * 15/100
        vals.cbibv_spmf17 = vals.cbibv17 * 20/100
        vals.cpetv_gsbo1_17 = vals.cpetv17 * 2/100
        vals.cpetv_gsbo2_17 = vals.cpetv17 * 12/100
        vals.cpetv_gsbo3_17 = vals.cpetv17 * 3/100
        vals.cpetv_gsbo4_17 = vals.cpetv17 * 15/100
        vals.cpetv_blendedoil1_17 = vals.cpetv17 * 3.3/100
        vals.cpetv_blendedoil2_17 = vals.cpetv17 * 40.3/100
        vals.cpetv_blendedoil3_17 = vals.cpetv17 * 4.5/100
        vals.cpetv_blendedoil4_17 = vals.cpetv17 * 1.8/100
        vals.cpetv_superolein1_17 = vals.cpetv17 * 1.3/100
        vals.cpetv_superolein2_17 = vals.cpetv17 * 13.4/100
        vals.cpetv_superolein3_17 = vals.cpetv17 * 1.5/100
        vals.cpetv_superolein4_17 = vals.cpetv17 * 1.9/100

        vals.cbibv18 = float(request.POST['cbibv18'])
        vals.cpetv18 = float(request.POST['cpetv18'])
        vals.cbibv_gsbo18 = vals.cbibv18 * 20/100
        vals.cbibv_blendedoil18 = vals.cbibv18 * 45/100
        vals.cbibv_rol18 = vals.cbibv18 * 15/100
        vals.cbibv_spmf18 = vals.cbibv18 * 20/100
        vals.cpetv_gsbo1_18 = vals.cpetv18 * 2/100
        vals.cpetv_gsbo2_18 = vals.cpetv18 * 12/100
        vals.cpetv_gsbo3_18 = vals.cpetv18 * 3/100
        vals.cpetv_gsbo4_18 = vals.cpetv18 * 15/100
        vals.cpetv_blendedoil1_18 = vals.cpetv18 * 3.3/100
        vals.cpetv_blendedoil2_18 = vals.cpetv18 * 40.3/100
        vals.cpetv_blendedoil3_18 = vals.cpetv18 * 4.5/100
        vals.cpetv_blendedoil4_18 = vals.cpetv18 * 1.8/100
        vals.cpetv_superolein1_18 = vals.cpetv18 * 1.3/100
        vals.cpetv_superolein2_18 = vals.cpetv18 * 13.4/100
        vals.cpetv_superolein3_18 = vals.cpetv18 * 1.5/100
        vals.cpetv_superolein4_18 = vals.cpetv18 * 1.9/100

        vals.cbibv19 = float(request.POST['cbibv19'])
        vals.cpetv19 = float(request.POST['cpetv19'])
        vals.cbibv_gsbo19 = vals.cbibv19 * 20/100
        vals.cbibv_blendedoil19 = vals.cbibv19 * 45/100
        vals.cbibv_rol19 = vals.cbibv19 * 15/100
        vals.cbibv_spmf19 = vals.cbibv19 * 20/100
        vals.cpetv_gsbo1_19 = vals.cpetv19 * 2/100
        vals.cpetv_gsbo2_19 = vals.cpetv19 * 12/100
        vals.cpetv_gsbo3_19 = vals.cpetv19 * 3/100
        vals.cpetv_gsbo4_19 = vals.cpetv19 * 15/100
        vals.cpetv_blendedoil1_19 = vals.cpetv19 * 3.3/100
        vals.cpetv_blendedoil2_19 = vals.cpetv19 * 40.3/100
        vals.cpetv_blendedoil3_19 = vals.cpetv19 * 4.5/100
        vals.cpetv_blendedoil4_19 = vals.cpetv19 * 1.8/100
        vals.cpetv_superolein1_19 = vals.cpetv19 * 1.3/100
        vals.cpetv_superolein2_19 = vals.cpetv19 * 13.4/100
        vals.cpetv_superolein3_19 = vals.cpetv19 * 1.5/100
        vals.cpetv_superolein4_19 = vals.cpetv19 * 1.9/100

        vals.cbibv20 = float(request.POST['cbibv20'])
        vals.cpetv20 = float(request.POST['cpetv20'])
        vals.cbibv_gsbo20 = vals.cbibv20 * 20/100
        vals.cbibv_blendedoil20 = vals.cbibv20 * 45/100
        vals.cbibv_rol20 = vals.cbibv20 * 15/100
        vals.cbibv_spmf20 = vals.cbibv20 * 20/100
        vals.cpetv_gsbo1_20 = vals.cpetv20 * 2/100
        vals.cpetv_gsbo2_20 = vals.cpetv20 * 12/100
        vals.cpetv_gsbo3_20 = vals.cpetv20 * 3/100
        vals.cpetv_gsbo4_20 = vals.cpetv20 * 15/100
        vals.cpetv_blendedoil1_20 = vals.cpetv20 * 3.3/100
        vals.cpetv_blendedoil2_20 = vals.cpetv20 * 40.3/100
        vals.cpetv_blendedoil3_20 = vals.cpetv20 * 4.5/100
        vals.cpetv_blendedoil4_20 = vals.cpetv20 * 1.8/100
        vals.cpetv_superolein1_20 = vals.cpetv20 * 1.3/100
        vals.cpetv_superolein2_20 = vals.cpetv20 * 13.4/100
        vals.cpetv_superolein3_20 = vals.cpetv20 * 1.5/100
        vals.cpetv_superolein4_20 = vals.cpetv20 * 1.9/100

        vals.cbibv21 = float(request.POST['cbibv21'])
        vals.cpetv21 = float(request.POST['cpetv21'])
        vals.cbibv_gsbo21 = vals.cbibv21 * 20/100
        vals.cbibv_blendedoil21 = vals.cbibv21 * 45/100
        vals.cbibv_rol21 = vals.cbibv21 * 15/100
        vals.cbibv_spmf21 = vals.cbibv21 * 20/100
        vals.cpetv_gsbo1_21 = vals.cpetv21 * 2/100
        vals.cpetv_gsbo2_21 = vals.cpetv21 * 12/100
        vals.cpetv_gsbo3_21 = vals.cpetv21 * 3/100
        vals.cpetv_gsbo4_21 = vals.cpetv21 * 15/100
        vals.cpetv_blendedoil1_21 = vals.cpetv21 * 3.3/100
        vals.cpetv_blendedoil2_21 = vals.cpetv21 * 40.3/100
        vals.cpetv_blendedoil3_21 = vals.cpetv21 * 4.5/100
        vals.cpetv_blendedoil4_21 = vals.cpetv21 * 1.8/100
        vals.cpetv_superolein1_21 = vals.cpetv21 * 1.3/100
        vals.cpetv_superolein2_21 = vals.cpetv21 * 13.4/100
        vals.cpetv_superolein3_21 = vals.cpetv21 * 1.5/100
        vals.cpetv_superolein4_21 = vals.cpetv21 * 1.9/100

        vals.cbibv22 = float(request.POST['cbibv22'])
        vals.cpetv22 = float(request.POST['cpetv22'])
        vals.cbibv_gsbo22 = vals.cbibv22 * 20/100
        vals.cbibv_blendedoil22 = vals.cbibv22 * 45/100
        vals.cbibv_rol22 = vals.cbibv22 * 15/100
        vals.cbibv_spmf22 = vals.cbibv22 * 20/100
        vals.cpetv_gsbo1_22 = vals.cpetv22 * 2/100
        vals.cpetv_gsbo2_22 = vals.cpetv22 * 12/100
        vals.cpetv_gsbo3_22 = vals.cpetv22 * 3/100
        vals.cpetv_gsbo4_22 = vals.cpetv22 * 15/100
        vals.cpetv_blendedoil1_22 = vals.cpetv22 * 3.3/100
        vals.cpetv_blendedoil2_22 = vals.cpetv22 * 40.3/100
        vals.cpetv_blendedoil3_22 = vals.cpetv22 * 4.5/100
        vals.cpetv_blendedoil4_22 = vals.cpetv22 * 1.8/100
        vals.cpetv_superolein1_22 = vals.cpetv22 * 1.3/100
        vals.cpetv_superolein2_22 = vals.cpetv22 * 13.4/100
        vals.cpetv_superolein3_22 = vals.cpetv22 * 1.5/100
        vals.cpetv_superolein4_22 = vals.cpetv22 * 1.9/100

        vals.cbibv23 = float(request.POST['cbibv23'])
        vals.cpetv23 = float(request.POST['cpetv23'])
        vals.cbibv_gsbo23 = vals.cbibv23 * 20/100
        vals.cbibv_blendedoil23 = vals.cbibv23 * 45/100
        vals.cbibv_rol23 = vals.cbibv23 * 15/100
        vals.cbibv_spmf23 = vals.cbibv23 * 20/100
        vals.cpetv_gsbo1_23 = vals.cpetv23 * 2/100
        vals.cpetv_gsbo2_23 = vals.cpetv23 * 12/100
        vals.cpetv_gsbo3_23 = vals.cpetv23 * 3/100
        vals.cpetv_gsbo4_23 = vals.cpetv23 * 15/100
        vals.cpetv_blendedoil1_23 = vals.cpetv23 * 3.3/100
        vals.cpetv_blendedoil2_23 = vals.cpetv23 * 40.3/100
        vals.cpetv_blendedoil3_23 = vals.cpetv23 * 4.5/100
        vals.cpetv_blendedoil4_23 = vals.cpetv23 * 1.8/100
        vals.cpetv_superolein1_23 = vals.cpetv23 * 1.3/100
        vals.cpetv_superolein2_23 = vals.cpetv23 * 13.4/100
        vals.cpetv_superolein3_23 = vals.cpetv23 * 1.5/100
        vals.cpetv_superolein4_23 = vals.cpetv23 * 1.9/100

        vals.cbibv24 = float(request.POST['cbibv24'])
        vals.cpetv24 = float(request.POST['cpetv24'])
        vals.cbibv_gsbo24 = vals.cbibv24 * 20/100
        vals.cbibv_blendedoil24 = vals.cbibv24 * 45/100
        vals.cbibv_rol24 = vals.cbibv24 * 15/100
        vals.cbibv_spmf24 = vals.cbibv24 * 20/100
        vals.cpetv_gsbo1_24 = vals.cpetv24 * 2/100
        vals.cpetv_gsbo2_24 = vals.cpetv24 * 12/100
        vals.cpetv_gsbo3_24 = vals.cpetv24 * 3/100
        vals.cpetv_gsbo4_24 = vals.cpetv24 * 15/100
        vals.cpetv_blendedoil1_24 = vals.cpetv24 * 3.3/100
        vals.cpetv_blendedoil2_24 = vals.cpetv24 * 40.3/100
        vals.cpetv_blendedoil3_24 = vals.cpetv24 * 4.5/100
        vals.cpetv_blendedoil4_24 = vals.cpetv24 * 1.8/100
        vals.cpetv_superolein1_24 = vals.cpetv24 * 1.3/100
        vals.cpetv_superolein2_24 = vals.cpetv24 * 13.4/100
        vals.cpetv_superolein3_24 = vals.cpetv24 * 1.5/100
        vals.cpetv_superolein4_24 = vals.cpetv24 * 1.9/100

        vals.mpbest15 = float(request.POST['mpbest15'])
        vals.mpbest16 = float(request.POST['mpbest16'])
        vals.mpbest17 = float(request.POST['mpbest17'])
        vals.mpbest18 = float(request.POST['mpbest18'])
        vals.mpbest19 = float(request.POST['mpbest19'])
        vals.mpbest20 = float(request.POST['mpbest20'])
        vals.mpbest21 = float(request.POST['mpbest21'])
        vals.mpbest22 = float(request.POST['mpbest22'])
        vals.mpbest23 = float(request.POST['mpbest23'])
        vals.mpbest24 = float(request.POST['mpbest24'])

        vals.mpbuis15 = float(request.POST['mpbuis15'])
        vals.mpbuis16 = float(request.POST['mpbuis16'])
        vals.mpbuis17 = float(request.POST['mpbuis17'])
        vals.mpbuis18 = float(request.POST['mpbuis18'])
        vals.mpbuis19 = float(request.POST['mpbuis19'])
        vals.mpbuis20 = float(request.POST['mpbuis20'])
        vals.mpbuis21 = float(request.POST['mpbuis21'])
        vals.mpbuis22 = float(request.POST['mpbuis22'])
        vals.mpbuis23 = float(request.POST['mpbuis23'])
        vals.mpbuis24 = float(request.POST['mpbuis24'])

        vals.buis_ratio15 = 0
        vals.buis_ratio16 = (vals.mpbuis16/vals.mpbuis15 - 1)*100 
        vals.buis_ratio17 = (vals.mpbuis17/vals.mpbuis16 - 1)*100
        vals.buis_ratio18 = (vals.mpbuis18/vals.mpbuis17 - 1)*100
        vals.buis_ratio19 = (vals.mpbuis19/vals.mpbuis18 - 1)*100
        vals.buis_ratio20 = (vals.mpbuis20/vals.mpbuis19 - 1)*100
        vals.buis_ratio21 = (vals.mpbuis21/vals.mpbuis20 - 1)*100
        vals.buis_ratio22 = (vals.mpbuis22/vals.mpbuis21 - 1)*100
        vals.buis_ratio23 = (vals.mpbuis23/vals.mpbuis22 - 1)*100
        vals.buis_ratio24 = (vals.mpbuis24/vals.mpbuis23 - 1)*100

        vals.pet15 = vals.mpbuis15*70/100
        vals.pet16 = vals.mpbuis16*70/100
        vals.pet17 = vals.mpbuis17*70/100
        vals.pet18 = vals.mpbuis18*70/100
        vals.pet19 = vals.mpbuis19*70/100
        vals.pet20 = vals.mpbuis20*70/100
        vals.pet21 = vals.mpbuis21*70/100
        vals.pet22 = vals.mpbuis22*70/100
        vals.pet23 = vals.mpbuis23*70/100
        vals.pet24 = vals.mpbuis24*70/100

        vals.bib15 = vals.mpbuis15*30/100
        vals.bib16 = vals.mpbuis16*30/100
        vals.bib17 = vals.mpbuis17*30/100
        vals.bib18 = vals.mpbuis18*30/100
        vals.bib19 = vals.mpbuis19*30/100
        vals.bib20 = vals.mpbuis20*30/100
        vals.bib21 = vals.mpbuis21*30/100
        vals.bib22 = vals.mpbuis22*30/100
        vals.bib23 = vals.mpbuis23*30/100
        vals.bib24 = vals.mpbuis24*30/100

        vals.a5l4buis15 = vals.mpbuis15*5/100
        vals.a20lbuis15 = vals.mpbuis15*46/100
        vals.a20lbbuis15 = vals.mpbuis15*6/100
        vals.a10l2buis15 = vals.mpbuis15*13/100
        vals.abib22lbuis15 = vals.mpbuis15*30/100
        vals.atotalbuis15 = vals.a5l4buis15 + vals.a20lbuis15 + vals.a20lbbuis15 + vals.a10l2buis15 + vals.abib22lbuis15

        vals.a5l4buis16 = vals.mpbuis16*5/100
        vals.a20lbuis16 = vals.mpbuis16*46/100
        vals.a20lbbuis16 = vals.mpbuis16*6/100
        vals.a10l2buis16 = vals.mpbuis16*13/100
        vals.abib22lbuis16 = vals.mpbuis16*30/100
        vals.atotalbuis16 = vals.a5l4buis16 + vals.a20lbuis16 + vals.a20lbbuis16 + vals.a10l2buis16 + vals.abib22lbuis16

        vals.a5l4buis17 = vals.mpbuis17*5/100
        vals.a20lbuis17 = vals.mpbuis17*46/100
        vals.a20lbbuis17 = vals.mpbuis17*6/100
        vals.a10l2buis17 = vals.mpbuis17*13/100
        vals.abib22lbuis17 = vals.mpbuis17*30/100
        vals.atotalbuis17 = vals.a5l4buis17 + vals.a20lbuis17 + vals.a20lbbuis17 + vals.a10l2buis17 + vals.abib22lbuis17

        vals.a5l4buis18 = vals.mpbuis18*5/100
        vals.a20lbuis18 = vals.mpbuis18*46/100
        vals.a20lbbuis18 = vals.mpbuis18*6/100
        vals.a10l2buis18 = vals.mpbuis18*13/100
        vals.abib22lbuis18 = vals.mpbuis18*30/100
        vals.atotalbuis18 = vals.a5l4buis18 + vals.a20lbuis18 + vals.a20lbbuis18 + vals.a10l2buis18 + vals.abib22lbuis18

        vals.a5l4buis19 = vals.mpbuis19*5/100
        vals.a20lbuis19 = vals.mpbuis19*46/100
        vals.a20lbbuis19 = vals.mpbuis19*6/100
        vals.a10l2buis19 = vals.mpbuis19*13/100
        vals.abib22lbuis19 = vals.mpbuis19*30/100
        vals.atotalbuis19 = vals.a5l4buis19 + vals.a20lbuis19 + vals.a20lbbuis19 + vals.a10l2buis19 + vals.abib22lbuis19

        vals.a5l4buis20 = vals.mpbuis20*5/100
        vals.a20lbuis20 = vals.mpbuis20*46/100
        vals.a20lbbuis20 = vals.mpbuis20*6/100
        vals.a10l2buis20 = vals.mpbuis20*13/100
        vals.abib22lbuis20 = vals.mpbuis20*30/100
        vals.atotalbuis20 = vals.a5l4buis20 + vals.a20lbuis20 + vals.a20lbbuis20 + vals.a10l2buis20 + vals.abib22lbuis20

        vals.a5l4buis21 = vals.mpbuis21*5/100
        vals.a20lbuis21 = vals.mpbuis21*46/100
        vals.a20lbbuis21 = vals.mpbuis21*6/100
        vals.a10l2buis21 = vals.mpbuis21*13/100
        vals.abib22lbuis21 = vals.mpbuis21*30/100
        vals.atotalbuis21 = vals.a5l4buis21 + vals.a20lbuis21 + vals.a20lbbuis21 + vals.a10l2buis21 + vals.abib22lbuis21

        vals.a5l4buis22 = vals.mpbuis22*5/100
        vals.a20lbuis22 = vals.mpbuis22*46/100
        vals.a20lbbuis22 = vals.mpbuis22*6/100
        vals.a10l2buis22 = vals.mpbuis22*13/100
        vals.abib22lbuis22 = vals.mpbuis22*30/100
        vals.atotalbuis22 = vals.a5l4buis22 + vals.a20lbuis22 + vals.a20lbbuis22 + vals.a10l2buis22 + vals.abib22lbuis22

        vals.a5l4buis23 = vals.mpbuis23*5/100
        vals.a20lbuis23 = vals.mpbuis23*46/100
        vals.a20lbbuis23 = vals.mpbuis23*6/100
        vals.a10l2buis23 = vals.mpbuis23*13/100
        vals.abib22lbuis23 = vals.mpbuis23*30/100
        vals.atotalbuis23 = vals.a5l4buis23 + vals.a20lbuis23 + vals.a20lbbuis23 + vals.a10l2buis23 + vals.abib22lbuis23

        vals.a5l4buis24 = vals.mpbuis24*5/100
        vals.a20lbuis24 = vals.mpbuis24*46/100
        vals.a20lbbuis24 = vals.mpbuis24*6/100
        vals.a10l2buis24 = vals.mpbuis24*13/100
        vals.abib22lbuis24 = vals.mpbuis24*30/100
        vals.atotalbuis24 = vals.a5l4buis24 + vals.a20lbuis24 + vals.a20lbbuis24 + vals.a10l2buis24 + vals.abib22lbuis24

        vals.m5l4buis15 = vals.mpbuis15*5/100
        vals.m20lbuis15 = vals.mpbuis15*46/100
        vals.m20lbbuis15 = vals.mpbuis15*6/100
        vals.m10l2buis15 = vals.mpbuis15*13/100
        vals.mbib22lbuis15 = vals.mpbuis15*30/100
        vals.mtotalbuis15 = vals.m5l4buis15 + vals.m20lbuis15 + vals.m20lbbuis15 + vals.m10l2buis15 + vals.mbib22lbuis15

        vals.m5l4buis16 = vals.mpbuis16*5/100
        vals.m20lbuis16 = vals.mpbuis16*46/100
        vals.m20lbbuis16 = vals.mpbuis16*6/100
        vals.m10l2buis16 = vals.mpbuis16*13/100
        vals.mbib22lbuis16 = vals.mpbuis16*30/100
        vals.mtotalbuis16 = vals.m5l4buis16 + vals.m20lbuis16 + vals.m20lbbuis16 + vals.m10l2buis16 + vals.mbib22lbuis16

        vals.m5l4buis17 = vals.mpbuis17*5/100
        vals.m20lbuis17 = vals.mpbuis17*46/100
        vals.m20lbbuis17 = vals.mpbuis17*6/100
        vals.m10l2buis17 = vals.mpbuis17*13/100
        vals.mbib22lbuis17 = vals.mpbuis17*30/100
        vals.mtotalbuis17 = vals.m5l4buis17 + vals.m20lbuis17 + vals.m20lbbuis17 + vals.m10l2buis17 + vals.mbib22lbuis17

        vals.m5l4buis18 = vals.mpbuis18*5/100
        vals.m20lbuis18 = vals.mpbuis18*46/100
        vals.m20lbbuis18 = vals.mpbuis18*6/100
        vals.m10l2buis18 = vals.mpbuis18*13/100
        vals.mbib22lbuis18 = vals.mpbuis18*30/100
        vals.mtotalbuis18 = vals.m5l4buis18 + vals.m20lbuis18 + vals.m20lbbuis18 + vals.m10l2buis18 + vals.mbib22lbuis18

        vals.m5l4buis19 = vals.mpbuis19*5/100
        vals.m20lbuis19 = vals.mpbuis19*46/100
        vals.m20lbbuis19 = vals.mpbuis19*6/100
        vals.m10l2buis19 = vals.mpbuis19*13/100
        vals.mbib22lbuis19 = vals.mpbuis19*30/100
        vals.mtotalbuis19 = vals.m5l4buis19 + vals.m20lbuis19 + vals.m20lbbuis19 + vals.m10l2buis19 + vals.mbib22lbuis19

        vals.m5l4buis20 = vals.mpbuis20*5/100
        vals.m20lbuis20 = vals.mpbuis20*46/100
        vals.m20lbbuis20 = vals.mpbuis20*6/100
        vals.m10l2buis20 = vals.mpbuis20*13/100
        vals.mbib22lbuis20 = vals.mpbuis20*30/100
        vals.mtotalbuis20 = vals.m5l4buis20 + vals.m20lbuis20 + vals.m20lbbuis20 + vals.m10l2buis20 + vals.mbib22lbuis20

        vals.m5l4buis21 = vals.mpbuis21*5/100
        vals.m20lbuis21 = vals.mpbuis21*46/100
        vals.m20lbbuis21 = vals.mpbuis21*6/100
        vals.m10l2buis21 = vals.mpbuis21*13/100
        vals.mbib22lbuis21 = vals.mpbuis21*30/100
        vals.mtotalbuis21 = vals.m5l4buis21 + vals.m20lbuis21 + vals.m20lbbuis21 + vals.m10l2buis21 + vals.mbib22lbuis21

        vals.m5l4buis22 = vals.mpbuis22*5/100
        vals.m20lbuis22 = vals.mpbuis22*46/100
        vals.m20lbbuis22 = vals.mpbuis22*6/100
        vals.m10l2buis22 = vals.mpbuis22*13/100
        vals.mbib22lbuis22 = vals.mpbuis22*30/100
        vals.mtotalbuis22 = vals.m5l4buis22 + vals.m20lbuis22 + vals.m20lbbuis22 + vals.m10l2buis22 + vals.mbib22lbuis22

        vals.m5l4buis23 = vals.mpbuis23*5/100
        vals.m20lbuis23 = vals.mpbuis23*46/100
        vals.m20lbbuis23 = vals.mpbuis23*6/100
        vals.m10l2buis23 = vals.mpbuis23*13/100
        vals.mbib22lbuis23 = vals.mpbuis23*30/100
        vals.mtotalbuis23 = vals.m5l4buis23 + vals.m20lbuis23 + vals.m20lbbuis23 + vals.m10l2buis23 + vals.mbib22lbuis23

        vals.m5l4buis24 = vals.mpbuis24*5/100
        vals.m20lbuis24 = vals.mpbuis24*46/100
        vals.m20lbbuis24 = vals.mpbuis24*6/100
        vals.m10l2buis24 = vals.mpbuis24*13/100
        vals.mbib22lbuis24 = vals.mpbuis24*30/100
        vals.mtotalbuis24 = vals.m5l4buis24 + vals.m20lbuis24 + vals.m20lbbuis24 + vals.m10l2buis24 + vals.mbib22lbuis24

        vals.a5l4best15 = vals.mpbest15*5/100
        vals.a20lbest15 = vals.mpbest15*46/100
        vals.a20lbbest15 = vals.mpbest15*6/100
        vals.a10l2best15 = vals.mpbest15*13/100
        vals.abib22lbest15 = vals.mpbest15*30/100
        vals.atotalbest15 = vals.a5l4best15 + vals.a20lbest15 + vals.a20lbbest15 + vals.a10l2best15 + vals.abib22lbest15

        vals.a5l4best16 = vals.mpbest16*5/100
        vals.a20lbest16 = vals.mpbest16*46/100
        vals.a20lbbest16 = vals.mpbest16*6/100
        vals.a10l2best16 = vals.mpbest16*13/100
        vals.abib22lbest16 = vals.mpbest16*30/100
        vals.atotalbest16 = vals.a5l4best16 + vals.a20lbest16 + vals.a20lbbest16 + vals.a10l2best16 + vals.abib22lbest16

        vals.a5l4best17 = vals.mpbest17*5/100
        vals.a20lbest17 = vals.mpbest17*46/100
        vals.a20lbbest17 = vals.mpbest17*6/100
        vals.a10l2best17 = vals.mpbest17*13/100
        vals.abib22lbest17 = vals.mpbest17*30/100
        vals.atotalbest17 = vals.a5l4best17 + vals.a20lbest17 + vals.a20lbbest17 + vals.a10l2best17 + vals.abib22lbest17

        vals.a5l4best18 = vals.mpbest18*5/100
        vals.a20lbest18 = vals.mpbest18*46/100
        vals.a20lbbest18 = vals.mpbest18*6/100
        vals.a10l2best18 = vals.mpbest18*13/100
        vals.abib22lbest18 = vals.mpbest18*30/100
        vals.atotalbest18 = vals.a5l4best18 + vals.a20lbest18 + vals.a20lbbest18 + vals.a10l2best18 + vals.abib22lbest18

        vals.a5l4best19 = vals.mpbest19*5/100
        vals.a20lbest19 = vals.mpbest19*46/100
        vals.a20lbbest19 = vals.mpbest19*6/100
        vals.a10l2best19 = vals.mpbest19*13/100
        vals.abib22lbest19 = vals.mpbest19*30/100
        vals.atotalbest19 = vals.a5l4best19 + vals.a20lbest19 + vals.a20lbbest19 + vals.a10l2best19 + vals.abib22lbest19

        vals.a5l4best20 = vals.mpbest20*5/100
        vals.a20lbest20 = vals.mpbest20*46/100
        vals.a20lbbest20 = vals.mpbest20*6/100
        vals.a10l2best20 = vals.mpbest20*13/100
        vals.abib22lbest20 = vals.mpbest20*30/100
        vals.atotalbest20 = vals.a5l4best20 + vals.a20lbest20 + vals.a20lbbest20 + vals.a10l2best20 + vals.abib22lbest20

        vals.a5l4best21 = vals.mpbest21*5/100
        vals.a20lbest21 = vals.mpbest21*46/100
        vals.a20lbbest21 = vals.mpbest21*6/100
        vals.a10l2best21 = vals.mpbest21*13/100
        vals.abib22lbest21 = vals.mpbest21*30/100
        vals.atotalbest21 = vals.a5l4best21 + vals.a20lbest21 + vals.a20lbbest21 + vals.a10l2best21 + vals.abib22lbest21

        vals.a5l4best22 = vals.mpbest22*5/100
        vals.a20lbest22 = vals.mpbest22*46/100
        vals.a20lbbest22 = vals.mpbest22*6/100
        vals.a10l2best22 = vals.mpbest22*13/100
        vals.abib22lbest22 = vals.mpbest22*30/100
        vals.atotalbest22 = vals.a5l4best22 + vals.a20lbest22 + vals.a20lbbest22 + vals.a10l2best22 + vals.abib22lbest22

        vals.a5l4best23 = vals.mpbest23*5/100
        vals.a20lbest23 = vals.mpbest23*46/100
        vals.a20lbbest23 = vals.mpbest23*6/100
        vals.a10l2best23 = vals.mpbest23*13/100
        vals.abib22lbest23 = vals.mpbest23*30/100
        vals.atotalbest23 = vals.a5l4best23 + vals.a20lbest23 + vals.a20lbbest23 + vals.a10l2best23 + vals.abib22lbest23

        vals.a5l4best24 = vals.mpbest24*5/100
        vals.a20lbest24 = vals.mpbest24*46/100
        vals.a20lbbest24 = vals.mpbest24*6/100
        vals.a10l2best24 = vals.mpbest24*13/100
        vals.abib22lbest24 = vals.mpbest24*30/100
        vals.atotalbest24 = vals.a5l4best24 + vals.a20lbest24 + vals.a20lbbest24 + vals.a10l2best24 + vals.abib22lbest24

        vals.m5l4best15 = vals.mpbest15*5/100
        vals.m20lbest15 = vals.mpbest15*46/100
        vals.m20lbbest15 = vals.mpbest15*6/100
        vals.m10l2best15 = vals.mpbest15*13/100
        vals.mbib22lbest15 = vals.mpbest15*30/100
        vals.mtotalbest15 = vals.m5l4best15 + vals.m20lbest15 + vals.m20lbbest15 + vals.m10l2best15 + vals.mbib22lbest15

        vals.m5l4best16 = vals.mpbest16*5/100
        vals.m20lbest16 = vals.mpbest16*46/100
        vals.m20lbbest16 = vals.mpbest16*6/100
        vals.m10l2best16 = vals.mpbest16*13/100
        vals.mbib22lbest16 = vals.mpbest16*30/100
        vals.mtotalbest16 = vals.m5l4best16 + vals.m20lbest16 + vals.m20lbbest16 + vals.m10l2best16 + vals.mbib22lbest16

        vals.m5l4best17 = vals.mpbest17*5/100
        vals.m20lbest17 = vals.mpbest17*46/100
        vals.m20lbbest17 = vals.mpbest17*6/100
        vals.m10l2best17 = vals.mpbest17*13/100
        vals.mbib22lbest17 = vals.mpbest17*30/100
        vals.mtotalbest17 = vals.m5l4best17 + vals.m20lbest17 + vals.m20lbbest17 + vals.m10l2best17 + vals.mbib22lbest17

        vals.m5l4best18 = vals.mpbest18*5/100
        vals.m20lbest18 = vals.mpbest18*46/100
        vals.m20lbbest18 = vals.mpbest18*6/100
        vals.m10l2best18 = vals.mpbest18*13/100
        vals.mbib22lbest18 = vals.mpbest18*30/100
        vals.mtotalbest18 = vals.m5l4best18 + vals.m20lbest18 + vals.m20lbbest18 + vals.m10l2best18 + vals.mbib22lbest18

        vals.m5l4best19 = vals.mpbest19*5/100
        vals.m20lbest19 = vals.mpbest19*46/100
        vals.m20lbbest19 = vals.mpbest19*6/100
        vals.m10l2best19 = vals.mpbest19*13/100
        vals.mbib22lbest19 = vals.mpbest19*30/100
        vals.mtotalbest19 = vals.m5l4best19 + vals.m20lbest19 + vals.m20lbbest19 + vals.m10l2best19 + vals.mbib22lbest19

        vals.m5l4best20 = vals.mpbest20*5/100
        vals.m20lbest20 = vals.mpbest20*46/100
        vals.m20lbbest20 = vals.mpbest20*6/100
        vals.m10l2best20 = vals.mpbest20*13/100
        vals.mbib22lbest20 = vals.mpbest20*30/100
        vals.mtotalbest20 = vals.m5l4best20 + vals.m20lbest20 + vals.m20lbbest20 + vals.m10l2best20 + vals.mbib22lbest20

        vals.m5l4best21 = vals.mpbest21*5/100
        vals.m20lbest21 = vals.mpbest21*46/100
        vals.m20lbbest21 = vals.mpbest21*6/100
        vals.m10l2best21 = vals.mpbest21*13/100
        vals.mbib22lbest21 = vals.mpbest21*30/100
        vals.mtotalbest21 = vals.m5l4best21 + vals.m20lbest21 + vals.m20lbbest21 + vals.m10l2best21 + vals.mbib22lbest21

        vals.m5l4best22 = vals.mpbest22*5/100
        vals.m20lbest22 = vals.mpbest22*46/100
        vals.m20lbbest22 = vals.mpbest22*6/100
        vals.m10l2best22 = vals.mpbest22*13/100
        vals.mbib22lbest22 = vals.mpbest22*30/100
        vals.mtotalbest22 = vals.m5l4best22 + vals.m20lbest22 + vals.m20lbbest22 + vals.m10l2best22 + vals.mbib22lbest22

        vals.m5l4best23 = vals.mpbest23*5/100
        vals.m20lbest23 = vals.mpbest23*46/100
        vals.m20lbbest23 = vals.mpbest23*6/100
        vals.m10l2best23 = vals.mpbest23*13/100
        vals.mbib22lbest23 = vals.mpbest23*30/100
        vals.mtotalbest23 = vals.m5l4best23 + vals.m20lbest23 + vals.m20lbbest23 + vals.m10l2best23 + vals.mbib22lbest23

        vals.m5l4best24 = vals.mpbest24*5/100
        vals.m20lbest24 = vals.mpbest24*46/100
        vals.m20lbbest24 = vals.mpbest24*6/100
        vals.m10l2best24 = vals.mpbest24*13/100
        vals.mbib22lbest24 = vals.mpbest24*30/100
        vals.mtotalbest24 = vals.m5l4best24 + vals.m20lbest24 + vals.m20lbbest24 + vals.m10l2best24 + vals.mbib22lbest24

        vals.lslt15 = float(request.POST['lslt15'])
        vals.wsaht15 = float(request.POST['wsaht15'])
        vals.wsalt15 = float(request.POST['wsalt15'])
        vals.wsltlt15 = float(request.POST['wsltlt15'])
        vals.wsltht15 = float(request.POST['wsltht15'])
        vals.ysaht15 = float(request.POST['ysaht15'])
        vals.ysalt15 = float(request.POST['ysalt15'])
        vals.ysltht15 = float(request.POST['ysltht15'])
        vals.ysltlt15 = float(request.POST['ysltlt15'])
        vals.cmaht15 = float(request.POST['cmaht15'])
        vals.cmalt15 = float(request.POST['cmalt15'])
        vals.cmltht1_15 = float(request.POST['cmltht1_15'])
        vals.cmltht2_15 = float(request.POST['cmltht2_15'])
        vals.cmltht3_15 = float(request.POST['cmltht3_15'])
        vals.cmltlt15 = float(request.POST['cmltlt15'])
        vals.smaht15 = float(request.POST['smaht15'])
        vals.smltht1_15 = float(request.POST['smltht1_15'])
        vals.smltht2_15 = float(request.POST['smltht2_15'])
        vals.totalsc15 = (vals.lslt15 + vals.wsaht15 + vals.wsltlt15 + vals.wsltht15 + vals.ysaht15 + vals.ysalt15 + vals.ysltlt15 +
                             vals.ysltht15 + vals.cmaht15 + vals.cmltht1_15 + vals.cmltht2_15 + vals.cmalt15 + vals.wsalt15 +
                                 vals.cmltht3_15 + vals.cmltlt15 + vals.smaht15 + vals.smltht1_15 + vals.smltht2_15)

        vals.lslt16 = float(request.POST['lslt16'])
        vals.wsaht16 = float(request.POST['wsaht16'])
        vals.wsalt16 = float(request.POST['wsalt16'])
        vals.wsltlt16 = float(request.POST['wsltlt16'])
        vals.wsltht16 = float(request.POST['wsltht16'])
        vals.ysaht16 = float(request.POST['ysaht16'])
        vals.ysalt16 = float(request.POST['ysalt16'])
        vals.ysltht16 = float(request.POST['ysltht16'])
        vals.ysltlt16 = float(request.POST['ysltlt16'])
        vals.cmaht16 = float(request.POST['cmaht16'])
        vals.cmalt16 = float(request.POST['cmalt16'])
        vals.cmltht1_16 = float(request.POST['cmltht1_16'])
        vals.cmltht2_16 = float(request.POST['cmltht2_16'])
        vals.cmltht3_16 = float(request.POST['cmltht3_16'])
        vals.cmltlt16 = float(request.POST['cmltlt16'])
        vals.smaht16 = float(request.POST['smaht16'])
        vals.smltht1_16 = float(request.POST['smltht1_16'])
        vals.smltht2_16 = float(request.POST['smltht2_16'])
        vals.totalsc16 = (vals.lslt16 + vals.wsaht16 + vals.wsltht16 + vals.wsltlt16 + vals.ysaht16 + vals.ysalt16 + vals.ysltlt16 +
                             vals.ysltht16 + vals.cmaht16 + vals.cmltht1_16 + vals.cmltht2_16 + vals.cmalt16 + vals.wsalt16 +
                                 vals.cmltht3_16 + vals.cmltlt16 + vals.smaht16 + vals.smltht1_16 + vals.smltht2_16)
                                 
        vals.lslt17 = float(request.POST['lslt17'])
        vals.wsaht17 = float(request.POST['wsaht17'])
        vals.wsalt17 = float(request.POST['wsalt17'])
        vals.wsltlt17 = float(request.POST['wsltlt17'])
        vals.wsltht17 = float(request.POST['wsltht17'])
        vals.ysaht17 = float(request.POST['ysaht17'])
        vals.ysalt17 = float(request.POST['ysalt17'])
        vals.ysltht17 = float(request.POST['ysltht17'])
        vals.ysltlt17 = float(request.POST['ysltlt17'])
        vals.cmaht17 = float(request.POST['cmaht17'])
        vals.cmalt17 = float(request.POST['cmalt17'])
        vals.cmltht1_17 = float(request.POST['cmltht1_17'])
        vals.cmltht2_17 = float(request.POST['cmltht2_17'])
        vals.cmltht3_17 = float(request.POST['cmltht3_17'])
        vals.cmltlt17 = float(request.POST['cmltlt17'])
        vals.smaht17 = float(request.POST['smaht17'])
        vals.smltht1_17 = float(request.POST['smltht1_17'])
        vals.smltht2_17 = float(request.POST['smltht2_17'])
        vals.totalsc17 = (vals.lslt17 + vals.wsaht17 + vals.wsltht17 + vals.wsltlt17 + vals.ysaht17 + vals.ysalt17 + vals.ysltlt17 +
                             vals.ysltht17 + vals.cmaht17 + vals.cmltht1_17 + vals.cmltht2_17 + vals.cmalt17 + vals.wsalt17 +
                                 vals.cmltht3_17 + vals.cmltlt17 + vals.smaht17 + vals.smltht1_17 + vals.smltht2_17)
                                 
        vals.lslt18 = float(request.POST['lslt18'])
        vals.wsaht18 = float(request.POST['wsaht18'])
        vals.wsalt18 = float(request.POST['wsalt18'])
        vals.wsltlt18 = float(request.POST['wsltlt18'])
        vals.wsltht18 = float(request.POST['wsltht18'])
        vals.ysaht18 = float(request.POST['ysaht18'])
        vals.ysalt18 = float(request.POST['ysalt18'])
        vals.ysltht18 = float(request.POST['ysltht18'])
        vals.ysltlt18 = float(request.POST['ysltlt18'])
        vals.cmaht18 = float(request.POST['cmaht18'])
        vals.cmalt18 = float(request.POST['cmalt18'])
        vals.cmltht1_18 = float(request.POST['cmltht1_18'])
        vals.cmltht2_18 = float(request.POST['cmltht2_18'])
        vals.cmltht3_18 = float(request.POST['cmltht3_18'])
        vals.cmltlt18 = float(request.POST['cmltlt18'])
        vals.smaht18 = float(request.POST['smaht18'])
        vals.smltht1_18 = float(request.POST['smltht1_18'])
        vals.smltht2_18 = float(request.POST['smltht2_18'])
        vals.totalsc18 = (vals.lslt18 + vals.wsaht18 + vals.wsltht18 + vals.wsltlt18 + vals.ysaht18 + vals.ysalt18 + vals.ysltlt18 +
                             vals.ysltht18 + vals.cmaht18 + vals.cmltht1_18 + vals.cmltht2_18 + vals.cmalt18 + vals.wsalt18 +
                                 vals.cmltht3_18 + vals.cmltlt18 + vals.smaht18 + vals.smltht1_18 + vals.smltht2_18)
                                 
        vals.lslt19 = float(request.POST['lslt19'])
        vals.wsaht19 = float(request.POST['wsaht19'])
        vals.wsalt19 = float(request.POST['wsalt19'])
        vals.wsltlt19 = float(request.POST['wsltlt19'])
        vals.wsltht19 = float(request.POST['wsltht19'])
        vals.ysaht19 = float(request.POST['ysaht19'])
        vals.ysalt19 = float(request.POST['ysalt19'])
        vals.ysltht19 = float(request.POST['ysltht19'])
        vals.ysltlt19 = float(request.POST['ysltlt19'])
        vals.cmaht19 = float(request.POST['cmaht19'])
        vals.cmalt19 = float(request.POST['cmalt19'])
        vals.cmltht1_19 = float(request.POST['cmltht1_19'])
        vals.cmltht2_19 = float(request.POST['cmltht2_19'])
        vals.cmltht3_19 = float(request.POST['cmltht3_19'])
        vals.cmltlt19 = float(request.POST['cmltlt19'])
        vals.smaht19 = float(request.POST['smaht19'])
        vals.smltht1_19 = float(request.POST['smltht1_19'])
        vals.smltht2_19 = float(request.POST['smltht2_19'])
        vals.totalsc19 = (vals.lslt19 + vals.wsaht19 + vals.wsltht19 + vals.wsltlt19 + vals.ysaht19 + vals.ysalt19 + vals.ysltlt19 +
                             vals.ysltht19 + vals.cmaht19 + vals.cmltht1_19 + vals.cmltht2_19 + vals.cmalt19 + vals.wsalt19 +
                                 vals.cmltht3_19 + vals.cmltlt19 + vals.smaht19 + vals.smltht1_19 + vals.smltht2_19)                                 
                                 
        vals.lslt20 = float(request.POST['lslt20'])
        vals.wsaht20 = float(request.POST['wsaht20'])
        vals.wsalt20 = float(request.POST['wsalt20'])
        vals.wsltlt20 = float(request.POST['wsltlt20'])
        vals.wsltht20 = float(request.POST['wsltht20'])
        vals.ysaht20 = float(request.POST['ysaht20'])
        vals.ysalt20 = float(request.POST['ysalt20'])
        vals.ysltht20 = float(request.POST['ysltht20'])
        vals.ysltlt20 = float(request.POST['ysltlt20'])
        vals.cmaht20 = float(request.POST['cmaht20'])
        vals.cmalt20 = float(request.POST['cmalt20'])
        vals.cmltht1_20 = float(request.POST['cmltht1_20'])
        vals.cmltht2_20 = float(request.POST['cmltht2_20'])
        vals.cmltht3_20 = float(request.POST['cmltht3_20'])
        vals.cmltlt20 = float(request.POST['cmltlt20'])
        vals.smaht20 = float(request.POST['smaht20'])
        vals.smltht1_20 = float(request.POST['smltht1_20'])
        vals.smltht2_20 = float(request.POST['smltht2_20'])
        vals.totalsc20 = (vals.lslt20 + vals.wsaht20 + vals.wsltht20 + vals.wsltlt20 + vals.ysaht20 + vals.ysalt20 + vals.ysltlt20 +
                             vals.ysltht20 + vals.cmaht20 + vals.cmltht1_20 + vals.cmltht2_20 +  vals.cmalt20 + vals.wsalt20 +
                                 vals.cmltht3_20 + vals.cmltlt20 + vals.smaht20 + vals.smltht1_20 + vals.smltht2_20)                                 
                                 
        vals.lslt21 = float(request.POST['lslt21'])
        vals.wsaht21 = float(request.POST['wsaht21'])
        vals.wsalt21 = float(request.POST['wsalt21'])
        vals.wsltlt21 = float(request.POST['wsltlt21'])
        vals.wsltht21 = float(request.POST['wsltht21'])
        vals.ysaht21 = float(request.POST['ysaht21'])
        vals.ysalt21 = float(request.POST['ysalt21'])
        vals.ysltht21 = float(request.POST['ysltht21'])
        vals.ysltlt21 = float(request.POST['ysltlt21'])
        vals.cmaht21 = float(request.POST['cmaht21'])
        vals.cmalt21 = float(request.POST['cmalt21'])
        vals.cmltht1_21 = float(request.POST['cmltht1_21'])
        vals.cmltht2_21 = float(request.POST['cmltht2_21'])
        vals.cmltht3_21 = float(request.POST['cmltht3_21'])
        vals.cmltlt21 = float(request.POST['cmltlt21'])
        vals.smaht21 = float(request.POST['smaht21'])
        vals.smltht1_21 = float(request.POST['smltht1_21'])
        vals.smltht2_21 = float(request.POST['smltht2_21'])
        vals.totalsc21 = (vals.lslt21 + vals.wsaht21 + vals.wsltht21 + vals.wsltlt21 + vals.ysaht21 + vals.ysalt21 + vals.ysltlt21 +
                             vals.ysltht21 + vals.cmaht21 + vals.cmltht1_21 + vals.cmltht2_21 + vals.cmalt21 + vals.wsalt21 +
                                 vals.cmltht3_21 + vals.cmltlt21 + vals.smaht21 + vals.smltht1_21 + vals.smltht2_21)                                 

        vals.lslt22 = float(request.POST['lslt22'])
        vals.wsaht22 = float(request.POST['wsaht22'])
        vals.wsalt22 = float(request.POST['wsalt22'])
        vals.wsltlt22 = float(request.POST['wsltlt22'])
        vals.wsltht22 = float(request.POST['wsltht22'])
        vals.ysaht22 = float(request.POST['ysaht22'])
        vals.ysalt22 = float(request.POST['ysalt22'])
        vals.ysltht22 = float(request.POST['ysltht22'])
        vals.ysltlt22 = float(request.POST['ysltlt22'])
        vals.cmaht22 = float(request.POST['cmaht22'])
        vals.cmalt22 = float(request.POST['cmalt22'])
        vals.cmltht1_22 = float(request.POST['cmltht1_22'])
        vals.cmltht2_22 = float(request.POST['cmltht2_22'])
        vals.cmltht3_22 = float(request.POST['cmltht3_22'])
        vals.cmltlt22 = float(request.POST['cmltlt22'])
        vals.smaht22 = float(request.POST['smaht22'])
        vals.smltht1_22 = float(request.POST['smltht1_22'])
        vals.smltht2_22 = float(request.POST['smltht2_22'])
        vals.totalsc22 = (vals.lslt22 + vals.wsaht22 + vals.wsltht22 + vals.wsltlt22 + vals.ysaht22 + vals.ysalt22 + vals.ysltlt22 +
                             vals.ysltht22 + vals.cmaht22 + vals.cmltht1_22 + vals.cmltht2_22 +  vals.cmalt22 + vals.wsalt22 +
                                 vals.cmltht3_22 + vals.cmltlt22 + vals.smaht22 + vals.smltht1_22 + vals.smltht2_22)                                 
                                 
        vals.lslt23 = float(request.POST['lslt23'])
        vals.wsaht23 = float(request.POST['wsaht23'])
        vals.wsalt23 = float(request.POST['wsalt23'])
        vals.wsltlt23 = float(request.POST['wsltlt23'])
        vals.wsltht23 = float(request.POST['wsltht23'])
        vals.ysaht23 = float(request.POST['ysaht23'])
        vals.ysalt23 = float(request.POST['ysalt23'])
        vals.ysltht23 = float(request.POST['ysltht23'])
        vals.ysltlt23 = float(request.POST['ysltlt23'])
        vals.cmaht23 = float(request.POST['cmaht23'])
        vals.cmalt23 = float(request.POST['cmalt23'])
        vals.cmltht1_23 = float(request.POST['cmltht1_23'])
        vals.cmltht2_23 = float(request.POST['cmltht2_23'])
        vals.cmltht3_23 = float(request.POST['cmltht3_23'])
        vals.cmltlt23 = float(request.POST['cmltlt23'])
        vals.smaht23 = float(request.POST['smaht23'])
        vals.smltht1_23 = float(request.POST['smltht1_23'])
        vals.smltht2_23 = float(request.POST['smltht2_23'])
        vals.totalsc23 = (vals.lslt23 + vals.wsaht23 + vals.wsltht23 + vals.wsltlt23 + vals.ysaht23 + vals.ysalt23 + vals.ysltlt23 +
                             vals.ysltht23 + vals.cmaht23 + vals.cmltht1_23 + vals.cmltht2_23 + vals.cmalt23 + vals.wsalt23 +
                                 vals.cmltht3_23 + vals.cmltlt23 + vals.smaht23 + vals.smltht1_23 + vals.smltht2_23)                                 
                                 
        vals.lslt24 = float(request.POST['lslt24'])
        vals.wsaht24 = float(request.POST['wsaht24'])
        vals.wsalt24 = float(request.POST['wsalt24'])
        vals.wsltlt24 = float(request.POST['wsltlt24'])
        vals.wsltht24 = float(request.POST['wsltht24'])
        vals.ysaht24 = float(request.POST['ysaht24'])
        vals.ysalt24 = float(request.POST['ysalt24'])
        vals.ysltht24 = float(request.POST['ysltht24'])
        vals.ysltlt24 = float(request.POST['ysltlt24'])
        vals.cmaht24 = float(request.POST['cmaht24'])
        vals.cmalt24 = float(request.POST['cmalt24'])
        vals.cmltht1_24 = float(request.POST['cmltht1_24'])
        vals.cmltht2_24 = float(request.POST['cmltht2_24'])
        vals.cmltht3_24 = float(request.POST['cmltht3_24'])
        vals.cmltlt24 = float(request.POST['cmltlt24'])
        vals.smaht24 = float(request.POST['smaht24'])
        vals.smltht1_24 = float(request.POST['smltht1_24'])
        vals.smltht2_24 = float(request.POST['smltht2_24'])
        vals.totalsc24 = (vals.lslt24 + vals.wsaht24 + vals.wsltht24 + vals.wsltlt24 + vals.ysaht24 + vals.ysalt24 + vals.ysltlt24 +
                             vals.ysltht24 + vals.cmaht24 + vals.cmltht1_24 + vals.cmltht2_24 + vals.cmalt24 + vals.wsalt24 +
                                 vals.cmltht3_24 + vals.cmltlt24 + vals.smaht24 + vals.smltht1_24 + vals.smltht2_24)                                 

        vals.tcwsalt15 = float(request.POST['tcwsalt15'])
        vals.tcwsltlt15 = float(request.POST['tcwsltlt15'])
        vals.tcysalt15 = float(request.POST['tcysalt15'])
        vals.tcysltlt15 = float(request.POST['tcysltlt15'])
        vals.scwsalt15 = float(request.POST['scwsalt15'])
        vals.scwsltlt15 = float(request.POST['scwsltlt15'])
        vals.scysalt15 = float(request.POST['scwsltlt15'])
        vals.scysltlt15 = float(request.POST['scwsltlt15'])
        vals.tccmalt15 = float(request.POST['tccmalt15'])
        vals.tccmltlt1_15 = float(request.POST['tccmltlt1_15'])
        vals.tccmltlt2_15 = float(request.POST['tccmltlt2_15'])
        vals.tccmltlt3_15 = float(request.POST['tccmltlt3_15'])
        vals.sccmalt15 = float(request.POST['sccmalt15'])
        vals.sccmltlt1_15 = float(request.POST['sccmltlt1_15'])
        vals.sccmltlt2_15 = float(request.POST['sccmltlt2_15'])
        vals.sccmltlt3_15 = float(request.POST['sccmltlt3_15'])
        vals.tcsmalt15 = float(request.POST['tcsmalt15'])
        vals.tcsmltlt1_15 = float(request.POST['tcsmltlt1_15'])
        vals.tcsmltlt2_15 = float(request.POST['tcsmltlt2_15'])
        vals.scsmalt15 = float(request.POST['scsmalt15'])
        vals.scsmltlt1_15 = float(request.POST['scsmltlt1_15'])
        vals.scsmltlt2_15 = float(request.POST['scsmltlt2_15'])
        vals.ietotal15 = (vals.tcwsalt15 + vals.tcwsltlt15 + vals.tcysalt15 + vals.tcysltlt15 + 
                            vals.tccmalt15 + vals.tccmltlt1_15 + vals.tccmltlt2_15 + vals.tccmltlt3_15 +
                                vals.tcsmalt15 + vals.tcsmltlt1_15 + vals.tcsmltlt2_15)
        
        vals.tcwsalt16 = float(request.POST['tcwsalt16'])
        vals.tcwsltlt16 = float(request.POST['tcwsltlt16'])
        vals.tcysalt16 = float(request.POST['tcysalt16'])
        vals.tcysltlt16 = float(request.POST['tcysltlt16'])
        vals.scwsalt16 = float(request.POST['scwsalt16'])
        vals.scwsltlt16 = float(request.POST['scwsltlt16'])
        vals.scysalt16 = float(request.POST['scwsltlt16'])
        vals.scysltlt16 = float(request.POST['scwsltlt16'])
        vals.tccmalt16 = float(request.POST['tccmalt16'])
        vals.tccmltlt1_16 = float(request.POST['tccmltlt1_16'])
        vals.tccmltlt2_16 = float(request.POST['tccmltlt2_16'])
        vals.tccmltlt3_16 = float(request.POST['tccmltlt3_16'])
        vals.sccmalt16 = float(request.POST['sccmalt16'])
        vals.sccmltlt1_16 = float(request.POST['sccmltlt1_16'])
        vals.sccmltlt2_16 = float(request.POST['sccmltlt2_16'])
        vals.sccmltlt3_16 = float(request.POST['sccmltlt3_16'])
        vals.tcsmalt16 = float(request.POST['tcsmalt16'])
        vals.tcsmltlt1_16 = float(request.POST['tcsmltlt1_16'])
        vals.tcsmltlt2_16 = float(request.POST['tcsmltlt2_16'])
        vals.scsmalt16 = float(request.POST['scsmalt16'])
        vals.scsmltlt1_16 = float(request.POST['scsmltlt1_16'])
        vals.scsmltlt2_16 = float(request.POST['scsmltlt2_16'])
        vals.ietotal16 = (vals.tcwsalt16 + vals.tcwsltlt16 + vals.tcysalt16 + vals.tcysltlt16 + 
                            vals.tccmalt16 + vals.tccmltlt1_16 + vals.tccmltlt2_16 + vals.tccmltlt3_16 +
                                vals.tcsmalt16 + vals.tcsmltlt1_16 + vals.tcsmltlt2_16)
                                
        vals.tcwsalt17 = float(request.POST['tcwsalt17'])
        vals.tcwsltlt17 = float(request.POST['tcwsltlt17'])
        vals.tcysalt17 = float(request.POST['tcysalt17'])
        vals.tcysltlt17 = float(request.POST['tcysltlt17'])
        vals.scwsalt17 = float(request.POST['scwsalt17'])
        vals.scwsltlt17 = float(request.POST['scwsltlt17'])
        vals.scysalt17 = float(request.POST['scwsltlt17'])
        vals.scysltlt17 = float(request.POST['scwsltlt17'])
        vals.tccmalt17 = float(request.POST['tccmalt17'])
        vals.tccmltlt1_17 = float(request.POST['tccmltlt1_17'])
        vals.tccmltlt2_17 = float(request.POST['tccmltlt2_17'])
        vals.tccmltlt3_17 = float(request.POST['tccmltlt3_17'])
        vals.sccmalt17 = float(request.POST['sccmalt17'])
        vals.sccmltlt1_17 = float(request.POST['sccmltlt1_17'])
        vals.sccmltlt2_17 = float(request.POST['sccmltlt2_17'])
        vals.sccmltlt3_17 = float(request.POST['sccmltlt3_17'])
        vals.tcsmalt17 = float(request.POST['tcsmalt17'])
        vals.tcsmltlt1_17 = float(request.POST['tcsmltlt1_17'])
        vals.tcsmltlt2_17 = float(request.POST['tcsmltlt2_17'])
        vals.scsmalt17 = float(request.POST['scsmalt17'])
        vals.scsmltlt1_17 = float(request.POST['scsmltlt1_17'])
        vals.scsmltlt2_17 = float(request.POST['scsmltlt2_17'])
        vals.ietotal17 = (vals.tcwsalt17 + vals.tcwsltlt17 + vals.tcysalt17 + vals.tcysltlt17 + 
                            vals.tccmalt17 + vals.tccmltlt1_17 + vals.tccmltlt2_17 + vals.tccmltlt3_17 +
                                vals.tcsmalt17 + vals.tcsmltlt1_17 + vals.tcsmltlt2_17)
                                
        vals.tcwsalt18 = float(request.POST['tcwsalt18'])
        vals.tcwsltlt18 = float(request.POST['tcwsltlt18'])
        vals.tcysalt18 = float(request.POST['tcysalt18'])
        vals.tcysltlt18 = float(request.POST['tcysltlt18'])
        vals.scwsalt18 = float(request.POST['scwsalt18'])
        vals.scwsltlt18 = float(request.POST['scwsltlt18'])
        vals.scysalt18 = float(request.POST['scwsltlt18'])
        vals.scysltlt18 = float(request.POST['scwsltlt18'])
        vals.tccmalt18 = float(request.POST['tccmalt18'])
        vals.tccmltlt1_18 = float(request.POST['tccmltlt1_18'])
        vals.tccmltlt2_18 = float(request.POST['tccmltlt2_18'])
        vals.tccmltlt3_18 = float(request.POST['tccmltlt3_18'])
        vals.sccmalt18 = float(request.POST['sccmalt18'])
        vals.sccmltlt1_18 = float(request.POST['sccmltlt1_18'])
        vals.sccmltlt2_18 = float(request.POST['sccmltlt2_18'])
        vals.sccmltlt3_18 = float(request.POST['sccmltlt3_18'])
        vals.tcsmalt18 = float(request.POST['tcsmalt18'])
        vals.tcsmltlt1_18 = float(request.POST['tcsmltlt1_18'])
        vals.tcsmltlt2_18 = float(request.POST['tcsmltlt2_18'])
        vals.scsmalt18 = float(request.POST['scsmalt18'])
        vals.scsmltlt1_18 = float(request.POST['scsmltlt1_18'])
        vals.scsmltlt2_18 = float(request.POST['scsmltlt2_18'])
        vals.ietotal18 = (vals.tcwsalt18 + vals.tcwsltlt18 + vals.tcysalt18 + vals.tcysltlt18 + 
                            vals.tccmalt18 + vals.tccmltlt1_18 + vals.tccmltlt2_18 + vals.tccmltlt3_18 +
                                vals.tcsmalt18 + vals.tcsmltlt1_18 + vals.tcsmltlt2_18)                                
                                
        vals.tcwsalt19 = float(request.POST['tcwsalt19'])
        vals.tcwsltlt19 = float(request.POST['tcwsltlt19'])
        vals.tcysalt19 = float(request.POST['tcysalt19'])
        vals.tcysltlt19 = float(request.POST['tcysltlt19'])
        vals.scwsalt19 = float(request.POST['scwsalt19'])
        vals.scwsltlt19 = float(request.POST['scwsltlt19'])
        vals.scysalt19 = float(request.POST['scwsltlt19'])
        vals.scysltlt19 = float(request.POST['scwsltlt19'])
        vals.tccmalt19 = float(request.POST['tccmalt19'])
        vals.tccmltlt1_19 = float(request.POST['tccmltlt1_19'])
        vals.tccmltlt2_19 = float(request.POST['tccmltlt2_19'])
        vals.tccmltlt3_19 = float(request.POST['tccmltlt3_19'])
        vals.sccmalt19 = float(request.POST['sccmalt19'])
        vals.sccmltlt1_19 = float(request.POST['sccmltlt1_19'])
        vals.sccmltlt2_19 = float(request.POST['sccmltlt2_19'])
        vals.sccmltlt3_19 = float(request.POST['sccmltlt3_19'])
        vals.tcsmalt19 = float(request.POST['tcsmalt19'])
        vals.tcsmltlt1_19 = float(request.POST['tcsmltlt1_19'])
        vals.tcsmltlt2_19 = float(request.POST['tcsmltlt2_19'])
        vals.scsmalt19 = float(request.POST['scsmalt19'])
        vals.scsmltlt1_19 = float(request.POST['scsmltlt1_19'])
        vals.scsmltlt2_19 = float(request.POST['scsmltlt2_19'])
        vals.ietotal19 = (vals.tcwsalt19 + vals.tcwsltlt19 + vals.tcysalt19 + vals.tcysltlt19 + 
                            vals.tccmalt19 + vals.tccmltlt1_19 + vals.tccmltlt2_19 + vals.tccmltlt3_19 +
                                vals.tcsmalt19 + vals.tcsmltlt1_19 + vals.tcsmltlt2_19)                                
                                
        vals.tcwsalt20 = float(request.POST['tcwsalt20'])
        vals.tcwsltlt20 = float(request.POST['tcwsltlt20'])
        vals.tcysalt20 = float(request.POST['tcysalt20'])
        vals.tcysltlt20 = float(request.POST['tcysltlt20'])
        vals.scwsalt20 = float(request.POST['scwsalt20'])
        vals.scwsltlt20 = float(request.POST['scwsltlt20'])
        vals.scysalt20 = float(request.POST['scwsltlt20'])
        vals.scysltlt20 = float(request.POST['scwsltlt20'])
        vals.tccmalt20 = float(request.POST['tccmalt20'])
        vals.tccmltlt1_20 = float(request.POST['tccmltlt1_20'])
        vals.tccmltlt2_20 = float(request.POST['tccmltlt2_20'])
        vals.tccmltlt3_20 = float(request.POST['tccmltlt3_20'])
        vals.sccmalt20 = float(request.POST['sccmalt20'])
        vals.sccmltlt1_20 = float(request.POST['sccmltlt1_20'])
        vals.sccmltlt2_20 = float(request.POST['sccmltlt2_20'])
        vals.sccmltlt3_20 = float(request.POST['sccmltlt3_20'])
        vals.tcsmalt20 = float(request.POST['tcsmalt20'])
        vals.tcsmltlt1_20 = float(request.POST['tcsmltlt1_20'])
        vals.tcsmltlt2_20 = float(request.POST['tcsmltlt2_20'])
        vals.scsmalt20 = float(request.POST['scsmalt20'])
        vals.scsmltlt1_20 = float(request.POST['scsmltlt1_20'])
        vals.scsmltlt2_20 = float(request.POST['scsmltlt2_20'])
        vals.ietotal20 = (vals.tcwsalt20 + vals.tcwsltlt20 + vals.tcysalt20 + vals.tcysltlt20 + 
                            vals.tccmalt20 + vals.tccmltlt1_20 + vals.tccmltlt2_20 + vals.tccmltlt3_20 +
                                vals.tcsmalt20 + vals.tcsmltlt1_20 + vals.tcsmltlt2_20)                                
                                
        vals.tcwsalt21 = float(request.POST['tcwsalt21'])
        vals.tcwsltlt21 = float(request.POST['tcwsltlt21'])
        vals.tcysalt21 = float(request.POST['tcysalt21'])
        vals.tcysltlt21 = float(request.POST['tcysltlt21'])
        vals.scwsalt21 = float(request.POST['scwsalt21'])
        vals.scwsltlt21 = float(request.POST['scwsltlt21'])
        vals.scysalt21 = float(request.POST['scwsltlt21'])
        vals.scysltlt21 = float(request.POST['scwsltlt21'])
        vals.tccmalt21 = float(request.POST['tccmalt21'])
        vals.tccmltlt1_21 = float(request.POST['tccmltlt1_21'])
        vals.tccmltlt2_21 = float(request.POST['tccmltlt2_21'])
        vals.tccmltlt3_21 = float(request.POST['tccmltlt3_21'])
        vals.sccmalt21 = float(request.POST['sccmalt21'])
        vals.sccmltlt1_21 = float(request.POST['sccmltlt1_21'])
        vals.sccmltlt2_21 = float(request.POST['sccmltlt2_21'])
        vals.sccmltlt3_21 = float(request.POST['sccmltlt3_21'])
        vals.tcsmalt21 = float(request.POST['tcsmalt21'])
        vals.tcsmltlt1_21 = float(request.POST['tcsmltlt1_21'])
        vals.tcsmltlt2_21 = float(request.POST['tcsmltlt2_21'])
        vals.scsmalt21 = float(request.POST['scsmalt21'])
        vals.scsmltlt1_21 = float(request.POST['scsmltlt1_21'])
        vals.scsmltlt2_21 = float(request.POST['scsmltlt2_21'])
        vals.ietotal21 = (vals.tcwsalt21 + vals.tcwsltlt21 + vals.tcysalt21 + vals.tcysltlt21 + 
                            vals.tccmalt21 + vals.tccmltlt1_21 + vals.tccmltlt2_21 + vals.tccmltlt3_21 +
                                vals.tcsmalt21 + vals.tcsmltlt1_21 + vals.tcsmltlt2_21)                                

        vals.tcwsalt22 = float(request.POST['tcwsalt22'])
        vals.tcwsltlt22 = float(request.POST['tcwsltlt22'])
        vals.tcysalt22 = float(request.POST['tcysalt22'])
        vals.tcysltlt22 = float(request.POST['tcysltlt22'])
        vals.scwsalt22 = float(request.POST['scwsalt22'])
        vals.scwsltlt22 = float(request.POST['scwsltlt22'])
        vals.scysalt22 = float(request.POST['scwsltlt22'])
        vals.scysltlt22 = float(request.POST['scwsltlt22'])
        vals.tccmalt22 = float(request.POST['tccmalt22'])
        vals.tccmltlt1_22 = float(request.POST['tccmltlt1_22'])
        vals.tccmltlt2_22 = float(request.POST['tccmltlt2_22'])
        vals.tccmltlt3_22 = float(request.POST['tccmltlt3_22'])
        vals.sccmalt22 = float(request.POST['sccmalt22'])
        vals.sccmltlt1_22 = float(request.POST['sccmltlt1_22'])
        vals.sccmltlt2_22 = float(request.POST['sccmltlt2_22'])
        vals.sccmltlt3_22 = float(request.POST['sccmltlt3_22'])
        vals.tcsmalt22 = float(request.POST['tcsmalt22'])
        vals.tcsmltlt1_22 = float(request.POST['tcsmltlt1_22'])
        vals.tcsmltlt2_22 = float(request.POST['tcsmltlt2_22'])
        vals.scsmalt22 = float(request.POST['scsmalt22'])
        vals.scsmltlt1_22 = float(request.POST['scsmltlt1_22'])
        vals.scsmltlt2_22 = float(request.POST['scsmltlt2_22'])
        vals.ietotal22 = (vals.tcwsalt22 + vals.tcwsltlt22 + vals.tcysalt22 + vals.tcysltlt22 + 
                            vals.tccmalt22 + vals.tccmltlt1_22 + vals.tccmltlt2_22 + vals.tccmltlt3_22 +
                                vals.tcsmalt22 + vals.tcsmltlt1_22 + vals.tcsmltlt2_22)                
                
        vals.tcwsalt23 = float(request.POST['tcwsalt23'])
        vals.tcwsltlt23 = float(request.POST['tcwsltlt23'])
        vals.tcysalt23 = float(request.POST['tcysalt23'])
        vals.tcysltlt23 = float(request.POST['tcysltlt23'])
        vals.scwsalt23 = float(request.POST['scwsalt23'])
        vals.scwsltlt23 = float(request.POST['scwsltlt23'])
        vals.scysalt23 = float(request.POST['scwsltlt23'])
        vals.scysltlt23 = float(request.POST['scwsltlt23'])
        vals.tccmalt23 = float(request.POST['tccmalt23'])
        vals.tccmltlt1_23 = float(request.POST['tccmltlt1_23'])
        vals.tccmltlt2_23 = float(request.POST['tccmltlt2_23'])
        vals.tccmltlt3_23 = float(request.POST['tccmltlt3_23'])
        vals.sccmalt23 = float(request.POST['sccmalt23'])
        vals.sccmltlt1_23 = float(request.POST['sccmltlt1_23'])
        vals.sccmltlt2_23 = float(request.POST['sccmltlt2_23'])
        vals.sccmltlt3_23 = float(request.POST['sccmltlt3_23'])
        vals.tcsmalt23 = float(request.POST['tcsmalt23'])
        vals.tcsmltlt1_23 = float(request.POST['tcsmltlt1_23'])
        vals.tcsmltlt2_23 = float(request.POST['tcsmltlt2_23'])
        vals.scsmalt23 = float(request.POST['scsmalt23'])
        vals.scsmltlt1_23 = float(request.POST['scsmltlt1_23'])
        vals.scsmltlt2_23 = float(request.POST['scsmltlt2_23'])
        vals.ietotal23 = (vals.tcwsalt23 + vals.tcwsltlt23 + vals.tcysalt23 + vals.tcysltlt23 + 
                            vals.tccmalt23 + vals.tccmltlt1_23 + vals.tccmltlt2_23 + vals.tccmltlt3_23 +
                                vals.tcsmalt23 + vals.tcsmltlt1_23 + vals.tcsmltlt2_23)                
                
        vals.tcwsalt24 = float(request.POST['tcwsalt24'])
        vals.tcwsltlt24 = float(request.POST['tcwsltlt24'])
        vals.tcysalt24 = float(request.POST['tcysalt24'])
        vals.tcysltlt24 = float(request.POST['tcysltlt24'])
        vals.scwsalt24 = float(request.POST['scwsalt24'])
        vals.scwsltlt24 = float(request.POST['scwsltlt24'])
        vals.scysalt24 = float(request.POST['scwsltlt24'])
        vals.scysltlt24 = float(request.POST['scwsltlt24'])
        vals.tccmalt24 = float(request.POST['tccmalt24'])
        vals.tccmltlt1_24 = float(request.POST['tccmltlt1_24'])
        vals.tccmltlt2_24 = float(request.POST['tccmltlt2_24'])
        vals.tccmltlt3_24 = float(request.POST['tccmltlt3_24'])
        vals.sccmalt24 = float(request.POST['sccmalt24'])
        vals.sccmltlt1_24 = float(request.POST['sccmltlt1_24'])
        vals.sccmltlt2_24 = float(request.POST['sccmltlt2_24'])
        vals.sccmltlt3_24 = float(request.POST['sccmltlt3_24'])
        vals.tcsmalt24 = float(request.POST['tcsmalt24'])
        vals.tcsmltlt1_24 = float(request.POST['tcsmltlt1_24'])
        vals.tcsmltlt2_24 = float(request.POST['tcsmltlt2_24'])
        vals.scsmalt24 = float(request.POST['scsmalt24'])
        vals.scsmltlt1_24 = float(request.POST['scsmltlt1_24'])
        vals.scsmltlt2_24 = float(request.POST['scsmltlt2_24'])
        vals.ietotal24 = (vals.tcwsalt24 + vals.tcwsltlt24 + vals.tcysalt24 + vals.tcysltlt24 + 
                            vals.tccmalt24 + vals.tccmltlt1_24 + vals.tccmltlt2_24 + vals.tccmltlt3_24 +
                                vals.tcsmalt24 + vals.tcsmltlt1_24 + vals.tcsmltlt2_24)

        vals.niecmaht15 = float(request.POST['niecmaht15'])
        vals.niecmalt15 = float(request.POST['niecmalt15'])
        vals.niecmltht1_15 = float(request.POST['niecmltht1_15'])
        vals.niecmltht2_15 = float(request.POST['niecmltht2_15'])
        vals.niecmltht3_15 = float(request.POST['niecmltht3_15'])
        vals.niecmltlt15 = float(request.POST['niecmltlt15'])
        vals.niesmaht15 = float(request.POST['niesmaht15'])
        vals.niesmltht1_15 = float(request.POST['niesmltht1_15'])
        vals.niesmltht2_15 = float(request.POST['niesmltht2_15'])
        vals.niemtotal15 = (vals.niecmaht15 + vals.niecmalt15 + vals.niecmltht1_15 + vals.niecmltht2_15 + vals.niecmltht3_15 + 
                                vals.niecmltlt15 + vals.niesmaht15 + vals.niesmltht1_15 + vals.niesmltht2_15)
        vals.nielslt15 = float(request.POST['nielslt15'])
        vals.niewsaht15 = float(request.POST['niewsaht15'])
        vals.niewsalt15 = float(request.POST['niewsalt15'])
        vals.niewsltht15 = float(request.POST['niewsltht15'])
        vals.niewsltlt15 = float(request.POST['niewsltlt15'])
        vals.nieysaht15 = float(request.POST['nieysaht15'])
        vals.nieysalt15 = float(request.POST['nieysalt15'])
        vals.nieysltht15 = float(request.POST['nieysltht15'])
        vals.nieysltlt15 = float(request.POST['nieysltlt15'])
        vals.niestotal15 = (vals.nielslt15 + vals.niewsaht15 + vals.niewsalt15 + vals.niewsltht15 + vals.niewsltlt15 +
                               vals.nieysalt15 +  vals.nieysltht15 + vals.nieysltlt15)
        vals.nietotal15 = vals.niemtotal15 + vals.niestotal15

        vals.niecmaht16 = float(request.POST['niecmaht16'])
        vals.niecmalt16 = float(request.POST['niecmalt16'])
        vals.niecmltht1_16 = float(request.POST['niecmltht1_16'])
        vals.niecmltht2_16 = float(request.POST['niecmltht2_16'])
        vals.niecmltht3_16 = float(request.POST['niecmltht3_16'])
        vals.niecmltlt16 = float(request.POST['niecmltlt16'])
        vals.niesmaht16 = float(request.POST['niesmaht16'])
        vals.niesmltht1_16 = float(request.POST['niesmltht1_16'])
        vals.niesmltht2_16 = float(request.POST['niesmltht2_16'])
        vals.niemtotal16 = (vals.niecmaht16 + vals.niecmalt16 + vals.niecmltht1_16 + vals.niecmltht2_16 + vals.niecmltht3_16 + 
                                vals.niecmltlt16 + vals.niesmaht16 + vals.niesmltht1_16 + vals.niesmltht2_16)
        vals.nielslt16 = float(request.POST['nielslt16'])
        vals.niewsaht16 = float(request.POST['niewsaht16'])
        vals.niewsalt16 = float(request.POST['niewsalt16'])
        vals.niewsltht16 = float(request.POST['niewsltht16'])
        vals.niewsltlt16 = float(request.POST['niewsltlt16'])
        vals.nieysaht16 = float(request.POST['nieysaht16'])
        vals.nieysalt16 = float(request.POST['nieysalt16'])
        vals.nieysltht16 = float(request.POST['nieysltht16'])
        vals.nieysltlt16 = float(request.POST['nieysltlt16'])
        vals.niestotal16 = (vals.nielslt16 + vals.niewsaht16 + vals.niewsalt16 + vals.niewsltht16 + vals.niewsltlt16 +
                               vals.nieysalt16 +  vals.nieysltht16 + vals.nieysltlt16 )
        vals.nietotal16 = vals.niemtotal16 + vals.niestotal16
        
        vals.niecmaht17 = float(request.POST['niecmaht17'])
        vals.niecmalt17 = float(request.POST['niecmalt17'])
        vals.niecmltht1_17 = float(request.POST['niecmltht1_17'])
        vals.niecmltht2_17 = float(request.POST['niecmltht2_17'])
        vals.niecmltht3_17 = float(request.POST['niecmltht3_17'])
        vals.niecmltlt17 = float(request.POST['niecmltlt17'])
        vals.niesmaht17 = float(request.POST['niesmaht17'])
        vals.niesmltht1_17 = float(request.POST['niesmltht1_17'])
        vals.niesmltht2_17 = float(request.POST['niesmltht2_17'])
        vals.niemtotal17 = (vals.niecmaht17 + vals.niecmalt17 + vals.niecmltht1_17 + vals.niecmltht2_17 + vals.niecmltht3_17 + 
                                vals.niecmltlt17 + vals.niesmaht17 + vals.niesmltht1_17 + vals.niesmltht2_17)
        vals.nielslt17 = float(request.POST['nielslt17'])
        vals.niewsaht17 = float(request.POST['niewsaht17'])
        vals.niewsalt17 = float(request.POST['niewsalt17'])
        vals.niewsltht17 = float(request.POST['niewsltht17'])
        vals.niewsltlt17 = float(request.POST['niewsltlt17'])
        vals.nieysaht17 = float(request.POST['nieysaht17'])
        vals.nieysalt17 = float(request.POST['nieysalt17'])
        vals.nieysltht17 = float(request.POST['nieysltht17'])
        vals.nieysltlt17 = float(request.POST['nieysltlt17'])
        vals.niestotal17 = (vals.nielslt17 + vals.niewsaht17 + vals.niewsalt17 + vals.niewsltht17 + vals.niewsltlt17 +
                               vals.nieysalt17 +  vals.nieysltht17 + vals.nieysltlt17)
        vals.nietotal17 = vals.niemtotal17 + vals.niestotal17
        
        vals.niecmaht18 = float(request.POST['niecmaht18'])
        vals.niecmalt18 = float(request.POST['niecmalt18'])
        vals.niecmltht1_18 = float(request.POST['niecmltht1_18'])
        vals.niecmltht2_18 = float(request.POST['niecmltht2_18'])
        vals.niecmltht3_18 = float(request.POST['niecmltht3_18'])
        vals.niecmltlt18 = float(request.POST['niecmltlt18'])
        vals.niesmaht18 = float(request.POST['niesmaht18'])
        vals.niesmltht1_18 = float(request.POST['niesmltht1_18'])
        vals.niesmltht2_18 = float(request.POST['niesmltht2_18'])
        vals.niemtotal18 = (vals.niecmaht18 + vals.niecmalt18 + vals.niecmltht1_18 + vals.niecmltht2_18 + vals.niecmltht3_18 + 
                                vals.niecmltlt18 + vals.niesmaht18 + vals.niesmltht1_18 + vals.niesmltht2_18)
        vals.nielslt18 = float(request.POST['nielslt18'])
        vals.niewsaht18 = float(request.POST['niewsaht18'])
        vals.niewsalt18 = float(request.POST['niewsalt18'])
        vals.niewsltht18 = float(request.POST['niewsltht18'])
        vals.niewsltlt18 = float(request.POST['niewsltlt18'])
        vals.nieysaht18 = float(request.POST['nieysaht18'])
        vals.nieysalt18 = float(request.POST['nieysalt18'])
        vals.nieysltht18 = float(request.POST['nieysltht18'])
        vals.nieysltlt18 = float(request.POST['nieysltlt18'])
        vals.niestotal18 = (vals.nielslt18 + vals.niewsaht18 + vals.niewsalt18 + vals.niewsltht18 + vals.niewsltlt18 +
                               vals.nieysalt18 +  vals.nieysltht18 + vals.nieysltlt18)
        vals.nietotal18 = vals.niemtotal18 + vals.niestotal18
        
        vals.niecmaht19 = float(request.POST['niecmaht19'])
        vals.niecmalt19 = float(request.POST['niecmalt19'])
        vals.niecmltht1_19 = float(request.POST['niecmltht1_19'])
        vals.niecmltht2_19 = float(request.POST['niecmltht2_19'])
        vals.niecmltht3_19 = float(request.POST['niecmltht3_19'])
        vals.niecmltlt19 = float(request.POST['niecmltlt19'])
        vals.niesmaht19 = float(request.POST['niesmaht19'])
        vals.niesmltht1_19 = float(request.POST['niesmltht1_19'])
        vals.niesmltht2_19 = float(request.POST['niesmltht2_19'])
        vals.niemtotal19 = (vals.niecmaht19 + vals.niecmalt19 + vals.niecmltht1_19 + vals.niecmltht2_19 + vals.niecmltht3_19 + 
                                vals.niecmltlt19 + vals.niesmaht19 + vals.niesmltht1_19 + vals.niesmltht2_19)
        vals.nielslt19 = float(request.POST['nielslt19'])
        vals.niewsaht19 = float(request.POST['niewsaht19'])
        vals.niewsalt19 = float(request.POST['niewsalt19'])
        vals.niewsltht19 = float(request.POST['niewsltht19'])
        vals.niewsltlt19 = float(request.POST['niewsltlt19'])
        vals.nieysaht19 = float(request.POST['nieysaht19'])
        vals.nieysalt19 = float(request.POST['nieysalt19'])
        vals.nieysltht19 = float(request.POST['nieysltht19'])
        vals.nieysltlt19 = float(request.POST['nieysltlt19'])
        vals.niestotal19 = (vals.nielslt19 + vals.niewsaht19 + vals.niewsalt19 + vals.niewsltht19 + vals.niewsltlt19 +
                               vals.nieysalt19 +  vals.nieysltht19 + vals.nieysltlt19)
        vals.nietotal19 = vals.niemtotal19 + vals.niestotal19
        
        vals.niecmaht20 = float(request.POST['niecmaht20'])
        vals.niecmalt20 = float(request.POST['niecmalt20'])
        vals.niecmltht1_20 = float(request.POST['niecmltht1_20'])
        vals.niecmltht2_20 = float(request.POST['niecmltht2_20'])
        vals.niecmltht3_20 = float(request.POST['niecmltht3_20'])
        vals.niecmltlt20 = float(request.POST['niecmltlt20'])
        vals.niesmaht20 = float(request.POST['niesmaht20'])
        vals.niesmltht1_20 = float(request.POST['niesmltht1_20'])
        vals.niesmltht2_20 = float(request.POST['niesmltht2_20'])
        vals.niemtotal20 = (vals.niecmaht20 + vals.niecmalt20 + vals.niecmltht1_20 + vals.niecmltht2_20 + vals.niecmltht3_20 + 
                                vals.niecmltlt20 + vals.niesmaht20 + vals.niesmltht1_20 + vals.niesmltht2_20)
        vals.nielslt20 = float(request.POST['nielslt20'])
        vals.niewsaht20 = float(request.POST['niewsaht20'])
        vals.niewsalt20 = float(request.POST['niewsalt20'])
        vals.niewsltht20 = float(request.POST['niewsltht20'])
        vals.niewsltlt20 = float(request.POST['niewsltlt20'])
        vals.nieysaht20 = float(request.POST['nieysaht20'])
        vals.nieysalt20 = float(request.POST['nieysalt20'])
        vals.nieysltht20 = float(request.POST['nieysltht20'])
        vals.nieysltlt20 = float(request.POST['nieysltlt20'])
        vals.niestotal20 = (vals.nielslt20 + vals.niewsaht20 + vals.niewsalt20 + vals.niewsltht20 + vals.niewsltlt20 +
                               vals.nieysalt20 +  vals.nieysltht20 + vals.nieysltlt20)
        vals.nietotal20 = vals.niemtotal20 + vals.niestotal20
        
        vals.niecmaht21 = float(request.POST['niecmaht21'])
        vals.niecmalt21 = float(request.POST['niecmalt21'])
        vals.niecmltht1_21 = float(request.POST['niecmltht1_21'])
        vals.niecmltht2_21 = float(request.POST['niecmltht2_21'])
        vals.niecmltht3_21 = float(request.POST['niecmltht3_21'])
        vals.niecmltlt21 = float(request.POST['niecmltlt21'])
        vals.niesmaht21 = float(request.POST['niesmaht21'])
        vals.niesmltht1_21 = float(request.POST['niesmltht1_21'])
        vals.niesmltht2_21 = float(request.POST['niesmltht2_21'])
        vals.niemtotal21 = (vals.niecmaht21 + vals.niecmalt21 + vals.niecmltht1_21 + vals.niecmltht2_21 + vals.niecmltht3_21 + 
                                vals.niecmltlt21 + vals.niesmaht21 + vals.niesmltht1_21 + vals.niesmltht2_21)
        vals.nielslt21 = float(request.POST['nielslt21'])
        vals.niewsaht21 = float(request.POST['niewsaht21'])
        vals.niewsalt21 = float(request.POST['niewsalt21'])
        vals.niewsltht21 = float(request.POST['niewsltht21'])
        vals.niewsltlt21 = float(request.POST['niewsltlt21'])
        vals.nieysaht21 = float(request.POST['nieysaht21'])
        vals.nieysalt21 = float(request.POST['nieysalt21'])
        vals.nieysltht21 = float(request.POST['nieysltht21'])
        vals.nieysltlt21 = float(request.POST['nieysltlt21'])
        vals.niestotal21 = (vals.nielslt21 + vals.niewsaht21 + vals.niewsalt21 + vals.niewsltht21 + vals.niewsltlt21 +
                               vals.nieysalt21 +  vals.nieysltht21 + vals.nieysltlt21)
        vals.nietotal21 = vals.niemtotal21 + vals.niestotal21
        
        vals.niecmaht22 = float(request.POST['niecmaht22'])
        vals.niecmalt22 = float(request.POST['niecmalt22'])
        vals.niecmltht1_22 = float(request.POST['niecmltht1_22'])
        vals.niecmltht2_22 = float(request.POST['niecmltht2_22'])
        vals.niecmltht3_22 = float(request.POST['niecmltht3_22'])
        vals.niecmltlt22 = float(request.POST['niecmltlt22'])
        vals.niesmaht22 = float(request.POST['niesmaht22'])
        vals.niesmltht1_22 = float(request.POST['niesmltht1_22'])
        vals.niesmltht2_22 = float(request.POST['niesmltht2_22'])
        vals.niemtotal22 = (vals.niecmaht22 + vals.niecmalt22 + vals.niecmltht1_22 + vals.niecmltht2_22 + vals.niecmltht3_22 + 
                                vals.niecmltlt22 + vals.niesmaht22 + vals.niesmltht1_22 + vals.niesmltht2_22)
        vals.nielslt22 = float(request.POST['nielslt22'])
        vals.niewsaht22 = float(request.POST['niewsaht22'])
        vals.niewsalt22 = float(request.POST['niewsalt22'])
        vals.niewsltht22 = float(request.POST['niewsltht22'])
        vals.niewsltlt22 = float(request.POST['niewsltlt22'])
        vals.nieysaht22 = float(request.POST['nieysaht22'])
        vals.nieysalt22 = float(request.POST['nieysalt22'])
        vals.nieysltht22 = float(request.POST['nieysltht22'])
        vals.nieysltlt22 = float(request.POST['nieysltlt22'])
        vals.niestotal22 = (vals.nielslt22 + vals.niewsaht22 + vals.niewsalt22 + vals.niewsltht22 + vals.niewsltlt22 +
                               vals.nieysalt22 +  vals.nieysltht22 + vals.nieysltlt22)
        vals.nietotal22 = vals.niemtotal22 + vals.niestotal22
        
        vals.niecmaht23 = float(request.POST['niecmaht23'])
        vals.niecmalt23 = float(request.POST['niecmalt23'])
        vals.niecmltht1_23 = float(request.POST['niecmltht1_23'])
        vals.niecmltht2_23 = float(request.POST['niecmltht2_23'])
        vals.niecmltht3_23 = float(request.POST['niecmltht3_23'])
        vals.niecmltlt23 = float(request.POST['niecmltlt23'])
        vals.niesmaht23 = float(request.POST['niesmaht23'])
        vals.niesmltht1_23 = float(request.POST['niesmltht1_23'])
        vals.niesmltht2_23 = float(request.POST['niesmltht2_23'])
        vals.niemtotal23 = (vals.niecmaht23 + vals.niecmalt23 + vals.niecmltht1_23 + vals.niecmltht2_23 + vals.niecmltht3_23 + 
                                vals.niecmltlt23 + vals.niesmaht23 + vals.niesmltht1_23 + vals.niesmltht2_23)
        vals.nielslt23 = float(request.POST['nielslt23'])
        vals.niewsaht23 = float(request.POST['niewsaht23'])
        vals.niewsalt23 = float(request.POST['niewsalt23'])
        vals.niewsltht23 = float(request.POST['niewsltht23'])
        vals.niewsltlt23 = float(request.POST['niewsltlt23'])
        vals.nieysaht23 = float(request.POST['nieysaht23'])
        vals.nieysalt23 = float(request.POST['nieysalt23'])
        vals.nieysltht23 = float(request.POST['nieysltht23'])
        vals.nieysltlt23 = float(request.POST['nieysltlt23'])
        vals.niestotal23 = (vals.nielslt23 + vals.niewsaht23 + vals.niewsalt23 + vals.niewsltht23 + vals.niewsltlt23 +
                               vals.nieysalt23 +  vals.nieysltht23 + vals.nieysltlt23)
        vals.nietotal23 = vals.niemtotal23 + vals.niestotal23
        
        vals.niecmaht24 = float(request.POST['niecmaht24'])
        vals.niecmalt24 = float(request.POST['niecmalt24'])
        vals.niecmltht1_24 = float(request.POST['niecmltht1_24'])
        vals.niecmltht2_24 = float(request.POST['niecmltht2_24'])
        vals.niecmltht3_24 = float(request.POST['niecmltht3_24'])
        vals.niecmltlt24 = float(request.POST['niecmltlt24'])
        vals.niesmaht24 = float(request.POST['niesmaht24'])
        vals.niesmltht1_24 = float(request.POST['niesmltht1_24'])
        vals.niesmltht2_24 = float(request.POST['niesmltht2_24'])
        vals.niemtotal24 = (vals.niecmaht24 + vals.niecmalt24 + vals.niecmltht1_24 + vals.niecmltht2_24 + vals.niecmltht3_24 + 
                                vals.niecmltlt24 + vals.niesmaht24 + vals.niesmltht1_24 + vals.niesmltht2_24)
        vals.nielslt24 = float(request.POST['nielslt24'])
        vals.niewsaht24 = float(request.POST['niewsaht24'])
        vals.niewsalt24 = float(request.POST['niewsalt24'])
        vals.niewsltht24 = float(request.POST['niewsltht24'])
        vals.niewsltlt24 = float(request.POST['niewsltlt24'])
        vals.nieysaht24 = float(request.POST['nieysaht24'])
        vals.nieysalt24 = float(request.POST['nieysalt24'])
        vals.nieysltht24 = float(request.POST['nieysltht24'])
        vals.nieysltlt24 = float(request.POST['nieysltlt24'])
        vals.niestotal24 = (vals.nielslt24 + vals.niewsaht24 + vals.niewsalt24 + vals.niewsltht24 + vals.niewsltlt24 +
                               vals.nieysalt24 +  vals.nieysltht24 + vals.nieysltlt24)
        vals.nietotal24 = vals.niemtotal24 + vals.niestotal24

        vals.total15 = vals.nietotal15 + vals.ietotal15 + vals.totalsc15
        vals.total16 = vals.nietotal16 + vals.ietotal16 + vals.totalsc16
        vals.total17 = vals.nietotal17 + vals.ietotal17 + vals.totalsc17
        vals.total18 = vals.nietotal18 + vals.ietotal18 + vals.totalsc18
        vals.total19 = vals.nietotal19 + vals.ietotal19 + vals.totalsc19
        vals.total20 = vals.nietotal20 + vals.ietotal20 + vals.totalsc20
        vals.total21 = vals.nietotal21 + vals.ietotal21 + vals.totalsc21
        vals.total22 = vals.nietotal22 + vals.ietotal22 + vals.totalsc22
        vals.total23 = vals.nietotal23 + vals.ietotal23 + vals.totalsc23
        vals.total24 = vals.nietotal24 + vals.ietotal24 + vals.totalsc24

        vals.niws15 = vals.wsaht15 + vals.wsalt15 + vals.wsltht15 + vals.wsltlt15
        vals.niys15 = vals.ysaht15 + vals.ysalt15 + vals.ysltht15 + vals.ysltlt15
        vals.nicm15 = vals.cmaht15 + vals.cmalt15 + vals.cmltht1_15 + vals.cmltht2_15 + vals.cmltht3_15 + vals.cmltlt15
        vals.nism15 = vals.smaht15 + vals.smltht1_15 + vals.smltht2_15
        vals.iws15 = vals.tcwsalt15 + vals.tcwsltlt15
        vals.iys15 = vals.tcysalt15 + vals.tcysltlt15
        vals.icm15 = vals.tccmalt15 + vals.tccmltlt1_15 + vals.tccmltlt2_15 + vals.tccmltlt3_15
        vals.ism15 = vals.tcsmalt15 + vals.tcsmltlt1_15 + vals.tcsmltlt2_15

        vals.niws16 = vals.wsaht16 + vals.wsalt16 + vals.wsltht16 + vals.wsltlt16
        vals.niys16 = vals.ysaht16 + vals.ysalt16 + vals.ysltht16 + vals.ysltlt16
        vals.nicm16 = vals.cmaht16 + vals.cmalt16 + vals.cmltht1_16 + vals.cmltht2_16 + vals.cmltht3_16 + vals.cmltlt16
        vals.nism16 = vals.smaht16 + vals.smltht1_16 + vals.smltht2_16
        vals.iws16 = vals.tcwsalt16 + vals.tcwsltlt16
        vals.iys16 = vals.tcysalt16 + vals.tcysltlt16
        vals.icm16 = vals.tccmalt16 + vals.tccmltlt1_16 + vals.tccmltlt2_16 + vals.tccmltlt3_16
        vals.ism16 = vals.tcsmalt16 + vals.tcsmltlt1_16 + vals.tcsmltlt2_16
        
        vals.niws17 = vals.wsaht17 + vals.wsalt17 + vals.wsltht17 + vals.wsltlt17
        vals.niys17 = vals.ysaht17 + vals.ysalt17 + vals.ysltht17 + vals.ysltlt17
        vals.nicm17 = vals.cmaht17 + vals.cmalt17 + vals.cmltht1_17 + vals.cmltht2_17 + vals.cmltht3_17 + vals.cmltlt17
        vals.nism17 = vals.smaht17 + vals.smltht1_17 + vals.smltht2_17
        vals.iws17 = vals.tcwsalt17 + vals.tcwsltlt17
        vals.iys17 = vals.tcysalt17 + vals.tcysltlt17
        vals.icm17 = vals.tccmalt17 + vals.tccmltlt1_17 + vals.tccmltlt2_17 + vals.tccmltlt3_17
        vals.ism17 = vals.tcsmalt17 + vals.tcsmltlt1_17 + vals.tcsmltlt2_17
        
        vals.niws18 = vals.wsaht18 + vals.wsalt18 + vals.wsltht18 + vals.wsltlt18
        vals.niys18 = vals.ysaht18 + vals.ysalt18 + vals.ysltht18 + vals.ysltlt18
        vals.nicm18 = vals.cmaht18 + vals.cmalt18 + vals.cmltht1_18 + vals.cmltht2_18 + vals.cmltht3_18 + vals.cmltlt18
        vals.nism18 = vals.smaht18 + vals.smltht1_18 + vals.smltht2_18
        vals.iws18 = vals.tcwsalt18 + vals.tcwsltlt18
        vals.iys18 = vals.tcysalt18 + vals.tcysltlt18
        vals.icm18 = vals.tccmalt18 + vals.tccmltlt1_18 + vals.tccmltlt2_18 + vals.tccmltlt3_18
        vals.ism18 = vals.tcsmalt18 + vals.tcsmltlt1_18 + vals.tcsmltlt2_18
        
        vals.niws19 = vals.wsaht19 + vals.wsalt19 + vals.wsltht19 + vals.wsltlt19   
        vals.niys19 = vals.ysaht19 + vals.ysalt19 + vals.ysltht19 + vals.ysltlt19
        vals.nicm19 = vals.cmaht19 + vals.cmalt19 + vals.cmltht1_19 + vals.cmltht2_19 + vals.cmltht3_19 + vals.cmltlt19
        vals.nism19 = vals.smaht19 + vals.smltht1_19 + vals.smltht2_19
        vals.iws19 = vals.tcwsalt19 + vals.tcwsltlt19
        vals.iys19 = vals.tcysalt19 + vals.tcysltlt19
        vals.icm19 = vals.tccmalt19 + vals.tccmltlt1_19 + vals.tccmltlt2_19 + vals.tccmltlt3_19
        vals.ism19 = vals.tcsmalt19 + vals.tcsmltlt1_19 + vals.tcsmltlt2_19
        
        vals.niws20 = vals.wsaht20 + vals.wsalt20 + vals.wsltht20 + vals.wsltlt20
        vals.niys20 = vals.ysaht20 + vals.ysalt20 + vals.ysltht20 + vals.ysltlt20
        vals.nicm20 = vals.cmaht20 + vals.cmalt20 + vals.cmltht1_20 + vals.cmltht2_20 + vals.cmltht3_20 + vals.cmltlt20
        vals.nism20 = vals.smaht20 + vals.smltht1_20 + vals.smltht2_20
        vals.iws20 = vals.tcwsalt20 + vals.tcwsltlt20
        vals.iys20 = vals.tcysalt20 + vals.tcysltlt20
        vals.icm20 = vals.tccmalt20 + vals.tccmltlt1_20 + vals.tccmltlt2_20 + vals.tccmltlt3_20
        vals.ism20 = vals.tcsmalt20 + vals.tcsmltlt1_20 + vals.tcsmltlt2_20
        
        vals.niws21 = vals.wsaht21 + vals.wsalt21 + vals.wsltht21 + vals.wsltlt21
        vals.niys21 = vals.ysaht21 + vals.ysalt21 + vals.ysltht21 + vals.ysltlt21
        vals.nicm21 = vals.cmaht21 + vals.cmalt21 + vals.cmltht1_21 + vals.cmltht2_21 + vals.cmltht3_21 + vals.cmltlt21
        vals.nism21 = vals.smaht21 + vals.smltht1_21 + vals.smltht2_21
        vals.iws21 = vals.tcwsalt21 + vals.tcwsltlt21
        vals.iys21 = vals.tcysalt21 + vals.tcysltlt21
        vals.icm21 = vals.tccmalt21 + vals.tccmltlt1_21 + vals.tccmltlt2_21 + vals.tccmltlt3_21
        vals.ism21 = vals.tcsmalt21 + vals.tcsmltlt1_21 + vals.tcsmltlt2_21
        
        vals.niws22 = vals.wsaht22 + vals.wsalt22 + vals.wsltht22 + vals.wsltlt22
        vals.niys22 = vals.ysaht22 + vals.ysalt22 + vals.ysltht22 + vals.ysltlt22
        vals.nicm22 = vals.cmaht22 + vals.cmalt22 + vals.cmltht1_22 + vals.cmltht2_22 + vals.cmltht3_22 + vals.cmltlt22
        vals.nism22 = vals.smaht22 + vals.smltht1_22 + vals.smltht2_22
        vals.iws22 = vals.tcwsalt22 + vals.tcwsltlt22
        vals.iys22 = vals.tcysalt22 + vals.tcysltlt22
        vals.icm22 = vals.tccmalt22 + vals.tccmltlt1_22 + vals.tccmltlt2_22 + vals.tccmltlt3_22
        vals.ism22 = vals.tcsmalt22 + vals.tcsmltlt1_22 + vals.tcsmltlt2_22

        vals.niws23 = vals.wsaht23 + vals.wsalt23 + vals.wsltht23 + vals.wsltlt23
        vals.niys23 = vals.ysaht23 + vals.ysalt23 + vals.ysltht23 + vals.ysltlt23
        vals.nicm23 = vals.cmaht23 + vals.cmalt23 + vals.cmltht1_23 + vals.cmltht2_23 + vals.cmltht3_23 + vals.cmltlt23
        vals.nism23 = vals.smaht23 + vals.smltht1_23 + vals.smltht2_23
        vals.iws23 = vals.tcwsalt23 + vals.tcwsltlt23
        vals.iys23 = vals.tcysalt23 + vals.tcysltlt23
        vals.icm23 = vals.tccmalt23 + vals.tccmltlt1_23 + vals.tccmltlt2_23 + vals.tccmltlt3_23
        vals.ism23 = vals.tcsmalt23 + vals.tcsmltlt1_23 + vals.tcsmltlt2_23
        
        vals.niws24 = vals.wsaht24 + vals.wsalt24 + vals.wsltht24 + vals.wsltlt24
        vals.niys24 = vals.ysaht24 + vals.ysalt24 + vals.ysltht24 + vals.ysltlt24
        vals.nicm24 = vals.cmaht24 + vals.cmalt24 + vals.cmltht1_24 + vals.cmltht2_24 + vals.cmltht3_24 + vals.cmltlt24
        vals.nism24 = vals.smaht24 + vals.smltht1_24 + vals.smltht2_24
        vals.iws24 = vals.tcwsalt24 + vals.tcwsltlt24
        vals.iys24 = vals.tcysalt24 + vals.tcysltlt24
        vals.icm24 = vals.tccmalt24 + vals.tccmltlt1_24 + vals.tccmltlt2_24 + vals.tccmltlt3_24
        vals.ism24 = vals.tcsmalt24 + vals.tcsmltlt1_24 + vals.tcsmltlt2_24

        vals.total15 = (vals.lslt15 + vals.niws15 + vals.niys15 + vals.nicm15 + vals.nism15 +
                        vals.iws15 + vals.iys15 + vals.icm15 + vals.ism15) 
        vals.total16 = (vals.lslt16 + vals.niws16 + vals.niys16 + vals.nicm16 + vals.nism16 +
                        vals.iws16 + vals.iys16 + vals.icm16 + vals.ism16)                
        vals.total17 = (vals.lslt17 + vals.niws17 + vals.niys17 + vals.nicm17 + vals.nism17 +
                                vals.iws17 + vals.iys17 + vals.icm17 + vals.ism17)                               
        vals.total18 = (vals.lslt18 + vals.niws18 + vals.niys18 + vals.nicm18 + vals.nism18 +
                                vals.iws18 + vals.iys18 + vals.icm18 + vals.ism18)                                
        vals.total19 = (vals.lslt19 + vals.niws19 + vals.niys19 + vals.nicm19 + vals.nism19 +
                                vals.iws19 + vals.iys19 + vals.icm19 + vals.ism19)                                                       
        vals.total20 = (vals.lslt20 + vals.niws20 + vals.niys20 + vals.nicm20 + vals.nism20 +
                                vals.iws20 + vals.iys20 + vals.icm20 + vals.ism20)                                                        
        vals.total21 = (vals.lslt21 + vals.niws21 + vals.niys21 + vals.nicm21 + vals.nism21 +
                                vals.iws21 + vals.iys21 + vals.icm21 + vals.ism21)                                 
        vals.total22 = (vals.lslt22 + vals.niws22 + vals.niys22 + vals.nicm22 + vals.nism22 +
                                vals.iws22 + vals.iys22 + vals.icm22 + vals.ism22)                         
        vals.total23 = (vals.lslt23 + vals.niws23 + vals.niys23 + vals.nicm23 + vals.nism23 +
                                vals.iws23 + vals.iys23 + vals.icm23 + vals.ism23)                                
        vals.total24 = (vals.lslt24 + vals.niws24 + vals.niys24 + vals.nicm24 + vals.nism24 +
                                vals.iws24 + vals.iys24 + vals.icm24 + vals.ism24)   

         # volume summary starts here
        vals2.nils15 = vals.nielslt15 + vals.lslt15
        vals2.niwsa15 = vals.wsaht15 + vals.wsalt15 + vals.niewsaht15 + vals.niewsalt15
        vals2.niwslt15 = vals.wsltht15 + vals.wsltlt15 + vals.niewsltht15 + vals.niewsltlt15
        vals2.niysa15 = vals.ysaht15 + vals.ysalt15 + vals.nieysaht15 + vals.nieysalt15
        vals2.niyslt15 = vals.ysltht15 + vals.ysltlt15 + vals.nieysltht15 + vals.nieysltlt15
        vals2.nicma15 = vals.cmaht15 + vals.cmalt15 + vals.niecmaht15 + vals.niecmalt15
        vals2.nicmlt15 = (vals.cmltht1_15 + vals.cmltht2_15 + vals.cmltht3_15 + vals.cmltlt15 + 
                            vals.niecmltht1_15 + vals.niecmltht2_15 + vals.niecmltht3_15 + vals.niecmltlt15)
        vals2.nisma15 = vals.smaht15 + vals.niesmaht15
        vals2.nismlt15 = vals.smltht1_15 + vals.smltht2_15 + vals.niesmltht1_15 + vals.niesmltht2_15
        vals2.icmlt15 = vals.tccmltlt1_15 + vals.tccmltlt2_15 + vals.tccmltlt3_15
        vals2.ismlt15 = vals.tcsmltlt1_15 + vals.tcsmltlt2_15
        vals2.vstotal1_15 = (vals2.nils15 + vals2.niwsa15 + vals2.niwslt15 + vals2.niysa15 + vals2.niyslt15 + vals2.nicma15 +
                                vals2.nicmlt15 + vals2.nisma15 + vals2.nismlt15 + vals2.icmlt15 + vals2.ismlt15 + vals.tcwsalt15 +
                                    vals.tcwsltlt15 + vals.tcysalt15 + vals.tcysltlt15 + vals.tccmalt15 + vals.tcsmalt15)
        vals2.niws15 = vals2.niwsa15 + vals2.niwslt15 
        vals2.niys15 = vals2.niysa15 + vals2.niyslt15
        vals2.nicm15 = vals2.nicma15 + vals2.nicmlt15
        vals2.nism15 = vals2.nisma15 + vals2.nismlt15
        vals2.iws15 = vals.tcwsalt15 + vals.tcwsltlt15
        vals2.iys15 = vals.tcysalt15 + vals.tcysltlt15
        vals2.icm15 = vals2.icmlt15 + vals.tccmalt15
        vals2.ism15 = vals2.ismlt15 + vals.tcsmalt15
        vals2.ltls15 = float(request.POST['ltls15'])
        vals2.ltwsa15 = float(request.POST['ltwsa15'])
        vals2.ltwslt15 = float(request.POST['ltwslt15'])
        vals2.ltysa15 = float(request.POST['ltysa15'])
        vals2.ltyslt15 = float(request.POST['ltyslt15'])
        vals2.htwsa15 = float(request.POST['htwsa15'])
        vals2.htwslt15 = float(request.POST['htwslt15'])
        vals2.htysa15 = float(request.POST['htysa15'])
        vals2.htyslt15 = float(request.POST['htyslt15'])
        vals2.ws15 = vals2.ltwsa15 + vals2.ltwslt15 + vals2.htwsa15 + vals2.htwslt15
        vals2.ys15 = vals2.ltysa15 + vals2.ltyslt15 + vals2.htysa15 + vals2.htyslt15
        vals2.vstotal2_15 = vals2.ltls15 + vals2.ws15 + vals2.ys15
        vals2.macdtc15 = float(request.POST['macdtc15'])
        vals2.cts15 = float(request.POST['cts15'])
        vals2.ctc15 = vals2.macdtc15 * vals2.cts15/100

        vals2.nils16 = vals.nielslt16 + vals.lslt16
        vals2.niwsa16 = vals.wsaht16 + vals.wsalt16 + vals.niewsaht16 + vals.niewsalt16
        vals2.niwslt16 = vals.wsltht16 + vals.wsltlt16 + vals.niewsltht16 + vals.niewsltlt16
        vals2.niysa16 = vals.ysaht16 + vals.ysalt16 + vals.nieysaht16 + vals.nieysalt16
        vals2.niyslt16 = vals.ysltht16 + vals.ysltlt16 + vals.nieysltht16 + vals.nieysltlt16
        vals2.nicma16 = vals.cmaht16 + vals.cmalt16 + vals.niecmaht16 + vals.niecmalt16
        vals2.nicmlt16 = (vals.cmltht1_16 + vals.cmltht2_16 + vals.cmltht3_16 + vals.cmltlt16 + 
                            vals.niecmltht1_16 + vals.niecmltht2_16 + vals.niecmltht3_16 + vals.niecmltlt16)
        vals2.nisma16 = vals.smaht16 + vals.niesmaht16
        vals2.nismlt16 = vals.smltht1_16 + vals.smltht2_16 + vals.niesmltht1_16 + vals.niesmltht2_16
        vals2.icmlt16 = vals.tccmltlt1_16 + vals.tccmltlt2_16 + vals.tccmltlt3_16
        vals2.ismlt16 = vals.tcsmltlt1_16 + vals.tcsmltlt2_16
        vals2.vstotal1_16 = (vals2.nils16 + vals2.niwsa16 + vals2.niwslt16 + vals2.niysa16 + vals2.niyslt16 + vals2.nicma16 +
                                vals2.nicmlt16 + vals2.nisma16 + vals2.nismlt16 + vals2.icmlt16 + vals2.ismlt16 + vals.tcwsalt16 +
                                    vals.tcwsltlt16 + vals.tcysalt16 + vals.tcysltlt16 + vals.tccmalt16 + vals.tcsmalt16)
        vals2.niws16 = vals2.niwsa16 + vals2.niwslt16 
        vals2.niys16 = vals2.niysa16 + vals2.niyslt16
        vals2.nicm16 = vals2.nicma16 + vals2.nicmlt16
        vals2.nism16 = vals2.nisma16 + vals2.nismlt16
        vals2.iws16 = vals.tcwsalt16 + vals.tcwsltlt16
        vals2.iys16 = vals.tcysalt16 + vals.tcysltlt16
        vals2.icm16 = vals2.icmlt16 + vals.tccmalt16
        vals2.ism16 = vals2.ismlt16 + vals.tcsmalt16
        vals2.ltls16 = float(request.POST['ltls16'])
        vals2.ltwsa16 = float(request.POST['ltwsa16'])
        vals2.ltwslt16 = float(request.POST['ltwslt16'])
        vals2.ltysa16 = float(request.POST['ltysa16'])
        vals2.ltyslt16 = float(request.POST['ltyslt16'])
        vals2.htwsa16 = float(request.POST['htwsa16'])
        vals2.htwslt16 = float(request.POST['htwslt16'])
        vals2.htysa16 = float(request.POST['htysa16'])
        vals2.htyslt16 = float(request.POST['htyslt16'])
        vals2.ws16 = vals2.ltwsa16 + vals2.ltwslt16 + vals2.htwsa16 + vals2.htwslt16
        vals2.ys16 = vals2.ltysa16 + vals2.ltyslt16 + vals2.htysa16 + vals2.htyslt16
        vals2.vstotal2_16 = vals2.ltls16 + vals2.ws16 + vals2.ys16
        vals2.macdtc16 = float(request.POST['macdtc16'])
        vals2.cts16 = float(request.POST['cts16'])
        vals2.ctc16 = vals2.macdtc16 * vals2.cts16/100
        
        vals2.nils17 = vals.nielslt17 + vals.lslt17
        vals2.niwsa17 = vals.wsaht17 + vals.wsalt17 + vals.niewsaht17 + vals.niewsalt17
        vals2.niwslt17 = vals.wsltht17 + vals.wsltlt17 + vals.niewsltht17 + vals.niewsltlt17
        vals2.niysa17 = vals.ysaht17 + vals.ysalt17 + vals.nieysaht17 + vals.nieysalt17
        vals2.niyslt17 = vals.ysltht17 + vals.ysltlt17 + vals.nieysltht17 + vals.nieysltlt17
        vals2.nicma17 = vals.cmaht17 + vals.cmalt17 + vals.niecmaht17 + vals.niecmalt17
        vals2.nicmlt17 = (vals.cmltht1_17 + vals.cmltht2_17 + vals.cmltht3_17 + vals.cmltlt17 + 
                            vals.niecmltht1_17 + vals.niecmltht2_17 + vals.niecmltht3_17 + vals.niecmltlt17)
        vals2.nisma17 = vals.smaht17 + vals.niesmaht17
        vals2.nismlt17 = vals.smltht1_17 + vals.smltht2_17 + vals.niesmltht1_17 + vals.niesmltht2_17
        vals2.icmlt17 = vals.tccmltlt1_17 + vals.tccmltlt2_17 + vals.tccmltlt3_17
        vals2.ismlt17 = vals.tcsmltlt1_17 + vals.tcsmltlt2_17
        vals2.vstotal1_17 = (vals2.nils17 + vals2.niwsa17 + vals2.niwslt17 + vals2.niysa17 + vals2.niyslt17 + vals2.nicma17 +
                                vals2.nicmlt17 + vals2.nisma17 + vals2.nismlt17 + vals2.icmlt17 + vals2.ismlt17 + vals.tcwsalt17 +
                                    vals.tcwsltlt17 + vals.tcysalt17 + vals.tcysltlt17 + vals.tccmalt17 + vals.tcsmalt17)
        vals2.niws17 = vals2.niwsa17 + vals2.niwslt17 
        vals2.niys17 = vals2.niysa17 + vals2.niyslt17
        vals2.nicm17 = vals2.nicma17 + vals2.nicmlt17
        vals2.nism17 = vals2.nisma17 + vals2.nismlt17
        vals2.iws17 = vals.tcwsalt17 + vals.tcwsltlt17
        vals2.iys17 = vals.tcysalt17 + vals.tcysltlt17
        vals2.icm17 = vals2.icmlt17 + vals.tccmalt17
        vals2.ism17 = vals2.ismlt17 + vals.tcsmalt17
        vals2.ltls17 = float(request.POST['ltls17'])
        vals2.ltwsa17 = float(request.POST['ltwsa17'])
        vals2.ltwslt17 = float(request.POST['ltwslt17'])
        vals2.ltysa17 = float(request.POST['ltysa17'])
        vals2.ltyslt17 = float(request.POST['ltyslt17'])
        vals2.htwsa17 = float(request.POST['htwsa17'])
        vals2.htwslt17 = float(request.POST['htwslt17'])
        vals2.htysa17 = float(request.POST['htysa17'])
        vals2.htyslt17 = float(request.POST['htyslt17'])
        vals2.ws17 = vals2.ltwsa17 + vals2.ltwslt17 + vals2.htwsa17 + vals2.htwslt17
        vals2.ys17 = vals2.ltysa17 + vals2.ltyslt17 + vals2.htysa17 + vals2.htyslt17
        vals2.vstotal2_17 = vals2.ltls17 + vals2.ws17 + vals2.ys17
        vals2.macdtc17 = float(request.POST['macdtc17'])
        vals2.cts17 = float(request.POST['cts17'])
        vals2.ctc17 = vals2.macdtc17 * vals2.cts17/100
        
        vals2.nils18 = vals.nielslt18 + vals.lslt18
        vals2.niwsa18 = vals.wsaht18 + vals.wsalt18 + vals.niewsaht18 + vals.niewsalt18
        vals2.niwslt18 = vals.wsltht18 + vals.wsltlt18 + vals.niewsltht18 + vals.niewsltlt18
        vals2.niysa18 = vals.ysaht18 + vals.ysalt18 + vals.nieysaht18 + vals.nieysalt18
        vals2.niyslt18 = vals.ysltht18 + vals.ysltlt18 + vals.nieysltht18 + vals.nieysltlt18
        vals2.nicma18 = vals.cmaht18 + vals.cmalt18 + vals.niecmaht18 + vals.niecmalt18
        vals2.nicmlt18 = (vals.cmltht1_18 + vals.cmltht2_18 + vals.cmltht3_18 + vals.cmltlt18 + 
                            vals.niecmltht1_18 + vals.niecmltht2_18 + vals.niecmltht3_18 + vals.niecmltlt18)
        vals2.nisma18 = vals.smaht18 + vals.niesmaht18
        vals2.nismlt18 = vals.smltht1_18 + vals.smltht2_18 + vals.niesmltht1_18 + vals.niesmltht2_18
        vals2.icmlt18 = vals.tccmltlt1_18 + vals.tccmltlt2_18 + vals.tccmltlt3_18
        vals2.ismlt18 = vals.tcsmltlt1_18 + vals.tcsmltlt2_18
        vals2.vstotal1_18 = (vals2.nils18 + vals2.niwsa18 + vals2.niwslt18 + vals2.niysa18 + vals2.niyslt18 + vals2.nicma18 +
                                vals2.nicmlt18 + vals2.nisma18 + vals2.nismlt18 + vals2.icmlt18 + vals2.ismlt18 + vals.tcwsalt18 +
                                    vals.tcwsltlt18 + vals.tcysalt18 + vals.tcysltlt18 + vals.tccmalt18 + vals.tcsmalt18)
        vals2.niws18 = vals2.niwsa18 + vals2.niwslt18 
        vals2.niys18 = vals2.niysa18 + vals2.niyslt18
        vals2.nicm18 = vals2.nicma18 + vals2.nicmlt18
        vals2.nism18 = vals2.nisma18 + vals2.nismlt18
        vals2.iws18 = vals.tcwsalt18 + vals.tcwsltlt18
        vals2.iys18 = vals.tcysalt18 + vals.tcysltlt18
        vals2.icm18 = vals2.icmlt18 + vals.tccmalt18
        vals2.ism18 = vals2.ismlt18 + vals.tcsmalt18
        vals2.ltls18 = float(request.POST['ltls18'])
        vals2.ltwsa18 = float(request.POST['ltwsa18'])
        vals2.ltwslt18 = float(request.POST['ltwslt18'])
        vals2.ltysa18 = float(request.POST['ltysa18'])
        vals2.ltyslt18 = float(request.POST['ltyslt18'])
        vals2.htwsa18 = float(request.POST['htwsa18'])
        vals2.htwslt18 = float(request.POST['htwslt18'])
        vals2.htysa18 = float(request.POST['htysa18'])
        vals2.htyslt18 = float(request.POST['htyslt18'])
        vals2.ws18 = vals2.ltwsa18 + vals2.ltwslt18 + vals2.htwsa18 + vals2.htwslt18
        vals2.ys18 = vals2.ltysa18 + vals2.ltyslt18 + vals2.htysa18 + vals2.htyslt18
        vals2.vstotal2_18 = vals2.ltls18 + vals2.ws18 + vals2.ys18
        vals2.macdtc18 = float(request.POST['macdtc18'])
        vals2.cts18 = float(request.POST['cts18'])
        vals2.ctc18 = vals2.macdtc18 * vals2.cts18/100
        
        vals2.nils19 = vals.nielslt19 + vals.lslt19
        vals2.niwsa19 = vals.wsaht19 + vals.wsalt19 + vals.niewsaht19 + vals.niewsalt19
        vals2.niwslt19 = vals.wsltht19 + vals.wsltlt19 + vals.niewsltht19 + vals.niewsltlt19
        vals2.niysa19 = vals.ysaht19 + vals.ysalt19 + vals.nieysaht19 + vals.nieysalt19
        vals2.niyslt19 = vals.ysltht19 + vals.ysltlt19 + vals.nieysltht19 + vals.nieysltlt19
        vals2.nicma19 = vals.cmaht19 + vals.cmalt19 + vals.niecmaht19 + vals.niecmalt19
        vals2.nicmlt19 = (vals.cmltht1_19 + vals.cmltht2_19 + vals.cmltht3_19 + vals.cmltlt19 + 
                            vals.niecmltht1_19 + vals.niecmltht2_19 + vals.niecmltht3_19 + vals.niecmltlt19)
        vals2.nisma19 = vals.smaht19 + vals.niesmaht19
        vals2.nismlt19 = vals.smltht1_19 + vals.smltht2_19 + vals.niesmltht1_19 + vals.niesmltht2_19
        vals2.icmlt19 = vals.tccmltlt1_19 + vals.tccmltlt2_19 + vals.tccmltlt3_19
        vals2.ismlt19 = vals.tcsmltlt1_19 + vals.tcsmltlt2_19
        vals2.vstotal1_19 = (vals2.nils19 + vals2.niwsa19 + vals2.niwslt19 + vals2.niysa19 + vals2.niyslt19 + vals2.nicma19 +
                                vals2.nicmlt19 + vals2.nisma19 + vals2.nismlt19 + vals2.icmlt19 + vals2.ismlt19 + vals.tcwsalt19 +
                                    vals.tcwsltlt19 + vals.tcysalt19 + vals.tcysltlt19 + vals.tccmalt19 + vals.tcsmalt19)
        vals2.niws19 = vals2.niwsa19 + vals2.niwslt19 
        vals2.niys19 = vals2.niysa19 + vals2.niyslt19
        vals2.nicm19 = vals2.nicma19 + vals2.nicmlt19
        vals2.nism19 = vals2.nisma19 + vals2.nismlt19
        vals2.iws19 = vals.tcwsalt19 + vals.tcwsltlt19
        vals2.iys19 = vals.tcysalt19 + vals.tcysltlt19
        vals2.icm19 = vals2.icmlt19 + vals.tccmalt19
        vals2.ism19 = vals2.ismlt19 + vals.tcsmalt19
        vals2.ltls19 = float(request.POST['ltls19'])
        vals2.ltwsa19 = float(request.POST['ltwsa19'])
        vals2.ltwslt19 = float(request.POST['ltwslt19'])
        vals2.ltysa19 = float(request.POST['ltysa19'])
        vals2.ltyslt19 = float(request.POST['ltyslt19'])
        vals2.htwsa19 = float(request.POST['htwsa19'])
        vals2.htwslt19 = float(request.POST['htwslt19'])
        vals2.htysa19 = float(request.POST['htysa19'])
        vals2.htyslt19 = float(request.POST['htyslt19'])
        vals2.ws19 = vals2.ltwsa19 + vals2.ltwslt19 + vals2.htwsa19 + vals2.htwslt19
        vals2.ys19 = vals2.ltysa19 + vals2.ltyslt19 + vals2.htysa19 + vals2.htyslt19
        vals2.vstotal2_19 = vals2.ltls19 + vals2.ws19 + vals2.ys19
        vals2.macdtc19 = float(request.POST['macdtc19'])
        vals2.cts19 = float(request.POST['cts19'])
        vals2.ctc19 = vals2.macdtc19 * vals2.cts19/100
        
        vals2.nils20 = vals.nielslt20 + vals.lslt20
        vals2.niwsa20 = vals.wsaht20 + vals.wsalt20 + vals.niewsaht20 + vals.niewsalt20
        vals2.niwslt20 = vals.wsltht20 + vals.wsltlt20 + vals.niewsltht20 + vals.niewsltlt20
        vals2.niysa20 = vals.ysaht20 + vals.ysalt20 + vals.nieysaht20 + vals.nieysalt20
        vals2.niyslt20 = vals.ysltht20 + vals.ysltlt20 + vals.nieysltht20 + vals.nieysltlt20
        vals2.nicma20 = vals.cmaht20 + vals.cmalt20 + vals.niecmaht20 + vals.niecmalt20
        vals2.nicmlt20 = (vals.cmltht1_20 + vals.cmltht2_20 + vals.cmltht3_20 + vals.cmltlt20 + 
                            vals.niecmltht1_20 + vals.niecmltht2_20 + vals.niecmltht3_20 + vals.niecmltlt20)
        vals2.nisma20 = vals.smaht20 + vals.niesmaht20
        vals2.nismlt20 = vals.smltht1_20 + vals.smltht2_20 + vals.niesmltht1_20 + vals.niesmltht2_20
        vals2.icmlt20 = vals.tccmltlt1_20 + vals.tccmltlt2_20 + vals.tccmltlt3_20
        vals2.ismlt20 = vals.tcsmltlt1_20 + vals.tcsmltlt2_20
        vals2.vstotal1_20 = (vals2.nils20 + vals2.niwsa20 + vals2.niwslt20 + vals2.niysa20 + vals2.niyslt20 + vals2.nicma20 +
                                vals2.nicmlt20 + vals2.nisma20 + vals2.nismlt20 + vals2.icmlt20 + vals2.ismlt20 + vals.tcwsalt20 +
                                    vals.tcwsltlt20 + vals.tcysalt20 + vals.tcysltlt20 + vals.tccmalt20 + vals.tcsmalt20)
        vals2.niws20 = vals2.niwsa20 + vals2.niwslt20 
        vals2.niys20 = vals2.niysa20 + vals2.niyslt20
        vals2.nicm20 = vals2.nicma20 + vals2.nicmlt20
        vals2.nism20 = vals2.nisma20 + vals2.nismlt20
        vals2.iws20 = vals.tcwsalt20 + vals.tcwsltlt20
        vals2.iys20 = vals.tcysalt20 + vals.tcysltlt20
        vals2.icm20 = vals2.icmlt20 + vals.tccmalt20
        vals2.ism20 = vals2.ismlt20 + vals.tcsmalt20
        vals2.ltls20 = float(request.POST['ltls20'])
        vals2.ltwsa20 = float(request.POST['ltwsa20'])
        vals2.ltwslt20 = float(request.POST['ltwslt20'])
        vals2.ltysa20 = float(request.POST['ltysa20'])
        vals2.ltyslt20 = float(request.POST['ltyslt20'])
        vals2.htwsa20 = float(request.POST['htwsa20'])
        vals2.htwslt20 = float(request.POST['htwslt20'])
        vals2.htysa20 = float(request.POST['htysa20'])
        vals2.htyslt20 = float(request.POST['htyslt20'])
        vals2.ws20 = vals2.ltwsa20 + vals2.ltwslt20 + vals2.htwsa20 + vals2.htwslt20
        vals2.ys20 = vals2.ltysa20 + vals2.ltyslt20 + vals2.htysa20 + vals2.htyslt20
        vals2.vstotal2_20 = vals2.ltls20 + vals2.ws20 + vals2.ys20
        vals2.macdtc20 = float(request.POST['macdtc20'])
        vals2.cts20 = float(request.POST['cts20'])
        vals2.ctc20 = vals2.macdtc20 * vals2.cts20/100
        
        vals2.nils21 = vals.nielslt21 + vals.lslt21
        vals2.niwsa21 = vals.wsaht21 + vals.wsalt21 + vals.niewsaht21 + vals.niewsalt21
        vals2.niwslt21 = vals.wsltht21 + vals.wsltlt21 + vals.niewsltht21 + vals.niewsltlt21
        vals2.niysa21 = vals.ysaht21 + vals.ysalt21 + vals.nieysaht21 + vals.nieysalt21
        vals2.niyslt21 = vals.ysltht21 + vals.ysltlt21 + vals.nieysltht21 + vals.nieysltlt21
        vals2.nicma21 = vals.cmaht21 + vals.cmalt21 + vals.niecmaht21 + vals.niecmalt21
        vals2.nicmlt21 = (vals.cmltht1_21 + vals.cmltht2_21 + vals.cmltht3_21 + vals.cmltlt21 + 
                            vals.niecmltht1_21 + vals.niecmltht2_21 + vals.niecmltht3_21 + vals.niecmltlt21)
        vals2.nisma21 = vals.smaht21 + vals.niesmaht21
        vals2.nismlt21 = vals.smltht1_21 + vals.smltht2_21 + vals.niesmltht1_21 + vals.niesmltht2_21
        vals2.icmlt21 = vals.tccmltlt1_21 + vals.tccmltlt2_21 + vals.tccmltlt3_21
        vals2.ismlt21 = vals.tcsmltlt1_21 + vals.tcsmltlt2_21
        vals2.vstotal1_21 = (vals2.nils21 + vals2.niwsa21 + vals2.niwslt21 + vals2.niysa21 + vals2.niyslt21 + vals2.nicma21 +
                                vals2.nicmlt21 + vals2.nisma21 + vals2.nismlt21 + vals2.icmlt21 + vals2.ismlt21 + vals.tcwsalt21 +
                                    vals.tcwsltlt21 + vals.tcysalt21 + vals.tcysltlt21 + vals.tccmalt21 + vals.tcsmalt21)
        vals2.niws21 = vals2.niwsa21 + vals2.niwslt21 
        vals2.niys21 = vals2.niysa21 + vals2.niyslt21
        vals2.nicm21 = vals2.nicma21 + vals2.nicmlt21
        vals2.nism21 = vals2.nisma21 + vals2.nismlt21
        vals2.iws21 = vals.tcwsalt21 + vals.tcwsltlt21
        vals2.iys21 = vals.tcysalt21 + vals.tcysltlt21
        vals2.icm21 = vals2.icmlt21 + vals.tccmalt21
        vals2.ism21 = vals2.ismlt21 + vals.tcsmalt21
        vals2.ltls21 = float(request.POST['ltls21'])
        vals2.ltwsa21 = float(request.POST['ltwsa21'])
        vals2.ltwslt21 = float(request.POST['ltwslt21'])
        vals2.ltysa21 = float(request.POST['ltysa21'])
        vals2.ltyslt21 = float(request.POST['ltyslt21'])
        vals2.htwsa21 = float(request.POST['htwsa21'])
        vals2.htwslt21 = float(request.POST['htwslt21'])
        vals2.htysa21 = float(request.POST['htysa21'])
        vals2.htyslt21 = float(request.POST['htyslt21'])
        vals2.ws21 = vals2.ltwsa21 + vals2.ltwslt21 + vals2.htwsa21 + vals2.htwslt21
        vals2.ys21 = vals2.ltysa21 + vals2.ltyslt21 + vals2.htysa21 + vals2.htyslt21
        vals2.vstotal2_21 = vals2.ltls21 + vals2.ws21 + vals2.ys21
        vals2.macdtc21 = float(request.POST['macdtc21'])
        vals2.cts21 = float(request.POST['cts21'])
        vals2.ctc21 = vals2.macdtc21 * vals2.cts21/100
        
        vals2.nils22 = vals.nielslt22 + vals.lslt22
        vals2.niwsa22 = vals.wsaht22 + vals.wsalt22 + vals.niewsaht22 + vals.niewsalt22
        vals2.niwslt22 = vals.wsltht22 + vals.wsltlt22 + vals.niewsltht22 + vals.niewsltlt22
        vals2.niysa22 = vals.ysaht22 + vals.ysalt22 + vals.nieysaht22 + vals.nieysalt22
        vals2.niyslt22 = vals.ysltht22 + vals.ysltlt22 + vals.nieysltht22 + vals.nieysltlt22
        vals2.nicma22 = vals.cmaht22 + vals.cmalt22 + vals.niecmaht22 + vals.niecmalt22
        vals2.nicmlt22 = (vals.cmltht1_22 + vals.cmltht2_22 + vals.cmltht3_22 + vals.cmltlt22 + 
                            vals.niecmltht1_22 + vals.niecmltht2_22 + vals.niecmltht3_22 + vals.niecmltlt22)
        vals2.nisma22 = vals.smaht22 + vals.niesmaht22
        vals2.nismlt22 = vals.smltht1_22 + vals.smltht2_22 + vals.niesmltht1_22 + vals.niesmltht2_22
        vals2.icmlt22 = vals.tccmltlt1_22 + vals.tccmltlt2_22 + vals.tccmltlt3_22
        vals2.ismlt22 = vals.tcsmltlt1_22 + vals.tcsmltlt2_22
        vals2.vstotal1_22 = (vals2.nils22 + vals2.niwsa22 + vals2.niwslt22 + vals2.niysa22 + vals2.niyslt22 + vals2.nicma22 +
                                vals2.nicmlt22 + vals2.nisma22 + vals2.nismlt22 + vals2.icmlt22 + vals2.ismlt22 + vals.tcwsalt22 +
                                    vals.tcwsltlt22 + vals.tcysalt22 + vals.tcysltlt22 + vals.tccmalt22 + vals.tcsmalt22)
        vals2.niws22 = vals2.niwsa22 + vals2.niwslt22 
        vals2.niys22 = vals2.niysa22 + vals2.niyslt22
        vals2.nicm22 = vals2.nicma22 + vals2.nicmlt22
        vals2.nism22 = vals2.nisma22 + vals2.nismlt22
        vals2.iws22 = vals.tcwsalt22 + vals.tcwsltlt22
        vals2.iys22 = vals.tcysalt22 + vals.tcysltlt22
        vals2.icm22 = vals2.icmlt22 + vals.tccmalt22
        vals2.ism22 = vals2.ismlt22 + vals.tcsmalt22
        vals2.ltls22 = float(request.POST['ltls22'])
        vals2.ltwsa22 = float(request.POST['ltwsa22'])
        vals2.ltwslt22 = float(request.POST['ltwslt22'])
        vals2.ltysa22 = float(request.POST['ltysa22'])
        vals2.ltyslt22 = float(request.POST['ltyslt22'])
        vals2.htwsa22 = float(request.POST['htwsa22'])
        vals2.htwslt22 = float(request.POST['htwslt22'])
        vals2.htysa22 = float(request.POST['htysa22'])
        vals2.htyslt22 = float(request.POST['htyslt22'])
        vals2.ws22 = vals2.ltwsa22 + vals2.ltwslt22 + vals2.htwsa22 + vals2.htwslt22
        vals2.ys22 = vals2.ltysa22 + vals2.ltyslt22 + vals2.htysa22 + vals2.htyslt22
        vals2.vstotal2_22 = vals2.ltls22 + vals2.ws22 + vals2.ys22
        vals2.macdtc22 = float(request.POST['macdtc22'])
        vals2.cts22 = float(request.POST['cts22'])
        vals2.ctc22 = vals2.macdtc22 * vals2.cts22/100
        
        vals2.nils23 = vals.nielslt23 + vals.lslt23
        vals2.niwsa23 = vals.wsaht23 + vals.wsalt23 + vals.niewsaht23 + vals.niewsalt23
        vals2.niwslt23 = vals.wsltht23 + vals.wsltlt23 + vals.niewsltht23 + vals.niewsltlt23
        vals2.niysa23 = vals.ysaht23 + vals.ysalt23 + vals.nieysaht23 + vals.nieysalt23
        vals2.niyslt23 = vals.ysltht23 + vals.ysltlt23 + vals.nieysltht23 + vals.nieysltlt23
        vals2.nicma23 = vals.cmaht23 + vals.cmalt23 + vals.niecmaht23 + vals.niecmalt23
        vals2.nicmlt23 = (vals.cmltht1_23 + vals.cmltht2_23 + vals.cmltht3_23 + vals.cmltlt23 + 
                            vals.niecmltht1_23 + vals.niecmltht2_23 + vals.niecmltht3_23 + vals.niecmltlt23)
        vals2.nisma23 = vals.smaht23 + vals.niesmaht23
        vals2.nismlt23 = vals.smltht1_23 + vals.smltht2_23 + vals.niesmltht1_23 + vals.niesmltht2_23
        vals2.icmlt23 = vals.tccmltlt1_23 + vals.tccmltlt2_23 + vals.tccmltlt3_23
        vals2.ismlt23 = vals.tcsmltlt1_23 + vals.tcsmltlt2_23
        vals2.vstotal1_23 = (vals2.nils23 + vals2.niwsa23 + vals2.niwslt23 + vals2.niysa23 + vals2.niyslt23 + vals2.nicma23 +
                                vals2.nicmlt23 + vals2.nisma23 + vals2.nismlt23 + vals2.icmlt23 + vals2.ismlt23 + vals.tcwsalt23 +
                                    vals.tcwsltlt23 + vals.tcysalt23 + vals.tcysltlt23 + vals.tccmalt23 + vals.tcsmalt23)
        vals2.niws23 = vals2.niwsa23 + vals2.niwslt23 
        vals2.niys23 = vals2.niysa23 + vals2.niyslt23
        vals2.nicm23 = vals2.nicma23 + vals2.nicmlt23
        vals2.nism23 = vals2.nisma23 + vals2.nismlt23
        vals2.iws23 = vals.tcwsalt23 + vals.tcwsltlt23
        vals2.iys23 = vals.tcysalt23 + vals.tcysltlt23
        vals2.icm23 = vals2.icmlt23 + vals.tccmalt23
        vals2.ism23 = vals2.ismlt23 + vals.tcsmalt23
        vals2.ltls23 = float(request.POST['ltls23'])
        vals2.ltwsa23 = float(request.POST['ltwsa23'])
        vals2.ltwslt23 = float(request.POST['ltwslt23'])
        vals2.ltysa23 = float(request.POST['ltysa23'])
        vals2.ltyslt23 = float(request.POST['ltyslt23'])
        vals2.htwsa23 = float(request.POST['htwsa23'])
        vals2.htwslt23 = float(request.POST['htwslt23'])
        vals2.htysa23 = float(request.POST['htysa23'])
        vals2.htyslt23 = float(request.POST['htyslt23'])
        vals2.ws23 = vals2.ltwsa23 + vals2.ltwslt23 + vals2.htwsa23 + vals2.htwslt23
        vals2.ys23 = vals2.ltysa23 + vals2.ltyslt23 + vals2.htysa23 + vals2.htyslt23
        vals2.vstotal2_23 = vals2.ltls23 + vals2.ws23 + vals2.ys23
        vals2.macdtc23 = float(request.POST['macdtc23'])
        vals2.cts23 = float(request.POST['cts23'])
        vals2.ctc23 = vals2.macdtc23 * vals2.cts23/100
        
        vals2.nils24 = vals.nielslt24 + vals.lslt24
        vals2.niwsa24 = vals.wsaht24 + vals.wsalt24 + vals.niewsaht24 + vals.niewsalt24
        vals2.niwslt24 = vals.wsltht24 + vals.wsltlt24 + vals.niewsltht24 + vals.niewsltlt24
        vals2.niysa24 = vals.ysaht24 + vals.ysalt24 + vals.nieysaht24 + vals.nieysalt24
        vals2.niyslt24 = vals.ysltht24 + vals.ysltlt24 + vals.nieysltht24 + vals.nieysltlt24
        vals2.nicma24 = vals.cmaht24 + vals.cmalt24 + vals.niecmaht24 + vals.niecmalt24
        vals2.nicmlt24 = (vals.cmltht1_24 + vals.cmltht2_24 + vals.cmltht3_24 + vals.cmltlt24 + 
                            vals.niecmltht1_24 + vals.niecmltht2_24 + vals.niecmltht3_24 + vals.niecmltlt24)
        vals2.nisma24 = vals.smaht24 + vals.niesmaht24
        vals2.nismlt24 = vals.smltht1_24 + vals.smltht2_24 + vals.niesmltht1_24 + vals.niesmltht2_24
        vals2.icmlt24 = vals.tccmltlt1_24 + vals.tccmltlt2_24 + vals.tccmltlt3_24
        vals2.ismlt24 = vals.tcsmltlt1_24 + vals.tcsmltlt2_24
        vals2.vstotal1_24 = (vals2.nils24 + vals2.niwsa24 + vals2.niwslt24 + vals2.niysa24 + vals2.niyslt24 + vals2.nicma24 +
                                vals2.nicmlt24 + vals2.nisma24 + vals2.nismlt24 + vals2.icmlt24 + vals2.ismlt24 + vals.tcwsalt24 +
                                    vals.tcwsltlt24 + vals.tcysalt24 + vals.tcysltlt24 + vals.tccmalt24 + vals.tcsmalt24)
        vals2.niws24 = vals2.niwsa24 + vals2.niwslt24 
        vals2.niys24 = vals2.niysa24 + vals2.niyslt24
        vals2.nicm24 = vals2.nicma24 + vals2.nicmlt24
        vals2.nism24 = vals2.nisma24 + vals2.nismlt24
        vals2.iws24 = vals.tcwsalt24 + vals.tcwsltlt24
        vals2.iys24 = vals.tcysalt24 + vals.tcysltlt24
        vals2.icm24 = vals2.icmlt24 + vals.tccmalt24
        vals2.ism24 = vals2.ismlt24 + vals.tcsmalt24
        vals2.ltls24 = float(request.POST['ltls24'])
        vals2.ltwsa24 = float(request.POST['ltwsa24'])
        vals2.ltwslt24 = float(request.POST['ltwslt24'])
        vals2.ltysa24 = float(request.POST['ltysa24'])
        vals2.ltyslt24 = float(request.POST['ltyslt24'])
        vals2.htwsa24 = float(request.POST['htwsa24'])
        vals2.htwslt24 = float(request.POST['htwslt24'])
        vals2.htysa24 = float(request.POST['htysa24'])
        vals2.htyslt24 = float(request.POST['htyslt24'])
        vals2.ws24 = vals2.ltwsa24 + vals2.ltwslt24 + vals2.htwsa24 + vals2.htwslt24
        vals2.ys24 = vals2.ltysa24 + vals2.ltyslt24 + vals2.htysa24 + vals2.htyslt24
        vals2.vstotal2_24 = vals2.ltls24 + vals2.ws24 + vals2.ys24
        vals2.macdtc24 = float(request.POST['macdtc24'])
        vals2.cts24 = float(request.POST['cts24'])
        vals2.ctc24 = vals2.macdtc24 * vals2.cts24/100

        vals2.incprice1 = float(request.POST['incprice1'])
        vals2.incprice2 = float(request.POST['incprice2'])
        vals2.incprice3 = float(request.POST['incprice3'])
        vals2.incprice4 = float(request.POST['incprice4'])
        vals2.incprice5 = float(request.POST['incprice5'])

        vals2.excprice1 = vals2.incprice1/(1+13/100)
        vals2.excprice2 = vals2.incprice2/(1+13/100)
        vals2.excprice3 = vals2.incprice3/(1+13/100)
        vals2.excprice4 = vals2.incprice4/(1+13/100)
        vals2.excprice5 = vals2.incprice5/(1+13/100)
        
        vals2.tcsmltlt15 = vals.tcsmltlt1_15 + vals.tcsmltlt2_15
        vals2.tcsmltlt16 = vals.tcsmltlt1_16 + vals.tcsmltlt2_16
        vals2.tcsmltlt17 = vals.tcsmltlt1_17 + vals.tcsmltlt2_17
        vals2.tcsmltlt18 = vals.tcsmltlt1_18 + vals.tcsmltlt2_18
        vals2.tcsmltlt19 = vals.tcsmltlt1_19 + vals.tcsmltlt2_19
        vals2.tcsmltlt20 = vals.tcsmltlt1_20 + vals.tcsmltlt2_20
        vals2.tcsmltlt21 = vals.tcsmltlt1_21 + vals.tcsmltlt2_21
        vals2.tcsmltlt22 = vals.tcsmltlt1_22 + vals.tcsmltlt2_22
        vals2.tcsmltlt23 = vals.tcsmltlt1_23 + vals.tcsmltlt2_23
        vals2.tcsmltlt24 = vals.tcsmltlt1_24 + vals.tcsmltlt2_24

        vals2.tccmltlt15 = vals.tccmltlt1_15 + vals.tccmltlt2_15 + vals.tccmltlt3_15
        vals2.tccmltlt16 = vals.tccmltlt1_16 + vals.tccmltlt2_16 + vals.tccmltlt3_16
        vals2.tccmltlt17 = vals.tccmltlt1_17 + vals.tccmltlt2_17 + vals.tccmltlt3_17
        vals2.tccmltlt18 = vals.tccmltlt1_18 + vals.tccmltlt2_18 + vals.tccmltlt3_18
        vals2.tccmltlt19 = vals.tccmltlt1_19 + vals.tccmltlt2_19 + vals.tccmltlt3_19
        vals2.tccmltlt20 = vals.tccmltlt1_20 + vals.tccmltlt2_20 + vals.tccmltlt3_20
        vals2.tccmltlt21 = vals.tccmltlt1_21 + vals.tccmltlt2_21 + vals.tccmltlt3_21
        vals2.tccmltlt22 = vals.tccmltlt1_22 + vals.tccmltlt2_22 + vals.tccmltlt3_22
        vals2.tccmltlt23 = vals.tccmltlt1_23 + vals.tccmltlt2_23 + vals.tccmltlt3_23
        vals2.tccmltlt24 = vals.tccmltlt1_24 + vals.tccmltlt2_24 + vals.tccmltlt3_24

        vals2.wsaieoil15 = vals.tcwsalt15 * 65.08/100
        vals2.wsahoil15 =  vals.tcwsalt15 * (39.41/100*15/100)
        vals2.wsltieoil15 = vals.tcwsltlt15 * 98.60/100
        vals2.wslthoil15 = vals.tcwsltlt15 * (24.7/100*15/100)
        vals2.ysaieoil15 = vals.tcysalt15 * 53.55/100
        vals2.ysahoil15 =  vals.tcysalt15 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil15 = vals.tcysltlt15 * 79.33/100
        vals2.yslthoil15 = vals.tcysltlt15 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil15 = vals.tccmalt15 * 54.62/100
        vals2.cmahoil15 =  vals.tccmalt15 * (33.1/100*15/100)
        vals2.cmltieoil15 = vals2.tccmltlt15 * 44.69/100
        vals2.cmlthoil15 = vals2.tccmltlt15 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil15 = vals.tcsmalt15 * 82.67/100
        vals2.smahoil15 =  vals.tcsmalt15 * (20.66/100*15/100)
        vals2.smltieoil15 = vals2.tcsmltlt15 * 66.20/100
        vals2.smlthoil15 = vals2.tcsmltlt15 * ((26.47/100*15/100) + (16.55/100*50/100))

        vals2.wsaieoil16 = vals.tcwsalt16 * 65.08/100
        vals2.wsahoil16 =  vals.tcwsalt16 * (39.41/100*15/100)
        vals2.wsltieoil16 = vals.tcwsltlt16 * 98.60/100
        vals2.wslthoil16 = vals.tcwsltlt16 * (24.7/100*15/100)
        vals2.ysaieoil16 = vals.tcysalt16 * 53.55/100
        vals2.ysahoil16 =  vals.tcysalt16 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil16 = vals.tcysltlt16 * 79.33/100
        vals2.yslthoil16 = vals.tcysltlt16 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil16 = vals.tccmalt16 * 54.62/100
        vals2.cmahoil16 =  vals.tccmalt16 * (33.1/100*15/100)
        vals2.cmltieoil16 = vals2.tccmltlt16 * 44.69/100
        vals2.cmlthoil16 = vals2.tccmltlt16 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil16 = vals.tcsmalt16 * 82.67/100
        vals2.smahoil16 =  vals.tcsmalt16 * (20.66/100*15/100)
        vals2.smltieoil16 = vals2.tcsmltlt16 * 66.20/100
        vals2.smlthoil16 = vals2.tcsmltlt16 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil17 = vals.tcwsalt17 * 65.08/100
        vals2.wsahoil17 =  vals.tcwsalt17 * (39.41/100*15/100)
        vals2.wsltieoil17 = vals.tcwsltlt17 * 98.60/100
        vals2.wslthoil17 = vals.tcwsltlt17 * (24.7/100*15/100)
        vals2.ysaieoil17 = vals.tcysalt17 * 53.55/100
        vals2.ysahoil17 =  vals.tcysalt17 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil17 = vals.tcysltlt17 * 79.33/100
        vals2.yslthoil17 = vals.tcysltlt17 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil17 = vals.tccmalt17 * 54.62/100
        vals2.cmahoil17 =  vals.tccmalt17 * (33.1/100*15/100)
        vals2.cmltieoil17 = vals2.tccmltlt17 * 44.69/100
        vals2.cmlthoil17 = vals2.tccmltlt17 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil17 = vals.tcsmalt17 * 82.67/100
        vals2.smahoil17 =  vals.tcsmalt17 * (20.66/100*15/100)
        vals2.smltieoil17 = vals2.tcsmltlt17 * 66.20/100
        vals2.smlthoil17 = vals2.tcsmltlt17 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil18 = vals.tcwsalt18 * 65.08/100
        vals2.wsahoil18 =  vals.tcwsalt18 * (39.41/100*15/100)
        vals2.wsltieoil18 = vals.tcwsltlt18 * 98.60/100
        vals2.wslthoil18 = vals.tcwsltlt18 * (24.7/100*15/100)
        vals2.ysaieoil18 = vals.tcysalt18 * 53.55/100
        vals2.ysahoil18 =  vals.tcysalt18 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil18 = vals.tcysltlt18 * 79.33/100
        vals2.yslthoil18 = vals.tcysltlt18 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil18 = vals.tccmalt18 * 54.62/100
        vals2.cmahoil18 =  vals.tccmalt18 * (33.1/100*15/100)
        vals2.cmltieoil18 = vals2.tccmltlt18 * 44.69/100
        vals2.cmlthoil18 = vals2.tccmltlt18 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil18 = vals.tcsmalt18 * 82.67/100
        vals2.smahoil18 =  vals.tcsmalt18 * (20.66/100*15/100)
        vals2.smltieoil18 = vals2.tcsmltlt18 * 66.20/100
        vals2.smlthoil18 = vals2.tcsmltlt18 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil19 = vals.tcwsalt19 * 65.08/100
        vals2.wsahoil19 =  vals.tcwsalt19 * (39.41/100*15/100)
        vals2.wsltieoil19 = vals.tcwsltlt19 * 98.60/100
        vals2.wslthoil19 = vals.tcwsltlt19 * (24.7/100*15/100)
        vals2.ysaieoil19 = vals.tcysalt19 * 53.55/100
        vals2.ysahoil19 =  vals.tcysalt19 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil19 = vals.tcysltlt19 * 79.33/100
        vals2.yslthoil19 = vals.tcysltlt19 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil19 = vals.tccmalt19 * 54.62/100
        vals2.cmahoil19 =  vals.tccmalt19 * (33.1/100*15/100)
        vals2.cmltieoil19 = vals2.tccmltlt19 * 44.69/100
        vals2.cmlthoil19 = vals2.tccmltlt19 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil19 = vals.tcsmalt19 * 82.67/100
        vals2.smahoil19 =  vals.tcsmalt19 * (20.66/100*15/100)
        vals2.smltieoil19 = vals2.tcsmltlt19 * 66.20/100
        vals2.smlthoil19 = vals2.tcsmltlt19 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil20 = vals.tcwsalt20 * 65.08/100
        vals2.wsahoil20 =  vals.tcwsalt20 * (39.41/100*15/100)
        vals2.wsltieoil20 = vals.tcwsltlt20 * 98.60/100
        vals2.wslthoil20 = vals.tcwsltlt20 * (24.7/100*15/100)
        vals2.ysaieoil20 = vals.tcysalt20 * 53.55/100
        vals2.ysahoil20 =  vals.tcysalt20 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil20 = vals.tcysltlt20 * 79.33/100
        vals2.yslthoil20 = vals.tcysltlt20 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil20 = vals.tccmalt20 * 54.62/100
        vals2.cmahoil20 =  vals.tccmalt20 * (33.1/100*15/100)
        vals2.cmltieoil20 = vals2.tccmltlt20 * 44.69/100
        vals2.cmlthoil20 = vals2.tccmltlt20 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil20 = vals.tcsmalt20 * 82.67/100
        vals2.smahoil20 =  vals.tcsmalt20 * (20.66/100*15/100)
        vals2.smltieoil20 = vals2.tcsmltlt20 * 66.20/100
        vals2.smlthoil20 = vals2.tcsmltlt20 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil21 = vals.tcwsalt21 * 65.08/100
        vals2.wsahoil21 =  vals.tcwsalt21 * (39.41/100*15/100)
        vals2.wsltieoil21 = vals.tcwsltlt21 * 98.60/100
        vals2.wslthoil21 = vals.tcwsltlt21 * (24.7/100*15/100)
        vals2.ysaieoil21 = vals.tcysalt21 * 53.55/100
        vals2.ysahoil21 =  vals.tcysalt21 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil21 = vals.tcysltlt21 * 79.33/100
        vals2.yslthoil21 = vals.tcysltlt21 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil21 = vals.tccmalt21 * 54.62/100
        vals2.cmahoil21 =  vals.tccmalt21 * (33.1/100*15/100)
        vals2.cmltieoil21 = vals2.tccmltlt21 * 44.69/100
        vals2.cmlthoil21 = vals2.tccmltlt21 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil21 = vals.tcsmalt21 * 82.67/100
        vals2.smahoil21 =  vals.tcsmalt21 * (20.66/100*15/100)
        vals2.smltieoil21 = vals2.tcsmltlt21 * 66.20/100
        vals2.smlthoil21 = vals2.tcsmltlt21 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil22 = vals.tcwsalt22 * 65.08/100
        vals2.wsahoil22 =  vals.tcwsalt22 * (39.41/100*15/100)
        vals2.wsltieoil22 = vals.tcwsltlt22 * 98.60/100
        vals2.wslthoil22 = vals.tcwsltlt22 * (24.7/100*15/100)
        vals2.ysaieoil22 = vals.tcysalt22 * 53.55/100
        vals2.ysahoil22 =  vals.tcysalt22 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil22 = vals.tcysltlt22 * 79.33/100
        vals2.yslthoil22 = vals.tcysltlt22 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil22 = vals.tccmalt22 * 54.62/100
        vals2.cmahoil22 =  vals.tccmalt22 * (33.1/100*15/100)
        vals2.cmltieoil22 = vals2.tccmltlt22 * 44.69/100
        vals2.cmlthoil22 = vals2.tccmltlt22 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil22 = vals.tcsmalt22 * 82.67/100
        vals2.smahoil22 =  vals.tcsmalt22 * (20.66/100*15/100)
        vals2.smltieoil22 = vals2.tcsmltlt22 * 66.20/100
        vals2.smlthoil22 = vals2.tcsmltlt22 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil23 = vals.tcwsalt23 * 65.08/100
        vals2.wsahoil23 =  vals.tcwsalt23 * (39.41/100*15/100)
        vals2.wsltieoil23 = vals.tcwsltlt23 * 98.60/100
        vals2.wslthoil23 = vals.tcwsltlt23 * (24.7/100*15/100)
        vals2.ysaieoil23 = vals.tcysalt23 * 53.55/100
        vals2.ysahoil23 =  vals.tcysalt23 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil23 = vals.tcysltlt23 * 79.33/100
        vals2.yslthoil23 = vals.tcysltlt23 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil23 = vals.tccmalt23 * 54.62/100
        vals2.cmahoil23 =  vals.tccmalt23 * (33.1/100*15/100)
        vals2.cmltieoil23 = vals2.tccmltlt23 * 44.69/100
        vals2.cmlthoil23 = vals2.tccmltlt23 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil23 = vals.tcsmalt23 * 82.67/100
        vals2.smahoil23 =  vals.tcsmalt23 * (20.66/100*15/100)
        vals2.smltieoil23 = vals2.tcsmltlt23 * 66.20/100
        vals2.smlthoil23 = vals2.tcsmltlt23 * ((26.47/100*15/100) + (16.55/100*50/100))
        
        vals2.wsaieoil24 = vals.tcwsalt24 * 65.08/100
        vals2.wsahoil24 =  vals.tcwsalt24 * (39.41/100*15/100)
        vals2.wsltieoil24 = vals.tcwsltlt24 * 98.60/100
        vals2.wslthoil24 = vals.tcwsltlt24 * (24.7/100*15/100)
        vals2.ysaieoil24 = vals.tcysalt24 * 53.55/100
        vals2.ysahoil24 =  vals.tcysalt24 * ((19.81/100*15/100) + (19.83/100*50/100))
        vals2.ysltieoil24 = vals.tcysltlt24 * 79.33/100
        vals2.yslthoil24 = vals.tcysltlt24 * ((31.7/100*15/100) + (19.83/100*50/100))
        vals2.cmaieoil24 = vals.tccmalt24 * 54.62/100
        vals2.cmahoil24 =  vals.tccmalt24 * (33.1/100*15/100)
        vals2.cmltieoil24 = vals2.tccmltlt24 * 44.69/100
        vals2.cmlthoil24 = vals2.tccmltlt24 * ((1.65/100*15/100) + (16.55/100*50/100))
        vals2.smaieoil24 = vals.tcsmalt24 * 82.67/100
        vals2.smahoil24 =  vals.tcsmalt24 * (20.66/100*15/100)
        vals2.smltieoil24 = vals2.tcsmltlt24 * 66.20/100
        vals2.smlthoil24 = vals2.tcsmltlt24 * ((26.47/100*15/100) + (16.55/100*50/100))

        vals2.hoil24 = (vals2.wsahoil24 + vals2.wslthoil24 + vals2.ysahoil24 + vals2.yslthoil24 + vals2.cmahoil24 + vals2.cmlthoil24 + vals2.smahoil24 + vals2.smlthoil24)
        vals2.hoil23 = (vals2.wsahoil23 + vals2.wslthoil23 + vals2.ysahoil23 + vals2.yslthoil23 + vals2.cmahoil23 + vals2.cmlthoil23 + vals2.smahoil23 + vals2.smlthoil23)
        vals2.hoil22 = (vals2.wsahoil22 + vals2.wslthoil22 + vals2.ysahoil22 + vals2.yslthoil22 + vals2.cmahoil22 + vals2.cmlthoil22 + vals2.smahoil22 + vals2.smlthoil22)
        vals2.hoil21 = vals2.wsahoil21 + vals2.wslthoil21 + vals2.ysahoil21 + vals2.yslthoil21 + vals2.cmahoil21 + vals2.cmlthoil21 + vals2.smahoil21 + vals2.smlthoil21
        vals2.hoil20 = vals2.wsahoil20 + vals2.wslthoil20 + vals2.ysahoil20 + vals2.yslthoil20 + vals2.cmahoil20 + vals2.cmlthoil20 + vals2.smahoil20 + vals2.smlthoil20
        vals2.hoil19 = vals2.wsahoil19 + vals2.wslthoil19 + vals2.ysahoil19 + vals2.yslthoil19 + vals2.cmahoil19 + vals2.cmlthoil19 + vals2.smahoil19 + vals2.smlthoil19
        vals2.hoil18 = vals2.wsahoil18 + vals2.wslthoil18 + vals2.ysahoil18 + vals2.yslthoil18 + vals2.cmahoil18 + vals2.cmlthoil18 + vals2.smahoil18 + vals2.smlthoil18
        vals2.hoil17 = vals2.wsahoil17 + vals2.wslthoil17 + vals2.ysahoil17 + vals2.yslthoil17 + vals2.cmahoil17 + vals2.cmlthoil17 + vals2.smahoil17 + vals2.smlthoil17
        vals2.hoil16 = vals2.wsahoil16 + vals2.wslthoil16 + vals2.ysahoil16 + vals2.yslthoil16 + vals2.cmahoil16 + vals2.cmlthoil16 + vals2.smahoil16 + vals2.smlthoil16
        vals2.hoil15 = vals2.wsahoil15 + vals2.wslthoil15 + vals2.ysahoil15 + vals2.yslthoil15 + vals2.cmahoil15 + vals2.cmlthoil15 + vals2.smahoil15 + vals2.smlthoil15
        
        vals2.ieoil24 = (vals2.wsaieoil24 + vals2.wsltieoil24 + vals2.ysaieoil24 + vals2.ysltieoil24 + vals2.cmaieoil24 + vals2.cmltieoil24 + vals2.smaieoil24 + vals2.smltieoil24)
        vals2.ieoil23 = (vals2.wsaieoil23 + vals2.wsltieoil23 + vals2.ysaieoil23 + vals2.ysltieoil23 + vals2.cmaieoil23 + vals2.cmltieoil23 + vals2.smaieoil23 + vals2.smltieoil23)
        vals2.ieoil22 = (vals2.wsaieoil22 + vals2.wsltieoil22 + vals2.ysaieoil22 + vals2.ysltieoil22 + vals2.cmaieoil22 + vals2.cmltieoil22 + vals2.smaieoil22 + vals2.smltieoil22)
        vals2.ieoil21 = vals2.wsaieoil21 + vals2.wsltieoil21 + vals2.ysaieoil21 + vals2.ysltieoil21 + vals2.cmaieoil21 + vals2.cmltieoil21 + vals2.smaieoil21 + vals2.smltieoil21
        vals2.ieoil20 = vals2.wsaieoil20 + vals2.wsltieoil20 + vals2.ysaieoil20 + vals2.ysltieoil20 + vals2.cmaieoil20 + vals2.cmltieoil20 + vals2.smaieoil20 + vals2.smltieoil20
        vals2.ieoil19 = vals2.wsaieoil19 + vals2.wsltieoil19 + vals2.ysaieoil19 + vals2.ysltieoil19 + vals2.cmaieoil19 + vals2.cmltieoil19 + vals2.smaieoil19 + vals2.smltieoil19
        vals2.ieoil18 = vals2.wsaieoil18 + vals2.wsltieoil18 + vals2.ysaieoil18 + vals2.ysltieoil18 + vals2.cmaieoil18 + vals2.cmltieoil18 + vals2.smaieoil18 + vals2.smltieoil18
        vals2.ieoil17 = (vals2.wsaieoil17 + vals2.wsltieoil17 + vals2.ysaieoil17 + vals2.ysltieoil17 + vals2.cmaieoil17 + vals2.cmltieoil17 + vals2.smaieoil17 + vals2.smltieoil17)+(8785/2)
        vals2.ieoil16 = (vals2.wsaieoil16 + vals2.wsltieoil16 + vals2.ysaieoil16 + vals2.ysltieoil16 + vals2.cmaieoil16 + vals2.cmltieoil16 + vals2.smaieoil16 + vals2.smltieoil16)+(9663/2)
        vals2.ieoil15 = (vals2.wsaieoil15 + vals2.wsltieoil15 + vals2.ysaieoil15 + vals2.ysltieoil15 + vals2.cmaieoil15 + vals2.cmltieoil15 + vals2.smaieoil15 + vals2.smltieoil15)+(10629/2)

        #Hydro Oil in non-IE Product
        vals2.wsahthoc15 = vals.wsaht15 * 50.603/100
        vals2.wsalthoc15 = vals.wsalt15 * 3.969/100
        vals2.wslththoc15 = vals.wsltht15 * 53.488/100
        vals2.wsltlthoc15 = vals.wsltlt15 * 1.984/100
        vals2.ysahthoc15 = vals.ysaht15 * 50.52/100
        vals2.ysalthoc15 = vals.ysalt15 * 3.879/100
        vals2.yslththoc15 = vals.ysltht15 * 52.778/100
        vals2.ysltlthoc15 = vals.ysltlt15 * 1.984/100
        vals2.cmahthoc15 = vals.cmaht15 * 38.46/100
        vals2.cmltht1_hoc15 = vals.cmltht1_15 * 43.478/100
        vals2.cmltht2_hoc15 = vals.cmltht2_15 * 24.81/100
        vals2.cmltht3_hoc15 = vals.cmltht3_15 * 12.24/100
        vals2.cmalthoc15 = vals.cmalt15 * 3.247/100
        vals2.cmltlthoc15 = vals.cmltlt15 * 1.624/100
        vals2.smahthoc15 = vals.smaht15 * 1.624/100
        vals2.smltht1_hoc15 = vals.smltht1_15 * 23.239/100
        vals2.smltht2_hoc15 = vals.smltht2_15 * 38.771/100

        vals2.wsahthoc16 = vals.wsaht16 * 50.603/100
        vals2.wsalthoc16 = vals.wsalt16 * 3.969/100
        vals2.wslththoc16 = vals.wsltht16 * 53.488/100
        vals2.wsltlthoc16 = vals.wsltlt16 * 1.984/100
        vals2.ysahthoc16 = vals.ysaht16 * 50.52/100
        vals2.ysalthoc16 = vals.ysalt16 * 3.879/100
        vals2.yslththoc16 = vals.ysltht16 * 52.778/100
        vals2.ysltlthoc16 = vals.ysltlt16 * 1.984/100
        vals2.cmahthoc16 = vals.cmaht16 * 38.46/100
        vals2.cmltht1_hoc16 = vals.cmltht1_16 * 43.478/100
        vals2.cmltht2_hoc16 = vals.cmltht2_16 * 24.81/100
        vals2.cmltht3_hoc16 = vals.cmltht3_16 * 12.24/100
        vals2.cmalthoc16 = vals.cmalt16 * 3.247/100
        vals2.cmltlthoc16 = vals.cmltlt16 * 1.624/100
        vals2.smahthoc16 = vals.smaht16 * 1.624/100
        vals2.smltht1_hoc16 = vals.smltht1_16 * 23.239/100
        vals2.smltht2_hoc16 = vals.smltht2_16 * 38.771/100
        
        vals2.wsahthoc17 = vals.wsaht17 * 50.603/100
        vals2.wsalthoc17 = vals.wsalt17 * 3.969/100
        vals2.wslththoc17 = vals.wsltht17 * 53.488/100
        vals2.wsltlthoc17 = vals.wsltlt17 * 1.984/100
        vals2.ysahthoc17 = vals.ysaht17 * 50.52/100
        vals2.ysalthoc17 = vals.ysalt17 * 3.879/100
        vals2.yslththoc17 = vals.ysltht17 * 52.778/100
        vals2.ysltlthoc17 = vals.ysltlt17 * 1.984/100
        vals2.cmahthoc17 = vals.cmaht17 * 38.46/100
        vals2.cmltht1_hoc17 = vals.cmltht1_17 * 43.478/100
        vals2.cmltht2_hoc17 = vals.cmltht2_17 * 24.81/100
        vals2.cmltht3_hoc17 = vals.cmltht3_17 * 12.24/100
        vals2.cmalthoc17 = vals.cmalt17 * 3.247/100
        vals2.cmltlthoc17 = vals.cmltlt17 * 1.624/100
        vals2.smahthoc17 = vals.smaht17 * 1.624/100
        vals2.smltht1_hoc17 = vals.smltht1_17 * 23.239/100
        vals2.smltht2_hoc17 = vals.smltht2_17 * 38.771/100
        
        vals2.wsahthoc18 = vals.wsaht18 * 50.603/100
        vals2.wsalthoc18 = vals.wsalt18 * 3.969/100
        vals2.wslththoc18 = vals.wsltht18 * 53.488/100
        vals2.wsltlthoc18 = vals.wsltlt18 * 1.984/100
        vals2.ysahthoc18 = vals.ysaht18 * 50.52/100
        vals2.ysalthoc18 = vals.ysalt18 * 3.879/100
        vals2.yslththoc18 = vals.ysltht18 * 52.778/100
        vals2.ysltlthoc18 = vals.ysltlt18 * 1.984/100
        vals2.cmahthoc18 = vals.cmaht18 * 38.46/100
        vals2.cmltht1_hoc18 = vals.cmltht1_18 * 43.478/100
        vals2.cmltht2_hoc18 = vals.cmltht2_18 * 24.81/100
        vals2.cmltht3_hoc18 = vals.cmltht3_18 * 12.24/100
        vals2.cmalthoc18 = vals.cmalt18 * 3.247/100
        vals2.cmltlthoc18 = vals.cmltlt18 * 1.624/100
        vals2.smahthoc18 = vals.smaht18 * 1.624/100
        vals2.smltht1_hoc18 = vals.smltht1_18 * 23.239/100
        vals2.smltht2_hoc18 = vals.smltht2_18 * 38.771/100
        
        vals2.wsahthoc19 = vals.wsaht19 * 50.603/100
        vals2.wsalthoc19 = vals.wsalt19 * 3.969/100
        vals2.wslththoc19 = vals.wsltht19 * 53.488/100
        vals2.wsltlthoc19 = vals.wsltlt19 * 1.984/100
        vals2.ysahthoc19 = vals.ysaht19 * 50.52/100
        vals2.ysalthoc19 = vals.ysalt19 * 3.879/100
        vals2.yslththoc19 = vals.ysltht19 * 52.778/100
        vals2.ysltlthoc19 = vals.ysltlt19 * 1.984/100
        vals2.cmahthoc19 = vals.cmaht19 * 38.46/100
        vals2.cmltht1_hoc19 = vals.cmltht1_19 * 43.478/100
        vals2.cmltht2_hoc19 = vals.cmltht2_19 * 24.81/100
        vals2.cmltht3_hoc19 = vals.cmltht3_19 * 12.24/100
        vals2.cmalthoc19 = vals.cmalt19 * 3.247/100
        vals2.cmltlthoc19 = vals.cmltlt19 * 1.624/100
        vals2.smahthoc19 = vals.smaht19 * 1.624/100
        vals2.smltht1_hoc19 = vals.smltht1_19 * 23.239/100
        vals2.smltht2_hoc19 = vals.smltht2_19 * 38.771/100
        
        vals2.wsahthoc20 = vals.wsaht20 * 50.603/100
        vals2.wsalthoc20 = vals.wsalt20 * 3.969/100
        vals2.wslththoc20 = vals.wsltht20 * 53.488/100
        vals2.wsltlthoc20 = vals.wsltlt20 * 1.984/100
        vals2.ysahthoc20 = vals.ysaht20 * 50.52/100
        vals2.ysalthoc20 = vals.ysalt20 * 3.879/100
        vals2.yslththoc20 = vals.ysltht20 * 52.778/100
        vals2.ysltlthoc20 = vals.ysltlt20 * 1.984/100
        vals2.cmahthoc20 = vals.cmaht20 * 38.46/100
        vals2.cmltht1_hoc20 = vals.cmltht1_20 * 43.478/100
        vals2.cmltht2_hoc20 = vals.cmltht2_20 * 24.81/100
        vals2.cmltht3_hoc20 = vals.cmltht3_20 * 12.24/100
        vals2.cmalthoc20 = vals.cmalt20 * 3.247/100
        vals2.cmltlthoc20 = vals.cmltlt20 * 1.624/100
        vals2.smahthoc20 = vals.smaht20 * 1.624/100
        vals2.smltht1_hoc20 = vals.smltht1_20 * 23.239/100
        vals2.smltht2_hoc20 = vals.smltht2_20 * 38.771/100
        
        vals2.wsahthoc21 = vals.wsaht21 * 50.603/100
        vals2.wsalthoc21 = vals.wsalt21 * 3.969/100
        vals2.wslththoc21 = vals.wsltht21 * 53.488/100
        vals2.wsltlthoc21 = vals.wsltlt21 * 1.984/100
        vals2.ysahthoc21 = vals.ysaht21 * 50.52/100
        vals2.ysalthoc21 = vals.ysalt21 * 3.879/100
        vals2.yslththoc21 = vals.ysltht21 * 52.778/100
        vals2.ysltlthoc21 = vals.ysltlt21 * 1.984/100
        vals2.cmahthoc21 = vals.cmaht21 * 38.46/100
        vals2.cmltht1_hoc21 = vals.cmltht1_21 * 43.478/100
        vals2.cmltht2_hoc21 = vals.cmltht2_21 * 24.81/100
        vals2.cmltht3_hoc21 = vals.cmltht3_21 * 12.24/100
        vals2.cmalthoc21 = vals.cmalt21 * 3.247/100
        vals2.cmltlthoc21 = vals.cmltlt21 * 1.624/100
        vals2.smahthoc21 = vals.smaht21 * 1.624/100
        vals2.smltht1_hoc21 = vals.smltht1_21 * 23.239/100
        vals2.smltht2_hoc21 = vals.smltht2_21 * 38.771/100
        
        vals2.wsahthoc22 = vals.wsaht22 * 50.603/100
        vals2.wsalthoc22 = vals.wsalt22 * 3.969/100
        vals2.wslththoc22 = vals.wsltht22 * 53.488/100
        vals2.wsltlthoc22 = vals.wsltlt22 * 1.984/100
        vals2.ysahthoc22 = vals.ysaht22 * 50.52/100
        vals2.ysalthoc22 = vals.ysalt22 * 3.879/100
        vals2.yslththoc22 = vals.ysltht22 * 52.778/100
        vals2.ysltlthoc22 = vals.ysltlt22 * 1.984/100
        vals2.cmahthoc22 = vals.cmaht22 * 38.46/100
        vals2.cmltht1_hoc22 = vals.cmltht1_22 * 43.478/100
        vals2.cmltht2_hoc22 = vals.cmltht2_22 * 24.81/100
        vals2.cmltht3_hoc22 = vals.cmltht3_22 * 12.24/100
        vals2.cmalthoc22 = vals.cmalt22 * 3.247/100
        vals2.cmltlthoc22 = vals.cmltlt22 * 1.624/100
        vals2.smahthoc22 = vals.smaht22 * 1.624/100
        vals2.smltht1_hoc22 = vals.smltht1_22 * 23.239/100
        vals2.smltht2_hoc22 = vals.smltht2_22 * 38.771/100
        
        vals2.wsahthoc23 = vals.wsaht23 * 50.603/100
        vals2.wsalthoc23 = vals.wsalt23 * 3.969/100
        vals2.wslththoc23 = vals.wsltht23 * 53.488/100
        vals2.wsltlthoc23 = vals.wsltlt23 * 1.984/100
        vals2.ysahthoc23 = vals.ysaht23 * 50.52/100
        vals2.ysalthoc23 = vals.ysalt23 * 3.879/100
        vals2.yslththoc23 = vals.ysltht23 * 52.778/100
        vals2.ysltlthoc23 = vals.ysltlt23 * 1.984/100
        vals2.cmahthoc23 = vals.cmaht23 * 38.46/100
        vals2.cmltht1_hoc23 = vals.cmltht1_23 * 43.478/100
        vals2.cmltht2_hoc23 = vals.cmltht2_23 * 24.81/100
        vals2.cmltht3_hoc23 = vals.cmltht3_23 * 12.24/100
        vals2.cmalthoc23 = vals.cmalt23 * 3.247/100
        vals2.cmltlthoc23 = vals.cmltlt23 * 1.624/100
        vals2.smahthoc23 = vals.smaht23 * 1.624/100
        vals2.smltht1_hoc23 = vals.smltht1_23 * 23.239/100
        vals2.smltht2_hoc23 = vals.smltht2_23 * 38.771/100
        
        vals2.wsahthoc24 = vals.wsaht24 * 50.603/100
        vals2.wsalthoc24 = vals.wsalt24 * 3.969/100
        vals2.wslththoc24 = vals.wsltht24 * 53.488/100
        vals2.wsltlthoc24 = vals.wsltlt24 * 1.984/100
        vals2.ysahthoc24 = vals.ysaht24 * 50.52/100
        vals2.ysalthoc24 = vals.ysalt24 * 3.879/100
        vals2.yslththoc24 = vals.ysltht24 * 52.778/100
        vals2.ysltlthoc24 = vals.ysltlt24 * 1.984/100
        vals2.cmahthoc24 = vals.cmaht24 * 38.46/100
        vals2.cmltht1_hoc24 = vals.cmltht1_24 * 43.478/100
        vals2.cmltht2_hoc24 = vals.cmltht2_24 * 24.81/100
        vals2.cmltht3_hoc24 = vals.cmltht3_24 * 12.24/100
        vals2.cmalthoc24 = vals.cmalt24 * 3.247/100
        vals2.cmltlthoc24 = vals.cmltlt24 * 1.624/100
        vals2.smahthoc24 = vals.smaht24 * 1.624/100
        vals2.smltht1_hoc24 = vals.smltht1_24 * 23.239/100
        vals2.smltht2_hoc24 = vals.smltht2_24 * 38.771/100

        vals2.hoctotal24 = (vals2.wsahthoc24 + vals2.wsalthoc24 + vals2.wslththoc24 + vals2.wsltlthoc24 + vals2.ysahthoc24 + 
                                vals2.ysalthoc24 + vals2.yslththoc24 + vals2.ysltlthoc24 + vals2.cmahthoc24 + vals2.cmltht1_hoc24 +
                                    vals2.cmltht2_hoc24 + vals2.cmltht3_hoc24 + vals2.cmalthoc24 + vals2.cmltlthoc24 + vals2.smahthoc24 +
                                        vals2.smltht1_hoc24 + vals2.smltht2_hoc24)
        
        vals2.hoctotal23 = (vals2.wsahthoc23 + vals2.wsalthoc23 + vals2.wslththoc23 + vals2.wsltlthoc23 + vals2.ysahthoc23 + 
                                vals2.ysalthoc23 + vals2.yslththoc23 + vals2.ysltlthoc23 + vals2.cmahthoc23 + vals2.cmltht1_hoc23 +
                                    vals2.cmltht2_hoc23 + vals2.cmltht3_hoc23 + vals2.cmalthoc23 + vals2.cmltlthoc23 + vals2.smahthoc23 +
                                        vals2.smltht1_hoc23 + vals2.smltht2_hoc23)
                                        
        vals2.hoctotal22 = (vals2.wsahthoc22 + vals2.wsalthoc22 + vals2.wslththoc22 + vals2.wsltlthoc22 + vals2.ysahthoc22 + 
                                        vals2.ysalthoc22 + vals2.yslththoc22 + vals2.ysltlthoc22 + vals2.cmahthoc22 + vals2.cmltht1_hoc22 +
                                            vals2.cmltht2_hoc22 + vals2.cmltht3_hoc22 + vals2.cmalthoc22 + vals2.cmltlthoc22 + vals2.smahthoc22 +
                                                vals2.smltht1_hoc22 + vals2.smltht2_hoc22)                                        
                                                
        vals2.hoctotal21 = (vals2.wsahthoc21 + vals2.wsalthoc21 + vals2.wslththoc21 + vals2.wsltlthoc21 + vals2.ysahthoc21 + 
                                        vals2.ysalthoc21 + vals2.yslththoc21 + vals2.ysltlthoc21 + vals2.cmahthoc21 + vals2.cmltht1_hoc21 +
                                            vals2.cmltht2_hoc21 + vals2.cmltht3_hoc21 + vals2.cmalthoc21 + vals2.cmltlthoc21 + vals2.smahthoc21 +
                                                vals2.smltht1_hoc21 + vals2.smltht2_hoc21)                                        
                                                
        vals2.hoctotal20 = (vals2.wsahthoc20 + vals2.wsalthoc20 + vals2.wslththoc20 + vals2.wsltlthoc20 + vals2.ysahthoc20 + 
                                        vals2.ysalthoc20 + vals2.yslththoc20 + vals2.ysltlthoc20 + vals2.cmahthoc20 + vals2.cmltht1_hoc20 +
                                            vals2.cmltht2_hoc20 + vals2.cmltht3_hoc20 + vals2.cmalthoc20 + vals2.cmltlthoc20 + vals2.smahthoc20 +
                                                vals2.smltht1_hoc20 + vals2.smltht2_hoc20)                                        
                                                
        vals2.hoctotal19 = (vals2.wsahthoc19 + vals2.wsalthoc19 + vals2.wslththoc19 + vals2.wsltlthoc19 + vals2.ysahthoc19 + 
                                        vals2.ysalthoc19 + vals2.yslththoc19 + vals2.ysltlthoc19 + vals2.cmahthoc19 + vals2.cmltht1_hoc19 +
                                            vals2.cmltht2_hoc19 + vals2.cmltht3_hoc19 + vals2.cmalthoc19 + vals2.cmltlthoc19 + vals2.smahthoc19 +
                                                vals2.smltht1_hoc19 + vals2.smltht2_hoc19)                                 
                                        
        vals2.hoctotal18 = (vals2.wsahthoc18 + vals2.wsalthoc18 + vals2.wslththoc18 + vals2.wsltlthoc18 + vals2.ysahthoc18 + 
                                        vals2.ysalthoc18 + vals2.yslththoc18 + vals2.ysltlthoc18 + vals2.cmahthoc18 + vals2.cmltht1_hoc18 +
                                            vals2.cmltht2_hoc18 + vals2.cmltht3_hoc18 + vals2.cmalthoc18 + vals2.cmltlthoc18 + vals2.smahthoc18 +
                                                vals2.smltht1_hoc18 + vals2.smltht2_hoc18)                                 

        vals2.hoctotal17 = (vals2.wsahthoc17 + vals2.wsalthoc17 + vals2.wslththoc17 + vals2.wsltlthoc17 + vals2.ysahthoc17 + 
                                        vals2.ysalthoc17 + vals2.yslththoc17 + vals2.ysltlthoc17 + vals2.cmahthoc17 + vals2.cmltht1_hoc17 +
                                            vals2.cmltht2_hoc17 + vals2.cmltht3_hoc17 + vals2.cmalthoc17 + vals2.cmltlthoc17 + vals2.smahthoc17 +
                                                vals2.smltht1_hoc17 + vals2.smltht2_hoc17)                                     
                                                
        vals2.hoctotal16 = (vals2.wsahthoc16 + vals2.wsalthoc16 + vals2.wslththoc16 + vals2.wsltlthoc16 + vals2.ysahthoc16 + 
                                        vals2.ysalthoc16 + vals2.yslththoc16 + vals2.ysltlthoc16 + vals2.cmahthoc16 + vals2.cmltht1_hoc16 +
                                            vals2.cmltht2_hoc16 + vals2.cmltht3_hoc16 + vals2.cmalthoc16 + vals2.cmltlthoc16 + vals2.smahthoc16 +
                                                vals2.smltht1_hoc16 + vals2.smltht2_hoc16)                                         
                                                
        vals2.hoctotal15 = (vals2.wsahthoc15 + vals2.wsalthoc15 + vals2.wslththoc15 + vals2.wsltlthoc15 + vals2.ysahthoc15 + 
                                        vals2.ysalthoc15 + vals2.yslththoc15 + vals2.ysltlthoc15 + vals2.cmahthoc15 + vals2.cmltht1_hoc15 +
                                            vals2.cmltht2_hoc15 + vals2.cmltht3_hoc15 + vals2.cmalthoc15 + vals2.cmltlthoc15 + vals2.smahthoc15 +
                                                vals2.smltht1_hoc15 + vals2.smltht2_hoc15)                                         
        

        vals2.mp5and10lpet15 = vals.a5l4buis15 + vals.a10l2buis15
        vals2.mp20lpet15 = vals.a20lbuis15 + vals.a20lbbuis15
        vals2.mp5and10l15 = vals2.mp5and10lpet15/10/24
        vals2.mp20l15 = vals2.mp20lpet15/18/24
        vals2.petline15 = vals2.mp20l15 + vals2.mp5and10l15
        vals2.bibline15 = vals.mpbtotal15/12/25

        vals2.mp5and10lpet16 = vals.a5l4buis16 + vals.a10l2buis16
        vals2.mp20lpet16 = vals.a20lbuis16 + vals.a20lbbuis16
        vals2.mp5and10l16 = vals2.mp5and10lpet16/10/24
        vals2.mp20l16 = vals2.mp20lpet16/18/24
        vals2.petline16 = vals2.mp20l16 + vals2.mp5and10l16
        vals2.bibline16 = vals.mpbtotal16/12/25
        
        vals2.mp5and10lpet17 = vals.a5l4buis17 + vals.a10l2buis17
        vals2.mp20lpet17 = vals.a20lbuis17 + vals.a20lbbuis17
        vals2.mp5and10l17 = vals2.mp5and10lpet17/10/24
        vals2.mp20l17 = vals2.mp20lpet17/18/24
        vals2.petline17 = vals2.mp20l17 + vals2.mp5and10l17
        vals2.bibline17 = vals.mpbtotal17/12/25
        
        vals2.mp5and10lpet18 = vals.a5l4buis18 + vals.a10l2buis18
        vals2.mp20lpet18 = vals.a20lbuis18 + vals.a20lbbuis18
        vals2.mp5and10l18 = vals2.mp5and10lpet18/10/24
        vals2.mp20l18 = vals2.mp20lpet18/18/24
        vals2.petline18 = vals2.mp20l18 + vals2.mp5and10l18
        vals2.bibline18 = vals.mpbtotal18/12/25
        
        vals2.mp5and10lpet19 = vals.a5l4buis19 + vals.a10l2buis19
        vals2.mp20lpet19 = vals.a20lbuis19 + vals.a20lbbuis19
        vals2.mp5and10l19 = vals2.mp5and10lpet19/10/24
        vals2.mp20l19 = vals2.mp20lpet19/18/24
        vals2.petline19 = vals2.mp20l19 + vals2.mp5and10l19
        vals2.bibline19 = vals.mpbtotal19/12/25
        
        vals2.mp5and10lpet20 = vals.a5l4buis20 + vals.a10l2buis20
        vals2.mp20lpet20 = vals.a20lbuis20 + vals.a20lbbuis20
        vals2.mp5and10l20 = vals2.mp5and10lpet20/10/24
        vals2.mp20l20 = vals2.mp20lpet20/18/24
        vals2.petline20 = vals2.mp20l20 + vals2.mp5and10l20
        vals2.bibline20 = vals.mpbtotal20/12/25
        
        vals2.mp5and10lpet21 = vals.a5l4buis21 + vals.a10l2buis21
        vals2.mp20lpet21 = vals.a20lbuis21 + vals.a20lbbuis21
        vals2.mp5and10l21 = vals2.mp5and10lpet21/10/24
        vals2.mp20l21 = vals2.mp20lpet21/18/24
        vals2.petline21 = vals2.mp20l21 + vals2.mp5and10l21
        vals2.bibline21 = vals.mpbtotal21/12/25
        
        vals2.mp5and10lpet22 = vals.a5l4buis22 + vals.a10l2buis22
        vals2.mp20lpet22 = vals.a20lbuis22 + vals.a20lbbuis22
        vals2.mp5and10l22 = vals2.mp5and10lpet22/10/24
        vals2.mp20l22 = vals2.mp20lpet22/18/24
        vals2.petline22 = vals2.mp20l22 + vals2.mp5and10l22
        vals2.bibline22 = vals.mpbtotal22/12/25
        
        vals2.mp5and10lpet23 = vals.a5l4buis23 + vals.a10l2buis23
        vals2.mp20lpet23 = vals.a20lbuis23 + vals.a20lbbuis23
        vals2.mp5and10l23 = vals2.mp5and10lpet23/10/24
        vals2.mp20l23 = vals2.mp20lpet23/18/24
        vals2.petline23 = vals2.mp20l23 + vals2.mp5and10l23
        vals2.bibline23 = vals.mpbtotal23/12/25
        
        vals2.mp5and10lpet24 = vals.a5l4buis24 + vals.a10l2buis24
        vals2.mp20lpet24 = vals.a20lbuis24 + vals.a20lbbuis24
        vals2.mp5and10l24 = vals2.mp5and10lpet24/10/24
        vals2.mp20l24 = vals2.mp20lpet24/18/24
        vals2.petline24 = vals2.mp20l24 + vals2.mp5and10l24
        vals2.bibline24 = vals.mpbtotal24/12/25

        vals2.rhpko_hydro15 = vals.rhpko15/200
        vals2.rhpko_1ref15 = vals.rhpko15*0
        vals2.rhpko_2ref15 = vals.rhpko15/400
        vals2.rhpko_loadout15 = vals.rhpko15/30/52
        vals2.rhpkol_hydro15 = vals.rhpkol15/200
        vals2.rhpkol_1ref15 = vals.rhpkol15*0
        vals2.rhpkol_2ref15 = vals.rhpkol15/400
        vals2.rhpkol_loadout15 = vals.rhpkol15/30/52
        vals2.shortening_hydro15 = vals.shortening15/200
        vals2.shortening_1ref15 = vals.shortening15*0
        vals2.shortening_2ref15 = vals.shortening15/400
        vals2.shortening_loadout15 = vals.shortening15/30/52
        vals2.rhpkst_hydro15 = vals.rhpkst15/200
        vals2.rhpkst_1ref15 = vals.rhpkst15*0
        vals2.rhpkst_2ref15 = vals.rhpkst15/400
        vals2.rhpkst_loadout15 = vals.rhpkst15/30/52
        vals2.rhpo_hydro15 = vals.rhpo15/200
        vals2.rhpo_1ref15 = vals.rhpo15*0
        vals2.rhpo_2ref15 = vals.rhpo15/400
        vals2.rhpo_loadout15 = vals.rhpo15/30/52
        vals2.rpst_hydro15 = vals.rpst15/200
        vals2.rpst_1ref15 = vals.rpst15*0
        vals2.rpst_2ref15 = vals.rpst15/400
        vals2.rpst_loadout15 = vals.rpst15/30/52
        vals2.rhpst_hydro15 = vals.rhpst15/120
        vals2.rhpst_1ref15 = vals.rhpst15*0
        vals2.rhpst_2ref15 = vals.rhpst15/400
        vals2.rhpst_loadout15 = vals.rhpst15/30/52
        vals2.rhcno_hydro15 = vals.rhcno15/200
        vals2.rhcno_1ref15 = vals.rhcno15*0
        vals2.rhcno_2ref15 = vals.rhcno15/400
        vals2.rhcno_loadout15 = vals.rhcno15/30/52
        vals2.rcno_hydro15 = vals.rcno15/200
        vals2.rcno_1ref15 = vals.rcno15*0
        vals2.rcno_2ref15 = vals.rcno15/400
        vals2.rcno_loadout15 = vals.rcno15/30/52
        vals2.rpko_hydro15 = vals.rpko15/200
        vals2.rpko_1ref15 = vals.rpko15*0
        vals2.rpko_2ref15 = vals.rpko15/400
        vals2.rpko_loadout15 = vals.rpko15/30/52

        vals2.rhpko_hydro16 = vals.rhpko16/200
        vals2.rhpko_1ref16 = vals.rhpko16*0
        vals2.rhpko_2ref16 = vals.rhpko16/400
        vals2.rhpko_loadout16 = vals.rhpko16/30/52
        vals2.rhpkol_hydro16 = vals.rhpkol16/200
        vals2.rhpkol_1ref16 = vals.rhpkol16*0
        vals2.rhpkol_2ref16 = vals.rhpkol16/400
        vals2.rhpkol_loadout16 = vals.rhpkol16/30/52
        vals2.shortening_hydro16 = vals.shortening16/200
        vals2.shortening_1ref16 = vals.shortening16*0
        vals2.shortening_2ref16 = vals.shortening16/400
        vals2.shortening_loadout16 = vals.shortening16/30/52
        vals2.rhpkst_hydro16 = vals.rhpkst16/200
        vals2.rhpkst_1ref16 = vals.rhpkst16*0
        vals2.rhpkst_2ref16 = vals.rhpkst16/400
        vals2.rhpkst_loadout16 = vals.rhpkst16/30/52
        vals2.rhpo_hydro16 = vals.rhpo16/200
        vals2.rhpo_1ref16 = vals.rhpo16*0
        vals2.rhpo_2ref16 = vals.rhpo16/400
        vals2.rhpo_loadout16 = vals.rhpo16/30/52
        vals2.rpst_hydro16 = vals.rpst16/200
        vals2.rpst_1ref16 = vals.rpst16*0
        vals2.rpst_2ref16 = vals.rpst16/400
        vals2.rpst_loadout16 = vals.rpst16/30/52
        vals2.rhpst_hydro16 = vals.rhpst16/120
        vals2.rhpst_1ref16 = vals.rhpst16*0
        vals2.rhpst_2ref16 = vals.rhpst16/400
        vals2.rhpst_loadout16 = vals.rhpst16/30/52
        vals2.rhcno_hydro16 = vals.rhcno16/200
        vals2.rhcno_1ref16 = vals.rhcno16*0
        vals2.rhcno_2ref16 = vals.rhcno16/400
        vals2.rhcno_loadout16 = vals.rhcno16/30/52
        vals2.rcno_hydro16 = vals.rcno16/200
        vals2.rcno_1ref16 = vals.rcno16*0
        vals2.rcno_2ref16 = vals.rcno16/400
        vals2.rcno_loadout16 = vals.rcno16/30/52
        vals2.rpko_hydro16 = vals.rpko16/200
        vals2.rpko_1ref16 = vals.rpko16*0
        vals2.rpko_2ref16 = vals.rpko16/400
        vals2.rpko_loadout16 = vals.rpko16/30/52
        
        vals2.rhpko_hydro17 = vals.rhpko17/200
        vals2.rhpko_1ref17 = vals.rhpko17*0
        vals2.rhpko_2ref17 = vals.rhpko17/400
        vals2.rhpko_loadout17 = vals.rhpko17/30/52
        vals2.rhpkol_hydro17 = vals.rhpkol17/200
        vals2.rhpkol_1ref17 = vals.rhpkol17*0
        vals2.rhpkol_2ref17 = vals.rhpkol17/400
        vals2.rhpkol_loadout17 = vals.rhpkol17/30/52
        vals2.shortening_hydro17 = vals.shortening17/200
        vals2.shortening_1ref17 = vals.shortening17*0
        vals2.shortening_2ref17 = vals.shortening17/400
        vals2.shortening_loadout17 = vals.shortening17/30/52
        vals2.rhpkst_hydro17 = vals.rhpkst17/200
        vals2.rhpkst_1ref17 = vals.rhpkst17*0
        vals2.rhpkst_2ref17 = vals.rhpkst17/400
        vals2.rhpkst_loadout17 = vals.rhpkst17/30/52
        vals2.rhpo_hydro17 = vals.rhpo17/200
        vals2.rhpo_1ref17 = vals.rhpo17*0
        vals2.rhpo_2ref17 = vals.rhpo17/400
        vals2.rhpo_loadout17 = vals.rhpo17/30/52
        vals2.rpst_hydro17 = vals.rpst17/200
        vals2.rpst_1ref17 = vals.rpst17*0
        vals2.rpst_2ref17 = vals.rpst17/400
        vals2.rpst_loadout17 = vals.rpst17/30/52
        vals2.rhpst_hydro17 = vals.rhpst17/120
        vals2.rhpst_1ref17 = vals.rhpst17*0
        vals2.rhpst_2ref17 = vals.rhpst17/400
        vals2.rhpst_loadout17 = vals.rhpst17/30/52
        vals2.rhcno_hydro17 = vals.rhcno17/200
        vals2.rhcno_1ref17 = vals.rhcno17*0
        vals2.rhcno_2ref17 = vals.rhcno17/400
        vals2.rhcno_loadout17 = vals.rhcno17/30/52
        vals2.rcno_hydro17 = vals.rcno17/200
        vals2.rcno_1ref17 = vals.rcno17*0
        vals2.rcno_2ref17 = vals.rcno17/400
        vals2.rcno_loadout17 = vals.rcno17/30/52
        vals2.rpko_hydro17 = vals.rpko17/200
        vals2.rpko_1ref17 = vals.rpko17*0
        vals2.rpko_2ref17 = vals.rpko17/400
        vals2.rpko_loadout17 = vals.rpko17/30/52
        
        vals2.rhpko_hydro18 = vals.rhpko18/200
        vals2.rhpko_1ref18 = vals.rhpko18*0
        vals2.rhpko_2ref18 = vals.rhpko18/400
        vals2.rhpko_loadout18 = vals.rhpko18/30/52
        vals2.rhpkol_hydro18 = vals.rhpkol18/200
        vals2.rhpkol_1ref18 = vals.rhpkol18*0
        vals2.rhpkol_2ref18 = vals.rhpkol18/400
        vals2.rhpkol_loadout18 = vals.rhpkol18/30/52
        vals2.shortening_hydro18 = vals.shortening18/200
        vals2.shortening_1ref18 = vals.shortening18*0
        vals2.shortening_2ref18 = vals.shortening18/400
        vals2.shortening_loadout18 = vals.shortening18/30/52
        vals2.rhpkst_hydro18 = vals.rhpkst18/200
        vals2.rhpkst_1ref18 = vals.rhpkst18*0
        vals2.rhpkst_2ref18 = vals.rhpkst18/400
        vals2.rhpkst_loadout18 = vals.rhpkst18/30/52
        vals2.rhpo_hydro18 = vals.rhpo18/200
        vals2.rhpo_1ref18 = vals.rhpo18*0
        vals2.rhpo_2ref18 = vals.rhpo18/400
        vals2.rhpo_loadout18 = vals.rhpo18/30/52
        vals2.rpst_hydro18 = vals.rpst18/200
        vals2.rpst_1ref18 = vals.rpst18*0
        vals2.rpst_2ref18 = vals.rpst18/400
        vals2.rpst_loadout18 = vals.rpst18/30/52
        vals2.rhpst_hydro18 = vals.rhpst18/120
        vals2.rhpst_1ref18 = vals.rhpst18*0
        vals2.rhpst_2ref18 = vals.rhpst18/400
        vals2.rhpst_loadout18 = vals.rhpst18/30/52
        vals2.rhcno_hydro18 = vals.rhcno18/200
        vals2.rhcno_1ref18 = vals.rhcno18*0
        vals2.rhcno_2ref18 = vals.rhcno18/400
        vals2.rhcno_loadout18 = vals.rhcno18/30/52
        vals2.rcno_hydro18 = vals.rcno18/200
        vals2.rcno_1ref18 = vals.rcno18*0
        vals2.rcno_2ref18 = vals.rcno18/400
        vals2.rcno_loadout18 = vals.rcno18/30/52
        vals2.rpko_hydro18 = vals.rpko18/200
        vals2.rpko_1ref18 = vals.rpko18*0
        vals2.rpko_2ref18 = vals.rpko18/400
        vals2.rpko_loadout18 = vals.rpko18/30/52
        
        vals2.rhpko_hydro19 = vals.rhpko19/200
        vals2.rhpko_1ref19 = vals.rhpko19*0
        vals2.rhpko_2ref19 = vals.rhpko19/400
        vals2.rhpko_loadout19 = vals.rhpko19/30/52
        vals2.rhpkol_hydro19 = vals.rhpkol19/200
        vals2.rhpkol_1ref19 = vals.rhpkol19*0
        vals2.rhpkol_2ref19 = vals.rhpkol19/400
        vals2.rhpkol_loadout19 = vals.rhpkol19/30/52
        vals2.shortening_hydro19 = vals.shortening19/200
        vals2.shortening_1ref19 = vals.shortening19*0
        vals2.shortening_2ref19 = vals.shortening19/400
        vals2.shortening_loadout19 = vals.shortening19/30/52
        vals2.rhpkst_hydro19 = vals.rhpkst19/200
        vals2.rhpkst_1ref19 = vals.rhpkst19*0
        vals2.rhpkst_2ref19 = vals.rhpkst19/400
        vals2.rhpkst_loadout19 = vals.rhpkst19/30/52
        vals2.rhpo_hydro19 = vals.rhpo19/200
        vals2.rhpo_1ref19 = vals.rhpo19*0
        vals2.rhpo_2ref19 = vals.rhpo19/400
        vals2.rhpo_loadout19 = vals.rhpo19/30/52
        vals2.rpst_hydro19 = vals.rpst19/200
        vals2.rpst_1ref19 = vals.rpst19*0
        vals2.rpst_2ref19 = vals.rpst19/400
        vals2.rpst_loadout19 = vals.rpst19/30/52
        vals2.rhpst_hydro19 = vals.rhpst19/120
        vals2.rhpst_1ref19 = vals.rhpst19*0
        vals2.rhpst_2ref19 = vals.rhpst19/400
        vals2.rhpst_loadout19 = vals.rhpst19/30/52
        vals2.rhcno_hydro19 = vals.rhcno19/200
        vals2.rhcno_1ref19 = vals.rhcno19*0
        vals2.rhcno_2ref19 = vals.rhcno19/400
        vals2.rhcno_loadout19 = vals.rhcno19/30/52
        vals2.rcno_hydro19 = vals.rcno19/200
        vals2.rcno_1ref19 = vals.rcno19*0
        vals2.rcno_2ref19 = vals.rcno19/400
        vals2.rcno_loadout19 = vals.rcno19/30/52
        vals2.rpko_hydro19 = vals.rpko19/200
        vals2.rpko_1ref19 = vals.rpko19*0
        vals2.rpko_2ref19 = vals.rpko19/400
        vals2.rpko_loadout19 = vals.rpko19/30/52
        
        vals2.rhpko_hydro20 = vals.rhpko20/200
        vals2.rhpko_1ref20 = vals.rhpko20*0
        vals2.rhpko_2ref20 = vals.rhpko20/400
        vals2.rhpko_loadout20 = vals.rhpko20/30/52
        vals2.rhpkol_hydro20 = vals.rhpkol20/200
        vals2.rhpkol_1ref20 = vals.rhpkol20*0
        vals2.rhpkol_2ref20 = vals.rhpkol20/400
        vals2.rhpkol_loadout20 = vals.rhpkol20/30/52
        vals2.shortening_hydro20 = vals.shortening20/200
        vals2.shortening_1ref20 = vals.shortening20*0
        vals2.shortening_2ref20 = vals.shortening20/400
        vals2.shortening_loadout20 = vals.shortening20/30/52
        vals2.rhpkst_hydro20 = vals.rhpkst20/200
        vals2.rhpkst_1ref20 = vals.rhpkst20*0
        vals2.rhpkst_2ref20 = vals.rhpkst20/400
        vals2.rhpkst_loadout20 = vals.rhpkst20/30/52
        vals2.rhpo_hydro20 = vals.rhpo20/200
        vals2.rhpo_1ref20 = vals.rhpo20*0
        vals2.rhpo_2ref20 = vals.rhpo20/400
        vals2.rhpo_loadout20 = vals.rhpo20/30/52
        vals2.rpst_hydro20 = vals.rpst20/200
        vals2.rpst_1ref20 = vals.rpst20*0
        vals2.rpst_2ref20 = vals.rpst20/400
        vals2.rpst_loadout20 = vals.rpst20/30/52
        vals2.rhpst_hydro20 = vals.rhpst20/120
        vals2.rhpst_1ref20 = vals.rhpst20*0
        vals2.rhpst_2ref20 = vals.rhpst20/400
        vals2.rhpst_loadout20 = vals.rhpst20/30/52
        vals2.rhcno_hydro20 = vals.rhcno20/200
        vals2.rhcno_1ref20 = vals.rhcno20*0
        vals2.rhcno_2ref20 = vals.rhcno20/400
        vals2.rhcno_loadout20 = vals.rhcno20/30/52
        vals2.rcno_hydro20 = vals.rcno20/200
        vals2.rcno_1ref20 = vals.rcno20*0
        vals2.rcno_2ref20 = vals.rcno20/400
        vals2.rcno_loadout20 = vals.rcno20/30/52
        vals2.rpko_hydro20 = vals.rpko20/200
        vals2.rpko_1ref20 = vals.rpko20*0
        vals2.rpko_2ref20 = vals.rpko20/400
        vals2.rpko_loadout20 = vals.rpko20/30/52
        
        vals2.rhpko_hydro21 = vals.rhpko21/200
        vals2.rhpko_1ref21 = vals.rhpko21*0
        vals2.rhpko_2ref21 = vals.rhpko21/400
        vals2.rhpko_loadout21 = vals.rhpko21/30/52
        vals2.rhpkol_hydro21 = vals.rhpkol21/200
        vals2.rhpkol_1ref21 = vals.rhpkol21*0
        vals2.rhpkol_2ref21 = vals.rhpkol21/400
        vals2.rhpkol_loadout21 = vals.rhpkol21/30/52
        vals2.shortening_hydro21 = vals.shortening21/200
        vals2.shortening_1ref21 = vals.shortening21*0
        vals2.shortening_2ref21 = vals.shortening21/400
        vals2.shortening_loadout21 = vals.shortening21/30/52
        vals2.rhpkst_hydro21 = vals.rhpkst21/200
        vals2.rhpkst_1ref21 = vals.rhpkst21*0
        vals2.rhpkst_2ref21 = vals.rhpkst21/400
        vals2.rhpkst_loadout21 = vals.rhpkst21/30/52
        vals2.rhpo_hydro21 = vals.rhpo21/200
        vals2.rhpo_1ref21 = vals.rhpo21*0
        vals2.rhpo_2ref21 = vals.rhpo21/400
        vals2.rhpo_loadout21 = vals.rhpo21/30/52
        vals2.rpst_hydro21 = vals.rpst21/200
        vals2.rpst_1ref21 = vals.rpst21*0
        vals2.rpst_2ref21 = vals.rpst21/400
        vals2.rpst_loadout21 = vals.rpst21/30/52
        vals2.rhpst_hydro21 = vals.rhpst21/120
        vals2.rhpst_1ref21 = vals.rhpst21*0
        vals2.rhpst_2ref21 = vals.rhpst21/400
        vals2.rhpst_loadout21 = vals.rhpst21/30/52
        vals2.rhcno_hydro21 = vals.rhcno21/200
        vals2.rhcno_1ref21 = vals.rhcno21*0
        vals2.rhcno_2ref21 = vals.rhcno21/400
        vals2.rhcno_loadout21 = vals.rhcno21/30/52
        vals2.rcno_hydro21 = vals.rcno21/200
        vals2.rcno_1ref21 = vals.rcno21*0
        vals2.rcno_2ref21 = vals.rcno21/400
        vals2.rcno_loadout21 = vals.rcno21/30/52
        vals2.rpko_hydro21 = vals.rpko21/200
        vals2.rpko_1ref21 = vals.rpko21*0
        vals2.rpko_2ref21 = vals.rpko21/400
        vals2.rpko_loadout21 = vals.rpko21/30/52
        
        vals2.rhpko_hydro22 = vals.rhpko22/200
        vals2.rhpko_1ref22 = vals.rhpko22*0
        vals2.rhpko_2ref22 = vals.rhpko22/400
        vals2.rhpko_loadout22 = vals.rhpko22/30/52
        vals2.rhpkol_hydro22 = vals.rhpkol22/200
        vals2.rhpkol_1ref22 = vals.rhpkol22*0
        vals2.rhpkol_2ref22 = vals.rhpkol22/400
        vals2.rhpkol_loadout22 = vals.rhpkol22/30/52
        vals2.shortening_hydro22 = vals.shortening22/200
        vals2.shortening_1ref22 = vals.shortening22*0
        vals2.shortening_2ref22 = vals.shortening22/400
        vals2.shortening_loadout22 = vals.shortening22/30/52
        vals2.rhpkst_hydro22 = vals.rhpkst22/200
        vals2.rhpkst_1ref22 = vals.rhpkst22*0
        vals2.rhpkst_2ref22 = vals.rhpkst22/400
        vals2.rhpkst_loadout22 = vals.rhpkst22/30/52
        vals2.rhpo_hydro22 = vals.rhpo22/200
        vals2.rhpo_1ref22 = vals.rhpo22*0
        vals2.rhpo_2ref22 = vals.rhpo22/400
        vals2.rhpo_loadout22 = vals.rhpo22/30/52
        vals2.rpst_hydro22 = vals.rpst22/200
        vals2.rpst_1ref22 = vals.rpst22*0
        vals2.rpst_2ref22 = vals.rpst22/400
        vals2.rpst_loadout22 = vals.rpst22/30/52
        vals2.rhpst_hydro22 = vals.rhpst22/120
        vals2.rhpst_1ref22 = vals.rhpst22*0
        vals2.rhpst_2ref22 = vals.rhpst22/400
        vals2.rhpst_loadout22 = vals.rhpst22/30/52
        vals2.rhcno_hydro22 = vals.rhcno22/200
        vals2.rhcno_1ref22 = vals.rhcno22*0
        vals2.rhcno_2ref22 = vals.rhcno22/400
        vals2.rhcno_loadout22 = vals.rhcno22/30/52
        vals2.rcno_hydro22 = vals.rcno22/200
        vals2.rcno_1ref22 = vals.rcno22*0
        vals2.rcno_2ref22 = vals.rcno22/400
        vals2.rcno_loadout22 = vals.rcno22/30/52
        vals2.rpko_hydro22 = vals.rpko22/200
        vals2.rpko_1ref22 = vals.rpko22*0
        vals2.rpko_2ref22 = vals.rpko22/400
        vals2.rpko_loadout22 = vals.rpko22/30/52
        
        vals2.rhpko_hydro23 = vals.rhpko23/200
        vals2.rhpko_1ref23 = vals.rhpko23*0
        vals2.rhpko_2ref23 = vals.rhpko23/400
        vals2.rhpko_loadout23 = vals.rhpko23/30/52
        vals2.rhpkol_hydro23 = vals.rhpkol23/200
        vals2.rhpkol_1ref23 = vals.rhpkol23*0
        vals2.rhpkol_2ref23 = vals.rhpkol23/400
        vals2.rhpkol_loadout23 = vals.rhpkol23/30/52
        vals2.shortening_hydro23 = vals.shortening23/200
        vals2.shortening_1ref23 = vals.shortening23*0
        vals2.shortening_2ref23 = vals.shortening23/400
        vals2.shortening_loadout23 = vals.shortening23/30/52
        vals2.rhpkst_hydro23 = vals.rhpkst23/200
        vals2.rhpkst_1ref23 = vals.rhpkst23*0
        vals2.rhpkst_2ref23 = vals.rhpkst23/400
        vals2.rhpkst_loadout23 = vals.rhpkst23/30/52
        vals2.rhpo_hydro23 = vals.rhpo23/200
        vals2.rhpo_1ref23 = vals.rhpo23*0
        vals2.rhpo_2ref23 = vals.rhpo23/400
        vals2.rhpo_loadout23 = vals.rhpo23/30/52
        vals2.rpst_hydro23 = vals.rpst23/200
        vals2.rpst_1ref23 = vals.rpst23*0
        vals2.rpst_2ref23 = vals.rpst23/400
        vals2.rpst_loadout23 = vals.rpst23/30/52
        vals2.rhpst_hydro23 = vals.rhpst23/120
        vals2.rhpst_1ref23 = vals.rhpst23*0
        vals2.rhpst_2ref23 = vals.rhpst23/400
        vals2.rhpst_loadout23 = vals.rhpst23/30/52
        vals2.rhcno_hydro23 = vals.rhcno23/200
        vals2.rhcno_1ref23 = vals.rhcno23*0
        vals2.rhcno_2ref23 = vals.rhcno23/400
        vals2.rhcno_loadout23 = vals.rhcno23/30/52
        vals2.rcno_hydro23 = vals.rcno23/200
        vals2.rcno_1ref23 = vals.rcno23*0
        vals2.rcno_2ref23 = vals.rcno23/400
        vals2.rcno_loadout23 = vals.rcno23/30/52
        vals2.rpko_hydro23 = vals.rpko23/200
        vals2.rpko_1ref23 = vals.rpko23*0
        vals2.rpko_2ref23 = vals.rpko23/400
        vals2.rpko_loadout23 = vals.rpko23/30/52
        
        vals2.rhpko_hydro24 = vals.rhpko24/200
        vals2.rhpko_1ref24 = vals.rhpko24*0
        vals2.rhpko_2ref24 = vals.rhpko24/400
        vals2.rhpko_loadout24 = vals.rhpko24/30/52
        vals2.rhpkol_hydro24 = vals.rhpkol24/200
        vals2.rhpkol_1ref24 = vals.rhpkol24*0
        vals2.rhpkol_2ref24 = vals.rhpkol24/400
        vals2.rhpkol_loadout24 = vals.rhpkol24/30/52
        vals2.shortening_hydro24 = vals.shortening24/200
        vals2.shortening_1ref24 = vals.shortening24*0
        vals2.shortening_2ref24 = vals.shortening24/400
        vals2.shortening_loadout24 = vals.shortening24/30/52
        vals2.rhpkst_hydro24 = vals.rhpkst24/200
        vals2.rhpkst_1ref24 = vals.rhpkst24*0
        vals2.rhpkst_2ref24 = vals.rhpkst24/400
        vals2.rhpkst_loadout24 = vals.rhpkst24/30/52
        vals2.rhpo_hydro24 = vals.rhpo24/200
        vals2.rhpo_1ref24 = vals.rhpo24*0
        vals2.rhpo_2ref24 = vals.rhpo24/400
        vals2.rhpo_loadout24 = vals.rhpo24/30/52
        vals2.rpst_hydro24 = vals.rpst24/200
        vals2.rpst_1ref24 = vals.rpst24*0
        vals2.rpst_2ref24 = vals.rpst24/400
        vals2.rpst_loadout24 = vals.rpst24/30/52
        vals2.rhpst_hydro24 = vals.rhpst24/120
        vals2.rhpst_1ref24 = vals.rhpst24*0
        vals2.rhpst_2ref24 = vals.rhpst24/400
        vals2.rhpst_loadout24 = vals.rhpst24/30/52
        vals2.rhcno_hydro24 = vals.rhcno24/200
        vals2.rhcno_1ref24 = vals.rhcno24*0
        vals2.rhcno_2ref24 = vals.rhcno24/400
        vals2.rhcno_loadout24 = vals.rhcno24/30/52
        vals2.rcno_hydro24 = vals.rcno24/200
        vals2.rcno_1ref24 = vals.rcno24*0
        vals2.rcno_2ref24 = vals.rcno24/400
        vals2.rcno_loadout24 = vals.rcno24/30/52
        vals2.rpko_hydro24 = vals.rpko24/200
        vals2.rpko_1ref24 = vals.rpko24*0
        vals2.rpko_2ref24 = vals.rpko24/400
        vals2.rpko_loadout24 = vals.rpko24/30/52

        vals2.apshortening_2ref15 = vals.apshortening15/400
        vals2.apshortening_perf15 = vals.apshortening15*100/7.5/24/80
        vals2.rhpoc_2ref15 = vals.rhpoc15/400
        vals2.rhpoc_perf15 = vals.rhpoc15*100/7.5/24/80
        vals2.rhsbo_2ref15 = vals.rhsbo15/400
        vals2.rhsbo_perf15 = vals.rhsbo15*100/7.5/24/80
        vals2.apshortening_2ref16 = vals.apshortening16/400
        vals2.apshortening_perf16 = vals.apshortening16*100/7.5/24/80
        vals2.rhpoc_2ref16 = vals.rhpoc16/400
        vals2.rhpoc_perf16 = vals.rhpoc16/7.5/24
        vals2.rhsbo_2ref16 = vals.rhsbo16/400
        vals2.rhsbo_perf16 = vals.rhsbo16*100/7.5/24/80
        vals2.apshortening_2ref17 = vals.apshortening17/400
        vals2.apshortening_perf17 = vals.apshortening17*100/7.5/24/80
        vals2.rhpoc_2ref17 = vals.rhpoc17/400
        vals2.rhpoc_perf17 = vals.rhpoc17/7.5/24
        vals2.rhsbo_2ref17 = vals.rhsbo17/400
        vals2.rhsbo_perf17 = vals.rhsbo17*100/7.5/24/80
        vals2.apshortening_2ref18 = vals.apshortening18/400
        vals2.apshortening_perf18 = vals.apshortening18*100/7.5/24/80
        vals2.rhpoc_2ref18 = vals.rhpoc18/400
        vals2.rhpoc_perf18 = vals.rhpoc18/7.5/24
        vals2.rhsbo_2ref18 = vals.rhsbo18/400
        vals2.rhsbo_perf18 = vals.rhsbo18*100/7.5/24/80
        vals2.apshortening_2ref19 = vals.apshortening19/400
        vals2.apshortening_perf19 = vals.apshortening19*100/7.5/24/80
        vals2.rhpoc_2ref19 = vals.rhpoc19/400
        vals2.rhpoc_perf19 = vals.rhpoc19/7.5/24
        vals2.rhsbo_2ref19 = vals.rhsbo19/400
        vals2.rhsbo_perf19 = vals.rhsbo19*100/7.5/24/80
        vals2.apshortening_2ref20 = vals.apshortening20/400
        vals2.apshortening_perf20 = vals.apshortening20*100/7.5/24/80
        vals2.rhpoc_2ref20 = vals.rhpoc20/400
        vals2.rhpoc_perf20 = vals.rhpoc20/7.5/24
        vals2.rhsbo_2ref20 = vals.rhsbo20/400
        vals2.rhsbo_perf20 = vals.rhsbo20*100/7.5/24/80
        vals2.apshortening_2ref21 = vals.apshortening21/400
        vals2.apshortening_perf21 = vals.apshortening21*100/7.5/24/80
        vals2.rhpoc_2ref21 = vals.rhpoc21/400
        vals2.rhpoc_perf21 = vals.rhpoc21/7.5/24
        vals2.rhsbo_2ref21 = vals.rhsbo21/400
        vals2.rhsbo_perf21 = vals.rhsbo21*100/7.5/24/80
        vals2.apshortening_2ref22 = vals.apshortening22/400
        vals2.apshortening_perf22 = vals.apshortening22*100/7.5/24/80
        vals2.rhpoc_2ref22 = vals.rhpoc22/400
        vals2.rhpoc_perf22 = vals.rhpoc22/7.5/24
        vals2.rhsbo_2ref22 = vals.rhsbo22/400
        vals2.rhsbo_perf22 = vals.rhsbo22*100/7.5/24/80
        vals2.apshortening_2ref23 = vals.apshortening23/400
        vals2.apshortening_perf23 = vals.apshortening23*100/7.5/24/80
        vals2.rhpoc_2ref23 = vals.rhpoc23/400
        vals2.rhpoc_perf23 = vals.rhpoc23/7.5/24
        vals2.rhsbo_2ref23 = vals.rhsbo23/400
        vals2.rhsbo_perf23 = vals.rhsbo23*100/7.5/24/80
        vals2.apshortening_2ref24 = vals.apshortening24/400
        vals2.apshortening_perf24 = vals.apshortening24*100/7.5/24/80
        vals2.rhpoc_2ref24 = vals.rhpoc24/400
        vals2.rhpoc_perf24 = vals.rhpoc24/7.5/24
        vals2.rhsbo_2ref24 = vals.rhsbo24/400
        vals2.rhsbo_perf24 = vals.rhsbo24*100/7.5/24/80

        vals2.ls_bibline15 = vals.ls15/10/24
        vals2.niscfl2_15 = vals.nis15*100/7.5/24/75
        vals2.nimcfl2_15 = vals.nim15*100/4.5/24/75
        vals2.iscfl2_15 = vals.is15*100/7.5/24/75
        vals2.imcfl2_15 = vals.im15*100/4.5/24/75
        vals2.asm_perf15 = vals.asm15*100/2/24/75
        vals2.asm_smp15 = vals.asm15/2/24
        vals2.ls_bibline16 = vals.ls16/10/24
        vals2.niscfl2_16 = vals.nis16*100/7.5/24/75
        vals2.nimcfl2_16 = vals.nim16*100/4.5/24/75
        vals2.iscfl2_16 = vals.is16*100/7.5/24/75
        vals2.imcfl2_16 = vals.im16*100/4.5/24/75
        vals2.asm_perf16 = vals.asm16*100/2/24/75
        vals2.asm_smp16 = vals.asm16/2/24
        vals2.ls_bibline17 = vals.ls17/10/24
        vals2.niscfl2_17 = vals.nis17*100/7.5/24/75
        vals2.nimcfl2_17 = vals.nim17*100/4.5/24/75
        vals2.iscfl2_17 = vals.is17*100/7.5/24/75
        vals2.imcfl2_17 = vals.im17*100/4.5/24/75
        vals2.asm_perf17 = vals.asm17*100/2/24/75
        vals2.asm_smp17 = vals.asm17/2/24
        vals2.ls_bibline18 = vals.ls18/10/24
        vals2.niscfl2_18 = vals.nis18*100/7.5/24/75
        vals2.nimcfl2_18 = vals.nim18*100/4.5/24/75
        vals2.iscfl2_18 = vals.is18*100/7.5/24/75
        vals2.imcfl2_18 = vals.im18*100/4.5/24/75
        vals2.asm_perf18 = vals.asm18*100/2/24/75
        vals2.asm_smp18 = vals.asm18/2/24
        vals2.ls_bibline19 = vals.ls19/10/24
        vals2.niscfl2_19 = vals.nis19*100/7.5/24/75
        vals2.nimcfl2_19 = vals.nim19*100/4.5/24/75
        vals2.iscfl2_19 = vals.is19*100/7.5/24/75
        vals2.imcfl2_19 = vals.im19*100/4.5/24/75
        vals2.asm_perf19 = vals.asm19*100/2/24/75
        vals2.asm_smp19 = vals.asm19/2/24
        vals2.ls_bibline20 = vals.ls20/10/24
        vals2.niscfl2_20 = vals.nis20*100/7.5/24/75
        vals2.nimcfl2_20 = vals.nim20*100/4.5/24/75
        vals2.iscfl2_20 = vals.is20*100/7.5/24/75
        vals2.imcfl2_20 = vals.im20*100/4.5/24/75
        vals2.asm_perf20 = vals.asm20*100/2/24/75
        vals2.asm_smp20 = vals.asm20/2/24
        vals2.ls_bibline21 = vals.ls21/10/24
        vals2.niscfl2_21 = vals.nis21*100/7.5/24/75
        vals2.nimcfl2_21 = vals.nim21*100/4.5/24/75
        vals2.iscfl2_21 = vals.is21*100/7.5/24/75
        vals2.imcfl2_21 = vals.im21*100/4.5/24/75
        vals2.asm_perf21 = vals.asm21*100/2/24/75
        vals2.asm_smp21 = vals.asm21/2/24
        vals2.ls_bibline22 = vals.ls22/10/24
        vals2.niscfl2_22 = vals.nis22*100/7.5/24/75
        vals2.nimcfl2_22 = vals.nim22*100/4.5/24/75
        vals2.iscfl2_22 = vals.is22*100/7.5/24/75
        vals2.imcfl2_22 = vals.im22*100/4.5/24/75
        vals2.asm_perf22 = vals.asm22*100/2/24/75
        vals2.asm_smp22 = vals.asm22/2/24
        vals2.ls_bibline23 = vals.ls23/10/24
        vals2.niscfl2_23 = vals.nis23*100/7.5/24/75
        vals2.nimcfl2_23 = vals.nim23*100/4.5/24/75
        vals2.iscfl2_23 = vals.is23*100/7.5/24/75
        vals2.imcfl2_23 = vals.im23*100/4.5/24/75
        vals2.asm_perf23 = vals.asm23*100/2/24/75
        vals2.asm_smp23 = vals.asm23/2/24
        vals2.ls_bibline24 = vals.ls24/10/24
        vals2.niscfl2_24 = vals.nis24*100/7.5/24/75
        vals2.nimcfl2_24 = vals.nim24*100/4.5/24/75
        vals2.iscfl2_24 = vals.is24*100/7.5/24/75
        vals2.imcfl2_24 = vals.im24*100/4.5/24/75
        vals2.asm_perf24 = vals.asm24*100/2/24/75
        vals2.asm_smp24 = vals.asm24/2/24

        vals2.ieoilb15 = vals2.ieoil15/80
        vals2.ieoild15 = vals2.ieoil15/100
        vals2.hoilh15 = vals2.hoil15/100
        vals2.hoilr15 = vals2.hoil15/400
        vals2.ieoilb16 = vals2.ieoil16/80
        vals2.ieoild16 = vals2.ieoil16/100
        vals2.hoilh16 = vals2.hoil16/100
        vals2.hoilr16 = vals2.hoil16/400
        vals2.ieoilb17 = vals2.ieoil17/80
        vals2.ieoild17 = vals2.ieoil17/100
        vals2.hoilh17 = vals2.hoil17/100
        vals2.hoilr17 = vals2.hoil17/400
        vals2.ieoilb18 = vals2.ieoil18/80
        vals2.ieoild18 = vals2.ieoil18/100
        vals2.hoilh18 = vals2.hoil18/100
        vals2.hoilr18 = vals2.hoil18/400
        vals2.ieoilb19 = vals2.ieoil19/80
        vals2.ieoild19 = vals2.ieoil19/100
        vals2.hoilh19 = vals2.hoil19/100
        vals2.hoilr19 = vals2.hoil19/400
        vals2.ieoilb20 = vals2.ieoil20/80
        vals2.ieoild20 = vals2.ieoil20/100
        vals2.hoilh20 = vals2.hoil20/100
        vals2.hoilr20 = vals2.hoil20/400
        vals2.ieoilb21 = vals2.ieoil21/80
        vals2.ieoild21 = vals2.ieoil21/100
        vals2.hoilh21 = vals2.hoil21/100
        vals2.hoilr21 = vals2.hoil21/400
        vals2.ieoilb22 = vals2.ieoil22/80
        vals2.ieoild22 = vals2.ieoil22/100
        vals2.hoilh22 = vals2.hoil22/100
        vals2.hoilr22 = vals2.hoil22/400
        vals2.ieoilb23 = vals2.ieoil23/80
        vals2.ieoild23 = vals2.ieoil23/100
        vals2.hoilh23 = vals2.hoil23/100
        vals2.hoilr23 = vals2.hoil23/400
        vals2.ieoilb24 = vals2.ieoil24/80
        vals2.ieoild24 = vals2.ieoil24/100
        vals2.hoilh24 = vals2.hoil24/100
        vals2.hoilr24 = vals2.hoil24/400

        vals2.rhsbo_hydro15 = vals.rhsbo15/120
        vals2.rhpoc_hydro15 = vals.rhpoc15/120
        vals2.neutral15 = vals.sob_n15 + vals.cpf_n15
        vals2.neutral_ecu15 = vals2.neutral15/350*100
        vals2.dewaxing15 = vals.sob_d15 + vals.cpf_d15
        vals2.dewaxing_ecu15 = vals2.dewaxing15/350*100
        vals2.firstref15 = vals.sob_fr15 + vals.cpf_fr15 + vals2.hoilr15
        vals2.secondref15 = (vals2.rhpko_2ref15 + vals2.rhpkol_2ref15 + vals2.rhpkst_2ref15 + vals2.shortening_2ref15 + 
                                vals2.rhpo_2ref15 + vals2.rpst_2ref15 + vals2.rhpst_2ref15 + vals2.rhcno_2ref15 + vals2.rcno_2ref15 + 
                                    vals2.rpko_2ref15 + vals2.apshortening_2ref15 + vals2.rhpoc_2ref15 + vals2.rhsbo_2ref15)
        vals2.tpd400ref15 = vals2.firstref15 + vals2.secondref15
        vals2.tpd400ref_ecu15 = vals2.tpd400ref15/350*100
        vals2.hydro15 = (vals2.rhsbo_hydro15 + vals2.rhpoc_hydro15 + vals2.hoilh15 + vals.sob_h15 + vals2.rhpko_hydro15 + 
                            vals2.rhpkol_hydro15 + vals2.rhpkst_hydro15 + vals2.rhpst_hydro15 + vals2.rhcno_hydro15)
        vals2.hydro_ecu15 = vals2.hydro15/350*100
        vals2.ieoilb_ecu15 = vals2.ieoilb15/350*100
        vals2.maxcap15 = 80*350
        vals2.ieoild_ecu15 = vals2.ieoild15/350*100
        vals2.perfectorb15 = vals2.asm_perf15 + vals2.imcfl2_15 + vals2.iscfl2_15 + vals2.nimcfl2_15 + vals2.niscfl2_15
        vals2.perfectorb_ecu15 = vals2.perfectorb15/350*100
        vals2.perfectora15 = vals2.rhpoc_perf15 + vals2.rhsbo_perf15 + vals2.apshortening_perf15 + vals.sob_perf15
        vals2.perfectora_ecu15 = vals2.perfectora15/350*100
        vals2.petline_ecu15 = vals2.petline15/350*100
        vals2.tbibline15 = vals2.ls_bibline15 + vals.sob_perf15 + vals2.bibline15
        vals2.tbibline_ecu15 = vals2.tbibline15/350*100
        vals2.cfl1t15 = vals2.rhpoc_perf15 + vals2.rhsbo_perf15 + vals2.apshortening_perf15
        vals2.cfl1t_ecu15 = vals2.cfl1t15/350*100
        vals2.cfl2t15 = vals2.niscfl2_15 + vals2.nimcfl2_15 + vals2.iscfl2_15 + vals2.imcfl2_15
        vals2.cfl2t_ecu15 = vals2.cfl2t15/350*100

        vals2.rhsbo_hydro16 = vals.rhsbo16/120
        vals2.rhpoc_hydro16 = vals.rhpoc16/120
        vals2.neutral16 = vals.sob_n16 + vals.cpf_n16
        vals2.neutral_ecu16 = vals2.neutral16/350*100
        vals2.dewaxing16 = vals.sob_d16 + vals.cpf_d16
        vals2.dewaxing_ecu16 = vals2.dewaxing16/350*100
        vals2.firstref16 = vals.sob_fr16 + vals.cpf_fr16 + vals2.hoilr16
        vals2.secondref16 = (vals2.rhpko_2ref16 + vals2.rhpkol_2ref16 + vals2.rhpkst_2ref16 + vals2.shortening_2ref16 + 
                                vals2.rhpo_2ref16 + vals2.rpst_2ref16 + vals2.rhpst_2ref16 + vals2.rhcno_2ref16 + vals2.rcno_2ref16 + 
                                    vals2.rpko_2ref16 + vals2.apshortening_2ref16 + vals2.rhpoc_2ref16 + vals2.rhsbo_2ref16)
        vals2.tpd400ref16 = vals2.firstref16 + vals2.secondref16
        vals2.tpd400ref_ecu16 = vals2.tpd400ref16/350*100
        vals2.hydro16 = (vals2.rhsbo_hydro16 + vals2.rhpoc_hydro16 + vals2.hoilh16 + vals.sob_h16 + vals2.rhpko_hydro16 + 
                            vals2.rhpkol_hydro16 + vals2.rhpkst_hydro16 + vals2.rhpst_hydro16 + vals2.rhcno_hydro16)
        vals2.hydro_ecu16 = vals2.hydro16/350*100
        vals2.ieoilb_ecu16 = vals2.ieoilb16/350*100
        vals2.maxcap16 = 80*350
        vals2.ieoild_ecu16 = vals2.ieoild16/350*100
        vals2.perfectorb16 = vals2.asm_perf16 + vals2.imcfl2_16 + vals2.iscfl2_16 + vals2.nimcfl2_16 + vals2.niscfl2_16
        vals2.perfectorb_ecu16 = vals2.perfectorb16/350*100
        vals2.perfectora16 = vals2.rhpoc_perf16 + vals2.rhsbo_perf16 + vals2.apshortening_perf16 + vals.sob_perf16
        vals2.perfectora_ecu16 = vals2.perfectora16/350*100
        vals2.petline_ecu16 = vals2.petline16/350*100
        vals2.tbibline16 = vals2.ls_bibline16 + vals.sob_perf16 + vals2.bibline16
        vals2.tbibline_ecu16 = vals2.tbibline16/350*100
        vals2.cfl1t16 = vals2.rhpoc_perf16 + vals2.rhsbo_perf16 + vals2.apshortening_perf16
        vals2.cfl1t_ecu16 = vals2.cfl1t16/350*100
        vals2.cfl2t16 = vals2.niscfl2_16 + vals2.nimcfl2_16 + vals2.iscfl2_16 + vals2.imcfl2_16
        vals2.cfl2t_ecu16 = vals2.cfl2t16/350*100
        
        vals2.rhsbo_hydro17 = vals.rhsbo17/120
        vals2.rhpoc_hydro17 = vals.rhpoc17/120
        vals2.neutral17 = vals.sob_n17 + vals.cpf_n17
        vals2.neutral_ecu17 = vals2.neutral17/350*100
        vals2.dewaxing17 = vals.sob_d17 + vals.cpf_d17
        vals2.dewaxing_ecu17 = vals2.dewaxing17/350*100
        vals2.firstref17 = vals.sob_fr17 + vals.cpf_fr17 + vals2.hoilr17
        vals2.secondref17 = (vals2.rhpko_2ref17 + vals2.rhpkol_2ref17 + vals2.rhpkst_2ref17 + vals2.shortening_2ref17 + 
                                vals2.rhpo_2ref17 + vals2.rpst_2ref17 + vals2.rhpst_2ref17 + vals2.rhcno_2ref17 + vals2.rcno_2ref17 + 
                                    vals2.rpko_2ref17 + vals2.apshortening_2ref17 + vals2.rhpoc_2ref17 + vals2.rhsbo_2ref17)
        vals2.tpd400ref17 = vals2.firstref17 + vals2.secondref17
        vals2.tpd400ref_ecu17 = vals2.tpd400ref17/350*100
        vals2.hydro17 = (vals2.rhsbo_hydro17 + vals2.rhpoc_hydro17 + vals2.hoilh17 + vals.sob_h17 + vals2.rhpko_hydro17 + 
                            vals2.rhpkol_hydro17 + vals2.rhpkst_hydro17 + vals2.rhpst_hydro17 + vals2.rhcno_hydro17)
        vals2.hydro_ecu17 = vals2.hydro17/350*100
        vals2.ieoilb_ecu17 = vals2.ieoilb17/350*100
        vals2.maxcap17 = 80*350
        vals2.ieoild_ecu17 = vals2.ieoild17/350*100
        vals2.perfectorb17 = vals2.asm_perf17 + vals2.imcfl2_17 + vals2.iscfl2_17 + vals2.nimcfl2_17 + vals2.niscfl2_17
        vals2.perfectorb_ecu17 = vals2.perfectorb17/350*100
        vals2.perfectora17 = vals2.rhpoc_perf17 + vals2.rhsbo_perf17 + vals2.apshortening_perf17 + vals.sob_perf17
        vals2.perfectora_ecu17 = vals2.perfectora17/350*100
        vals2.petline_ecu17 = vals2.petline17/350*100
        vals2.tbibline17 = vals2.ls_bibline17 + vals.sob_perf17 + vals2.bibline17
        vals2.tbibline_ecu17 = vals2.tbibline17/350*100
        vals2.cfl1t17 = vals2.rhpoc_perf17 + vals2.rhsbo_perf17 + vals2.apshortening_perf17
        vals2.cfl1t_ecu17 = vals2.cfl1t17/350*100
        vals2.cfl2t17 = vals2.niscfl2_17 + vals2.nimcfl2_17 + vals2.iscfl2_17 + vals2.imcfl2_17
        vals2.cfl2t_ecu17 = vals2.cfl2t17/350*100
        
        vals2.rhsbo_hydro18 = vals.rhsbo18/120
        vals2.rhpoc_hydro18 = vals.rhpoc18/120
        vals2.neutral18 = vals.sob_n18 + vals.cpf_n18
        vals2.neutral_ecu18 = vals2.neutral18/350*100
        vals2.dewaxing18 = vals.sob_d18 + vals.cpf_d18
        vals2.dewaxing_ecu18 = vals2.dewaxing18/350*100
        vals2.firstref18 = vals.sob_fr18 + vals.cpf_fr18 + vals2.hoilr18
        vals2.secondref18 = (vals2.rhpko_2ref18 + vals2.rhpkol_2ref18 + vals2.rhpkst_2ref18 + vals2.shortening_2ref18 + 
                                vals2.rhpo_2ref18 + vals2.rpst_2ref18 + vals2.rhpst_2ref18 + vals2.rhcno_2ref18 + vals2.rcno_2ref18 + 
                                    vals2.rpko_2ref18 + vals2.apshortening_2ref18 + vals2.rhpoc_2ref18 + vals2.rhsbo_2ref18)
        vals2.tpd400ref18 = vals2.firstref18 + vals2.secondref18
        vals2.tpd400ref_ecu18 = vals2.tpd400ref18/350*100
        vals2.hydro18 = (vals2.rhsbo_hydro18 + vals2.rhpoc_hydro18 + vals2.hoilh18 + vals.sob_h18 + vals2.rhpko_hydro18 + 
                            vals2.rhpkol_hydro18 + vals2.rhpkst_hydro18 + vals2.rhpst_hydro18 + vals2.rhcno_hydro18)
        vals2.hydro_ecu18 = vals2.hydro18/350*100
        vals2.ieoilb_ecu18 = vals2.ieoilb18/350*100
        vals2.maxcap18 = 80*350
        vals2.ieoild_ecu18 = vals2.ieoild18/350*100
        vals2.perfectorb18 = vals2.asm_perf18 + vals2.imcfl2_18 + vals2.iscfl2_18 + vals2.nimcfl2_18 + vals2.niscfl2_18
        vals2.perfectorb_ecu18 = vals2.perfectorb18/350*100
        vals2.perfectora18 = vals2.rhpoc_perf18 + vals2.rhsbo_perf18 + vals2.apshortening_perf18 + vals.sob_perf18
        vals2.perfectora_ecu18 = vals2.perfectora18/350*100
        vals2.petline_ecu18 = vals2.petline18/350*100
        vals2.tbibline18 = vals2.ls_bibline18 + vals.sob_perf18 + vals2.bibline18
        vals2.tbibline_ecu18 = vals2.tbibline18/350*100
        vals2.cfl1t18 = vals2.rhpoc_perf18 + vals2.rhsbo_perf18 + vals2.apshortening_perf18
        vals2.cfl1t_ecu18 = vals2.cfl1t18/350*100
        vals2.cfl2t18 = vals2.niscfl2_18 + vals2.nimcfl2_18 + vals2.iscfl2_18 + vals2.imcfl2_18
        vals2.cfl2t_ecu18 = vals2.cfl2t18/350*100
        
        vals2.rhsbo_hydro19 = vals.rhsbo19/120
        vals2.rhpoc_hydro19 = vals.rhpoc19/120
        vals2.neutral19 = vals.sob_n19 + vals.cpf_n19
        vals2.neutral_ecu19 = vals2.neutral19/350*100
        vals2.dewaxing19 = vals.sob_d19 + vals.cpf_d19
        vals2.dewaxing_ecu19 = vals2.dewaxing19/350*100
        vals2.firstref19 = vals.sob_fr19 + vals.cpf_fr19 + vals2.hoilr19
        vals2.secondref19 = (vals2.rhpko_2ref19 + vals2.rhpkol_2ref19 + vals2.rhpkst_2ref19 + vals2.shortening_2ref19 + 
                                vals2.rhpo_2ref19 + vals2.rpst_2ref19 + vals2.rhpst_2ref19 + vals2.rhcno_2ref19 + vals2.rcno_2ref19 + 
                                    vals2.rpko_2ref19 + vals2.apshortening_2ref19 + vals2.rhpoc_2ref19 + vals2.rhsbo_2ref19)
        vals2.tpd400ref19 = vals2.firstref19 + vals2.secondref19
        vals2.tpd400ref_ecu19 = vals2.tpd400ref19/350*100
        vals2.hydro19 = (vals2.rhsbo_hydro19 + vals2.rhpoc_hydro19 + vals2.hoilh19 + vals.sob_h19 + vals2.rhpko_hydro19 + 
                            vals2.rhpkol_hydro19 + vals2.rhpkst_hydro19 + vals2.rhpst_hydro19 + vals2.rhcno_hydro19)
        vals2.hydro_ecu19 = vals2.hydro19/350*100
        vals2.ieoilb_ecu19 = vals2.ieoilb19/350*100
        vals2.maxcap19 = 80*350
        vals2.ieoild_ecu19 = vals2.ieoild19/350*100
        vals2.perfectorb19 = vals2.asm_perf19 + vals2.imcfl2_19 + vals2.iscfl2_19 + vals2.nimcfl2_19 + vals2.niscfl2_19
        vals2.perfectorb_ecu19 = vals2.perfectorb19/350*100
        vals2.perfectora19 = vals2.rhpoc_perf19 + vals2.rhsbo_perf19 + vals2.apshortening_perf19 + vals.sob_perf19
        vals2.perfectora_ecu19 = vals2.perfectora19/350*100
        vals2.petline_ecu19 = vals2.petline19/350*100
        vals2.tbibline19 = vals2.ls_bibline19 + vals.sob_perf19 + vals2.bibline19
        vals2.tbibline_ecu19 = vals2.tbibline19/350*100
        vals2.cfl1t19 = vals2.rhpoc_perf19 + vals2.rhsbo_perf19 + vals2.apshortening_perf19
        vals2.cfl1t_ecu19 = vals2.cfl1t19/350*100
        vals2.cfl2t19 = vals2.niscfl2_19 + vals2.nimcfl2_19 + vals2.iscfl2_19 + vals2.imcfl2_19
        vals2.cfl2t_ecu19 = vals2.cfl2t19/350*100
        
        vals2.rhsbo_hydro20 = vals.rhsbo20/120
        vals2.rhpoc_hydro20 = vals.rhpoc20/120
        vals2.neutral20 = vals.sob_n20 + vals.cpf_n20
        vals2.neutral_ecu20 = vals2.neutral20/350*100
        vals2.dewaxing20 = vals.sob_d20 + vals.cpf_d20
        vals2.dewaxing_ecu20 = vals2.dewaxing20/350*100
        vals2.firstref20 = vals.sob_fr20 + vals.cpf_fr20 + vals2.hoilr20
        vals2.secondref20 = (vals2.rhpko_2ref20 + vals2.rhpkol_2ref20 + vals2.rhpkst_2ref20 + vals2.shortening_2ref20 + 
                                vals2.rhpo_2ref20 + vals2.rpst_2ref20 + vals2.rhpst_2ref20 + vals2.rhcno_2ref20 + vals2.rcno_2ref20 + 
                                    vals2.rpko_2ref20 + vals2.apshortening_2ref20 + vals2.rhpoc_2ref20 + vals2.rhsbo_2ref20)
        vals2.tpd400ref20 = vals2.firstref20 + vals2.secondref20
        vals2.tpd400ref_ecu20 = vals2.tpd400ref20/350*100
        vals2.hydro20 = (vals2.rhsbo_hydro20 + vals2.rhpoc_hydro20 + vals2.hoilh20 + vals.sob_h20 + vals2.rhpko_hydro20 + 
                            vals2.rhpkol_hydro20 + vals2.rhpkst_hydro20 + vals2.rhpst_hydro20 + vals2.rhcno_hydro20)
        vals2.hydro_ecu20 = vals2.hydro20/350*100
        vals2.ieoilb_ecu20 = vals2.ieoilb20/350*100
        vals2.maxcap20 = 80*350
        vals2.ieoild_ecu20 = vals2.ieoild20/350*100
        vals2.perfectorb20 = vals2.asm_perf20 + vals2.imcfl2_20 + vals2.iscfl2_20 + vals2.nimcfl2_20 + vals2.niscfl2_20
        vals2.perfectorb_ecu20 = vals2.perfectorb20/350*100
        vals2.perfectora20 = vals2.rhpoc_perf20 + vals2.rhsbo_perf20 + vals2.apshortening_perf20 + vals.sob_perf20
        vals2.perfectora_ecu20 = vals2.perfectora20/350*100
        vals2.petline_ecu20 = vals2.petline20/350*100
        vals2.tbibline20 = vals2.ls_bibline20 + vals.sob_perf20 + vals2.bibline20
        vals2.tbibline_ecu20 = vals2.tbibline20/350*100
        vals2.cfl1t20 = vals2.rhpoc_perf20 + vals2.rhsbo_perf20 + vals2.apshortening_perf20
        vals2.cfl1t_ecu20 = vals2.cfl1t20/350*100
        vals2.cfl2t20 = vals2.niscfl2_20 + vals2.nimcfl2_20 + vals2.iscfl2_20 + vals2.imcfl2_20
        vals2.cfl2t_ecu20 = vals2.cfl2t20/350*100
        
        vals2.rhsbo_hydro21 = vals.rhsbo21/120
        vals2.rhpoc_hydro21 = vals.rhpoc21/120
        vals2.neutral21 = vals.sob_n21 + vals.cpf_n21
        vals2.neutral_ecu21 = vals2.neutral21/350*100
        vals2.dewaxing21 = vals.sob_d21 + vals.cpf_d21
        vals2.dewaxing_ecu21 = vals2.dewaxing21/350*100
        vals2.firstref21 = vals.sob_fr21 + vals.cpf_fr21 + vals2.hoilr21
        vals2.secondref21 = (vals2.rhpko_2ref21 + vals2.rhpkol_2ref21 + vals2.rhpkst_2ref21 + vals2.shortening_2ref21 + 
                                vals2.rhpo_2ref21 + vals2.rpst_2ref21 + vals2.rhpst_2ref21 + vals2.rhcno_2ref21 + vals2.rcno_2ref21 + 
                                    vals2.rpko_2ref21 + vals2.apshortening_2ref21 + vals2.rhpoc_2ref21 + vals2.rhsbo_2ref21)
        vals2.tpd400ref21 = vals2.firstref21 + vals2.secondref21
        vals2.tpd400ref_ecu21 = vals2.tpd400ref21/350*100
        vals2.hydro21 = (vals2.rhsbo_hydro21 + vals2.rhpoc_hydro21 + vals2.hoilh21 + vals.sob_h21 + vals2.rhpko_hydro21 + 
                            vals2.rhpkol_hydro21 + vals2.rhpkst_hydro21 + vals2.rhpst_hydro21 + vals2.rhcno_hydro21)
        vals2.hydro_ecu21 = vals2.hydro21/350*100
        vals2.ieoilb_ecu21 = vals2.ieoilb21/350*100
        vals2.maxcap21 = 80*350
        vals2.ieoild_ecu21 = vals2.ieoild21/350*100
        vals2.perfectorb21 = vals2.asm_perf21 + vals2.imcfl2_21 + vals2.iscfl2_21 + vals2.nimcfl2_21 + vals2.niscfl2_21
        vals2.perfectorb_ecu21 = vals2.perfectorb21/350*100
        vals2.perfectora21 = vals2.rhpoc_perf21 + vals2.rhsbo_perf21 + vals2.apshortening_perf21 + vals.sob_perf21
        vals2.perfectora_ecu21 = vals2.perfectora21/350*100
        vals2.petline_ecu21 = vals2.petline21/350*100
        vals2.tbibline21 = vals2.ls_bibline21 + vals.sob_perf21 + vals2.bibline21
        vals2.tbibline_ecu21 = vals2.tbibline21/350*100
        vals2.cfl1t21 = vals2.rhpoc_perf21 + vals2.rhsbo_perf21 + vals2.apshortening_perf21
        vals2.cfl1t_ecu21 = vals2.cfl1t21/350*100
        vals2.cfl2t21 = vals2.niscfl2_21 + vals2.nimcfl2_21 + vals2.iscfl2_21 + vals2.imcfl2_21
        vals2.cfl2t_ecu21 = vals2.cfl2t21/350*100
        
        vals2.rhsbo_hydro22 = vals.rhsbo22/120
        vals2.rhpoc_hydro22 = vals.rhpoc22/120
        vals2.neutral22 = vals.sob_n22 + vals.cpf_n22
        vals2.neutral_ecu22 = vals2.neutral22/350*100
        vals2.dewaxing22 = vals.sob_d22 + vals.cpf_d22
        vals2.dewaxing_ecu22 = vals2.dewaxing22/350*100
        vals2.firstref22 = vals.sob_fr22 + vals.cpf_fr22 + vals2.hoilr22
        vals2.secondref22 = (vals2.rhpko_2ref22 + vals2.rhpkol_2ref22 + vals2.rhpkst_2ref22 + vals2.shortening_2ref22 + 
                                vals2.rhpo_2ref22 + vals2.rpst_2ref22 + vals2.rhpst_2ref22 + vals2.rhcno_2ref22 + vals2.rcno_2ref22 + 
                                    vals2.rpko_2ref22 + vals2.apshortening_2ref22 + vals2.rhpoc_2ref22 + vals2.rhsbo_2ref22)
        vals2.tpd400ref22 = vals2.firstref22 + vals2.secondref22
        vals2.tpd400ref_ecu22 = vals2.tpd400ref22/350*100
        vals2.hydro22 = (vals2.rhsbo_hydro22 + vals2.rhpoc_hydro22 + vals2.hoilh22 + vals.sob_h22 + vals2.rhpko_hydro22 + 
                            vals2.rhpkol_hydro22 + vals2.rhpkst_hydro22 + vals2.rhpst_hydro22 + vals2.rhcno_hydro22)
        vals2.hydro_ecu22 = vals2.hydro22/350*100
        vals2.ieoilb_ecu22 = vals2.ieoilb22/350*100
        vals2.maxcap22 = 80*350
        vals2.ieoild_ecu22 = vals2.ieoild22/350*100
        vals2.perfectorb22 = vals2.asm_perf22 + vals2.imcfl2_22 + vals2.iscfl2_22 + vals2.nimcfl2_22 + vals2.niscfl2_22
        vals2.perfectorb_ecu22 = vals2.perfectorb22/350*100
        vals2.perfectora22 = vals2.rhpoc_perf22 + vals2.rhsbo_perf22 + vals2.apshortening_perf22 + vals.sob_perf22
        vals2.perfectora_ecu22 = vals2.perfectora22/350*100
        vals2.petline_ecu22 = vals2.petline22/350*100
        vals2.tbibline22 = vals2.ls_bibline22 + vals.sob_perf22 + vals2.bibline22
        vals2.tbibline_ecu22 = vals2.tbibline22/350*100
        vals2.cfl1t22 = vals2.rhpoc_perf22 + vals2.rhsbo_perf22 + vals2.apshortening_perf22
        vals2.cfl1t_ecu22 = vals2.cfl1t22/350*100
        vals2.cfl2t22 = vals2.niscfl2_22 + vals2.nimcfl2_22 + vals2.iscfl2_22 + vals2.imcfl2_22
        vals2.cfl2t_ecu22 = vals2.cfl2t22/350*100
        
        vals2.rhsbo_hydro23 = vals.rhsbo23/120
        vals2.rhpoc_hydro23 = vals.rhpoc23/120
        vals2.neutral23 = vals.sob_n23 + vals.cpf_n23
        vals2.neutral_ecu23 = vals2.neutral23/350*100
        vals2.dewaxing23 = vals.sob_d23 + vals.cpf_d23
        vals2.dewaxing_ecu23 = vals2.dewaxing23/350*100
        vals2.firstref23 = vals.sob_fr23 + vals.cpf_fr23 + vals2.hoilr23
        vals2.secondref23 = (vals2.rhpko_2ref23 + vals2.rhpkol_2ref23 + vals2.rhpkst_2ref23 + vals2.shortening_2ref23 + 
                                vals2.rhpo_2ref23 + vals2.rpst_2ref23 + vals2.rhpst_2ref23 + vals2.rhcno_2ref23 + vals2.rcno_2ref23 + 
                                    vals2.rpko_2ref23 + vals2.apshortening_2ref23 + vals2.rhpoc_2ref23 + vals2.rhsbo_2ref23)
        vals2.tpd400ref23 = vals2.firstref23 + vals2.secondref23
        vals2.tpd400ref_ecu23 = vals2.tpd400ref23/350*100
        vals2.hydro23 = (vals2.rhsbo_hydro23 + vals2.rhpoc_hydro23 + vals2.hoilh23 + vals.sob_h23 + vals2.rhpko_hydro23 + 
                            vals2.rhpkol_hydro23 + vals2.rhpkst_hydro23 + vals2.rhpst_hydro23 + vals2.rhcno_hydro23)
        vals2.hydro_ecu23 = vals2.hydro23/350*100
        vals2.ieoilb_ecu23 = vals2.ieoilb23/350*100
        vals2.maxcap23 = 80*350
        vals2.ieoild_ecu23 = vals2.ieoild23/350*100
        vals2.perfectorb23 = vals2.asm_perf23 + vals2.imcfl2_23 + vals2.iscfl2_23 + vals2.nimcfl2_23 + vals2.niscfl2_23
        vals2.perfectorb_ecu23 = vals2.perfectorb23/350*100
        vals2.perfectora23 = vals2.rhpoc_perf23 + vals2.rhsbo_perf23 + vals2.apshortening_perf23 + vals.sob_perf23
        vals2.perfectora_ecu23 = vals2.perfectora23/350*100
        vals2.petline_ecu23 = vals2.petline23/350*100
        vals2.tbibline23 = vals2.ls_bibline23 + vals.sob_perf23 + vals2.bibline23
        vals2.tbibline_ecu23 = vals2.tbibline23/350*100
        vals2.cfl1t23 = vals2.rhpoc_perf23 + vals2.rhsbo_perf23 + vals2.apshortening_perf23
        vals2.cfl1t_ecu23 = vals2.cfl1t23/350*100
        vals2.cfl2t23 = vals2.niscfl2_23 + vals2.nimcfl2_23 + vals2.iscfl2_23 + vals2.imcfl2_23
        vals2.cfl2t_ecu23 = vals2.cfl2t23/350*100
        
        vals2.rhsbo_hydro24 = vals.rhsbo24/120
        vals2.rhpoc_hydro24 = vals.rhpoc24/120
        vals2.neutral24 = vals.sob_n24 + vals.cpf_n24
        vals2.neutral_ecu24 = vals2.neutral24/350*100
        vals2.dewaxing24 = vals.sob_d24 + vals.cpf_d24
        vals2.dewaxing_ecu24 = vals2.dewaxing24/350*100
        vals2.firstref24 = vals.sob_fr24 + vals.cpf_fr24 + vals2.hoilr24
        vals2.secondref24 = (vals2.rhpko_2ref24 + vals2.rhpkol_2ref24 + vals2.rhpkst_2ref24 + vals2.shortening_2ref24 + 
                                vals2.rhpo_2ref24 + vals2.rpst_2ref24 + vals2.rhpst_2ref24 + vals2.rhcno_2ref24 + vals2.rcno_2ref24 + 
                                    vals2.rpko_2ref24 + vals2.apshortening_2ref24 + vals2.rhpoc_2ref24 + vals2.rhsbo_2ref24)
        vals2.tpd400ref24 = vals2.firstref24 + vals2.secondref24
        vals2.tpd400ref_ecu24 = vals2.tpd400ref24/350*100
        vals2.hydro24 = (vals2.rhsbo_hydro24 + vals2.rhpoc_hydro24 + vals2.hoilh24 + vals.sob_h24 + vals2.rhpko_hydro24 + 
                            vals2.rhpkol_hydro24 + vals2.rhpkst_hydro24 + vals2.rhpst_hydro24 + vals2.rhcno_hydro24)
        vals2.hydro_ecu24 = vals2.hydro24/350*100
        vals2.ieoilb_ecu24 = vals2.ieoilb24/350*100
        vals2.maxcap24 = 80*350
        vals2.ieoild_ecu24 = vals2.ieoild24/350*100
        vals2.perfectorb24 = vals2.asm_perf24 + vals2.imcfl2_24 + vals2.iscfl2_24 + vals2.nimcfl2_24 + vals2.niscfl2_24
        vals2.perfectorb_ecu24 = vals2.perfectorb24/350*100
        vals2.perfectora24 = vals2.rhpoc_perf24 + vals2.rhsbo_perf24 + vals2.apshortening_perf24 + vals.sob_perf24
        vals2.perfectora_ecu24 = vals2.perfectora24/350*100
        vals2.petline_ecu24 = vals2.petline24/350*100
        vals2.tbibline24 = vals2.ls_bibline24 + vals.sob_perf24 + vals2.bibline24
        vals2.tbibline_ecu24 = vals2.tbibline24/350*100
        vals2.cfl1t24 = vals2.rhpoc_perf24 + vals2.rhsbo_perf24 + vals2.apshortening_perf24
        vals2.cfl1t_ecu24 = vals2.cfl1t24/350*100
        vals2.cfl2t24 = vals2.niscfl2_24 + vals2.nimcfl2_24 + vals2.iscfl2_24 + vals2.imcfl2_24
        vals2.cfl2t_ecu24 = vals2.cfl2t24/350*100


        #Rounding Values
        vals.hocan15 = round(vals.hocan15,2) 
        vals.g1sb015 = round(vals.g1sb015,2)
        vals.corn15 = round(vals.corn15,2)
        vals.hsbo15 = round(vals.hsbo15,2)
        vals.stote_oil_blend15 = round(vals.stote_oil_blend15,2)
        vals.chicken_par_fry15 = round(vals.chicken_par_fry15,2)
        vals.macd_system_total15 = round(vals.macd_system_total15,2)

        vals.hocan16 = round(vals.hocan16,2) 
        vals.g1sb016 = round(vals.g1sb016,2)
        vals.corn16 = round(vals.corn16,2)
        vals.hsbo16 = round(vals.hsbo16,2)
        vals.stote_oil_blend16 = round(vals.stote_oil_blend16,2)
        vals.chicken_par_fry16 = round(vals.chicken_par_fry16,2)
        vals.macd_system_total16 = round(vals.macd_system_total16,2)
        
        vals.hocan17 = round(vals.hocan17,2) 
        vals.g1sb017 = round(vals.g1sb017,2)
        vals.corn17 = round(vals.corn17,2)
        vals.hsbo17 = round(vals.hsbo17,2)
        vals.stote_oil_blend17 = round(vals.stote_oil_blend17,2)
        vals.chicken_par_fry17 = round(vals.chicken_par_fry17,2)
        vals.macd_system_total17 = round(vals.macd_system_total17,2)
        
        vals.hocan18 = round(vals.hocan18,2) 
        vals.g1sb018 = round(vals.g1sb018,2)
        vals.corn18 = round(vals.corn18,2)
        vals.hsbo18 = round(vals.hsbo18,2)
        vals.stote_oil_blend18 = round(vals.stote_oil_blend18,2)
        vals.chicken_par_fry18 = round(vals.chicken_par_fry18,2)
        vals.macd_system_total18 = round(vals.macd_system_total18,2)
        
        vals.hocan19 = round(vals.hocan19,2) 
        vals.g1sb019 = round(vals.g1sb019,2)
        vals.corn19 = round(vals.corn19,2)
        vals.hsbo19 = round(vals.hsbo19,2)
        vals.stote_oil_blend19 = round(vals.stote_oil_blend19,2)
        vals.chicken_par_fry19 = round(vals.chicken_par_fry19,2)
        vals.macd_system_total19 = round(vals.macd_system_total19,2)
        
        vals.hocan20 = round(vals.hocan20,2) 
        vals.g1sb020 = round(vals.g1sb020,2)
        vals.corn20 = round(vals.corn20,2)
        vals.hsbo20 = round(vals.hsbo20,2)
        vals.stote_oil_blend20 = round(vals.stote_oil_blend20,2)
        vals.chicken_par_fry20 = round(vals.chicken_par_fry20,2)
        vals.macd_system_total20 = round(vals.macd_system_total20,2)
        
        vals.hocan21 = round(vals.hocan21,2) 
        vals.g1sb021 = round(vals.g1sb021,2)
        vals.corn21 = round(vals.corn21,2)
        vals.hsbo21 = round(vals.hsbo21,2)
        vals.stote_oil_blend21 = round(vals.stote_oil_blend21,2)
        vals.chicken_par_fry21 = round(vals.chicken_par_fry21,2)
        vals.macd_system_total21 = round(vals.macd_system_total21,2)
        
        vals.hocan22 = round(vals.hocan22,2) 
        vals.g1sb022 = round(vals.g1sb022,2)
        vals.corn22 = round(vals.corn22,2)
        vals.hsbo22 = round(vals.hsbo22,2)
        vals.stote_oil_blend22 = round(vals.stote_oil_blend22,2)
        vals.chicken_par_fry22 = round(vals.chicken_par_fry22,2)
        vals.macd_system_total22 = round(vals.macd_system_total22,2)
        
        vals.hocan23 = round(vals.hocan23,2) 
        vals.g1sb023 = round(vals.g1sb023,2)
        vals.corn23 = round(vals.corn23,2)
        vals.hsbo23 = round(vals.hsbo23,2)
        vals.stote_oil_blend23 = round(vals.stote_oil_blend23,2)
        vals.chicken_par_fry23 = round(vals.chicken_par_fry23,2)
        vals.macd_system_total23 = round(vals.macd_system_total23,2)
        
        vals.hocan24 = round(vals.hocan24,2) 
        vals.g1sb024 = round(vals.g1sb024,2)
        vals.corn24 = round(vals.corn24,2)
        vals.hsbo24 = round(vals.hsbo24,2)
        vals.stote_oil_blend24 = round(vals.stote_oil_blend24,2)
        vals.chicken_par_fry24 = round(vals.chicken_par_fry24,2)
        vals.macd_system_total24 = round(vals.macd_system_total24,2)

        vals.rhpko15 = round(vals.rhpko15,2)
        vals.rhpkol15 = round(vals.rhpkol15,2)
        vals.rhpkst15 = round(vals.rhpkst15,2)
        vals.shortening15 = round(vals.shortening15,2)
        vals.rhpo15 = round(vals.rhpo15,2)
        vals.rpst15 = round(vals.rpst15,2)
        vals.rhpst15 = round(vals.rhpst15,2)
        vals.rhcno15 = round(vals.rhcno15,2)
        vals.rcno15 = round(vals.rcno15,2)
        vals.rpko15 = round(vals.rpko15,2)
        vals.subtotal15 = round(vals.subtotal15,2)

        vals.rhpko16 = round(vals.rhpko16,2)
        vals.rhpkol16 = round(vals.rhpkol16,2)
        vals.rhpkst16 = round(vals.rhpkst16,2)
        vals.shortening16 = round(vals.shortening16,2)
        vals.rhpo16 = round(vals.rhpo16,2)
        vals.rpst16 = round(vals.rpst16,2)
        vals.rhpst16 = round(vals.rhpst16,2)
        vals.rhcno16 = round(vals.rhcno16,2)
        vals.rcno16 = round(vals.rcno16,2)
        vals.rpko16 = round(vals.rpko16,2)
        vals.subtotal16 = round(vals.subtotal16,2)
        
        vals.rhpko17 = round(vals.rhpko17,2)
        vals.rhpkol17 = round(vals.rhpkol17,2)
        vals.rhpkst17 = round(vals.rhpkst17,2)
        vals.shortening17 = round(vals.shortening17,2)
        vals.rhpo17 = round(vals.rhpo17,2)
        vals.rpst17 = round(vals.rpst17,2)
        vals.rhpst17 = round(vals.rhpst17,2)
        vals.rhcno17 = round(vals.rhcno17,2)
        vals.rcno17 = round(vals.rcno17,2)
        vals.rpko17 = round(vals.rpko17,2)
        vals.subtotal17 = round(vals.subtotal17,2)
        
        vals.rhpko18 = round(vals.rhpko18,2)
        vals.rhpkol18 = round(vals.rhpkol18,2)
        vals.rhpkst18 = round(vals.rhpkst18,2)
        vals.shortening18 = round(vals.shortening18,2)
        vals.rhpo18 = round(vals.rhpo18,2)
        vals.rpst18 = round(vals.rpst18,2)
        vals.rhpst18 = round(vals.rhpst18,2)
        vals.rhcno18 = round(vals.rhcno18,2)
        vals.rcno18 = round(vals.rcno18,2)
        vals.rpko18 = round(vals.rpko18,2)
        vals.subtotal18 = round(vals.subtotal18,2)
        
        vals.rhpko19 = round(vals.rhpko19,2)
        vals.rhpkol19 = round(vals.rhpkol19,2)
        vals.rhpkst19 = round(vals.rhpkst19,2)
        vals.shortening19 = round(vals.shortening19,2)
        vals.rhpo19 = round(vals.rhpo19,2)
        vals.rpst19 = round(vals.rpst19,2)
        vals.rhpst19 = round(vals.rhpst19,2)
        vals.rhcno19 = round(vals.rhcno19,2)
        vals.rcno19 = round(vals.rcno19,2)
        vals.rpko19 = round(vals.rpko19,2)
        vals.subtotal19 = round(vals.subtotal19,2)
        
        vals.rhpko20 = round(vals.rhpko20,2)
        vals.rhpkol20 = round(vals.rhpkol20,2)
        vals.rhpkst20 = round(vals.rhpkst20,2)
        vals.shortening20 = round(vals.shortening20,2)
        vals.rhpo20 = round(vals.rhpo20,2)
        vals.rpst20 = round(vals.rpst20,2)
        vals.rhpst20 = round(vals.rhpst20,2)
        vals.rhcno20 = round(vals.rhcno20,2)
        vals.rcno20 = round(vals.rcno20,2)
        vals.rpko20 = round(vals.rpko20,2)
        vals.subtotal20 = round(vals.subtotal20,2)
        
        vals.rhpko21 = round(vals.rhpko21,2)
        vals.rhpkol21 = round(vals.rhpkol21,2)
        vals.rhpkst21 = round(vals.rhpkst21,2)
        vals.shortening21 = round(vals.shortening21,2)
        vals.rhpo21 = round(vals.rhpo21,2)
        vals.rpst21 = round(vals.rpst21,2)
        vals.rhpst21 = round(vals.rhpst21,2)
        vals.rhcno21 = round(vals.rhcno21,2)
        vals.rcno21 = round(vals.rcno21,2)
        vals.rpko21 = round(vals.rpko21,2)
        vals.subtotal21 = round(vals.subtotal21,2)
        
        vals.rhpko22 = round(vals.rhpko22,2)
        vals.rhpkol22 = round(vals.rhpkol22,2)
        vals.rhpkst22 = round(vals.rhpkst22,2)
        vals.shortening22 = round(vals.shortening22,2)
        vals.rhpo22 = round(vals.rhpo22,2)
        vals.rpst22 = round(vals.rpst22,2)
        vals.rhpst22 = round(vals.rhpst22,2)
        vals.rhcno22 = round(vals.rhcno22,2)
        vals.rcno22 = round(vals.rcno22,2)
        vals.rpko22 = round(vals.rpko22,2)
        vals.subtotal22 = round(vals.subtotal22,2)
        
        vals.rhpko23 = round(vals.rhpko23,2)
        vals.rhpkol23 = round(vals.rhpkol23,2)
        vals.rhpkst23 = round(vals.rhpkst23,2)
        vals.shortening23 = round(vals.shortening23,2)
        vals.rhpo23 = round(vals.rhpo23,2)
        vals.rpst23 = round(vals.rpst23,2)
        vals.rhpst23 = round(vals.rhpst23,2)
        vals.rhcno23 = round(vals.rhcno23,2)
        vals.rcno23 = round(vals.rcno23,2)
        vals.rpko23 = round(vals.rpko23,2)
        vals.subtotal23 = round(vals.subtotal23,2)
        
        vals.rhpko24 = round(vals.rhpko24,2)
        vals.rhpkol24 = round(vals.rhpkol24,2)
        vals.rhpkst24 = round(vals.rhpkst24,2)
        vals.shortening24 = round(vals.shortening24,2)
        vals.rhpo24 = round(vals.rhpo24,2)
        vals.rpst24 = round(vals.rpst24,2)
        vals.rhpst24 = round(vals.rhpst24,2)
        vals.rhcno24 = round(vals.rhcno24,2)
        vals.rcno24 = round(vals.rcno24,2)
        vals.rpko24 = round(vals.rpko24,2)
        vals.subtotal24 = round(vals.subtotal24,2)

        vals.rhpoc15 = round(vals.rhpoc15,2) 
        vals.rhpoc16 = round(vals.rhpoc16,2) 
        vals.rhpoc17 = round(vals.rhpoc17,2) 
        vals.rhpoc18 = round(vals.rhpoc18,2) 
        vals.rhpoc19 = round(vals.rhpoc19,2) 
        vals.rhpoc20 = round(vals.rhpoc20,2) 
        vals.rhpoc21 = round(vals.rhpoc21,2) 
        vals.rhpoc22 = round(vals.rhpoc22,2) 
        vals.rhpoc23 = round(vals.rhpoc23,2) 
        vals.rhpoc24 = round(vals.rhpoc24,2) 

        vals.rhsbo15 = round(vals.rhsbo15,2) 
        vals.rhsbo16 = round(vals.rhsbo16,2) 
        vals.rhsbo17 = round(vals.rhsbo17,2) 
        vals.rhsbo18 = round(vals.rhsbo18,2) 
        vals.rhsbo19 = round(vals.rhsbo19,2) 
        vals.rhsbo20 = round(vals.rhsbo20,2) 
        vals.rhsbo21 = round(vals.rhsbo21,2) 
        vals.rhsbo22 = round(vals.rhsbo22,2) 
        vals.rhsbo23 = round(vals.rhsbo23,2) 
        vals.rhsbo24 = round(vals.rhsbo24,2) 

        vals.subtotal_15 = round(vals.subtotal_15,2)
        vals.subtotal_16 = round(vals.subtotal_16,2)
        vals.subtotal_17 = round(vals.subtotal_17,2)
        vals.subtotal_18 = round(vals.subtotal_18,2)
        vals.subtotal_19 = round(vals.subtotal_19,2)
        vals.subtotal_20 = round(vals.subtotal_20,2)
        vals.subtotal_21 = round(vals.subtotal_21,2)
        vals.subtotal_22 = round(vals.subtotal_22,2)
        vals.subtotal_23 = round(vals.subtotal_23,2)
        vals.subtotal_24 = round(vals.subtotal_24,2)

        vals.sf_total15 = round(vals.sf_total15,2)
        vals.sf_total16 = round(vals.sf_total16,2)
        vals.sf_total17 = round(vals.sf_total17,2)
        vals.sf_total18 = round(vals.sf_total18,2)
        vals.sf_total19 = round(vals.sf_total19,2)
        vals.sf_total20 = round(vals.sf_total20,2)
        vals.sf_total21 = round(vals.sf_total21,2)
        vals.sf_total22 = round(vals.sf_total22,2)
        vals.sf_total23 = round(vals.sf_total23,2)
        vals.sf_total24 = round(vals.sf_total24,2)

        vals.g1sbo15 = round(vals.g1sbo15,2)
        vals.g1sbo16 = round(vals.g1sbo16,2)
        vals.g1sbo17 = round(vals.g1sbo17,2)
        vals.g1sbo18 = round(vals.g1sbo18,2)
        vals.g1sbo19 = round(vals.g1sbo19,2)
        vals.g1sbo20 = round(vals.g1sbo20,2)
        vals.g1sbo21 = round(vals.g1sbo21,2)
        vals.g1sbo22 = round(vals.g1sbo22,2)
        vals.g1sbo23 = round(vals.g1sbo23,2)
        vals.g1sbo24 = round(vals.g1sbo24,2)

        vals.blendedoil15 = round(vals.blendedoil15,2)
        vals.blendedoil16 = round(vals.blendedoil16,2)
        vals.blendedoil17 = round(vals.blendedoil17,2)
        vals.blendedoil18 = round(vals.blendedoil18,2)
        vals.blendedoil19 = round(vals.blendedoil19,2)
        vals.blendedoil20 = round(vals.blendedoil20,2)
        vals.blendedoil21 = round(vals.blendedoil21,2)
        vals.blendedoil22 = round(vals.blendedoil22,2)
        vals.blendedoil23 = round(vals.blendedoil23,2)
        vals.blendedoil24 = round(vals.blendedoil24,2)

        vals.rol15 = round(vals.rol15,2)       
        vals.rol16 = round(vals.rol16,2)       
        vals.rol17 = round(vals.rol17,2)
        vals.rol18 = round(vals.rol18,2)
        vals.rol19 = round(vals.rol19,2)
        vals.rol20 = round(vals.rol20,2)
        vals.rol21 = round(vals.rol21,2)
        vals.rol22 = round(vals.rol22,2)
        vals.rol23 = round(vals.rol23,2)
        vals.rol24 = round(vals.rol24,2)

        vals.spmf15 = round(vals.spmf15,2)
        vals.spmf16 = round(vals.spmf16,2)
        vals.spmf17 = round(vals.spmf17,2)
        vals.spmf18 = round(vals.spmf18,2)
        vals.spmf19 = round(vals.spmf19,2)
        vals.spmf20 = round(vals.spmf20,2)
        vals.spmf21 = round(vals.spmf21,2)
        vals.spmf22 = round(vals.spmf22,2)
        vals.spmf23 = round(vals.spmf23,2)
        vals.spmf24 = round(vals.spmf24,2)

        vals.mpbtotal15 = round(vals.mpbtotal15,2)
        vals.mpbtotal16 = round(vals.mpbtotal16,2)
        vals.mpbtotal17 = round(vals.mpbtotal17,2)
        vals.mpbtotal18 = round(vals.mpbtotal18,2)
        vals.mpbtotal19 = round(vals.mpbtotal19,2)
        vals.mpbtotal20 = round(vals.mpbtotal20,2)
        vals.mpbtotal21 = round(vals.mpbtotal21,2)
        vals.mpbtotal22 = round(vals.mpbtotal22,2)
        vals.mpbtotal23 = round(vals.mpbtotal23,2)
        vals.mpbtotal24 = round(vals.mpbtotal24,2)

        vals.g1sbo1_15 = round(vals.g1sbo1_15,2)
        vals.g1sbo1_16 = round(vals.g1sbo1_16,2)
        vals.g1sbo1_17 = round(vals.g1sbo1_17,2)
        vals.g1sbo1_18 = round(vals.g1sbo1_18,2)
        vals.g1sbo1_19 = round(vals.g1sbo1_19,2)
        vals.g1sbo1_20 = round(vals.g1sbo1_20,2)
        vals.g1sbo1_21 = round(vals.g1sbo1_21,2)
        vals.g1sbo1_22 = round(vals.g1sbo1_22,2)
        vals.g1sbo1_23 = round(vals.g1sbo1_23,2)
        vals.g1sbo1_24 = round(vals.g1sbo1_24,2)

        vals.g1sbo2_15 = round(vals.g1sbo2_15,2)
        vals.g1sbo2_16 = round(vals.g1sbo2_16,2)
        vals.g1sbo2_17 = round(vals.g1sbo2_17,2)
        vals.g1sbo2_18 = round(vals.g1sbo2_18,2)
        vals.g1sbo2_19 = round(vals.g1sbo2_19,2)
        vals.g1sbo2_20 = round(vals.g1sbo2_20,2)
        vals.g1sbo2_21 = round(vals.g1sbo2_21,2)
        vals.g1sbo2_22 = round(vals.g1sbo2_22,2)
        vals.g1sbo2_23 = round(vals.g1sbo2_23,2)
        vals.g1sbo2_24 = round(vals.g1sbo2_24,2)

        vals.g1sbo3_15 = round(vals.g1sbo3_15,2)
        vals.g1sbo3_16 = round(vals.g1sbo3_16,2)
        vals.g1sbo3_17 = round(vals.g1sbo3_17,2)
        vals.g1sbo3_18 = round(vals.g1sbo3_18,2)
        vals.g1sbo3_19 = round(vals.g1sbo3_19,2)
        vals.g1sbo3_20 = round(vals.g1sbo3_20,2)
        vals.g1sbo3_21 = round(vals.g1sbo3_21,2)
        vals.g1sbo3_22 = round(vals.g1sbo3_22,2)
        vals.g1sbo3_23 = round(vals.g1sbo3_23,2)
        vals.g1sbo3_24 = round(vals.g1sbo3_24,2)

        vals.g1sbo4_15 = round(vals.g1sbo4_15,2)
        vals.g1sbo4_16 = round(vals.g1sbo4_16,2)
        vals.g1sbo4_17 = round(vals.g1sbo4_17,2)
        vals.g1sbo4_18 = round(vals.g1sbo4_18,2)
        vals.g1sbo4_19 = round(vals.g1sbo4_19,2)
        vals.g1sbo4_20 = round(vals.g1sbo4_20,2)
        vals.g1sbo4_21 = round(vals.g1sbo4_21,2)
        vals.g1sbo4_22 = round(vals.g1sbo4_22,2)
        vals.g1sbo4_23 = round(vals.g1sbo4_23,2)
        vals.g1sbo4_24 = round(vals.g1sbo4_24,2)

        vals.blendedoil1_15 = round(vals.blendedoil1_15,2) 
        vals.blendedoil1_16 = round(vals.blendedoil1_16,2) 
        vals.blendedoil1_17 = round(vals.blendedoil1_17,2) 
        vals.blendedoil1_18 = round(vals.blendedoil1_18,2) 
        vals.blendedoil1_19 = round(vals.blendedoil1_19,2) 
        vals.blendedoil1_20 = round(vals.blendedoil1_20,2) 
        vals.blendedoil1_21 = round(vals.blendedoil1_21,2) 
        vals.blendedoil1_22 = round(vals.blendedoil1_22,2) 
        vals.blendedoil1_23 = round(vals.blendedoil1_23,2) 
        vals.blendedoil1_24 = round(vals.blendedoil1_24,2) 

        vals.blendedoil2_15 = round(vals.blendedoil2_15,2)
        vals.blendedoil2_16 = round(vals.blendedoil2_16,2)
        vals.blendedoil2_17 = round(vals.blendedoil2_17,2)
        vals.blendedoil2_18 = round(vals.blendedoil2_18,2)
        vals.blendedoil2_19 = round(vals.blendedoil2_19,2)
        vals.blendedoil2_20 = round(vals.blendedoil2_20,2)
        vals.blendedoil2_21 = round(vals.blendedoil2_21,2)
        vals.blendedoil2_22 = round(vals.blendedoil2_22,2)
        vals.blendedoil2_23 = round(vals.blendedoil2_23,2)
        vals.blendedoil2_24 = round(vals.blendedoil2_24,2)

        vals.blendedoil3_15 = round(vals.blendedoil3_15,2)
        vals.blendedoil3_16 = round(vals.blendedoil3_16,2)
        vals.blendedoil3_17 = round(vals.blendedoil3_17,2)
        vals.blendedoil3_18 = round(vals.blendedoil3_18,2)
        vals.blendedoil3_19 = round(vals.blendedoil3_19,2)
        vals.blendedoil3_20 = round(vals.blendedoil3_20,2)
        vals.blendedoil3_21 = round(vals.blendedoil3_21,2)
        vals.blendedoil3_22 = round(vals.blendedoil3_22,2)
        vals.blendedoil3_23 = round(vals.blendedoil3_23,2)
        vals.blendedoil3_24 = round(vals.blendedoil3_24,2)

        vals.blendedoil4_15 = round(vals.blendedoil4_15,2)
        vals.blendedoil4_16 = round(vals.blendedoil4_16,2)
        vals.blendedoil4_17 = round(vals.blendedoil4_17,2)
        vals.blendedoil4_18 = round(vals.blendedoil4_18,2)
        vals.blendedoil4_19 = round(vals.blendedoil4_19,2)
        vals.blendedoil4_20 = round(vals.blendedoil4_20,2)
        vals.blendedoil4_21 = round(vals.blendedoil4_21,2)
        vals.blendedoil4_22 = round(vals.blendedoil4_22,2)
        vals.blendedoil4_23 = round(vals.blendedoil4_23,2)
        vals.blendedoil4_24 = round(vals.blendedoil4_24,2)

        vals.superolein1_15 = round(vals.superolein1_15,2)
        vals.superolein1_16 = round(vals.superolein1_16,2)
        vals.superolein1_17 = round(vals.superolein1_17,2)
        vals.superolein1_18 = round(vals.superolein1_18,2)
        vals.superolein1_19 = round(vals.superolein1_19,2)
        vals.superolein1_20 = round(vals.superolein1_20,2)
        vals.superolein1_21 = round(vals.superolein1_21,2)
        vals.superolein1_22 = round(vals.superolein1_22,2)
        vals.superolein1_23 = round(vals.superolein1_23,2)
        vals.superolein1_24 = round(vals.superolein1_24,2)

        vals.superolein4_15 = round(vals.superolein4_15,2)
        vals.superolein4_16 = round(vals.superolein4_16,2)
        vals.superolein4_17 = round(vals.superolein4_17,2)
        vals.superolein4_18 = round(vals.superolein4_18,2)
        vals.superolein4_19 = round(vals.superolein4_19,2)
        vals.superolein4_20 = round(vals.superolein4_20,2)
        vals.superolein4_21 = round(vals.superolein4_21,2)
        vals.superolein4_22 = round(vals.superolein4_22,2)
        vals.superolein4_23 = round(vals.superolein4_23,2)
        vals.superolein4_24 = round(vals.superolein4_24,2)

        vals.superolein2_15 = round(vals.superolein2_15,2)
        vals.superolein2_16 = round(vals.superolein2_16,2)
        vals.superolein2_17 = round(vals.superolein2_17,2)
        vals.superolein2_18 = round(vals.superolein2_18,2)
        vals.superolein2_19 = round(vals.superolein2_19,2)
        vals.superolein2_20 = round(vals.superolein2_20,2)
        vals.superolein2_21 = round(vals.superolein2_21,2)
        vals.superolein2_22 = round(vals.superolein2_22,2)
        vals.superolein2_23 = round(vals.superolein2_23,2)
        vals.superolein2_24 = round(vals.superolein2_24,2)

        vals.superolein3_15 = round(vals.superolein4_15,2)
        vals.superolein3_16 = round(vals.superolein4_16,2)
        vals.superolein3_17 = round(vals.superolein4_17,2)
        vals.superolein3_18 = round(vals.superolein4_18,2)
        vals.superolein3_19 = round(vals.superolein4_19,2)
        vals.superolein3_20 = round(vals.superolein4_20,2)
        vals.superolein3_21 = round(vals.superolein4_21,2)
        vals.superolein3_22 = round(vals.superolein4_22,2)
        vals.superolein3_23 = round(vals.superolein4_23,2)
        vals.superolein3_24 = round(vals.superolein4_24,2)

        vals.mpptotal15 = round(vals.mpptotal15,2)
        vals.mpptotal16 = round(vals.mpptotal16,2)
        vals.mpptotal17 = round(vals.mpptotal17,2)
        vals.mpptotal18 = round(vals.mpptotal18,2)
        vals.mpptotal19 = round(vals.mpptotal19,2)
        vals.mpptotal20 = round(vals.mpptotal20,2)
        vals.mpptotal21 = round(vals.mpptotal21,2)
        vals.mpptotal22 = round(vals.mpptotal22,2)
        vals.mpptotal23 = round(vals.mpptotal23,2)
        vals.mpptotal24 = round(vals.mpptotal24,2)

        vals.ls15 = round(vals.ls15,2)
        vals.ls16 = round(vals.ls16,2)
        vals.ls17 = round(vals.ls17,2)
        vals.ls18 = round(vals.ls18,2)
        vals.ls19 = round(vals.ls19,2)
        vals.ls20 = round(vals.ls20,2)
        vals.ls21 = round(vals.ls21,2)
        vals.ls22 = round(vals.ls22,2)
        vals.ls23 = round(vals.ls23,2)
        vals.ls24 = round(vals.ls24,2)

        vals.nis15 = round(vals.nis15,2)
        vals.nis16 = round(vals.nis16,2)
        vals.nis17 = round(vals.nis17,2)
        vals.nis18 = round(vals.nis18,2)
        vals.nis19 = round(vals.nis19,2)
        vals.nis20 = round(vals.nis20,2)
        vals.nis21 = round(vals.nis21,2)
        vals.nis22 = round(vals.nis22,2)
        vals.nis23 = round(vals.nis23,2)
        vals.nis24 = round(vals.nis24,2)

        vals.nim15 = round(vals.nim15,2)
        vals.nim16 = round(vals.nim16,2)
        vals.nim17 = round(vals.nim17,2)
        vals.nim18 = round(vals.nim18,2)
        vals.nim19 = round(vals.nim19,2)
        vals.nim20 = round(vals.nim20,2)
        vals.nim21 = round(vals.nim21,2)
        vals.nim22 = round(vals.nim22,2)
        vals.nim23 = round(vals.nim23,2)
        vals.nim24 = round(vals.nim24,2)

        vals.is15 = round(vals.is15,2)
        vals.is16 = round(vals.is16,2)
        vals.is17 = round(vals.is17,2)
        vals.is18 = round(vals.is18,2)
        vals.is19 = round(vals.is19,2)
        vals.is20 = round(vals.is20,2)
        vals.is21 = round(vals.is21,2)
        vals.is22 = round(vals.is22,2)
        vals.is23 = round(vals.is23,2)
        vals.is24 = round(vals.is24,2)

        vals.im15 = round(vals.im15,2)
        vals.im16 = round(vals.im16,2)
        vals.im17 = round(vals.im17,2)
        vals.im18 = round(vals.im18,2)
        vals.im19 = round(vals.im19,2)
        vals.im20 = round(vals.im20,2)
        vals.im21 = round(vals.im21,2)
        vals.im22 = round(vals.im22,2)
        vals.im23 = round(vals.im23,2)
        vals.im24 = round(vals.im24,2)

        vals.asm15 = round(vals.asm15,2)
        vals.asm16 = round(vals.asm16,2)
        vals.asm17 = round(vals.asm17,2)
        vals.asm18 = round(vals.asm18,2)
        vals.asm19 = round(vals.asm19,2)
        vals.asm20 = round(vals.asm20,2)
        vals.asm21 = round(vals.asm21,2)
        vals.asm22 = round(vals.asm22,2)
        vals.asm23 = round(vals.asm23,2)
        vals.asm24 = round(vals.asm24,2)

        vals.bot15 = round(vals.bot15,2)
        vals.bot16 = round(vals.bot16,2)
        vals.bot17 = round(vals.bot17,2)
        vals.bot18 = round(vals.bot18,2)
        vals.bot19 = round(vals.bot19,2)
        vals.bot20 = round(vals.bot20,2)
        vals.bot21 = round(vals.bot21,2)
        vals.bot22 = round(vals.bot22,2)
        vals.bot23 = round(vals.bot23,2)
        vals.bot24 = round(vals.bot24,2)

        vals.tvp15 = round(vals.tvp15,2)
        vals.tvp16 = round(vals.tvp16,2)
        vals.tvp17 = round(vals.tvp17,2)
        vals.tvp18 = round(vals.tvp18,2)
        vals.tvp19 = round(vals.tvp19,2)
        vals.tvp20 = round(vals.tvp20,2)
        vals.tvp21 = round(vals.tvp21,2)
        vals.tvp22 = round(vals.tvp22,2)
        vals.tvp23 = round(vals.tvp23,2)
        vals.tvp24 = round(vals.tvp24,2)

        vals.bulk15 = round(vals.bulk15,2)
        vals.bulk16 = round(vals.bulk16,2)
        vals.bulk17 = round(vals.bulk17,2)
        vals.bulk18 = round(vals.bulk18,2)
        vals.bulk19 = round(vals.bulk19,2)
        vals.bulk20 = round(vals.bulk20,2)
        vals.bulk21 = round(vals.bulk21,2)
        vals.bulk22 = round(vals.bulk22,2)
        vals.bulk23 = round(vals.bulk23,2)
        vals.bulk24 = round(vals.bulk24,2)

        vals.packaged15 = round(vals.packaged15,2)
        vals.packaged16 = round(vals.packaged16,2)
        vals.packaged17 = round(vals.packaged17,2)
        vals.packaged18 = round(vals.packaged18,2)
        vals.packaged19 = round(vals.packaged19,2)
        vals.packaged20 = round(vals.packaged20,2)
        vals.packaged21 = round(vals.packaged21,2)
        vals.packaged22 = round(vals.packaged22,2)
        vals.packaged23 = round(vals.packaged23,2)
        vals.packaged24 = round(vals.packaged24,2)

        vals.sob_n15 = round(vals.sob_n15,2)
        vals.sob_n16 = round(vals.sob_n16,2)
        vals.sob_n17 = round(vals.sob_n17,2)
        vals.sob_n18 = round(vals.sob_n18,2)
        vals.sob_n19 = round(vals.sob_n19,2)
        vals.sob_n20 = round(vals.sob_n20,2)
        vals.sob_n21 = round(vals.sob_n21,2)
        vals.sob_n22 = round(vals.sob_n22,2)
        vals.sob_n23 = round(vals.sob_n23,2)
        vals.sob_n24 = round(vals.sob_n24,2)

        vals.cpf_n15 = round(vals.cpf_n15,2)
        vals.cpf_n16 = round(vals.cpf_n16,2)
        vals.cpf_n17 = round(vals.cpf_n17,2)
        vals.cpf_n18 = round(vals.cpf_n18,2)
        vals.cpf_n19 = round(vals.cpf_n19,2)
        vals.cpf_n20 = round(vals.cpf_n20,2)
        vals.cpf_n21 = round(vals.cpf_n21,2)
        vals.cpf_n22 = round(vals.cpf_n22,2)
        vals.cpf_n23 = round(vals.cpf_n23,2)
        vals.cpf_n24 = round(vals.cpf_n24,2)

        vals.sob_d15 = round(vals.sob_d15,2)
        vals.sob_d16 = round(vals.sob_d16,2)
        vals.sob_d17 = round(vals.sob_d17,2)
        vals.sob_d18 = round(vals.sob_d18,2)
        vals.sob_d19 = round(vals.sob_d19,2)
        vals.sob_d20 = round(vals.sob_d20,2)
        vals.sob_d21 = round(vals.sob_d21,2)
        vals.sob_d22 = round(vals.sob_d22,2)
        vals.sob_d23 = round(vals.sob_d23,2)
        vals.sob_d24 = round(vals.sob_d24,2)

        vals.cpf_d15 = round(vals.cpf_d15,2)
        vals.cpf_d16 = round(vals.cpf_d16,2)
        vals.cpf_d17 = round(vals.cpf_d17,2)
        vals.cpf_d18 = round(vals.cpf_d18,2)
        vals.cpf_d19 = round(vals.cpf_d19,2)
        vals.cpf_d20 = round(vals.cpf_d20,2)
        vals.cpf_d21 = round(vals.cpf_d21,2)
        vals.cpf_d22 = round(vals.cpf_d22,2)
        vals.cpf_d23 = round(vals.cpf_d23,2)
        vals.cpf_d24 = round(vals.cpf_d24,2)

        vals.sob_fr15 = round(vals.sob_fr15,2)
        vals.sob_fr16 = round(vals.sob_fr16,2)
        vals.sob_fr17 = round(vals.sob_fr17,2)
        vals.sob_fr18 = round(vals.sob_fr18,2)
        vals.sob_fr19 = round(vals.sob_fr19,2)
        vals.sob_fr20 = round(vals.sob_fr20,2)
        vals.sob_fr21 = round(vals.sob_fr21,2)
        vals.sob_fr22 = round(vals.sob_fr22,2)
        vals.sob_fr23 = round(vals.sob_fr23,2)
        vals.sob_fr24 = round(vals.sob_fr24,2)

        vals.cpf_fr15 = round(vals.cpf_fr15,2)
        vals.cpf_fr16 = round(vals.cpf_fr16,2)
        vals.cpf_fr17 = round(vals.cpf_fr17,2)
        vals.cpf_fr18 = round(vals.cpf_fr18,2)
        vals.cpf_fr19 = round(vals.cpf_fr19,2)
        vals.cpf_fr20 = round(vals.cpf_fr20,2)
        vals.cpf_fr21 = round(vals.cpf_fr21,2)
        vals.cpf_fr22 = round(vals.cpf_fr22,2)
        vals.cpf_fr23 = round(vals.cpf_fr23,2)
        vals.cpf_fr24 = round(vals.cpf_fr24,2)

        vals.sob_h15 = round(vals.sob_h15,2)
        vals.sob_h16 = round(vals.sob_h16,2)
        vals.sob_h17 = round(vals.sob_h17,2)
        vals.sob_h18 = round(vals.sob_h18,2)
        vals.sob_h19 = round(vals.sob_h19,2)
        vals.sob_h20 = round(vals.sob_h20,2)
        vals.sob_h21 = round(vals.sob_h21,2)
        vals.sob_h22 = round(vals.sob_h22,2)
        vals.sob_h23 = round(vals.sob_h23,2)
        vals.sob_h24 = round(vals.sob_h24,2)

        vals.sob_perf15 = round(vals.sob_perf15,2)
        vals.sob_perf16 = round(vals.sob_perf16,2)
        vals.sob_perf17 = round(vals.sob_perf17,2)
        vals.sob_perf18 = round(vals.sob_perf18,2)
        vals.sob_perf19 = round(vals.sob_perf19,2)
        vals.sob_perf20 = round(vals.sob_perf20,2)
        vals.sob_perf21 = round(vals.sob_perf21,2)
        vals.sob_perf22 = round(vals.sob_perf22,2)
        vals.sob_perf23 = round(vals.sob_perf23,2)
        vals.sob_perf24 = round(vals.sob_perf24,2)

        vals.cpf_lv15 = round(vals.cpf_lv15,2)
        vals.cpf_lv16 = round(vals.cpf_lv16,2)
        vals.cpf_lv17 = round(vals.cpf_lv17,2)
        vals.cpf_lv18 = round(vals.cpf_lv18,2)
        vals.cpf_lv19 = round(vals.cpf_lv19,2)
        vals.cpf_lv20 = round(vals.cpf_lv20,2)
        vals.cpf_lv21 = round(vals.cpf_lv21,2)
        vals.cpf_lv22 = round(vals.cpf_lv22,2)
        vals.cpf_lv23 = round(vals.cpf_lv23,2)
        vals.cpf_lv24 = round(vals.cpf_lv24,2)

        vals.cbibv15 = round(vals.cbibv15,2)         
        vals.cbibv16 = round(vals.cbibv16,2) 
        vals.cbibv17 = round(vals.cbibv17,2) 
        vals.cbibv18 = round(vals.cbibv18,2) 
        vals.cbibv19 = round(vals.cbibv19,2)         
        vals.cbibv20 = round(vals.cbibv20,2) 
        vals.cbibv21 = round(vals.cbibv21,2)         
        vals.cbibv22 = round(vals.cbibv22,2)         
        vals.cbibv23 = round(vals.cbibv23,2)         
        vals.cbibv24 = round(vals.cbibv24,2)   

        vals.cbibv_gsbo15 = round(vals.cbibv_gsbo15,2)         
        vals.cbibv_gsbo16 = round(vals.cbibv_gsbo16,2) 
        vals.cbibv_gsbo17 = round(vals.cbibv_gsbo17,2) 
        vals.cbibv_gsbo18 = round(vals.cbibv_gsbo18,2) 
        vals.cbibv_gsbo19 = round(vals.cbibv_gsbo19,2)         
        vals.cbibv_gsbo20 = round(vals.cbibv_gsbo20,2) 
        vals.cbibv_gsbo21 = round(vals.cbibv_gsbo21,2)         
        vals.cbibv_gsbo22 = round(vals.cbibv_gsbo22,2)         
        vals.cbibv_gsbo23 = round(vals.cbibv_gsbo23,2)         
        vals.cbibv_gsbo24 = round(vals.cbibv_gsbo24,2)   

        vals.cbibv_blendedoil15 = round(vals.cbibv_blendedoil15,2)         
        vals.cbibv_blendedoil16 = round(vals.cbibv_blendedoil16,2) 
        vals.cbibv_blendedoil17 = round(vals.cbibv_blendedoil17,2) 
        vals.cbibv_blendedoil18 = round(vals.cbibv_blendedoil18,2) 
        vals.cbibv_blendedoil19 = round(vals.cbibv_blendedoil19,2)         
        vals.cbibv_blendedoil20 = round(vals.cbibv_blendedoil20,2) 
        vals.cbibv_blendedoil21 = round(vals.cbibv_blendedoil21,2)         
        vals.cbibv_blendedoil22 = round(vals.cbibv_blendedoil22,2)         
        vals.cbibv_blendedoil23 = round(vals.cbibv_blendedoil23,2)         
        vals.cbibv_blendedoil24 = round(vals.cbibv_blendedoil24,2)   

        vals.cbibv_rol15 = round(vals.cbibv_rol15,2)         
        vals.cbibv_rol16 = round(vals.cbibv_rol16,2) 
        vals.cbibv_rol17 = round(vals.cbibv_rol17,2) 
        vals.cbibv_rol18 = round(vals.cbibv_rol18,2) 
        vals.cbibv_rol19 = round(vals.cbibv_rol19,2)         
        vals.cbibv_rol20 = round(vals.cbibv_rol20,2) 
        vals.cbibv_rol21 = round(vals.cbibv_rol21,2)         
        vals.cbibv_rol22 = round(vals.cbibv_rol22,2)         
        vals.cbibv_rol23 = round(vals.cbibv_rol23,2)         
        vals.cbibv_rol24 = round(vals.cbibv_rol24,2)  

        vals.cbibv_spmf15 = round(vals.cbibv_spmf15,2)         
        vals.cbibv_spmf16 = round(vals.cbibv_spmf16,2) 
        vals.cbibv_spmf17 = round(vals.cbibv_spmf17,2) 
        vals.cbibv_spmf18 = round(vals.cbibv_spmf18,2) 
        vals.cbibv_spmf19 = round(vals.cbibv_spmf19,2)         
        vals.cbibv_spmf20 = round(vals.cbibv_spmf20,2) 
        vals.cbibv_spmf21 = round(vals.cbibv_spmf21,2)         
        vals.cbibv_spmf22 = round(vals.cbibv_spmf22,2)         
        vals.cbibv_spmf23 = round(vals.cbibv_spmf23,2)         
        vals.cbibv_spmf24 = round(vals.cbibv_spmf24,2)    

        vals.cpetv15 = round(vals.cpetv15,2)
        vals.cpetv16 = round(vals.cpetv16,2)
        vals.cpetv17 = round(vals.cpetv17,2)
        vals.cpetv18 = round(vals.cpetv18,2)
        vals.cpetv19 = round(vals.cpetv19,2)
        vals.cpetv20 = round(vals.cpetv20,2)
        vals.cpetv21 = round(vals.cpetv21,2)
        vals.cpetv22 = round(vals.cpetv22,2)
        vals.cpetv23 = round(vals.cpetv23,2)
        vals.cpetv24 = round(vals.cpetv24,2)

        vals.cpetv_gsbo1_15 = round(vals.cpetv_gsbo1_15,2)        
        vals.cpetv_gsbo1_16 = round(vals.cpetv_gsbo1_16,2)
        vals.cpetv_gsbo1_17 = round(vals.cpetv_gsbo1_17,2)
        vals.cpetv_gsbo1_18 = round(vals.cpetv_gsbo1_18,2)
        vals.cpetv_gsbo1_19 = round(vals.cpetv_gsbo1_19,2)
        vals.cpetv_gsbo1_20 = round(vals.cpetv_gsbo1_20,2)
        vals.cpetv_gsbo1_21 = round(vals.cpetv_gsbo1_21,2)
        vals.cpetv_gsbo1_22 = round(vals.cpetv_gsbo1_22,2)
        vals.cpetv_gsbo1_23 = round(vals.cpetv_gsbo1_23,2)
        vals.cpetv_gsbo1_24 = round(vals.cpetv_gsbo1_24,2)

        vals.cpetv_gsbo2_15 = round(vals.cpetv_gsbo2_15,2)        
        vals.cpetv_gsbo2_16 = round(vals.cpetv_gsbo2_16,2)
        vals.cpetv_gsbo2_17 = round(vals.cpetv_gsbo2_17,2)
        vals.cpetv_gsbo2_18 = round(vals.cpetv_gsbo2_18,2)
        vals.cpetv_gsbo2_19 = round(vals.cpetv_gsbo2_19,2)
        vals.cpetv_gsbo2_20 = round(vals.cpetv_gsbo2_20,2)
        vals.cpetv_gsbo2_21 = round(vals.cpetv_gsbo2_21,2)
        vals.cpetv_gsbo2_22 = round(vals.cpetv_gsbo2_22,2)
        vals.cpetv_gsbo2_23 = round(vals.cpetv_gsbo2_23,2)
        vals.cpetv_gsbo2_24 = round(vals.cpetv_gsbo2_24,2)

        vals.cpetv_gsbo3_15 = round(vals.cpetv_gsbo3_15,2)        
        vals.cpetv_gsbo3_16 = round(vals.cpetv_gsbo3_16,2)
        vals.cpetv_gsbo3_17 = round(vals.cpetv_gsbo3_17,2)
        vals.cpetv_gsbo3_18 = round(vals.cpetv_gsbo3_18,2)
        vals.cpetv_gsbo3_19 = round(vals.cpetv_gsbo3_19,2)
        vals.cpetv_gsbo3_20 = round(vals.cpetv_gsbo3_20,2)
        vals.cpetv_gsbo3_21 = round(vals.cpetv_gsbo3_21,2)
        vals.cpetv_gsbo3_22 = round(vals.cpetv_gsbo3_22,2)
        vals.cpetv_gsbo3_23 = round(vals.cpetv_gsbo3_23,2)
        vals.cpetv_gsbo3_24 = round(vals.cpetv_gsbo3_24,2)

        vals.cpetv_gsbo4_15 = round(vals.cpetv_gsbo4_15,2)        
        vals.cpetv_gsbo4_16 = round(vals.cpetv_gsbo4_16,2)
        vals.cpetv_gsbo4_17 = round(vals.cpetv_gsbo4_17,2)
        vals.cpetv_gsbo4_18 = round(vals.cpetv_gsbo4_18,2)
        vals.cpetv_gsbo4_19 = round(vals.cpetv_gsbo4_19,2)
        vals.cpetv_gsbo4_20 = round(vals.cpetv_gsbo4_20,2)
        vals.cpetv_gsbo4_21 = round(vals.cpetv_gsbo4_21,2)
        vals.cpetv_gsbo4_22 = round(vals.cpetv_gsbo4_22,2)
        vals.cpetv_gsbo4_23 = round(vals.cpetv_gsbo4_23,2)
        vals.cpetv_gsbo4_24 = round(vals.cpetv_gsbo4_24,2)

        vals.cpetv_blendedoil1_15 = round(vals.cpetv_blendedoil1_15,2)
        vals.cpetv_blendedoil1_16 = round(vals.cpetv_blendedoil1_16,2)
        vals.cpetv_blendedoil1_17 = round(vals.cpetv_blendedoil1_17,2)
        vals.cpetv_blendedoil1_18 = round(vals.cpetv_blendedoil1_18,2)
        vals.cpetv_blendedoil1_19 = round(vals.cpetv_blendedoil1_19,2)
        vals.cpetv_blendedoil1_20 = round(vals.cpetv_blendedoil1_20,2)
        vals.cpetv_blendedoil1_21 = round(vals.cpetv_blendedoil1_21,2)
        vals.cpetv_blendedoil1_22 = round(vals.cpetv_blendedoil1_22,2)
        vals.cpetv_blendedoil1_23 = round(vals.cpetv_blendedoil1_23,2)
        vals.cpetv_blendedoil1_24 = round(vals.cpetv_blendedoil1_24,2) 

        vals.cpetv_blendedoil2_15 = round(vals.cpetv_blendedoil2_15,2)
        vals.cpetv_blendedoil2_16 = round(vals.cpetv_blendedoil2_16,2)
        vals.cpetv_blendedoil2_17 = round(vals.cpetv_blendedoil2_17,2)
        vals.cpetv_blendedoil2_18 = round(vals.cpetv_blendedoil2_18,2)
        vals.cpetv_blendedoil2_19 = round(vals.cpetv_blendedoil2_19,2)
        vals.cpetv_blendedoil2_20 = round(vals.cpetv_blendedoil2_20,2)
        vals.cpetv_blendedoil2_21 = round(vals.cpetv_blendedoil2_21,2)
        vals.cpetv_blendedoil2_22 = round(vals.cpetv_blendedoil2_22,2)
        vals.cpetv_blendedoil2_23 = round(vals.cpetv_blendedoil2_23,2)
        vals.cpetv_blendedoil2_24 = round(vals.cpetv_blendedoil2_24,2)

        vals.cpetv_blendedoil3_15 = round(vals.cpetv_blendedoil3_15,2)
        vals.cpetv_blendedoil3_16 = round(vals.cpetv_blendedoil3_16,2)
        vals.cpetv_blendedoil3_17 = round(vals.cpetv_blendedoil3_17,2)
        vals.cpetv_blendedoil3_18 = round(vals.cpetv_blendedoil3_18,2)
        vals.cpetv_blendedoil3_19 = round(vals.cpetv_blendedoil3_19,2)
        vals.cpetv_blendedoil3_20 = round(vals.cpetv_blendedoil3_20,2)
        vals.cpetv_blendedoil3_21 = round(vals.cpetv_blendedoil3_21,2)
        vals.cpetv_blendedoil3_22 = round(vals.cpetv_blendedoil3_22,2)
        vals.cpetv_blendedoil3_23 = round(vals.cpetv_blendedoil3_23,2)
        vals.cpetv_blendedoil3_24 = round(vals.cpetv_blendedoil3_24,2)

        vals.cpetv_blendedoil4_15 = round(vals.cpetv_blendedoil4_15,2)
        vals.cpetv_blendedoil4_16 = round(vals.cpetv_blendedoil4_16,2)
        vals.cpetv_blendedoil4_17 = round(vals.cpetv_blendedoil4_17,2)
        vals.cpetv_blendedoil4_18 = round(vals.cpetv_blendedoil4_18,2)
        vals.cpetv_blendedoil4_19 = round(vals.cpetv_blendedoil4_19,2)
        vals.cpetv_blendedoil4_20 = round(vals.cpetv_blendedoil4_20,2)
        vals.cpetv_blendedoil4_21 = round(vals.cpetv_blendedoil4_21,2)
        vals.cpetv_blendedoil4_22 = round(vals.cpetv_blendedoil4_22,2)
        vals.cpetv_blendedoil4_23 = round(vals.cpetv_blendedoil4_23,2)
        vals.cpetv_blendedoil4_24 = round(vals.cpetv_blendedoil4_24,2)

        vals.cpetv_superolein1_15 = round(vals.cpetv_superolein1_15,2)          
        vals.cpetv_superolein1_16 = round(vals.cpetv_superolein1_16,2)
        vals.cpetv_superolein1_17 = round(vals.cpetv_superolein1_17,2)
        vals.cpetv_superolein1_18 = round(vals.cpetv_superolein1_18,2)
        vals.cpetv_superolein1_19 = round(vals.cpetv_superolein1_19,2)
        vals.cpetv_superolein1_20 = round(vals.cpetv_superolein1_20,2)
        vals.cpetv_superolein1_21 = round(vals.cpetv_superolein1_21,2)
        vals.cpetv_superolein1_22 = round(vals.cpetv_superolein1_22,2)
        vals.cpetv_superolein1_23 = round(vals.cpetv_superolein1_23,2)
        vals.cpetv_superolein1_24 = round(vals.cpetv_superolein1_24,2)

        vals.cpetv_superolein2_15 = round(vals.cpetv_superolein2_15,2)          
        vals.cpetv_superolein2_16 = round(vals.cpetv_superolein2_16,2)
        vals.cpetv_superolein2_17 = round(vals.cpetv_superolein2_17,2)
        vals.cpetv_superolein2_18 = round(vals.cpetv_superolein2_18,2)
        vals.cpetv_superolein2_19 = round(vals.cpetv_superolein2_19,2)
        vals.cpetv_superolein2_20 = round(vals.cpetv_superolein2_20,2)
        vals.cpetv_superolein2_21 = round(vals.cpetv_superolein2_21,2)
        vals.cpetv_superolein2_22 = round(vals.cpetv_superolein2_22,2)
        vals.cpetv_superolein2_23 = round(vals.cpetv_superolein2_23,2)
        vals.cpetv_superolein2_24 = round(vals.cpetv_superolein2_24,2)

        vals.cpetv_superolein3_15 = round(vals.cpetv_superolein3_15,2)          
        vals.cpetv_superolein3_16 = round(vals.cpetv_superolein3_16,2)
        vals.cpetv_superolein3_17 = round(vals.cpetv_superolein3_17,2)
        vals.cpetv_superolein3_18 = round(vals.cpetv_superolein3_18,2)
        vals.cpetv_superolein3_19 = round(vals.cpetv_superolein3_19,2)
        vals.cpetv_superolein3_20 = round(vals.cpetv_superolein3_20,2)
        vals.cpetv_superolein3_21 = round(vals.cpetv_superolein3_21,2)
        vals.cpetv_superolein3_22 = round(vals.cpetv_superolein3_22,2)
        vals.cpetv_superolein3_23 = round(vals.cpetv_superolein3_23,2)
        vals.cpetv_superolein3_24 = round(vals.cpetv_superolein3_24,2)

        vals.cpetv_superolein4_15 = round(vals.cpetv_superolein4_15,2)          
        vals.cpetv_superolein4_16 = round(vals.cpetv_superolein4_16,2)
        vals.cpetv_superolein4_17 = round(vals.cpetv_superolein4_17,2)
        vals.cpetv_superolein4_18 = round(vals.cpetv_superolein4_18,2)
        vals.cpetv_superolein4_19 = round(vals.cpetv_superolein4_19,2)
        vals.cpetv_superolein4_20 = round(vals.cpetv_superolein4_20,2)
        vals.cpetv_superolein4_21 = round(vals.cpetv_superolein4_21,2)
        vals.cpetv_superolein4_22 = round(vals.cpetv_superolein4_22,2)
        vals.cpetv_superolein4_23 = round(vals.cpetv_superolein4_23,2)
        vals.cpetv_superolein4_24 = round(vals.cpetv_superolein4_24,2)

        vals.mpbest15 = round(vals.mpbest15,2)
        vals.mpbest16 = round(vals.mpbest16,2)
        vals.mpbest17 = round(vals.mpbest17,2)
        vals.mpbest18 = round(vals.mpbest18,2)
        vals.mpbest19 = round(vals.mpbest19,2)
        vals.mpbest20 = round(vals.mpbest20,2)
        vals.mpbest21 = round(vals.mpbest21,2)
        vals.mpbest22 = round(vals.mpbest22,2)
        vals.mpbest23 = round(vals.mpbest23,2)
        vals.mpbest24 = round(vals.mpbest24,2)

        vals.mpbuis15 = round(vals.mpbuis15,2)
        vals.mpbuis16 = round(vals.mpbuis16,2)
        vals.mpbuis17 = round(vals.mpbuis17,2)
        vals.mpbuis18 = round(vals.mpbuis18,2)
        vals.mpbuis19 = round(vals.mpbuis19,2)
        vals.mpbuis20 = round(vals.mpbuis20,2)
        vals.mpbuis21 = round(vals.mpbuis21,2)
        vals.mpbuis22 = round(vals.mpbuis22,2)
        vals.mpbuis23 = round(vals.mpbuis23,2)
        vals.mpbuis24 = round(vals.mpbuis24,2)

        vals.bib15 = round(vals.bib15,2)
        vals.bib16 = round(vals.bib16,2)
        vals.bib17 = round(vals.bib17,2)
        vals.bib18 = round(vals.bib18,2)
        vals.bib19 = round(vals.bib19,2)
        vals.bib20 = round(vals.bib20,2)
        vals.bib21 = round(vals.bib21,2)
        vals.bib22 = round(vals.bib22,2)
        vals.bib23 = round(vals.bib23,2)
        vals.bib24 = round(vals.bib24,2)

        vals.pet15 = round(vals.pet15,2)
        vals.pet16 = round(vals.pet16,2)
        vals.pet17 = round(vals.pet17,2)
        vals.pet18 = round(vals.pet18,2)
        vals.pet19 = round(vals.pet19,2)
        vals.pet20 = round(vals.pet20,2)
        vals.pet21 = round(vals.pet21,2)
        vals.pet22 = round(vals.pet22,2)
        vals.pet23 = round(vals.pet23,2)
        vals.pet24 = round(vals.pet24,2)

        vals.a5l4buis15 = round(vals.a5l4buis15,2)        
        vals.a5l4buis16 = round(vals.a5l4buis16,2)
        vals.a5l4buis17 = round(vals.a5l4buis17,2)
        vals.a5l4buis18 = round(vals.a5l4buis18,2)
        vals.a5l4buis19 = round(vals.a5l4buis19,2)
        vals.a5l4buis20 = round(vals.a5l4buis20,2)
        vals.a5l4buis21 = round(vals.a5l4buis21,2)
        vals.a5l4buis22 = round(vals.a5l4buis22,2)
        vals.a5l4buis23 = round(vals.a5l4buis23,2)
        vals.a5l4buis24 = round(vals.a5l4buis24,2)

        vals.a20lbuis15 = round(vals.a20lbuis15,2)
        vals.a20lbuis16 = round(vals.a20lbuis16,2)
        vals.a20lbuis17 = round(vals.a20lbuis17,2)
        vals.a20lbuis18 = round(vals.a20lbuis18,2)
        vals.a20lbuis19 = round(vals.a20lbuis19,2)
        vals.a20lbuis20 = round(vals.a20lbuis20,2)
        vals.a20lbuis21 = round(vals.a20lbuis21,2)
        vals.a20lbuis22 = round(vals.a20lbuis22,2)
        vals.a20lbuis23 = round(vals.a20lbuis23,2)
        vals.a20lbuis24 = round(vals.a20lbuis24,2)

        vals.a20lbbuis15 = round(vals.a20lbbuis15,2)
        vals.a20lbbuis16 = round(vals.a20lbbuis16,2)
        vals.a20lbbuis17 = round(vals.a20lbbuis17,2)
        vals.a20lbbuis18 = round(vals.a20lbbuis18,2)
        vals.a20lbbuis19 = round(vals.a20lbbuis19,2)
        vals.a20lbbuis20 = round(vals.a20lbbuis20,2)
        vals.a20lbbuis21 = round(vals.a20lbbuis21,2)
        vals.a20lbbuis22 = round(vals.a20lbbuis22,2)
        vals.a20lbbuis23 = round(vals.a20lbbuis23,2)
        vals.a20lbbuis24 = round(vals.a20lbbuis24,2)

        vals.a10l2buis15 = round(vals.a10l2buis15,2)
        vals.a10l2buis16 = round(vals.a10l2buis16,2)
        vals.a10l2buis17 = round(vals.a10l2buis17,2)
        vals.a10l2buis18 = round(vals.a10l2buis18,2)
        vals.a10l2buis19 = round(vals.a10l2buis19,2)
        vals.a10l2buis20 = round(vals.a10l2buis20,2)
        vals.a10l2buis21 = round(vals.a10l2buis21,2)
        vals.a10l2buis22 = round(vals.a10l2buis22,2)
        vals.a10l2buis23 = round(vals.a10l2buis23,2)
        vals.a10l2buis24 = round(vals.a10l2buis24,2)

        vals.abib22lbuis15 = round(vals.abib22lbuis15,2)
        vals.abib22lbuis16 = round(vals.abib22lbuis16,2)
        vals.abib22lbuis17 = round(vals.abib22lbuis17,2)
        vals.abib22lbuis18 = round(vals.abib22lbuis18,2)
        vals.abib22lbuis19 = round(vals.abib22lbuis19,2)
        vals.abib22lbuis20 = round(vals.abib22lbuis20,2)
        vals.abib22lbuis21 = round(vals.abib22lbuis21,2)
        vals.abib22lbuis22 = round(vals.abib22lbuis22,2)
        vals.abib22lbuis23 = round(vals.abib22lbuis23,2)
        vals.abib22lbuis24 = round(vals.abib22lbuis24,2)

        vals.atotalbuis15 = round(vals.atotalbuis15,2)
        vals.atotalbuis16 = round(vals.atotalbuis16,2)
        vals.atotalbuis17 = round(vals.atotalbuis17,2)
        vals.atotalbuis18 = round(vals.atotalbuis18,2)
        vals.atotalbuis19 = round(vals.atotalbuis19,2)
        vals.atotalbuis20 = round(vals.atotalbuis20,2)
        vals.atotalbuis21 = round(vals.atotalbuis21,2)
        vals.atotalbuis22 = round(vals.atotalbuis22,2)
        vals.atotalbuis23 = round(vals.atotalbuis23,2)
        vals.atotalbuis24 = round(vals.atotalbuis24,2)

        vals.m5l4buis15 = round(vals.m5l4buis15,2)        
        vals.m5l4buis16 = round(vals.m5l4buis16,2)
        vals.m5l4buis17 = round(vals.m5l4buis17,2)
        vals.m5l4buis18 = round(vals.m5l4buis18,2)
        vals.m5l4buis19 = round(vals.m5l4buis19,2)
        vals.m5l4buis20 = round(vals.m5l4buis20,2)
        vals.m5l4buis21 = round(vals.m5l4buis21,2)
        vals.m5l4buis22 = round(vals.m5l4buis22,2)
        vals.m5l4buis23 = round(vals.m5l4buis23,2)
        vals.m5l4buis24 = round(vals.m5l4buis24,2)

        vals.m20lbuis15 = round(vals.m20lbuis15,2)
        vals.m20lbuis16 = round(vals.m20lbuis16,2)
        vals.m20lbuis17 = round(vals.m20lbuis17,2)
        vals.m20lbuis18 = round(vals.m20lbuis18,2)
        vals.m20lbuis19 = round(vals.m20lbuis19,2)
        vals.m20lbuis20 = round(vals.m20lbuis20,2)
        vals.m20lbuis21 = round(vals.m20lbuis21,2)
        vals.m20lbuis22 = round(vals.m20lbuis22,2)
        vals.m20lbuis23 = round(vals.m20lbuis23,2)
        vals.m20lbuis24 = round(vals.m20lbuis24,2)

        vals.m20lbbuis15 = round(vals.m20lbbuis15,2)
        vals.m20lbbuis16 = round(vals.m20lbbuis16,2)
        vals.m20lbbuis17 = round(vals.m20lbbuis17,2)
        vals.m20lbbuis18 = round(vals.m20lbbuis18,2)
        vals.m20lbbuis19 = round(vals.m20lbbuis19,2)
        vals.m20lbbuis20 = round(vals.m20lbbuis20,2)
        vals.m20lbbuis21 = round(vals.m20lbbuis21,2)
        vals.m20lbbuis22 = round(vals.m20lbbuis22,2)
        vals.m20lbbuis23 = round(vals.m20lbbuis23,2)
        vals.m20lbbuis24 = round(vals.m20lbbuis24,2)

        vals.m10l2buis15 = round(vals.m10l2buis15,2)
        vals.m10l2buis16 = round(vals.m10l2buis16,2)
        vals.m10l2buis17 = round(vals.m10l2buis17,2)
        vals.m10l2buis18 = round(vals.m10l2buis18,2)
        vals.m10l2buis19 = round(vals.m10l2buis19,2)
        vals.m10l2buis20 = round(vals.m10l2buis20,2)
        vals.m10l2buis21 = round(vals.m10l2buis21,2)
        vals.m10l2buis22 = round(vals.m10l2buis22,2)
        vals.m10l2buis23 = round(vals.m10l2buis23,2)
        vals.m10l2buis24 = round(vals.m10l2buis24,2)

        vals.mbib22lbuis15 = round(vals.mbib22lbuis15,2)
        vals.mbib22lbuis16 = round(vals.mbib22lbuis16,2)
        vals.mbib22lbuis17 = round(vals.mbib22lbuis17,2)
        vals.mbib22lbuis18 = round(vals.mbib22lbuis18,2)
        vals.mbib22lbuis19 = round(vals.mbib22lbuis19,2)
        vals.mbib22lbuis20 = round(vals.mbib22lbuis20,2)
        vals.mbib22lbuis21 = round(vals.mbib22lbuis21,2)
        vals.mbib22lbuis22 = round(vals.mbib22lbuis22,2)
        vals.mbib22lbuis23 = round(vals.mbib22lbuis23,2)
        vals.mbib22lbuis24 = round(vals.mbib22lbuis24,2)

        vals.mtotalbuis15 = round(vals.mtotalbuis15,2)
        vals.mtotalbuis16 = round(vals.mtotalbuis16,2)
        vals.mtotalbuis17 = round(vals.mtotalbuis17,2)
        vals.mtotalbuis18 = round(vals.mtotalbuis18,2)
        vals.mtotalbuis19 = round(vals.mtotalbuis19,2)
        vals.mtotalbuis20 = round(vals.mtotalbuis20,2)
        vals.mtotalbuis21 = round(vals.mtotalbuis21,2)
        vals.mtotalbuis22 = round(vals.mtotalbuis22,2)
        vals.mtotalbuis23 = round(vals.mtotalbuis23,2)
        vals.mtotalbuis24 = round(vals.mtotalbuis24,2)

        vals.a5l4best15 = round(vals.a5l4best15,2)        
        vals.a5l4best16 = round(vals.a5l4best16,2)
        vals.a5l4best17 = round(vals.a5l4best17,2)
        vals.a5l4best18 = round(vals.a5l4best18,2)
        vals.a5l4best19 = round(vals.a5l4best19,2)
        vals.a5l4best20 = round(vals.a5l4best20,2)
        vals.a5l4best21 = round(vals.a5l4best21,2)
        vals.a5l4best22 = round(vals.a5l4best22,2)
        vals.a5l4best23 = round(vals.a5l4best23,2)
        vals.a5l4best24 = round(vals.a5l4best24,2)

        vals.a20lbest15 = round(vals.a20lbest15,2)
        vals.a20lbest16 = round(vals.a20lbest16,2)
        vals.a20lbest17 = round(vals.a20lbest17,2)
        vals.a20lbest18 = round(vals.a20lbest18,2)
        vals.a20lbest19 = round(vals.a20lbest19,2)
        vals.a20lbest20 = round(vals.a20lbest20,2)
        vals.a20lbest21 = round(vals.a20lbest21,2)
        vals.a20lbest22 = round(vals.a20lbest22,2)
        vals.a20lbest23 = round(vals.a20lbest23,2)
        vals.a20lbest24 = round(vals.a20lbest24,2)

        vals.a20lbbest15 = round(vals.a20lbbest15,2)
        vals.a20lbbest16 = round(vals.a20lbbest16,2)
        vals.a20lbbest17 = round(vals.a20lbbest17,2)
        vals.a20lbbest18 = round(vals.a20lbbest18,2)
        vals.a20lbbest19 = round(vals.a20lbbest19,2)
        vals.a20lbbest20 = round(vals.a20lbbest20,2)
        vals.a20lbbest21 = round(vals.a20lbbest21,2)
        vals.a20lbbest22 = round(vals.a20lbbest22,2)
        vals.a20lbbest23 = round(vals.a20lbbest23,2)
        vals.a20lbbest24 = round(vals.a20lbbest24,2)

        vals.a10l2best15 = round(vals.a10l2best15,2)
        vals.a10l2best16 = round(vals.a10l2best16,2)
        vals.a10l2best17 = round(vals.a10l2best17,2)
        vals.a10l2best18 = round(vals.a10l2best18,2)
        vals.a10l2best19 = round(vals.a10l2best19,2)
        vals.a10l2best20 = round(vals.a10l2best20,2)
        vals.a10l2best21 = round(vals.a10l2best21,2)
        vals.a10l2best22 = round(vals.a10l2best22,2)
        vals.a10l2best23 = round(vals.a10l2best23,2)
        vals.a10l2best24 = round(vals.a10l2best24,2)

        vals.abib22lbest15 = round(vals.abib22lbest15,2)
        vals.abib22lbest16 = round(vals.abib22lbest16,2)
        vals.abib22lbest17 = round(vals.abib22lbest17,2)
        vals.abib22lbest18 = round(vals.abib22lbest18,2)
        vals.abib22lbest19 = round(vals.abib22lbest19,2)
        vals.abib22lbest20 = round(vals.abib22lbest20,2)
        vals.abib22lbest21 = round(vals.abib22lbest21,2)
        vals.abib22lbest22 = round(vals.abib22lbest22,2)
        vals.abib22lbest23 = round(vals.abib22lbest23,2)
        vals.abib22lbest24 = round(vals.abib22lbest24,2)

        vals.atotalbest15 = round(vals.atotalbest15,2)
        vals.atotalbest16 = round(vals.atotalbest16,2)
        vals.atotalbest17 = round(vals.atotalbest17,2)
        vals.atotalbest18 = round(vals.atotalbest18,2)
        vals.atotalbest19 = round(vals.atotalbest19,2)
        vals.atotalbest20 = round(vals.atotalbest20,2)
        vals.atotalbest21 = round(vals.atotalbest21,2)
        vals.atotalbest22 = round(vals.atotalbest22,2)
        vals.atotalbest23 = round(vals.atotalbest23,2)
        vals.atotalbest24 = round(vals.atotalbest24,2)

        vals.m5l4best15 = round(vals.m5l4best15,2)        
        vals.m5l4best16 = round(vals.m5l4best16,2)
        vals.m5l4best17 = round(vals.m5l4best17,2)
        vals.m5l4best18 = round(vals.m5l4best18,2)
        vals.m5l4best19 = round(vals.m5l4best19,2)
        vals.m5l4best20 = round(vals.m5l4best20,2)
        vals.m5l4best21 = round(vals.m5l4best21,2)
        vals.m5l4best22 = round(vals.m5l4best22,2)
        vals.m5l4best23 = round(vals.m5l4best23,2)
        vals.m5l4best24 = round(vals.m5l4best24,2)

        vals.m20lbest15 = round(vals.m20lbest15,2)
        vals.m20lbest16 = round(vals.m20lbest16,2)
        vals.m20lbest17 = round(vals.m20lbest17,2)
        vals.m20lbest18 = round(vals.m20lbest18,2)
        vals.m20lbest19 = round(vals.m20lbest19,2)
        vals.m20lbest20 = round(vals.m20lbest20,2)
        vals.m20lbest21 = round(vals.m20lbest21,2)
        vals.m20lbest22 = round(vals.m20lbest22,2)
        vals.m20lbest23 = round(vals.m20lbest23,2)
        vals.m20lbest24 = round(vals.m20lbest24,2)

        vals.m20lbbest15 = round(vals.m20lbbest15,2)
        vals.m20lbbest16 = round(vals.m20lbbest16,2)
        vals.m20lbbest17 = round(vals.m20lbbest17,2)
        vals.m20lbbest18 = round(vals.m20lbbest18,2)
        vals.m20lbbest19 = round(vals.m20lbbest19,2)
        vals.m20lbbest20 = round(vals.m20lbbest20,2)
        vals.m20lbbest21 = round(vals.m20lbbest21,2)
        vals.m20lbbest22 = round(vals.m20lbbest22,2)
        vals.m20lbbest23 = round(vals.m20lbbest23,2)
        vals.m20lbbest24 = round(vals.m20lbbest24,2)

        vals.m10l2best15 = round(vals.m10l2best15,2)
        vals.m10l2best16 = round(vals.m10l2best16,2)
        vals.m10l2best17 = round(vals.m10l2best17,2)
        vals.m10l2best18 = round(vals.m10l2best18,2)
        vals.m10l2best19 = round(vals.m10l2best19,2)
        vals.m10l2best20 = round(vals.m10l2best20,2)
        vals.m10l2best21 = round(vals.m10l2best21,2)
        vals.m10l2best22 = round(vals.m10l2best22,2)
        vals.m10l2best23 = round(vals.m10l2best23,2)
        vals.m10l2best24 = round(vals.m10l2best24,2)

        vals.mbib22lbest15 = round(vals.mbib22lbest15,2)
        vals.mbib22lbest16 = round(vals.mbib22lbest16,2)
        vals.mbib22lbest17 = round(vals.mbib22lbest17,2)
        vals.mbib22lbest18 = round(vals.mbib22lbest18,2)
        vals.mbib22lbest19 = round(vals.mbib22lbest19,2)
        vals.mbib22lbest20 = round(vals.mbib22lbest20,2)
        vals.mbib22lbest21 = round(vals.mbib22lbest21,2)
        vals.mbib22lbest22 = round(vals.mbib22lbest22,2)
        vals.mbib22lbest23 = round(vals.mbib22lbest23,2)
        vals.mbib22lbest24 = round(vals.mbib22lbest24,2)

        vals.mtotalbest15 = round(vals.mtotalbest15,2)
        vals.mtotalbest16 = round(vals.mtotalbest16,2)
        vals.mtotalbest17 = round(vals.mtotalbest17,2)
        vals.mtotalbest18 = round(vals.mtotalbest18,2)
        vals.mtotalbest19 = round(vals.mtotalbest19,2)
        vals.mtotalbest20 = round(vals.mtotalbest20,2)
        vals.mtotalbest21 = round(vals.mtotalbest21,2)
        vals.mtotalbest22 = round(vals.mtotalbest22,2)
        vals.mtotalbest23 = round(vals.mtotalbest23,2)
        vals.mtotalbest24 = round(vals.mtotalbest24,2)

        vals.lslt15 = round(vals.lslt15,2)
        vals.lslt16 = round(vals.lslt16,2)
        vals.lslt17 = round(vals.lslt17,2)
        vals.lslt18 = round(vals.lslt18,2)
        vals.lslt19 = round(vals.lslt19,2)
        vals.lslt20 = round(vals.lslt20,2)
        vals.lslt21 = round(vals.lslt21,2)
        vals.lslt22 = round(vals.lslt22,2)
        vals.lslt23 = round(vals.lslt23,2)
        vals.lslt24 = round(vals.lslt24,2)

        vals.wsaht15 = round(vals.wsaht15,2)
        vals.wsaht16 = round(vals.wsaht16,2)
        vals.wsaht17 = round(vals.wsaht17,2)
        vals.wsaht18 = round(vals.wsaht18,2)
        vals.wsaht19 = round(vals.wsaht19,2)
        vals.wsaht20 = round(vals.wsaht20,2)
        vals.wsaht21 = round(vals.wsaht21,2)
        vals.wsaht22 = round(vals.wsaht22,2)
        vals.wsaht23 = round(vals.wsaht23,2)
        vals.wsaht24 = round(vals.wsaht24,2)

        vals.wsalt15 = round(vals.wsalt15,2)
        vals.wsalt16 = round(vals.wsalt16,2)
        vals.wsalt17 = round(vals.wsalt17,2)
        vals.wsalt18 = round(vals.wsalt18,2)
        vals.wsalt19 = round(vals.wsalt19,2)
        vals.wsalt20 = round(vals.wsalt20,2)
        vals.wsalt21 = round(vals.wsalt21,2)
        vals.wsalt22 = round(vals.wsalt22,2)
        vals.wsalt23 = round(vals.wsalt23,2)
        vals.wsalt24 = round(vals.wsalt24,2)

        vals.wsltlt15 = round(vals.wsltlt15,2)
        vals.wsltlt16 = round(vals.wsltlt16,2)
        vals.wsltlt17 = round(vals.wsltlt17,2)
        vals.wsltlt18 = round(vals.wsltlt18,2)
        vals.wsltlt19 = round(vals.wsltlt19,2)
        vals.wsltlt20 = round(vals.wsltlt20,2)
        vals.wsltlt21 = round(vals.wsltlt21,2)
        vals.wsltlt22 = round(vals.wsltlt22,2)
        vals.wsltlt23 = round(vals.wsltlt23,2)
        vals.wsltlt24 = round(vals.wsltlt24,2)

        vals.wsltht15 = round(vals.wsltht15,2)
        vals.wsltht16 = round(vals.wsltht16,2)
        vals.wsltht17 = round(vals.wsltht17,2)
        vals.wsltht18 = round(vals.wsltht18,2)
        vals.wsltht19 = round(vals.wsltht19,2)
        vals.wsltht20 = round(vals.wsltht20,2)
        vals.wsltht21 = round(vals.wsltht21,2)
        vals.wsltht22 = round(vals.wsltht22,2)
        vals.wsltht23 = round(vals.wsltht23,2)
        vals.wsltht24 = round(vals.wsltht24,2)

        vals.ysaht15 = round(vals.ysaht15,2)
        vals.ysaht16 = round(vals.ysaht16,2)
        vals.ysaht17 = round(vals.ysaht17,2)
        vals.ysaht18 = round(vals.ysaht18,2)
        vals.ysaht19 = round(vals.ysaht19,2)
        vals.ysaht20 = round(vals.ysaht20,2)
        vals.ysaht21 = round(vals.ysaht21,2)
        vals.ysaht22 = round(vals.ysaht22,2)
        vals.ysaht23 = round(vals.ysaht23,2)
        vals.ysaht24 = round(vals.ysaht24,2)

        vals.ysalt15 = round(vals.ysalt15,2)
        vals.ysalt16 = round(vals.ysalt16,2)
        vals.ysalt17 = round(vals.ysalt17,2)
        vals.ysalt18 = round(vals.ysalt18,2)
        vals.ysalt19 = round(vals.ysalt19,2)
        vals.ysalt20 = round(vals.ysalt20,2)
        vals.ysalt21 = round(vals.ysalt21,2)
        vals.ysalt22 = round(vals.ysalt22,2)
        vals.ysalt23 = round(vals.ysalt23,2)
        vals.ysalt24 = round(vals.ysalt24,2)

        vals.ysltlt15 = round(vals.ysltlt15,2)
        vals.ysltlt16 = round(vals.ysltlt16,2)
        vals.ysltlt17 = round(vals.ysltlt17,2)
        vals.ysltlt18 = round(vals.ysltlt18,2)
        vals.ysltlt19 = round(vals.ysltlt19,2)
        vals.ysltlt20 = round(vals.ysltlt20,2)
        vals.ysltlt21 = round(vals.ysltlt21,2)
        vals.ysltlt22 = round(vals.ysltlt22,2)
        vals.ysltlt23 = round(vals.ysltlt23,2)
        vals.ysltlt24 = round(vals.ysltlt24,2)

        vals.ysltht15 = round(vals.ysltht15,2)
        vals.ysltht16 = round(vals.ysltht16,2)
        vals.ysltht17 = round(vals.ysltht17,2)
        vals.ysltht18 = round(vals.ysltht18,2)
        vals.ysltht19 = round(vals.ysltht19,2)
        vals.ysltht20 = round(vals.ysltht20,2)
        vals.ysltht21 = round(vals.ysltht21,2)
        vals.ysltht22 = round(vals.ysltht22,2)
        vals.ysltht23 = round(vals.ysltht23,2)
        vals.ysltht24 = round(vals.ysltht24,2)

        vals.cmaht15 = round(vals.cmaht15,2)
        vals.cmaht16 = round(vals.cmaht16,2)
        vals.cmaht17 = round(vals.cmaht17,2)
        vals.cmaht18 = round(vals.cmaht18,2)
        vals.cmaht19 = round(vals.cmaht19,2)
        vals.cmaht20 = round(vals.cmaht20,2)
        vals.cmaht21 = round(vals.cmaht21,2)
        vals.cmaht22 = round(vals.cmaht22,2)
        vals.cmaht23 = round(vals.cmaht23,2)
        vals.cmaht24 = round(vals.cmaht24,2)

        vals.cmalt15 = round(vals.cmalt15,2)
        vals.cmalt16 = round(vals.cmalt16,2)
        vals.cmalt17 = round(vals.cmalt17,2)
        vals.cmalt18 = round(vals.cmalt18,2)
        vals.cmalt19 = round(vals.cmalt19,2)
        vals.cmalt20 = round(vals.cmalt20,2)
        vals.cmalt21 = round(vals.cmalt21,2)
        vals.cmalt22 = round(vals.cmalt22,2)
        vals.cmalt23 = round(vals.cmalt23,2)
        vals.cmalt24 = round(vals.cmalt24,2)

        vals.cmltht1_15 = round(vals.cmltht1_15,2)
        vals.cmltht1_16 = round(vals.cmltht1_16,2)
        vals.cmltht1_17 = round(vals.cmltht1_17,2)
        vals.cmltht1_18 = round(vals.cmltht1_18,2)
        vals.cmltht1_19 = round(vals.cmltht1_19,2)
        vals.cmltht1_20 = round(vals.cmltht1_20,2)
        vals.cmltht1_21 = round(vals.cmltht1_21,2)
        vals.cmltht1_22 = round(vals.cmltht1_22,2)
        vals.cmltht1_23 = round(vals.cmltht1_23,2)
        vals.cmltht1_24 = round(vals.cmltht1_24,2)

        vals.cmltht2_15 = round(vals.cmltht2_15,2)
        vals.cmltht2_16 = round(vals.cmltht2_16,2)
        vals.cmltht2_17 = round(vals.cmltht2_17,2)
        vals.cmltht2_18 = round(vals.cmltht2_18,2)
        vals.cmltht2_19 = round(vals.cmltht2_19,2)
        vals.cmltht2_20 = round(vals.cmltht2_20,2)
        vals.cmltht2_21 = round(vals.cmltht2_21,2)
        vals.cmltht2_22 = round(vals.cmltht2_22,2)
        vals.cmltht2_23 = round(vals.cmltht2_23,2)
        vals.cmltht2_24 = round(vals.cmltht2_24,2)

        vals.cmltht3_15 = round(vals.cmltht3_15,2)
        vals.cmltht3_16 = round(vals.cmltht3_16,2)
        vals.cmltht3_17 = round(vals.cmltht3_17,2)
        vals.cmltht3_18 = round(vals.cmltht3_18,2)
        vals.cmltht3_19 = round(vals.cmltht3_19,2)
        vals.cmltht3_20 = round(vals.cmltht3_20,2)
        vals.cmltht3_21 = round(vals.cmltht3_21,2)
        vals.cmltht3_22 = round(vals.cmltht3_22,2)
        vals.cmltht3_23 = round(vals.cmltht3_23,2)
        vals.cmltht3_24 = round(vals.cmltht3_24,2)

        vals.cmltlt15 = round(vals.cmltlt15,2)
        vals.cmltlt16 = round(vals.cmltlt16,2)
        vals.cmltlt17 = round(vals.cmltlt17,2)
        vals.cmltlt18 = round(vals.cmltlt18,2)
        vals.cmltlt19 = round(vals.cmltlt19,2)
        vals.cmltlt20 = round(vals.cmltlt20,2)
        vals.cmltlt21 = round(vals.cmltlt21,2)
        vals.cmltlt22 = round(vals.cmltlt22,2)
        vals.cmltlt23 = round(vals.cmltlt23,2)
        vals.cmltlt24 = round(vals.cmltlt24,2)

        vals.smaht15 = round(vals.smaht15,2)
        vals.smaht16 = round(vals.smaht16,2)
        vals.smaht17 = round(vals.smaht17,2)
        vals.smaht18 = round(vals.smaht18,2)
        vals.smaht19 = round(vals.smaht19,2)
        vals.smaht20 = round(vals.smaht20,2)
        vals.smaht21 = round(vals.smaht21,2)
        vals.smaht22 = round(vals.smaht22,2)
        vals.smaht23 = round(vals.smaht23,2)
        vals.smaht24 = round(vals.smaht24,2)

        vals.smltht1_15 = round(vals.smltht1_15,2)
        vals.smltht1_16 = round(vals.smltht1_16,2)
        vals.smltht1_17 = round(vals.smltht1_17,2)
        vals.smltht1_18 = round(vals.smltht1_18,2)
        vals.smltht1_19 = round(vals.smltht1_19,2)
        vals.smltht1_20 = round(vals.smltht1_20,2)
        vals.smltht1_21 = round(vals.smltht1_21,2)
        vals.smltht1_22 = round(vals.smltht1_22,2)
        vals.smltht1_23 = round(vals.smltht1_23,2)
        vals.smltht1_24 = round(vals.smltht1_24,2)

        vals.smltht2_15 = round(vals.smltht2_15,2)
        vals.smltht2_16 = round(vals.smltht2_16,2)
        vals.smltht2_17 = round(vals.smltht2_17,2)
        vals.smltht2_18 = round(vals.smltht2_18,2)
        vals.smltht2_19 = round(vals.smltht2_19,2)
        vals.smltht2_20 = round(vals.smltht2_20,2)
        vals.smltht2_21 = round(vals.smltht2_21,2)
        vals.smltht2_22 = round(vals.smltht2_22,2)
        vals.smltht2_23 = round(vals.smltht2_23,2)
        vals.smltht2_24 = round(vals.smltht2_24,2)

        vals.totalsc15 = round(vals.totalsc15,2)
        vals.totalsc16 = round(vals.totalsc16,2)
        vals.totalsc17 = round(vals.totalsc17,2)
        vals.totalsc18 = round(vals.totalsc18,2)
        vals.totalsc19 = round(vals.totalsc19,2)
        vals.totalsc20 = round(vals.totalsc20,2)
        vals.totalsc21 = round(vals.totalsc21,2)
        vals.totalsc22 = round(vals.totalsc22,2)
        vals.totalsc23 = round(vals.totalsc23,2)
        vals.totalsc24 = round(vals.totalsc24,2)

        vals.tcwsalt15 = round(vals.tcwsalt15,2)
        vals.tcwsalt16 = round(vals.tcwsalt16,2)
        vals.tcwsalt17 = round(vals.tcwsalt17,2)        
        vals.tcwsalt18 = round(vals.tcwsalt18,2)
        vals.tcwsalt19 = round(vals.tcwsalt19,2)        
        vals.tcwsalt20 = round(vals.tcwsalt20,2)
        vals.tcwsalt21 = round(vals.tcwsalt21,2)
        vals.tcwsalt22 = round(vals.tcwsalt22,2)
        vals.tcwsalt23 = round(vals.tcwsalt23,2)
        vals.tcwsalt24 = round(vals.tcwsalt24,2)

        vals.tcwsltlt15 = round(vals.tcwsltlt15,2)
        vals.tcwsltlt16 = round(vals.tcwsltlt16,2)
        vals.tcwsltlt17 = round(vals.tcwsltlt17,2)        
        vals.tcwsltlt18 = round(vals.tcwsltlt18,2)
        vals.tcwsltlt19 = round(vals.tcwsltlt19,2)        
        vals.tcwsltlt20 = round(vals.tcwsltlt20,2)
        vals.tcwsltlt21 = round(vals.tcwsltlt21,2)
        vals.tcwsltlt22 = round(vals.tcwsltlt22,2)
        vals.tcwsltlt23 = round(vals.tcwsltlt23,2)
        vals.tcwsltlt24 = round(vals.tcwsltlt24,2)

        vals.tcwsalt15 = round(vals.tcwsalt15,2)
        vals.tcwsalt16 = round(vals.tcwsalt16,2)
        vals.tcwsalt17 = round(vals.tcwsalt17,2)        
        vals.tcwsalt18 = round(vals.tcwsalt18,2)
        vals.tcwsalt19 = round(vals.tcwsalt19,2)        
        vals.tcwsalt20 = round(vals.tcwsalt20,2)
        vals.tcwsalt21 = round(vals.tcwsalt21,2)
        vals.tcwsalt22 = round(vals.tcwsalt22,2)
        vals.tcwsalt23 = round(vals.tcwsalt23,2)
        vals.tcwsalt24 = round(vals.tcwsalt24,2)

        vals.tcysltlt15 = round(vals.tcysltlt15,2)
        vals.tcysltlt16 = round(vals.tcysltlt16,2)
        vals.tcysltlt17 = round(vals.tcysltlt17,2)        
        vals.tcysltlt18 = round(vals.tcysltlt18,2)
        vals.tcysltlt19 = round(vals.tcysltlt19,2)        
        vals.tcysltlt20 = round(vals.tcysltlt20,2)
        vals.tcysltlt21 = round(vals.tcysltlt21,2)
        vals.tcysltlt22 = round(vals.tcysltlt22,2)
        vals.tcysltlt23 = round(vals.tcysltlt23,2)
        vals.tcysltlt24 = round(vals.tcysltlt24,2)

        vals.scwsalt15 = round(vals.scwsalt15,2)
        vals.scwsalt16 = round(vals.scwsalt16,2)
        vals.scwsalt17 = round(vals.scwsalt17,2)        
        vals.scwsalt18 = round(vals.scwsalt18,2)
        vals.scwsalt19 = round(vals.scwsalt19,2)        
        vals.scwsalt20 = round(vals.scwsalt20,2)
        vals.scwsalt21 = round(vals.scwsalt21,2)
        vals.scwsalt22 = round(vals.scwsalt22,2)
        vals.scwsalt23 = round(vals.scwsalt23,2)
        vals.scwsalt24 = round(vals.scwsalt24,2)

        vals.scwsltlt15 = round(vals.scwsltlt15,2)
        vals.scwsltlt16 = round(vals.scwsltlt16,2)
        vals.scwsltlt17 = round(vals.scwsltlt17,2)        
        vals.scwsltlt18 = round(vals.scwsltlt18,2)
        vals.scwsltlt19 = round(vals.scwsltlt19,2)        
        vals.scwsltlt20 = round(vals.scwsltlt20,2)
        vals.scwsltlt21 = round(vals.scwsltlt21,2)
        vals.scwsltlt22 = round(vals.scwsltlt22,2)
        vals.scwsltlt23 = round(vals.scwsltlt23,2)
        vals.scwsltlt24 = round(vals.scwsltlt24,2)

        vals.scwsalt15 = round(vals.scwsalt15,2)
        vals.scwsalt16 = round(vals.scwsalt16,2)
        vals.scwsalt17 = round(vals.scwsalt17,2)        
        vals.scwsalt18 = round(vals.scwsalt18,2)
        vals.scwsalt19 = round(vals.scwsalt19,2)        
        vals.scwsalt20 = round(vals.scwsalt20,2)
        vals.scwsalt21 = round(vals.scwsalt21,2)
        vals.scwsalt22 = round(vals.scwsalt22,2)
        vals.scwsalt23 = round(vals.scwsalt23,2)
        vals.scwsalt24 = round(vals.scwsalt24,2)

        vals.scysltlt15 = round(vals.scysltlt15,2)
        vals.scysltlt16 = round(vals.scysltlt16,2)
        vals.scysltlt17 = round(vals.scysltlt17,2)        
        vals.scysltlt18 = round(vals.scysltlt18,2)
        vals.scysltlt19 = round(vals.scysltlt19,2)        
        vals.scysltlt20 = round(vals.scysltlt20,2)
        vals.scysltlt21 = round(vals.scysltlt21,2)
        vals.scysltlt22 = round(vals.scysltlt22,2)
        vals.scysltlt23 = round(vals.scysltlt23,2)
        vals.scysltlt24 = round(vals.scysltlt24,2)

        vals.tccmalt15 = round(vals.tccmalt15,2)
        vals.tccmalt16 = round(vals.tccmalt16,2)
        vals.tccmalt17 = round(vals.tccmalt17,2)
        vals.tccmalt18 = round(vals.tccmalt18,2)
        vals.tccmalt19 = round(vals.tccmalt19,2)
        vals.tccmalt20 = round(vals.tccmalt20,2)
        vals.tccmalt21 = round(vals.tccmalt21,2)
        vals.tccmalt22 = round(vals.tccmalt22,2)
        vals.tccmalt23 = round(vals.tccmalt23,2)
        vals.tccmalt24 = round(vals.tccmalt24,2)

        vals.tccmltlt1_15 = round(vals.tccmltlt1_15,2)        
        vals.tccmltlt1_16 = round(vals.tccmltlt1_16,2)
        vals.tccmltlt1_17 = round(vals.tccmltlt1_17,2)
        vals.tccmltlt1_18 = round(vals.tccmltlt1_18,2)
        vals.tccmltlt1_19 = round(vals.tccmltlt1_19,2)
        vals.tccmltlt1_20 = round(vals.tccmltlt1_20,2)
        vals.tccmltlt1_21 = round(vals.tccmltlt1_21,2)
        vals.tccmltlt1_22 = round(vals.tccmltlt1_22,2)
        vals.tccmltlt1_23 = round(vals.tccmltlt1_23,2)
        vals.tccmltlt1_24 = round(vals.tccmltlt1_24,2)

        vals.tccmltlt2_15 = round(vals.tccmltlt2_15,2)        
        vals.tccmltlt2_16 = round(vals.tccmltlt2_16,2)
        vals.tccmltlt2_17 = round(vals.tccmltlt2_17,2)
        vals.tccmltlt2_18 = round(vals.tccmltlt2_18,2)
        vals.tccmltlt2_19 = round(vals.tccmltlt2_19,2)
        vals.tccmltlt2_20 = round(vals.tccmltlt2_20,2)
        vals.tccmltlt2_21 = round(vals.tccmltlt2_21,2)
        vals.tccmltlt2_22 = round(vals.tccmltlt2_22,2)
        vals.tccmltlt2_23 = round(vals.tccmltlt2_23,2)
        vals.tccmltlt2_24 = round(vals.tccmltlt2_24,2)

        vals.tccmltlt3_15 = round(vals.tccmltlt3_15,2)        
        vals.tccmltlt3_16 = round(vals.tccmltlt3_16,2)
        vals.tccmltlt3_17 = round(vals.tccmltlt3_17,2)
        vals.tccmltlt3_18 = round(vals.tccmltlt3_18,2)
        vals.tccmltlt3_19 = round(vals.tccmltlt3_19,2)
        vals.tccmltlt3_20 = round(vals.tccmltlt3_20,2)
        vals.tccmltlt3_21 = round(vals.tccmltlt3_21,2)
        vals.tccmltlt3_22 = round(vals.tccmltlt3_22,2)
        vals.tccmltlt3_23 = round(vals.tccmltlt3_23,2)
        vals.tccmltlt3_24 = round(vals.tccmltlt3_24,2)

        vals.sccmalt15 = round(vals.sccmalt15,2)
        vals.sccmalt16 = round(vals.sccmalt16,2)
        vals.sccmalt17 = round(vals.sccmalt17,2)
        vals.sccmalt18 = round(vals.sccmalt18,2)
        vals.sccmalt19 = round(vals.sccmalt19,2)
        vals.sccmalt20 = round(vals.sccmalt20,2)
        vals.sccmalt21 = round(vals.sccmalt21,2)
        vals.sccmalt22 = round(vals.sccmalt22,2)
        vals.sccmalt23 = round(vals.sccmalt23,2)
        vals.sccmalt24 = round(vals.sccmalt24,2)

        vals.sccmltlt1_15 = round(vals.sccmltlt1_15,2)        
        vals.sccmltlt1_16 = round(vals.sccmltlt1_16,2)
        vals.sccmltlt1_17 = round(vals.sccmltlt1_17,2)
        vals.sccmltlt1_18 = round(vals.sccmltlt1_18,2)
        vals.sccmltlt1_19 = round(vals.sccmltlt1_19,2)
        vals.sccmltlt1_20 = round(vals.sccmltlt1_20,2)
        vals.sccmltlt1_21 = round(vals.sccmltlt1_21,2)
        vals.sccmltlt1_22 = round(vals.sccmltlt1_22,2)
        vals.sccmltlt1_23 = round(vals.sccmltlt1_23,2)
        vals.sccmltlt1_24 = round(vals.sccmltlt1_24,2)

        vals.sccmltlt2_15 = round(vals.sccmltlt2_15,2)        
        vals.sccmltlt2_16 = round(vals.sccmltlt2_16,2)
        vals.sccmltlt2_17 = round(vals.sccmltlt2_17,2)
        vals.sccmltlt2_18 = round(vals.sccmltlt2_18,2)
        vals.sccmltlt2_19 = round(vals.sccmltlt2_19,2)
        vals.sccmltlt2_20 = round(vals.sccmltlt2_20,2)
        vals.sccmltlt2_21 = round(vals.sccmltlt2_21,2)
        vals.sccmltlt2_22 = round(vals.sccmltlt2_22,2)
        vals.sccmltlt2_23 = round(vals.sccmltlt2_23,2)
        vals.sccmltlt2_24 = round(vals.sccmltlt2_24,2)

        vals.sccmltlt3_15 = round(vals.sccmltlt3_15,2)        
        vals.sccmltlt3_16 = round(vals.sccmltlt3_16,2)
        vals.sccmltlt3_17 = round(vals.sccmltlt3_17,2)
        vals.sccmltlt3_18 = round(vals.sccmltlt3_18,2)
        vals.sccmltlt3_19 = round(vals.sccmltlt3_19,2)
        vals.sccmltlt3_20 = round(vals.sccmltlt3_20,2)
        vals.sccmltlt3_21 = round(vals.sccmltlt3_21,2)
        vals.sccmltlt3_22 = round(vals.sccmltlt3_22,2)
        vals.sccmltlt3_23 = round(vals.sccmltlt3_23,2)
        vals.sccmltlt3_24 = round(vals.sccmltlt3_24,2)

        vals.tcsmltlt1_15 = round(vals.tcsmltlt1_15,2)
        vals.tcsmltlt1_16 = round(vals.tcsmltlt1_16,2)
        vals.tcsmltlt1_17 = round(vals.tcsmltlt1_17,2)
        vals.tcsmltlt1_18 = round(vals.tcsmltlt1_18,2)
        vals.tcsmltlt1_19 = round(vals.tcsmltlt1_19,2)
        vals.tcsmltlt1_20 = round(vals.tcsmltlt1_20,2)
        vals.tcsmltlt1_21 = round(vals.tcsmltlt1_21,2)
        vals.tcsmltlt1_22 = round(vals.tcsmltlt1_22,2)
        vals.tcsmltlt1_23 = round(vals.tcsmltlt1_23,2)
        vals.tcsmltlt1_24 = round(vals.tcsmltlt1_24,2)

        vals.tcsmltlt2_15 = round(vals.tcsmltlt2_15,2)
        vals.tcsmltlt2_16 = round(vals.tcsmltlt2_16,2)
        vals.tcsmltlt2_17 = round(vals.tcsmltlt2_17,2)
        vals.tcsmltlt2_18 = round(vals.tcsmltlt2_18,2)
        vals.tcsmltlt2_19 = round(vals.tcsmltlt2_19,2)
        vals.tcsmltlt2_20 = round(vals.tcsmltlt2_20,2)
        vals.tcsmltlt2_21 = round(vals.tcsmltlt2_21,2)
        vals.tcsmltlt2_22 = round(vals.tcsmltlt2_22,2)
        vals.tcsmltlt2_23 = round(vals.tcsmltlt2_23,2)
        vals.tcsmltlt2_24 = round(vals.tcsmltlt2_24,2)

        vals.tcsmalt15 = round(vals.tcsmalt15,2)
        vals.tcsmalt16 = round(vals.tcsmalt16,2)
        vals.tcsmalt17 = round(vals.tcsmalt17,2)
        vals.tcsmalt18 = round(vals.tcsmalt18,2)
        vals.tcsmalt19 = round(vals.tcsmalt19,2)
        vals.tcsmalt20 = round(vals.tcsmalt20,2)
        vals.tcsmalt21 = round(vals.tcsmalt21,2)
        vals.tcsmalt22 = round(vals.tcsmalt22,2)
        vals.tcsmalt23 = round(vals.tcsmalt23,2)
        vals.tcsmalt24 = round(vals.tcsmalt24,2)

        vals.scsmltlt1_15 = round(vals.scsmltlt1_15,2)
        vals.scsmltlt1_16 = round(vals.scsmltlt1_16,2)
        vals.scsmltlt1_17 = round(vals.scsmltlt1_17,2)
        vals.scsmltlt1_18 = round(vals.scsmltlt1_18,2)
        vals.scsmltlt1_19 = round(vals.scsmltlt1_19,2)
        vals.scsmltlt1_20 = round(vals.scsmltlt1_20,2)
        vals.scsmltlt1_21 = round(vals.scsmltlt1_21,2)
        vals.scsmltlt1_22 = round(vals.scsmltlt1_22,2)
        vals.scsmltlt1_23 = round(vals.scsmltlt1_23,2)
        vals.scsmltlt1_24 = round(vals.scsmltlt1_24,2)

        vals.scsmltlt2_15 = round(vals.scsmltlt2_15,2)
        vals.scsmltlt2_16 = round(vals.scsmltlt2_16,2)
        vals.scsmltlt2_17 = round(vals.scsmltlt2_17,2)
        vals.scsmltlt2_18 = round(vals.scsmltlt2_18,2)
        vals.scsmltlt2_19 = round(vals.scsmltlt2_19,2)
        vals.scsmltlt2_20 = round(vals.scsmltlt2_20,2)
        vals.scsmltlt2_21 = round(vals.scsmltlt2_21,2)
        vals.scsmltlt2_22 = round(vals.scsmltlt2_22,2)
        vals.scsmltlt2_23 = round(vals.scsmltlt2_23,2)
        vals.scsmltlt2_24 = round(vals.scsmltlt2_24,2)

        vals.scsmalt15 = round(vals.scsmalt15,2)
        vals.scsmalt16 = round(vals.scsmalt16,2)
        vals.scsmalt17 = round(vals.scsmalt17,2)
        vals.scsmalt18 = round(vals.scsmalt18,2)
        vals.scsmalt19 = round(vals.scsmalt19,2)
        vals.scsmalt20 = round(vals.scsmalt20,2)
        vals.scsmalt21 = round(vals.scsmalt21,2)
        vals.scsmalt22 = round(vals.scsmalt22,2)
        vals.scsmalt23 = round(vals.scsmalt23,2)
        vals.scsmalt24 = round(vals.scsmalt24,2)

        vals.ietotal15 = round(vals.ietotal15,2)        
        vals.ietotal16 = round(vals.ietotal16,2)
        vals.ietotal17 = round(vals.ietotal17,2)
        vals.ietotal18 = round(vals.ietotal18,2)
        vals.ietotal19 = round(vals.ietotal19,2)
        vals.ietotal20 = round(vals.ietotal20,2)
        vals.ietotal21 = round(vals.ietotal21,2)
        vals.ietotal22 = round(vals.ietotal22,2)
        vals.ietotal23 = round(vals.ietotal23,2)
        vals.ietotal24 = round(vals.ietotal24,2)

        vals.niecmaht15 = round(vals.niecmaht15,2)        
        vals.niecmaht16 = round(vals.niecmaht16,2)
        vals.niecmaht17 = round(vals.niecmaht17,2)
        vals.niecmaht18 = round(vals.niecmaht18,2)
        vals.niecmaht19 = round(vals.niecmaht19,2)
        vals.niecmaht20 = round(vals.niecmaht20,2)
        vals.niecmaht21 = round(vals.niecmaht21,2)
        vals.niecmaht22 = round(vals.niecmaht22,2)
        vals.niecmaht23 = round(vals.niecmaht23,2)
        vals.niecmaht24 = round(vals.niecmaht24,2)

        vals.niecmalt15 = round(vals.niecmaht15,2)
        vals.niecmalt16 = round(vals.niecmaht16,2)
        vals.niecmalt17 = round(vals.niecmaht17,2)
        vals.niecmalt18 = round(vals.niecmaht18,2)
        vals.niecmalt19 = round(vals.niecmaht19,2)
        vals.niecmalt20 = round(vals.niecmaht20,2)
        vals.niecmalt21 = round(vals.niecmaht21,2)
        vals.niecmalt22 = round(vals.niecmaht22,2)
        vals.niecmalt23 = round(vals.niecmaht23,2)
        vals.niecmalt24 = round(vals.niecmaht24,2)

        vals.niecmltht1_15 = round(vals.niecmltht1_15,2)
        vals.niecmltht1_16 = round(vals.niecmltht1_16,2)
        vals.niecmltht1_17 = round(vals.niecmltht1_17,2)
        vals.niecmltht1_18 = round(vals.niecmltht1_18,2)
        vals.niecmltht1_19 = round(vals.niecmltht1_19,2)
        vals.niecmltht1_20 = round(vals.niecmltht1_20,2)
        vals.niecmltht1_21 = round(vals.niecmltht1_21,2)
        vals.niecmltht1_22 = round(vals.niecmltht1_22,2)
        vals.niecmltht1_23 = round(vals.niecmltht1_23,2)
        vals.niecmltht1_24 = round(vals.niecmltht1_24,2)

        vals.niecmltht2_15 = round(vals.niecmltht2_15,2)
        vals.niecmltht2_16 = round(vals.niecmltht2_16,2)
        vals.niecmltht2_17 = round(vals.niecmltht2_17,2)
        vals.niecmltht2_18 = round(vals.niecmltht2_18,2)
        vals.niecmltht2_19 = round(vals.niecmltht2_19,2)
        vals.niecmltht2_20 = round(vals.niecmltht2_20,2)
        vals.niecmltht2_21 = round(vals.niecmltht2_21,2)
        vals.niecmltht2_22 = round(vals.niecmltht2_22,2)
        vals.niecmltht2_23 = round(vals.niecmltht2_23,2)
        vals.niecmltht2_24 = round(vals.niecmltht2_24,2)

        vals.niecmltht3_15 = round(vals.niecmltht3_15,2)
        vals.niecmltht3_16 = round(vals.niecmltht3_16,2)
        vals.niecmltht3_17 = round(vals.niecmltht3_17,2)
        vals.niecmltht3_18 = round(vals.niecmltht3_18,2)
        vals.niecmltht3_19 = round(vals.niecmltht3_19,2)
        vals.niecmltht3_20 = round(vals.niecmltht3_20,2)
        vals.niecmltht3_21 = round(vals.niecmltht3_21,2)
        vals.niecmltht3_22 = round(vals.niecmltht3_22,2)
        vals.niecmltht3_23 = round(vals.niecmltht3_23,2)
        vals.niecmltht3_24 = round(vals.niecmltht3_24,2)

        vals.niecmltlt15 = round(vals.niecmltlt15,2)
        vals.niecmltlt16 = round(vals.niecmltlt16,2)
        vals.niecmltlt17 = round(vals.niecmltlt17,2)
        vals.niecmltlt18 = round(vals.niecmltlt18,2)
        vals.niecmltlt19 = round(vals.niecmltlt19,2)
        vals.niecmltlt20 = round(vals.niecmltlt20,2)
        vals.niecmltlt21 = round(vals.niecmltlt21,2)
        vals.niecmltlt22 = round(vals.niecmltlt22,2)
        vals.niecmltlt23 = round(vals.niecmltlt23,2)
        vals.niecmltlt24 = round(vals.niecmltlt24,2)

        vals.niesmaht15 = round(vals.niesmaht15,2)        
        vals.niesmaht16 = round(vals.niesmaht16,2)
        vals.niesmaht17 = round(vals.niesmaht17,2)
        vals.niesmaht18 = round(vals.niesmaht18,2)
        vals.niesmaht19 = round(vals.niesmaht19,2)
        vals.niesmaht20 = round(vals.niesmaht20,2)
        vals.niesmaht21 = round(vals.niesmaht21,2)
        vals.niesmaht22 = round(vals.niesmaht22,2)
        vals.niesmaht23 = round(vals.niesmaht23,2)
        vals.niesmaht24 = round(vals.niesmaht24,2)

        vals.niesmltht1_15 = round(vals.niesmltht1_15,2)
        vals.niesmltht1_16 = round(vals.niesmltht1_16,2)
        vals.niesmltht1_17 = round(vals.niesmltht1_17,2)
        vals.niesmltht1_18 = round(vals.niesmltht1_18,2)
        vals.niesmltht1_19 = round(vals.niesmltht1_19,2)
        vals.niesmltht1_20 = round(vals.niesmltht1_20,2)
        vals.niesmltht1_21 = round(vals.niesmltht1_21,2)
        vals.niesmltht1_22 = round(vals.niesmltht1_22,2)
        vals.niesmltht1_23 = round(vals.niesmltht1_23,2)
        vals.niesmltht1_24 = round(vals.niesmltht1_24,2)

        vals.niesmltht2_15 = round(vals.niesmltht2_15,2)
        vals.niesmltht2_16 = round(vals.niesmltht2_16,2)
        vals.niesmltht2_17 = round(vals.niesmltht2_17,2)
        vals.niesmltht2_18 = round(vals.niesmltht2_18,2)
        vals.niesmltht2_19 = round(vals.niesmltht2_19,2)
        vals.niesmltht2_20 = round(vals.niesmltht2_20,2)
        vals.niesmltht2_21 = round(vals.niesmltht2_21,2)
        vals.niesmltht2_22 = round(vals.niesmltht2_22,2)
        vals.niesmltht2_23 = round(vals.niesmltht2_23,2)
        vals.niesmltht2_24 = round(vals.niesmltht2_24,2)

        vals.niemtotal15 = round(vals.niemtotal15,2)        
        vals.niemtotal16 = round(vals.niemtotal16,2)
        vals.niemtotal17 = round(vals.niemtotal17,2)
        vals.niemtotal18 = round(vals.niemtotal18,2)
        vals.niemtotal19 = round(vals.niemtotal19,2)
        vals.niemtotal20 = round(vals.niemtotal20,2)
        vals.niemtotal21 = round(vals.niemtotal21,2)
        vals.niemtotal22 = round(vals.niemtotal22,2)
        vals.niemtotal23 = round(vals.niemtotal23,2)
        vals.niemtotal24 = round(vals.niemtotal24,2)

        vals.niewsaht15 = round(vals.niewsaht15,2)
        vals.niewsaht16 = round(vals.niewsaht16,2)
        vals.niewsaht17 = round(vals.niewsaht17,2)
        vals.niewsaht18 = round(vals.niewsaht18,2)
        vals.niewsaht19 = round(vals.niewsaht19,2)
        vals.niewsaht20 = round(vals.niewsaht20,2)
        vals.niewsaht21 = round(vals.niewsaht21,2)
        vals.niewsaht22 = round(vals.niewsaht22,2)
        vals.niewsaht23 = round(vals.niewsaht23,2)
        vals.niewsaht24 = round(vals.niewsaht24,2)

        vals.niewsalt15 = round(vals.niewsalt15,2)
        vals.niewsalt16 = round(vals.niewsalt16,2)
        vals.niewsalt17 = round(vals.niewsalt17,2)
        vals.niewsalt18 = round(vals.niewsalt18,2)
        vals.niewsalt19 = round(vals.niewsalt19,2)
        vals.niewsalt20 = round(vals.niewsalt20,2)
        vals.niewsalt21 = round(vals.niewsalt21,2)
        vals.niewsalt22 = round(vals.niewsalt22,2)
        vals.niewsalt23 = round(vals.niewsalt23,2)
        vals.niewsalt24 = round(vals.niewsalt24,2)

        vals.niewsltlt15 = round(vals.niewsltlt15,2)
        vals.niewsltlt16 = round(vals.niewsltlt16,2)
        vals.niewsltlt17 = round(vals.niewsltlt17,2)
        vals.niewsltlt18 = round(vals.niewsltlt18,2)
        vals.niewsltlt19 = round(vals.niewsltlt19,2)
        vals.niewsltlt20 = round(vals.niewsltlt20,2)
        vals.niewsltlt21 = round(vals.niewsltlt21,2)
        vals.niewsltlt22 = round(vals.niewsltlt22,2)
        vals.niewsltlt23 = round(vals.niewsltlt23,2)
        vals.niewsltlt24 = round(vals.niewsltlt24,2)

        vals.niewsltht15 = round(vals.niewsltht15,2)
        vals.niewsltht16 = round(vals.niewsltht16,2)
        vals.niewsltht17 = round(vals.niewsltht17,2)
        vals.niewsltht18 = round(vals.niewsltht18,2)
        vals.niewsltht19 = round(vals.niewsltht19,2)
        vals.niewsltht20 = round(vals.niewsltht20,2)
        vals.niewsltht21 = round(vals.niewsltht21,2)
        vals.niewsltht22 = round(vals.niewsltht22,2)
        vals.niewsltht23 = round(vals.niewsltht23,2)
        vals.niewsltht24 = round(vals.niewsltht24,2)

        vals.nieysaht15 = round(vals.nieysaht15,2)
        vals.nieysaht16 = round(vals.nieysaht16,2)
        vals.nieysaht17 = round(vals.nieysaht17,2)
        vals.nieysaht18 = round(vals.nieysaht18,2)
        vals.nieysaht19 = round(vals.nieysaht19,2)
        vals.nieysaht20 = round(vals.nieysaht20,2)
        vals.nieysaht21 = round(vals.nieysaht21,2)
        vals.nieysaht22 = round(vals.nieysaht22,2)
        vals.nieysaht23 = round(vals.nieysaht23,2)
        vals.nieysaht24 = round(vals.nieysaht24,2)

        vals.nieysalt15 = round(vals.nieysalt15,2)
        vals.nieysalt16 = round(vals.nieysalt16,2)
        vals.nieysalt17 = round(vals.nieysalt17,2)
        vals.nieysalt18 = round(vals.nieysalt18,2)
        vals.nieysalt19 = round(vals.nieysalt19,2)
        vals.nieysalt20 = round(vals.nieysalt20,2)
        vals.nieysalt21 = round(vals.nieysalt21,2)
        vals.nieysalt22 = round(vals.nieysalt22,2)
        vals.nieysalt23 = round(vals.nieysalt23,2)
        vals.nieysalt24 = round(vals.nieysalt24,2)

        vals.nieysltlt15 = round(vals.nieysltlt15,2)
        vals.nieysltlt16 = round(vals.nieysltlt16,2)
        vals.nieysltlt17 = round(vals.nieysltlt17,2)
        vals.nieysltlt18 = round(vals.nieysltlt18,2)
        vals.nieysltlt19 = round(vals.nieysltlt19,2)
        vals.nieysltlt20 = round(vals.nieysltlt20,2)
        vals.nieysltlt21 = round(vals.nieysltlt21,2)
        vals.nieysltlt22 = round(vals.nieysltlt22,2)
        vals.nieysltlt23 = round(vals.nieysltlt23,2)
        vals.nieysltlt24 = round(vals.nieysltlt24,2)

        vals.nieysltht15 = round(vals.nieysltht15,2)
        vals.nieysltht16 = round(vals.nieysltht16,2)
        vals.nieysltht17 = round(vals.nieysltht17,2)
        vals.nieysltht18 = round(vals.nieysltht18,2)
        vals.nieysltht19 = round(vals.nieysltht19,2)
        vals.nieysltht20 = round(vals.nieysltht20,2)
        vals.nieysltht21 = round(vals.nieysltht21,2)
        vals.nieysltht22 = round(vals.nieysltht22,2)
        vals.nieysltht23 = round(vals.nieysltht23,2)
        vals.nieysltht24 = round(vals.nieysltht24,2)

        vals.niestotal15 = round(vals.niestotal15,2)        
        vals.niestotal16 = round(vals.niestotal16,2)
        vals.niestotal17 = round(vals.niestotal17,2)
        vals.niestotal18 = round(vals.niestotal18,2)
        vals.niestotal19 = round(vals.niestotal19,2)
        vals.niestotal20 = round(vals.niestotal20,2)
        vals.niestotal21 = round(vals.niestotal21,2)
        vals.niestotal22 = round(vals.niestotal22,2)
        vals.niestotal23 = round(vals.niestotal23,2)
        vals.niestotal24 = round(vals.niestotal24,2)

        vals.nietotal15 = round(vals.nietotal15,2)        
        vals.nietotal16 = round(vals.nietotal16,2)
        vals.nietotal17 = round(vals.nietotal17,2)
        vals.nietotal18 = round(vals.nietotal18,2)
        vals.nietotal19 = round(vals.nietotal19,2)
        vals.nietotal20 = round(vals.nietotal20,2)
        vals.nietotal21 = round(vals.nietotal21,2)
        vals.nietotal22 = round(vals.nietotal22,2)
        vals.nietotal23 = round(vals.nietotal23,2)
        vals.nietotal24 = round(vals.nietotal24,2)

        vals.total15 = round(vals.total15,2)        
        vals.total16 = round(vals.total16,2)
        vals.total17 = round(vals.total17,2)
        vals.total18 = round(vals.total18,2)
        vals.total19 = round(vals.total19,2)
        vals.total20 = round(vals.total20,2)
        vals.total21 = round(vals.total21,2)
        vals.total22 = round(vals.total22,2)
        vals.total23 = round(vals.total23,2)
        vals.total24 = round(vals.total24,2)

        vals.niws15 = round(vals.niws15,2)        
        vals.niws16 = round(vals.niws16,2)
        vals.niws17 = round(vals.niws17,2)
        vals.niws18 = round(vals.niws18,2)
        vals.niws19 = round(vals.niws19,2)
        vals.niws20 = round(vals.niws20,2)
        vals.niws21 = round(vals.niws21,2)
        vals.niws22 = round(vals.niws22,2)
        vals.niws23 = round(vals.niws23,2)
        vals.niws24 = round(vals.niws24,2)

        vals.niys15 = round(vals.niys15,2)        
        vals.niys16 = round(vals.niys16,2)
        vals.niys17 = round(vals.niys17,2)
        vals.niys18 = round(vals.niys18,2)
        vals.niys19 = round(vals.niys19,2)
        vals.niys20 = round(vals.niys20,2)
        vals.niys21 = round(vals.niys21,2)
        vals.niys22 = round(vals.niys22,2)
        vals.niys23 = round(vals.niys23,2)
        vals.niys24 = round(vals.niys24,2)

        vals.nicm15 = round(vals.nicm15,2)        
        vals.nicm16 = round(vals.nicm16,2)
        vals.nicm17 = round(vals.nicm17,2)
        vals.nicm18 = round(vals.nicm18,2)
        vals.nicm19 = round(vals.nicm19,2)
        vals.nicm20 = round(vals.nicm20,2)
        vals.nicm21 = round(vals.nicm21,2)
        vals.nicm22 = round(vals.nicm22,2)
        vals.nicm23 = round(vals.nicm23,2)
        vals.nicm24 = round(vals.nicm24,2)

        vals.nism15 = round(vals.nism15,2)        
        vals.nism16 = round(vals.nism16,2)
        vals.nism17 = round(vals.nism17,2)
        vals.nism18 = round(vals.nism18,2)
        vals.nism19 = round(vals.nism19,2)
        vals.nism20 = round(vals.nism20,2)
        vals.nism21 = round(vals.nism21,2)
        vals.nism22 = round(vals.nism22,2)
        vals.nism23 = round(vals.nism23,2)
        vals.nism24 = round(vals.nism24,2)

        vals.iws15 = round(vals.iws15,2)        
        vals.iws16 = round(vals.iws16,2)
        vals.iws17 = round(vals.iws17,2)
        vals.iws18 = round(vals.iws18,2)
        vals.iws19 = round(vals.iws19,2)
        vals.iws20 = round(vals.iws20,2)
        vals.iws21 = round(vals.iws21,2)
        vals.iws22 = round(vals.iws22,2)
        vals.iws23 = round(vals.iws23,2)
        vals.iws24 = round(vals.iws24,2)

        vals.iys15 = round(vals.iys15,2)        
        vals.iys16 = round(vals.iys16,2)
        vals.iys17 = round(vals.iys17,2)
        vals.iys18 = round(vals.iys18,2)
        vals.iys19 = round(vals.iys19,2)
        vals.iys20 = round(vals.iys20,2)
        vals.iys21 = round(vals.iys21,2)
        vals.iys22 = round(vals.iys22,2)
        vals.iys23 = round(vals.iys23,2)
        vals.iys24 = round(vals.iys24,2)

        vals.icm15 = round(vals.icm15,2)        
        vals.icm16 = round(vals.icm16,2)
        vals.icm17 = round(vals.icm17,2)
        vals.icm18 = round(vals.icm18,2)
        vals.icm19 = round(vals.icm19,2)
        vals.icm20 = round(vals.icm20,2)
        vals.icm21 = round(vals.icm21,2)
        vals.icm22 = round(vals.icm22,2)
        vals.icm23 = round(vals.icm23,2)
        vals.icm24 = round(vals.icm24,2)

        vals.ism15 = round(vals.ism15,2)        
        vals.ism16 = round(vals.ism16,2)
        vals.ism17 = round(vals.ism17,2)
        vals.ism18 = round(vals.ism18,2)
        vals.ism19 = round(vals.ism19,2)
        vals.ism20 = round(vals.ism20,2)
        vals.ism21 = round(vals.ism21,2)
        vals.ism22 = round(vals.ism22,2)
        vals.ism23 = round(vals.ism23,2)
        vals.ism24 = round(vals.ism24,2)

        vals2.nils15 = round(vals2.nils15,2)
        vals2.nils16 = round(vals2.nils16,2)
        vals2.nils17 = round(vals2.nils17,2)        
        vals2.nils18 = round(vals2.nils18,2)
        vals2.nils19 = round(vals2.nils19,2)
        vals2.nils20 = round(vals2.nils20,2)
        vals2.nils21 = round(vals2.nils21,2)
        vals2.nils22 = round(vals2.nils22,2)
        vals2.nils23 = round(vals2.nils23,2)
        vals2.nils24 = round(vals2.nils24,2)

        vals2.niwsa15 = round(vals2.niwsa15,2)
        vals2.niwsa16 = round(vals2.niwsa16,2)
        vals2.niwsa17 = round(vals2.niwsa17,2)
        vals2.niwsa18 = round(vals2.niwsa18,2)
        vals2.niwsa19 = round(vals2.niwsa19,2)
        vals2.niwsa20 = round(vals2.niwsa20,2)
        vals2.niwsa21 = round(vals2.niwsa21,2)
        vals2.niwsa22 = round(vals2.niwsa22,2)
        vals2.niwsa23 = round(vals2.niwsa23,2)
        vals2.niwsa24 = round(vals2.niwsa24,2)

        vals2.niwslt15 = round(vals2.niwslt15,2)
        vals2.niwslt16 = round(vals2.niwslt16,2)
        vals2.niwslt17 = round(vals2.niwslt17,2)
        vals2.niwslt18 = round(vals2.niwslt18,2)
        vals2.niwslt19 = round(vals2.niwslt19,2)
        vals2.niwslt20 = round(vals2.niwslt20,2)
        vals2.niwslt21 = round(vals2.niwslt21,2)
        vals2.niwslt22 = round(vals2.niwslt22,2)
        vals2.niwslt23 = round(vals2.niwslt23,2)
        vals2.niwslt24 = round(vals2.niwslt24,2)

        vals2.niysa15 = round(vals2.niysa15,2)
        vals2.niysa16 = round(vals2.niysa16,2)
        vals2.niysa17 = round(vals2.niysa17,2)
        vals2.niysa18 = round(vals2.niysa18,2)
        vals2.niysa19 = round(vals2.niysa19,2)
        vals2.niysa20 = round(vals2.niysa20,2)
        vals2.niysa21 = round(vals2.niysa21,2)
        vals2.niysa22 = round(vals2.niysa22,2)
        vals2.niysa23 = round(vals2.niysa23,2)
        vals2.niysa24 = round(vals2.niysa24,2)

        vals2.niyslt15 = round(vals2.niyslt15,2)
        vals2.niyslt16 = round(vals2.niyslt16,2)
        vals2.niyslt17 = round(vals2.niyslt17,2)
        vals2.niyslt18 = round(vals2.niyslt18,2)
        vals2.niyslt19 = round(vals2.niyslt19,2)
        vals2.niyslt20 = round(vals2.niyslt20,2)
        vals2.niyslt21 = round(vals2.niyslt21,2)
        vals2.niyslt22 = round(vals2.niyslt22,2)
        vals2.niyslt23 = round(vals2.niyslt23,2)
        vals2.niyslt24 = round(vals2.niyslt24,2)

        vals2.nicma15 = round(vals2.nicma15,2)
        vals2.nicma16 = round(vals2.nicma16,2)
        vals2.nicma17 = round(vals2.nicma17,2)
        vals2.nicma18 = round(vals2.nicma18,2)
        vals2.nicma19 = round(vals2.nicma19,2)
        vals2.nicma20 = round(vals2.nicma20,2)
        vals2.nicma21 = round(vals2.nicma21,2)
        vals2.nicma22 = round(vals2.nicma22,2)
        vals2.nicma23 = round(vals2.nicma23,2)
        vals2.nicma24 = round(vals2.nicma24,2)

        vals2.nicmlt15 = round(vals2.nicmlt15,2)
        vals2.nicmlt16 = round(vals2.nicmlt16,2)
        vals2.nicmlt17 = round(vals2.nicmlt17,2)
        vals2.nicmlt18 = round(vals2.nicmlt18,2)
        vals2.nicmlt19 = round(vals2.nicmlt19,2)
        vals2.nicmlt20 = round(vals2.nicmlt20,2)
        vals2.nicmlt21 = round(vals2.nicmlt21,2)
        vals2.nicmlt22 = round(vals2.nicmlt22,2)
        vals2.nicmlt23 = round(vals2.nicmlt23,2)
        vals2.nicmlt24 = round(vals2.nicmlt24,2)

        vals2.nisma15 = round(vals2.nisma15,2)
        vals2.nisma16 = round(vals2.nisma16,2)
        vals2.nisma17 = round(vals2.nisma17,2)
        vals2.nisma18 = round(vals2.nisma18,2)
        vals2.nisma19 = round(vals2.nisma19,2)
        vals2.nisma20 = round(vals2.nisma20,2)
        vals2.nisma21 = round(vals2.nisma21,2)
        vals2.nisma22 = round(vals2.nisma22,2)
        vals2.nisma23 = round(vals2.nisma23,2)
        vals2.nisma24 = round(vals2.nisma24,2)

        vals2.nismlt15 = round(vals2.nismlt15,2)
        vals2.nismlt16 = round(vals2.nismlt16,2)
        vals2.nismlt17 = round(vals2.nismlt17,2)
        vals2.nismlt18 = round(vals2.nismlt18,2)
        vals2.nismlt19 = round(vals2.nismlt19,2)
        vals2.nismlt20 = round(vals2.nismlt20,2)
        vals2.nismlt21 = round(vals2.nismlt21,2)
        vals2.nismlt22 = round(vals2.nismlt22,2)
        vals2.nismlt23 = round(vals2.nismlt23,2)
        vals2.nismlt24 = round(vals2.nismlt24,2)

        vals2.ismlt15 = round(vals2.ismlt15,2)
        vals2.ismlt16 = round(vals2.ismlt16,2)
        vals2.ismlt17 = round(vals2.ismlt17,2)
        vals2.ismlt18 = round(vals2.ismlt18,2)
        vals2.ismlt19 = round(vals2.ismlt19,2)
        vals2.ismlt20 = round(vals2.ismlt20,2)
        vals2.ismlt21 = round(vals2.ismlt21,2)
        vals2.ismlt22 = round(vals2.ismlt22,2)
        vals2.ismlt23 = round(vals2.ismlt23,2)
        vals2.ismlt24 = round(vals2.ismlt24,2)

        vals2.icmlt15 = round(vals2.icmlt15,2)
        vals2.icmlt16 = round(vals2.icmlt16,2)
        vals2.icmlt17 = round(vals2.icmlt17,2)
        vals2.icmlt18 = round(vals2.icmlt18,2)
        vals2.icmlt19 = round(vals2.icmlt19,2)
        vals2.icmlt20 = round(vals2.icmlt20,2)
        vals2.icmlt21 = round(vals2.icmlt21,2)
        vals2.icmlt22 = round(vals2.icmlt22,2)
        vals2.icmlt23 = round(vals2.icmlt23,2)
        vals2.icmlt24 = round(vals2.icmlt24,2)

        vals2.vstotal1_15 = round(vals2.vstotal1_15,2)        
        vals2.vstotal1_16 = round(vals2.vstotal1_16,2)
        vals2.vstotal1_17 = round(vals2.vstotal1_17,2)
        vals2.vstotal1_18 = round(vals2.vstotal1_18,2)
        vals2.vstotal1_19 = round(vals2.vstotal1_19,2)
        vals2.vstotal1_20 = round(vals2.vstotal1_20,2)
        vals2.vstotal1_21 = round(vals2.vstotal1_21,2)
        vals2.vstotal1_22 = round(vals2.vstotal1_22,2)
        vals2.vstotal1_23 = round(vals2.vstotal1_23,2)
        vals2.vstotal1_24 = round(vals2.vstotal1_24,2)

        vals2.niws15 = round(vals2.niws15,2)
        vals2.niws16 = round(vals2.niws16,2)
        vals2.niws17 = round(vals2.niws17,2)
        vals2.niws18 = round(vals2.niws18,2)
        vals2.niws19 = round(vals2.niws19,2)
        vals2.niws20 = round(vals2.niws20,2)
        vals2.niws21 = round(vals2.niws21,2)
        vals2.niws22 = round(vals2.niws22,2)
        vals2.niws23 = round(vals2.niws23,2)
        vals2.niws24 = round(vals2.niws24,2)

        vals2.niys15 = round(vals2.niys15,2)
        vals2.niys16 = round(vals2.niys16,2)
        vals2.niys17 = round(vals2.niys17,2)
        vals2.niys18 = round(vals2.niys18,2)
        vals2.niys19 = round(vals2.niys19,2)
        vals2.niys20 = round(vals2.niys20,2)
        vals2.niys21 = round(vals2.niys21,2)
        vals2.niys22 = round(vals2.niys22,2)
        vals2.niys23 = round(vals2.niys23,2)
        vals2.niys24 = round(vals2.niys24,2)

        vals2.nism15 = round(vals2.nism15,2)
        vals2.nism16 = round(vals2.nism16,2)
        vals2.nism17 = round(vals2.nism17,2)
        vals2.nism18 = round(vals2.nism18,2)
        vals2.nism19 = round(vals2.nism19,2)
        vals2.nism20 = round(vals2.nism20,2)
        vals2.nism21 = round(vals2.nism21,2)
        vals2.nism22 = round(vals2.nism22,2)
        vals2.nism23 = round(vals2.nism23,2)
        vals2.nism24 = round(vals2.nism24,2)

        vals2.nicm15 = round(vals2.nicm15,2)
        vals2.nicm16 = round(vals2.nicm16,2)
        vals2.nicm17 = round(vals2.nicm17,2)
        vals2.nicm18 = round(vals2.nicm18,2)
        vals2.nicm19 = round(vals2.nicm19,2)
        vals2.nicm20 = round(vals2.nicm20,2)
        vals2.nicm21 = round(vals2.nicm21,2)
        vals2.nicm22 = round(vals2.nicm22,2)
        vals2.nicm23 = round(vals2.nicm23,2)
        vals2.nicm24 = round(vals2.nicm24,2)

        vals2.iws15 = round(vals2.iws15,2)
        vals2.iws16 = round(vals2.iws16,2)
        vals2.iws17 = round(vals2.iws17,2)
        vals2.iws18 = round(vals2.iws18,2)
        vals2.iws19 = round(vals2.iws19,2)
        vals2.iws20 = round(vals2.iws20,2)
        vals2.iws21 = round(vals2.iws21,2)
        vals2.iws22 = round(vals2.iws22,2)
        vals2.iws23 = round(vals2.iws23,2)
        vals2.iws24 = round(vals2.iws24,2)

        vals2.iys15 = round(vals2.iys15,2)
        vals2.iys16 = round(vals2.iys16,2)
        vals2.iys17 = round(vals2.iys17,2)
        vals2.iys18 = round(vals2.iys18,2)
        vals2.iys19 = round(vals2.iys19,2)
        vals2.iys20 = round(vals2.iys20,2)
        vals2.iys21 = round(vals2.iys21,2)
        vals2.iys22 = round(vals2.iys22,2)
        vals2.iys23 = round(vals2.iys23,2)
        vals2.iys24 = round(vals2.iys24,2)

        vals2.ism15 = round(vals2.ism15,2)
        vals2.ism16 = round(vals2.ism16,2)
        vals2.ism17 = round(vals2.ism17,2)
        vals2.ism18 = round(vals2.ism18,2)
        vals2.ism19 = round(vals2.ism19,2)
        vals2.ism20 = round(vals2.ism20,2)
        vals2.ism21 = round(vals2.ism21,2)
        vals2.ism22 = round(vals2.ism22,2)
        vals2.ism23 = round(vals2.ism23,2)
        vals2.ism24 = round(vals2.ism24,2)

        vals2.icm15 = round(vals2.icm15,2)
        vals2.icm16 = round(vals2.icm16,2)
        vals2.icm17 = round(vals2.icm17,2)
        vals2.icm18 = round(vals2.icm18,2)
        vals2.icm19 = round(vals2.icm19,2)
        vals2.icm20 = round(vals2.icm20,2)
        vals2.icm21 = round(vals2.icm21,2)
        vals2.icm22 = round(vals2.icm22,2)
        vals2.icm23 = round(vals2.icm23,2)
        vals2.icm24 = round(vals2.icm24,2)

        vals2.ltls15 = round(vals2.ltls15,2)        
        vals2.ltls16 = round(vals2.ltls16,2)
        vals2.ltls17 = round(vals2.ltls17,2)
        vals2.ltls18 = round(vals2.ltls18,2)
        vals2.ltls19 = round(vals2.ltls19,2)
        vals2.ltls20 = round(vals2.ltls20,2)
        vals2.ltls21 = round(vals2.ltls21,2)
        vals2.ltls22 = round(vals2.ltls22,2)
        vals2.ltls23 = round(vals2.ltls23,2)
        vals2.ltls24 = round(vals2.ltls24,2)

        vals2.ltwsa15 = round(vals2.ltwsa15,2)        
        vals2.ltwsa16 = round(vals2.ltwsa16,2)
        vals2.ltwsa17 = round(vals2.ltwsa17,2)
        vals2.ltwsa18 = round(vals2.ltwsa18,2)
        vals2.ltwsa19 = round(vals2.ltwsa19,2)
        vals2.ltwsa20 = round(vals2.ltwsa20,2)
        vals2.ltwsa21 = round(vals2.ltwsa21,2)
        vals2.ltwsa22 = round(vals2.ltwsa22,2)
        vals2.ltwsa23 = round(vals2.ltwsa23,2)
        vals2.ltwsa24 = round(vals2.ltwsa24,2)

        vals2.ltwslt15 = round(vals2.ltwslt15,2)        
        vals2.ltwslt16 = round(vals2.ltwslt16,2)
        vals2.ltwslt17 = round(vals2.ltwslt17,2)
        vals2.ltwslt18 = round(vals2.ltwslt18,2)
        vals2.ltwslt19 = round(vals2.ltwslt19,2)
        vals2.ltwslt20 = round(vals2.ltwslt20,2)
        vals2.ltwslt21 = round(vals2.ltwslt21,2)
        vals2.ltwslt22 = round(vals2.ltwslt22,2)
        vals2.ltwslt23 = round(vals2.ltwslt23,2)
        vals2.ltwslt24 = round(vals2.ltwslt24,2)

        vals2.ltysa15 = round(vals2.ltysa15,2)        
        vals2.ltysa16 = round(vals2.ltysa16,2)
        vals2.ltysa17 = round(vals2.ltysa17,2)
        vals2.ltysa18 = round(vals2.ltysa18,2)
        vals2.ltysa19 = round(vals2.ltysa19,2)
        vals2.ltysa20 = round(vals2.ltysa20,2)
        vals2.ltysa21 = round(vals2.ltysa21,2)
        vals2.ltysa22 = round(vals2.ltysa22,2)
        vals2.ltysa23 = round(vals2.ltysa23,2)
        vals2.ltysa24 = round(vals2.ltysa24,2)

        vals2.ltyslt15 = round(vals2.ltyslt15,2)        
        vals2.ltyslt16 = round(vals2.ltyslt16,2)
        vals2.ltyslt17 = round(vals2.ltyslt17,2)
        vals2.ltyslt18 = round(vals2.ltyslt18,2)
        vals2.ltyslt19 = round(vals2.ltyslt19,2)
        vals2.ltyslt20 = round(vals2.ltyslt20,2)
        vals2.ltyslt21 = round(vals2.ltyslt21,2)
        vals2.ltyslt22 = round(vals2.ltyslt22,2)
        vals2.ltyslt23 = round(vals2.ltyslt23,2)
        vals2.ltyslt24 = round(vals2.ltyslt24,2)

        vals2.htwsa15 = round(vals2.htwsa15,2)        
        vals2.htwsa16 = round(vals2.htwsa16,2)
        vals2.htwsa17 = round(vals2.htwsa17,2)
        vals2.htwsa18 = round(vals2.htwsa18,2)
        vals2.htwsa19 = round(vals2.htwsa19,2)
        vals2.htwsa20 = round(vals2.htwsa20,2)
        vals2.htwsa21 = round(vals2.htwsa21,2)
        vals2.htwsa22 = round(vals2.htwsa22,2)
        vals2.htwsa23 = round(vals2.htwsa23,2)
        vals2.htwsa24 = round(vals2.htwsa24,2)

        vals2.htwslt15 = round(vals2.htwslt15,2)        
        vals2.htwslt16 = round(vals2.htwslt16,2)
        vals2.htwslt17 = round(vals2.htwslt17,2)
        vals2.htwslt18 = round(vals2.htwslt18,2)
        vals2.htwslt19 = round(vals2.htwslt19,2)
        vals2.htwslt20 = round(vals2.htwslt20,2)
        vals2.htwslt21 = round(vals2.htwslt21,2)
        vals2.htwslt22 = round(vals2.htwslt22,2)
        vals2.htwslt23 = round(vals2.htwslt23,2)
        vals2.htwslt24 = round(vals2.htwslt24,2)

        vals2.htysa15 = round(vals2.htysa15,2)        
        vals2.htysa16 = round(vals2.htysa16,2)
        vals2.htysa17 = round(vals2.htysa17,2)
        vals2.htysa18 = round(vals2.htysa18,2)
        vals2.htysa19 = round(vals2.htysa19,2)
        vals2.htysa20 = round(vals2.htysa20,2)
        vals2.htysa21 = round(vals2.htysa21,2)
        vals2.htysa22 = round(vals2.htysa22,2)
        vals2.htysa23 = round(vals2.htysa23,2)
        vals2.htysa24 = round(vals2.htysa24,2)

        vals2.htyslt15 = round(vals2.htyslt15,2)        
        vals2.htyslt16 = round(vals2.htyslt16,2)
        vals2.htyslt17 = round(vals2.htyslt17,2)
        vals2.htyslt18 = round(vals2.htyslt18,2)
        vals2.htyslt19 = round(vals2.htyslt19,2)
        vals2.htyslt20 = round(vals2.htyslt20,2)
        vals2.htyslt21 = round(vals2.htyslt21,2)
        vals2.htyslt22 = round(vals2.htyslt22,2)
        vals2.htyslt23 = round(vals2.htyslt23,2)
        vals2.htyslt24 = round(vals2.htyslt24,2)

        vals2.ws15 = round(vals2.ws15,2)
        vals2.ws16 = round(vals2.ws16,2)
        vals2.ws17 = round(vals2.ws17,2)
        vals2.ws18 = round(vals2.ws18,2)
        vals2.ws19 = round(vals2.ws19,2)
        vals2.ws20 = round(vals2.ws20,2)
        vals2.ws21 = round(vals2.ws21,2)
        vals2.ws22 = round(vals2.ws22,2)
        vals2.ws23 = round(vals2.ws23,2)
        vals2.ws24 = round(vals2.ws24,2)

        vals2.ys15 = round(vals2.ys15,2)
        vals2.ys16 = round(vals2.ys16,2)
        vals2.ys17 = round(vals2.ys17,2)
        vals2.ys18 = round(vals2.ys18,2)
        vals2.ys19 = round(vals2.ys19,2)
        vals2.ys20 = round(vals2.ys20,2)
        vals2.ys21 = round(vals2.ys21,2)
        vals2.ys22 = round(vals2.ys22,2)
        vals2.ys23 = round(vals2.ys23,2)
        vals2.ys24 = round(vals2.ys24,2)

        vals2.vstotal2_15 = round(vals2.vstotal2_15,2)        
        vals2.vstotal2_16 = round(vals2.vstotal2_16,2)
        vals2.vstotal2_17 = round(vals2.vstotal2_17,2)
        vals2.vstotal2_18 = round(vals2.vstotal2_18,2)
        vals2.vstotal2_19 = round(vals2.vstotal2_19,2)
        vals2.vstotal2_20 = round(vals2.vstotal2_20,2)
        vals2.vstotal2_21 = round(vals2.vstotal2_21,2)
        vals2.vstotal2_22 = round(vals2.vstotal2_22,2)
        vals2.vstotal2_23 = round(vals2.vstotal2_23,2)
        vals2.vstotal2_24 = round(vals2.vstotal2_24,2)

        vals2.macdtc15 = round(vals2.macdtc15,2)
        vals2.macdtc16 = round(vals2.macdtc16,2)
        vals2.macdtc17 = round(vals2.macdtc17,2)
        vals2.macdtc18 = round(vals2.macdtc18,2)
        vals2.macdtc19 = round(vals2.macdtc19,2)
        vals2.macdtc20 = round(vals2.macdtc20,2)
        vals2.macdtc21 = round(vals2.macdtc21,2)
        vals2.macdtc22 = round(vals2.macdtc22,2)
        vals2.macdtc23 = round(vals2.macdtc23,2)
        vals2.macdtc24 = round(vals2.macdtc24,2)

        vals2.cts15 = round(vals2.cts15,2)
        vals2.cts16 = round(vals2.cts16,2)
        vals2.cts17 = round(vals2.cts17,2)
        vals2.cts18 = round(vals2.cts18,2)
        vals2.cts19 = round(vals2.cts19,2)
        vals2.cts20 = round(vals2.cts20,2)
        vals2.cts21 = round(vals2.cts21,2)
        vals2.cts22 = round(vals2.cts22,2)
        vals2.cts23 = round(vals2.cts23,2)
        vals2.cts24 = round(vals2.cts24,2)

        vals2.ctc15 = round(vals2.ctc15,2)
        vals2.ctc16 = round(vals2.ctc16,2)
        vals2.ctc17 = round(vals2.ctc17,2)
        vals2.ctc18 = round(vals2.ctc18,2)
        vals2.ctc19 = round(vals2.ctc19,2)
        vals2.ctc20 = round(vals2.ctc20,2)
        vals2.ctc21 = round(vals2.ctc21,2)
        vals2.ctc22 = round(vals2.ctc22,2)
        vals2.ctc23 = round(vals2.ctc23,2)
        vals2.ctc24 = round(vals2.ctc24,2)

        vals2.incprice1 = round(vals2.incprice1,2)        
        vals2.incprice2 = round(vals2.incprice2,2)
        vals2.incprice3 = round(vals2.incprice3,2)
        vals2.incprice4 = round(vals2.incprice4,2)
        vals2.incprice5 = round(vals2.incprice5,2)
        vals2.excprice1 = round(vals2.excprice1,2)
        vals2.excprice2 = round(vals2.excprice2,2)
        vals2.excprice3 = round(vals2.excprice3,2)
        vals2.excprice4 = round(vals2.excprice4,2)
        vals2.excprice5 = round(vals2.excprice5,2)

        vals2.tcsmltlt15 = round(vals2.tcsmltlt15,2)
        vals2.tcsmltlt16 = round(vals2.tcsmltlt16,2)
        vals2.tcsmltlt17 = round(vals2.tcsmltlt17,2)
        vals2.tcsmltlt18 = round(vals2.tcsmltlt18,2)
        vals2.tcsmltlt19 = round(vals2.tcsmltlt19,2)
        vals2.tcsmltlt20 = round(vals2.tcsmltlt20,2)
        vals2.tcsmltlt21 = round(vals2.tcsmltlt21,2)
        vals2.tcsmltlt22 = round(vals2.tcsmltlt22,2)
        vals2.tcsmltlt23 = round(vals2.tcsmltlt23,2)
        vals2.tcsmltlt24 = round(vals2.tcsmltlt24,2)

        vals2.tccmltlt15 = round(vals2.tccmltlt15,2)
        vals2.tccmltlt16 = round(vals2.tccmltlt16,2)
        vals2.tccmltlt17 = round(vals2.tccmltlt17,2)
        vals2.tccmltlt18 = round(vals2.tccmltlt18,2)
        vals2.tccmltlt19 = round(vals2.tccmltlt19,2)
        vals2.tccmltlt20 = round(vals2.tccmltlt20,2)
        vals2.tccmltlt21 = round(vals2.tccmltlt21,2)
        vals2.tccmltlt22 = round(vals2.tccmltlt22,2)
        vals2.tccmltlt23 = round(vals2.tccmltlt23,2)
        vals2.tccmltlt24 = round(vals2.tccmltlt24,2)

        vals2.wsahthoc15 = round(vals2.wsahthoc15,2)
        vals2.wsahthoc16 = round(vals2.wsahthoc16,2)
        vals2.wsahthoc17 = round(vals2.wsahthoc17,2)
        vals2.wsahthoc18 = round(vals2.wsahthoc18,2)
        vals2.wsahthoc19 = round(vals2.wsahthoc19,2)
        vals2.wsahthoc20 = round(vals2.wsahthoc20,2)
        vals2.wsahthoc21 = round(vals2.wsahthoc21,2)
        vals2.wsahthoc22 = round(vals2.wsahthoc22,2)
        vals2.wsahthoc23 = round(vals2.wsahthoc23,2)
        vals2.wsahthoc24 = round(vals2.wsahthoc24,2)

        vals2.wsalthoc15 = round(vals2.wsalthoc15,2)
        vals2.wsalthoc16 = round(vals2.wsalthoc16,2)
        vals2.wsalthoc17 = round(vals2.wsalthoc17,2)
        vals2.wsalthoc18 = round(vals2.wsalthoc18,2)
        vals2.wsalthoc19 = round(vals2.wsalthoc19,2)
        vals2.wsalthoc20 = round(vals2.wsalthoc20,2)
        vals2.wsalthoc21 = round(vals2.wsalthoc21,2)
        vals2.wsalthoc22 = round(vals2.wsalthoc22,2)
        vals2.wsalthoc23 = round(vals2.wsalthoc23,2)
        vals2.wsalthoc24 = round(vals2.wsalthoc24,2)

        vals2.wsahthoc15 = round(vals2.wsahthoc15,2)
        vals2.wsahthoc16 = round(vals2.wsahthoc16,2)
        vals2.wsahthoc17 = round(vals2.wsahthoc17,2)
        vals2.wsahthoc18 = round(vals2.wsahthoc18,2)
        vals2.wsahthoc19 = round(vals2.wsahthoc19,2)
        vals2.wsahthoc20 = round(vals2.wsahthoc20,2)
        vals2.wsahthoc21 = round(vals2.wsahthoc21,2)
        vals2.wsahthoc22 = round(vals2.wsahthoc22,2)
        vals2.wsahthoc23 = round(vals2.wsahthoc23,2)
        vals2.wsahthoc24 = round(vals2.wsahthoc24,2)

        vals2.wsltlthoc15 = round(vals2.wsltlthoc15,2)
        vals2.wsltlthoc16 = round(vals2.wsltlthoc16,2)
        vals2.wsltlthoc17 = round(vals2.wsltlthoc17,2)
        vals2.wsltlthoc18 = round(vals2.wsltlthoc18,2)
        vals2.wsltlthoc19 = round(vals2.wsltlthoc19,2)
        vals2.wsltlthoc20 = round(vals2.wsltlthoc20,2)
        vals2.wsltlthoc21 = round(vals2.wsltlthoc21,2)
        vals2.wsltlthoc22 = round(vals2.wsltlthoc22,2)
        vals2.wsltlthoc23 = round(vals2.wsltlthoc23,2)
        vals2.wsltlthoc24 = round(vals2.wsltlthoc24,2)

        vals2.ysahthoc15 = round(vals2.ysahthoc15,2)
        vals2.ysahthoc16 = round(vals2.ysahthoc16,2)
        vals2.ysahthoc17 = round(vals2.ysahthoc17,2)
        vals2.ysahthoc18 = round(vals2.ysahthoc18,2)
        vals2.ysahthoc19 = round(vals2.ysahthoc19,2)
        vals2.ysahthoc20 = round(vals2.ysahthoc20,2)
        vals2.ysahthoc21 = round(vals2.ysahthoc21,2)
        vals2.ysahthoc22 = round(vals2.ysahthoc22,2)
        vals2.ysahthoc23 = round(vals2.ysahthoc23,2)
        vals2.ysahthoc24 = round(vals2.ysahthoc24,2)

        vals2.ysalthoc15 = round(vals2.ysalthoc15,2)
        vals2.ysalthoc16 = round(vals2.ysalthoc16,2)
        vals2.ysalthoc17 = round(vals2.ysalthoc17,2)
        vals2.ysalthoc18 = round(vals2.ysalthoc18,2)
        vals2.ysalthoc19 = round(vals2.ysalthoc19,2)
        vals2.ysalthoc20 = round(vals2.ysalthoc20,2)
        vals2.ysalthoc21 = round(vals2.ysalthoc21,2)
        vals2.ysalthoc22 = round(vals2.ysalthoc22,2)
        vals2.ysalthoc23 = round(vals2.ysalthoc23,2)
        vals2.ysalthoc24 = round(vals2.ysalthoc24,2)

        vals2.ysahthoc15 = round(vals2.ysahthoc15,2)
        vals2.ysahthoc16 = round(vals2.ysahthoc16,2)
        vals2.ysahthoc17 = round(vals2.ysahthoc17,2)
        vals2.ysahthoc18 = round(vals2.ysahthoc18,2)
        vals2.ysahthoc19 = round(vals2.ysahthoc19,2)
        vals2.ysahthoc20 = round(vals2.ysahthoc20,2)
        vals2.ysahthoc21 = round(vals2.ysahthoc21,2)
        vals2.ysahthoc22 = round(vals2.ysahthoc22,2)
        vals2.ysahthoc23 = round(vals2.ysahthoc23,2)
        vals2.ysahthoc24 = round(vals2.ysahthoc24,2)

        vals2.ysltlthoc15 = round(vals2.ysltlthoc15,2)
        vals2.ysltlthoc16 = round(vals2.ysltlthoc16,2)
        vals2.ysltlthoc17 = round(vals2.ysltlthoc17,2)
        vals2.ysltlthoc18 = round(vals2.ysltlthoc18,2)
        vals2.ysltlthoc19 = round(vals2.ysltlthoc19,2)
        vals2.ysltlthoc20 = round(vals2.ysltlthoc20,2)
        vals2.ysltlthoc21 = round(vals2.ysltlthoc21,2)
        vals2.ysltlthoc22 = round(vals2.ysltlthoc22,2)
        vals2.ysltlthoc23 = round(vals2.ysltlthoc23,2)
        vals2.ysltlthoc24 = round(vals2.ysltlthoc24,2)

        vals2.cmahthoc15 = round(vals2.cmahthoc15,2)        
        vals2.cmahthoc16 = round(vals2.cmahthoc16,2)
        vals2.cmahthoc17 = round(vals2.cmahthoc17,2)
        vals2.cmahthoc18 = round(vals2.cmahthoc18,2)
        vals2.cmahthoc19 = round(vals2.cmahthoc19,2)
        vals2.cmahthoc20 = round(vals2.cmahthoc20,2)
        vals2.cmahthoc21 = round(vals2.cmahthoc21,2)
        vals2.cmahthoc22 = round(vals2.cmahthoc22,2)
        vals2.cmahthoc23 = round(vals2.cmahthoc23,2)
        vals2.cmahthoc24 = round(vals2.cmahthoc24,2)

        vals2.cmltht1_hoc15 = round(vals2.cmltht1_hoc15,2)
        vals2.cmltht1_hoc16 = round(vals2.cmltht1_hoc16,2)
        vals2.cmltht1_hoc17 = round(vals2.cmltht1_hoc17,2)
        vals2.cmltht1_hoc18 = round(vals2.cmltht1_hoc18,2)
        vals2.cmltht1_hoc19 = round(vals2.cmltht1_hoc19,2)
        vals2.cmltht1_hoc20 = round(vals2.cmltht1_hoc20,2)
        vals2.cmltht1_hoc21 = round(vals2.cmltht1_hoc21,2)
        vals2.cmltht1_hoc22 = round(vals2.cmltht1_hoc22,2)
        vals2.cmltht1_hoc23 = round(vals2.cmltht1_hoc23,2)
        vals2.cmltht1_hoc24 = round(vals2.cmltht1_hoc24,2)

        vals2.cmltht2_hoc15 = round(vals2.cmltht2_hoc15,2)
        vals2.cmltht2_hoc16 = round(vals2.cmltht2_hoc16,2)
        vals2.cmltht2_hoc17 = round(vals2.cmltht2_hoc17,2)
        vals2.cmltht2_hoc18 = round(vals2.cmltht2_hoc18,2)
        vals2.cmltht2_hoc19 = round(vals2.cmltht2_hoc19,2)
        vals2.cmltht2_hoc20 = round(vals2.cmltht2_hoc20,2)
        vals2.cmltht2_hoc21 = round(vals2.cmltht2_hoc21,2)
        vals2.cmltht2_hoc22 = round(vals2.cmltht2_hoc22,2)
        vals2.cmltht2_hoc23 = round(vals2.cmltht2_hoc23,2)
        vals2.cmltht2_hoc24 = round(vals2.cmltht2_hoc24,2)

        vals2.cmltht3_hoc15 = round(vals2.cmltht3_hoc15,2)
        vals2.cmltht3_hoc16 = round(vals2.cmltht3_hoc16,2)
        vals2.cmltht3_hoc17 = round(vals2.cmltht3_hoc17,2)
        vals2.cmltht3_hoc18 = round(vals2.cmltht3_hoc18,2)
        vals2.cmltht3_hoc19 = round(vals2.cmltht3_hoc19,2)
        vals2.cmltht3_hoc20 = round(vals2.cmltht3_hoc20,2)
        vals2.cmltht3_hoc21 = round(vals2.cmltht3_hoc21,2)
        vals2.cmltht3_hoc22 = round(vals2.cmltht3_hoc22,2)
        vals2.cmltht3_hoc23 = round(vals2.cmltht3_hoc23,2)
        vals2.cmltht3_hoc24 = round(vals2.cmltht3_hoc24,2)

        vals2.cmalthoc15 = round(vals2.cmalthoc15,2)        
        vals2.cmalthoc16 = round(vals2.cmalthoc16,2)
        vals2.cmalthoc17 = round(vals2.cmalthoc17,2)
        vals2.cmalthoc18 = round(vals2.cmalthoc18,2)
        vals2.cmalthoc19 = round(vals2.cmalthoc19,2)
        vals2.cmalthoc20 = round(vals2.cmalthoc20,2)
        vals2.cmalthoc21 = round(vals2.cmalthoc21,2)
        vals2.cmalthoc22 = round(vals2.cmalthoc22,2)
        vals2.cmalthoc23 = round(vals2.cmalthoc23,2)
        vals2.cmalthoc24 = round(vals2.cmalthoc24,2)

        vals2.cmltlthoc15 = round(vals2.cmltlthoc15,2)        
        vals2.cmltlthoc16 = round(vals2.cmltlthoc16,2)
        vals2.cmltlthoc17 = round(vals2.cmltlthoc17,2)
        vals2.cmltlthoc18 = round(vals2.cmltlthoc18,2)
        vals2.cmltlthoc19 = round(vals2.cmltlthoc19,2)
        vals2.cmltlthoc20 = round(vals2.cmltlthoc20,2)
        vals2.cmltlthoc21 = round(vals2.cmltlthoc21,2)
        vals2.cmltlthoc22 = round(vals2.cmltlthoc22,2)
        vals2.cmltlthoc23 = round(vals2.cmltlthoc23,2)
        vals2.cmltlthoc24 = round(vals2.cmltlthoc24,2)

        vals2.smahthoc15 = round(vals2.smahthoc15,2)        
        vals2.smahthoc16 = round(vals2.smahthoc16,2)
        vals2.smahthoc17 = round(vals2.smahthoc17,2)
        vals2.smahthoc18 = round(vals2.smahthoc18,2)
        vals2.smahthoc19 = round(vals2.smahthoc19,2)
        vals2.smahthoc20 = round(vals2.smahthoc20,2)
        vals2.smahthoc21 = round(vals2.smahthoc21,2)
        vals2.smahthoc22 = round(vals2.smahthoc22,2)
        vals2.smahthoc23 = round(vals2.smahthoc23,2)
        vals2.smahthoc24 = round(vals2.smahthoc24,2)

        vals2.smltht2_hoc15 = round(vals2.smltht2_hoc15,2)
        vals2.smltht2_hoc16 = round(vals2.smltht2_hoc16,2)
        vals2.smltht2_hoc17 = round(vals2.smltht2_hoc17,2)
        vals2.smltht2_hoc18 = round(vals2.smltht2_hoc18,2)
        vals2.smltht2_hoc19 = round(vals2.smltht2_hoc19,2)
        vals2.smltht2_hoc20 = round(vals2.smltht2_hoc20,2)
        vals2.smltht2_hoc21 = round(vals2.smltht2_hoc21,2)
        vals2.smltht2_hoc22 = round(vals2.smltht2_hoc22,2)
        vals2.smltht2_hoc23 = round(vals2.smltht2_hoc23,2)
        vals2.smltht2_hoc24 = round(vals2.smltht2_hoc24,2)

        vals2.smltht1_hoc15 = round(vals2.smltht1_hoc15,2)
        vals2.smltht1_hoc16 = round(vals2.smltht1_hoc16,2)
        vals2.smltht1_hoc17 = round(vals2.smltht1_hoc17,2)
        vals2.smltht1_hoc18 = round(vals2.smltht1_hoc18,2)
        vals2.smltht1_hoc19 = round(vals2.smltht1_hoc19,2)
        vals2.smltht1_hoc20 = round(vals2.smltht1_hoc20,2)
        vals2.smltht1_hoc21 = round(vals2.smltht1_hoc21,2)
        vals2.smltht1_hoc22 = round(vals2.smltht1_hoc22,2)
        vals2.smltht1_hoc23 = round(vals2.smltht1_hoc23,2)
        vals2.smltht1_hoc24 = round(vals2.smltht1_hoc24,2)

        vals2.hoctotal15 = round(vals2.hoctotal15,2)        
        vals2.hoctotal16 = round(vals2.hoctotal16,2)
        vals2.hoctotal17 = round(vals2.hoctotal17,2)
        vals2.hoctotal18 = round(vals2.hoctotal18,2)
        vals2.hoctotal19 = round(vals2.hoctotal19,2)
        vals2.hoctotal20 = round(vals2.hoctotal20,2)
        vals2.hoctotal21 = round(vals2.hoctotal21,2)
        vals2.hoctotal22 = round(vals2.hoctotal22,2)
        vals2.hoctotal23 = round(vals2.hoctotal23,2)
        vals2.hoctotal24 = round(vals2.hoctotal24,2)

        vals2.mp5and10lpet15 = round(vals2.mp5and10lpet15,2)        
        vals2.mp5and10lpet16 = round(vals2.mp5and10lpet16,2)
        vals2.mp5and10lpet17 = round(vals2.mp5and10lpet17,2)
        vals2.mp5and10lpet18 = round(vals2.mp5and10lpet18,2)
        vals2.mp5and10lpet19 = round(vals2.mp5and10lpet19,2)
        vals2.mp5and10lpet20 = round(vals2.mp5and10lpet20,2)
        vals2.mp5and10lpet21 = round(vals2.mp5and10lpet21,2)
        vals2.mp5and10lpet22 = round(vals2.mp5and10lpet22,2)
        vals2.mp5and10lpet23 = round(vals2.mp5and10lpet23,2)
        vals2.mp5and10lpet24 = round(vals2.mp5and10lpet24,2)

        vals2.mp20lpet15 = round(vals2.mp20lpet15,2)        
        vals2.mp20lpet16 = round(vals2.mp20lpet16,2)
        vals2.mp20lpet17 = round(vals2.mp20lpet17,2)
        vals2.mp20lpet18 = round(vals2.mp20lpet18,2)
        vals2.mp20lpet19 = round(vals2.mp20lpet19,2)
        vals2.mp20lpet20 = round(vals2.mp20lpet20,2)
        vals2.mp20lpet21 = round(vals2.mp20lpet21,2)
        vals2.mp20lpet22 = round(vals2.mp20lpet22,2)
        vals2.mp20lpet23 = round(vals2.mp20lpet23,2)
        vals2.mp20lpet24 = round(vals2.mp20lpet24,2)

        vals2.mp5and10l15 = round(vals2.mp5and10l15,2)        
        vals2.mp5and10l16 = round(vals2.mp5and10l16,2)
        vals2.mp5and10l17 = round(vals2.mp5and10l17,2)
        vals2.mp5and10l18 = round(vals2.mp5and10l18,2)
        vals2.mp5and10l19 = round(vals2.mp5and10l19,2)
        vals2.mp5and10l20 = round(vals2.mp5and10l20,2)
        vals2.mp5and10l21 = round(vals2.mp5and10l21,2)
        vals2.mp5and10l22 = round(vals2.mp5and10l22,2)
        vals2.mp5and10l23 = round(vals2.mp5and10l23,2)
        vals2.mp5and10l24 = round(vals2.mp5and10l24,2)

        vals2.mp20l15 = round(vals2.mp20l15,2)        
        vals2.mp20l16 = round(vals2.mp20l16,2)
        vals2.mp20l17 = round(vals2.mp20l17,2)
        vals2.mp20l18 = round(vals2.mp20l18,2)
        vals2.mp20l19 = round(vals2.mp20l19,2)
        vals2.mp20l20 = round(vals2.mp20l20,2)
        vals2.mp20l21 = round(vals2.mp20l21,2)
        vals2.mp20l22 = round(vals2.mp20l22,2)
        vals2.mp20l23 = round(vals2.mp20l23,2)
        vals2.mp20l24 = round(vals2.mp20l24,2)
        
        vals2.petline15 = round(vals2.petline15,2)        
        vals2.petline16 = round(vals2.petline16,2)
        vals2.petline17 = round(vals2.petline17,2)
        vals2.petline18 = round(vals2.petline18,2)
        vals2.petline19 = round(vals2.petline19,2)
        vals2.petline20 = round(vals2.petline20,2)
        vals2.petline21 = round(vals2.petline21,2)
        vals2.petline22 = round(vals2.petline22,2)
        vals2.petline23 = round(vals2.petline23,2)
        vals2.petline24 = round(vals2.petline24,2)

        vals2.bibline15 = round(vals2.bibline15,2)        
        vals2.bibline16 = round(vals2.bibline16,2)
        vals2.bibline17 = round(vals2.bibline17,2)
        vals2.bibline18 = round(vals2.bibline18,2)
        vals2.bibline19 = round(vals2.bibline19,2)
        vals2.bibline20 = round(vals2.bibline20,2)
        vals2.bibline21 = round(vals2.bibline21,2)
        vals2.bibline22 = round(vals2.bibline22,2)
        vals2.bibline23 = round(vals2.bibline23,2)
        vals2.bibline24 = round(vals2.bibline24,2)

        vals2.rhpko_hydro15 = round(vals2.rhpko_hydro15,2)        
        vals2.rhpko_hydro16 = round(vals2.rhpko_hydro16,2)
        vals2.rhpko_hydro17 = round(vals2.rhpko_hydro17,2)
        vals2.rhpko_hydro18 = round(vals2.rhpko_hydro18,2)
        vals2.rhpko_hydro19 = round(vals2.rhpko_hydro19,2)
        vals2.rhpko_hydro20 = round(vals2.rhpko_hydro20,2)
        vals2.rhpko_hydro21 = round(vals2.rhpko_hydro21,2)
        vals2.rhpko_hydro22 = round(vals2.rhpko_hydro22,2)
        vals2.rhpko_hydro23 = round(vals2.rhpko_hydro23,2)
        vals2.rhpko_hydro24 = round(vals2.rhpko_hydro24,2)

        vals2.rhpko_1ref15 = round(vals2.rhpko_1ref15,2)        
        vals2.rhpko_1ref16 = round(vals2.rhpko_1ref16,2)
        vals2.rhpko_1ref17 = round(vals2.rhpko_1ref17,2)
        vals2.rhpko_1ref18 = round(vals2.rhpko_1ref18,2)
        vals2.rhpko_1ref19 = round(vals2.rhpko_1ref19,2)
        vals2.rhpko_1ref20 = round(vals2.rhpko_1ref20,2)
        vals2.rhpko_1ref21 = round(vals2.rhpko_1ref21,2)
        vals2.rhpko_1ref22 = round(vals2.rhpko_1ref22,2)
        vals2.rhpko_1ref23 = round(vals2.rhpko_1ref23,2)
        vals2.rhpko_1ref24 = round(vals2.rhpko_1ref24,2)

        vals2.rhpko_2ref15 = round(vals2.rhpko_2ref15,2)        
        vals2.rhpko_2ref16 = round(vals2.rhpko_2ref16,2)
        vals2.rhpko_2ref17 = round(vals2.rhpko_2ref17,2)
        vals2.rhpko_2ref18 = round(vals2.rhpko_2ref18,2)
        vals2.rhpko_2ref19 = round(vals2.rhpko_2ref19,2)
        vals2.rhpko_2ref20 = round(vals2.rhpko_2ref20,2)
        vals2.rhpko_2ref21 = round(vals2.rhpko_2ref21,2)
        vals2.rhpko_2ref22 = round(vals2.rhpko_2ref22,2)
        vals2.rhpko_2ref23 = round(vals2.rhpko_2ref23,2)
        vals2.rhpko_2ref24 = round(vals2.rhpko_2ref24,2)

        vals2.rhpko_loadout15 = round(vals2.rhpko_loadout15,2)        
        vals2.rhpko_loadout16 = round(vals2.rhpko_loadout16,2)
        vals2.rhpko_loadout17 = round(vals2.rhpko_loadout17,2)
        vals2.rhpko_loadout18 = round(vals2.rhpko_loadout18,2)
        vals2.rhpko_loadout19 = round(vals2.rhpko_loadout19,2)
        vals2.rhpko_loadout20 = round(vals2.rhpko_loadout20,2)
        vals2.rhpko_loadout21 = round(vals2.rhpko_loadout21,2)
        vals2.rhpko_loadout22 = round(vals2.rhpko_loadout22,2)
        vals2.rhpko_loadout23 = round(vals2.rhpko_loadout23,2)
        vals2.rhpko_loadout24 = round(vals2.rhpko_loadout24,2)

        vals2.rhpkol_hydro15 = round(vals2.rhpkol_hydro15,2)        
        vals2.rhpkol_hydro16 = round(vals2.rhpkol_hydro16,2)
        vals2.rhpkol_hydro17 = round(vals2.rhpkol_hydro17,2)
        vals2.rhpkol_hydro18 = round(vals2.rhpkol_hydro18,2)
        vals2.rhpkol_hydro19 = round(vals2.rhpkol_hydro19,2)
        vals2.rhpkol_hydro20 = round(vals2.rhpkol_hydro20,2)
        vals2.rhpkol_hydro21 = round(vals2.rhpkol_hydro21,2)
        vals2.rhpkol_hydro22 = round(vals2.rhpkol_hydro22,2)
        vals2.rhpkol_hydro23 = round(vals2.rhpkol_hydro23,2)
        vals2.rhpkol_hydro24 = round(vals2.rhpkol_hydro24,2)

        vals2.rhpkol_1ref15 = round(vals2.rhpkol_1ref15,2)        
        vals2.rhpkol_1ref16 = round(vals2.rhpkol_1ref16,2)
        vals2.rhpkol_1ref17 = round(vals2.rhpkol_1ref17,2)
        vals2.rhpkol_1ref18 = round(vals2.rhpkol_1ref18,2)
        vals2.rhpkol_1ref19 = round(vals2.rhpkol_1ref19,2)
        vals2.rhpkol_1ref20 = round(vals2.rhpkol_1ref20,2)
        vals2.rhpkol_1ref21 = round(vals2.rhpkol_1ref21,2)
        vals2.rhpkol_1ref22 = round(vals2.rhpkol_1ref22,2)
        vals2.rhpkol_1ref23 = round(vals2.rhpkol_1ref23,2)
        vals2.rhpkol_1ref24 = round(vals2.rhpkol_1ref24,2)

        vals2.rhpkol_2ref15 = round(vals2.rhpkol_2ref15,2)        
        vals2.rhpkol_2ref16 = round(vals2.rhpkol_2ref16,2)
        vals2.rhpkol_2ref17 = round(vals2.rhpkol_2ref17,2)
        vals2.rhpkol_2ref18 = round(vals2.rhpkol_2ref18,2)
        vals2.rhpkol_2ref19 = round(vals2.rhpkol_2ref19,2)
        vals2.rhpkol_2ref20 = round(vals2.rhpkol_2ref20,2)
        vals2.rhpkol_2ref21 = round(vals2.rhpkol_2ref21,2)
        vals2.rhpkol_2ref22 = round(vals2.rhpkol_2ref22,2)
        vals2.rhpkol_2ref23 = round(vals2.rhpkol_2ref23,2)
        vals2.rhpkol_2ref24 = round(vals2.rhpkol_2ref24,2)

        vals2.rhpkol_loadout15 = round(vals2.rhpkol_loadout15,2)        
        vals2.rhpkol_loadout16 = round(vals2.rhpkol_loadout16,2)
        vals2.rhpkol_loadout17 = round(vals2.rhpkol_loadout17,2)
        vals2.rhpkol_loadout18 = round(vals2.rhpkol_loadout18,2)
        vals2.rhpkol_loadout19 = round(vals2.rhpkol_loadout19,2)
        vals2.rhpkol_loadout20 = round(vals2.rhpkol_loadout20,2)
        vals2.rhpkol_loadout21 = round(vals2.rhpkol_loadout21,2)
        vals2.rhpkol_loadout22 = round(vals2.rhpkol_loadout22,2)
        vals2.rhpkol_loadout23 = round(vals2.rhpkol_loadout23,2)
        vals2.rhpkol_loadout24 = round(vals2.rhpkol_loadout24,2)

        vals2.rhpkst_hydro15 = round(vals2.rhpkst_hydro15,2)        
        vals2.rhpkst_hydro16 = round(vals2.rhpkst_hydro16,2)
        vals2.rhpkst_hydro17 = round(vals2.rhpkst_hydro17,2)
        vals2.rhpkst_hydro18 = round(vals2.rhpkst_hydro18,2)
        vals2.rhpkst_hydro19 = round(vals2.rhpkst_hydro19,2)
        vals2.rhpkst_hydro20 = round(vals2.rhpkst_hydro20,2)
        vals2.rhpkst_hydro21 = round(vals2.rhpkst_hydro21,2)
        vals2.rhpkst_hydro22 = round(vals2.rhpkst_hydro22,2)
        vals2.rhpkst_hydro23 = round(vals2.rhpkst_hydro23,2)
        vals2.rhpkst_hydro24 = round(vals2.rhpkst_hydro24,2)

        vals2.rhpkst_1ref15 = round(vals2.rhpkst_1ref15,2)        
        vals2.rhpkst_1ref16 = round(vals2.rhpkst_1ref16,2)
        vals2.rhpkst_1ref17 = round(vals2.rhpkst_1ref17,2)
        vals2.rhpkst_1ref18 = round(vals2.rhpkst_1ref18,2)
        vals2.rhpkst_1ref19 = round(vals2.rhpkst_1ref19,2)
        vals2.rhpkst_1ref20 = round(vals2.rhpkst_1ref20,2)
        vals2.rhpkst_1ref21 = round(vals2.rhpkst_1ref21,2)
        vals2.rhpkst_1ref22 = round(vals2.rhpkst_1ref22,2)
        vals2.rhpkst_1ref23 = round(vals2.rhpkst_1ref23,2)
        vals2.rhpkst_1ref24 = round(vals2.rhpkst_1ref24,2)

        vals2.rhpkst_2ref15 = round(vals2.rhpkst_2ref15,2)        
        vals2.rhpkst_2ref16 = round(vals2.rhpkst_2ref16,2)
        vals2.rhpkst_2ref17 = round(vals2.rhpkst_2ref17,2)
        vals2.rhpkst_2ref18 = round(vals2.rhpkst_2ref18,2)
        vals2.rhpkst_2ref19 = round(vals2.rhpkst_2ref19,2)
        vals2.rhpkst_2ref20 = round(vals2.rhpkst_2ref20,2)
        vals2.rhpkst_2ref21 = round(vals2.rhpkst_2ref21,2)
        vals2.rhpkst_2ref22 = round(vals2.rhpkst_2ref22,2)
        vals2.rhpkst_2ref23 = round(vals2.rhpkst_2ref23,2)
        vals2.rhpkst_2ref24 = round(vals2.rhpkst_2ref24,2)

        vals2.rhpkst_loadout15 = round(vals2.rhpkst_loadout15,2)        
        vals2.rhpkst_loadout16 = round(vals2.rhpkst_loadout16,2)
        vals2.rhpkst_loadout17 = round(vals2.rhpkst_loadout17,2)
        vals2.rhpkst_loadout18 = round(vals2.rhpkst_loadout18,2)
        vals2.rhpkst_loadout19 = round(vals2.rhpkst_loadout19,2)
        vals2.rhpkst_loadout20 = round(vals2.rhpkst_loadout20,2)
        vals2.rhpkst_loadout21 = round(vals2.rhpkst_loadout21,2)
        vals2.rhpkst_loadout22 = round(vals2.rhpkst_loadout22,2)
        vals2.rhpkst_loadout23 = round(vals2.rhpkst_loadout23,2)
        vals2.rhpkst_loadout24 = round(vals2.rhpkst_loadout24,2)

        vals2.shortening_hydro15 = round(vals2.shortening_hydro15,2)        
        vals2.shortening_hydro16 = round(vals2.shortening_hydro16,2)
        vals2.shortening_hydro17 = round(vals2.shortening_hydro17,2)
        vals2.shortening_hydro18 = round(vals2.shortening_hydro18,2)
        vals2.shortening_hydro19 = round(vals2.shortening_hydro19,2)
        vals2.shortening_hydro20 = round(vals2.shortening_hydro20,2)
        vals2.shortening_hydro21 = round(vals2.shortening_hydro21,2)
        vals2.shortening_hydro22 = round(vals2.shortening_hydro22,2)
        vals2.shortening_hydro23 = round(vals2.shortening_hydro23,2)
        vals2.shortening_hydro24 = round(vals2.shortening_hydro24,2)

        vals2.shortening_1ref15 = round(vals2.shortening_1ref15,2)        
        vals2.shortening_1ref16 = round(vals2.shortening_1ref16,2)
        vals2.shortening_1ref17 = round(vals2.shortening_1ref17,2)
        vals2.shortening_1ref18 = round(vals2.shortening_1ref18,2)
        vals2.shortening_1ref19 = round(vals2.shortening_1ref19,2)
        vals2.shortening_1ref20 = round(vals2.shortening_1ref20,2)
        vals2.shortening_1ref21 = round(vals2.shortening_1ref21,2)
        vals2.shortening_1ref22 = round(vals2.shortening_1ref22,2)
        vals2.shortening_1ref23 = round(vals2.shortening_1ref23,2)
        vals2.shortening_1ref24 = round(vals2.shortening_1ref24,2)

        vals2.shortening_2ref15 = round(vals2.shortening_2ref15,2)        
        vals2.shortening_2ref16 = round(vals2.shortening_2ref16,2)
        vals2.shortening_2ref17 = round(vals2.shortening_2ref17,2)
        vals2.shortening_2ref18 = round(vals2.shortening_2ref18,2)
        vals2.shortening_2ref19 = round(vals2.shortening_2ref19,2)
        vals2.shortening_2ref20 = round(vals2.shortening_2ref20,2)
        vals2.shortening_2ref21 = round(vals2.shortening_2ref21,2)
        vals2.shortening_2ref22 = round(vals2.shortening_2ref22,2)
        vals2.shortening_2ref23 = round(vals2.shortening_2ref23,2)
        vals2.shortening_2ref24 = round(vals2.shortening_2ref24,2)

        vals2.shortening_loadout15 = round(vals2.shortening_loadout15,2)        
        vals2.shortening_loadout16 = round(vals2.shortening_loadout16,2)
        vals2.shortening_loadout17 = round(vals2.shortening_loadout17,2)
        vals2.shortening_loadout18 = round(vals2.shortening_loadout18,2)
        vals2.shortening_loadout19 = round(vals2.shortening_loadout19,2)
        vals2.shortening_loadout20 = round(vals2.shortening_loadout20,2)
        vals2.shortening_loadout21 = round(vals2.shortening_loadout21,2)
        vals2.shortening_loadout22 = round(vals2.shortening_loadout22,2)
        vals2.shortening_loadout23 = round(vals2.shortening_loadout23,2)
        vals2.shortening_loadout24 = round(vals2.shortening_loadout24,2)

        vals2.rhpo_hydro15 = round(vals2.rhpo_hydro15,2)        
        vals2.rhpo_hydro16 = round(vals2.rhpo_hydro16,2)
        vals2.rhpo_hydro17 = round(vals2.rhpo_hydro17,2)
        vals2.rhpo_hydro18 = round(vals2.rhpo_hydro18,2)
        vals2.rhpo_hydro19 = round(vals2.rhpo_hydro19,2)
        vals2.rhpo_hydro20 = round(vals2.rhpo_hydro20,2)
        vals2.rhpo_hydro21 = round(vals2.rhpo_hydro21,2)
        vals2.rhpo_hydro22 = round(vals2.rhpo_hydro22,2)
        vals2.rhpo_hydro23 = round(vals2.rhpo_hydro23,2)
        vals2.rhpo_hydro24 = round(vals2.rhpo_hydro24,2)

        vals2.rhpo_1ref15 = round(vals2.rhpo_1ref15,2)        
        vals2.rhpo_1ref16 = round(vals2.rhpo_1ref16,2)
        vals2.rhpo_1ref17 = round(vals2.rhpo_1ref17,2)
        vals2.rhpo_1ref18 = round(vals2.rhpo_1ref18,2)
        vals2.rhpo_1ref19 = round(vals2.rhpo_1ref19,2)
        vals2.rhpo_1ref20 = round(vals2.rhpo_1ref20,2)
        vals2.rhpo_1ref21 = round(vals2.rhpo_1ref21,2)
        vals2.rhpo_1ref22 = round(vals2.rhpo_1ref22,2)
        vals2.rhpo_1ref23 = round(vals2.rhpo_1ref23,2)
        vals2.rhpo_1ref24 = round(vals2.rhpo_1ref24,2)

        vals2.rhpo_2ref15 = round(vals2.rhpo_2ref15,2)        
        vals2.rhpo_2ref16 = round(vals2.rhpo_2ref16,2)
        vals2.rhpo_2ref17 = round(vals2.rhpo_2ref17,2)
        vals2.rhpo_2ref18 = round(vals2.rhpo_2ref18,2)
        vals2.rhpo_2ref19 = round(vals2.rhpo_2ref19,2)
        vals2.rhpo_2ref20 = round(vals2.rhpo_2ref20,2)
        vals2.rhpo_2ref21 = round(vals2.rhpo_2ref21,2)
        vals2.rhpo_2ref22 = round(vals2.rhpo_2ref22,2)
        vals2.rhpo_2ref23 = round(vals2.rhpo_2ref23,2)
        vals2.rhpo_2ref24 = round(vals2.rhpo_2ref24,2)

        vals2.rhpo_loadout15 = round(vals2.rhpo_loadout15,2)        
        vals2.rhpo_loadout16 = round(vals2.rhpo_loadout16,2)
        vals2.rhpo_loadout17 = round(vals2.rhpo_loadout17,2)
        vals2.rhpo_loadout18 = round(vals2.rhpo_loadout18,2)
        vals2.rhpo_loadout19 = round(vals2.rhpo_loadout19,2)
        vals2.rhpo_loadout20 = round(vals2.rhpo_loadout20,2)
        vals2.rhpo_loadout21 = round(vals2.rhpo_loadout21,2)
        vals2.rhpo_loadout22 = round(vals2.rhpo_loadout22,2)
        vals2.rhpo_loadout23 = round(vals2.rhpo_loadout23,2)
        vals2.rhpo_loadout24 = round(vals2.rhpo_loadout24,2)

        vals2.rpst_hydro15 = round(vals2.rpst_hydro15,2)        
        vals2.rpst_hydro16 = round(vals2.rpst_hydro16,2)
        vals2.rpst_hydro17 = round(vals2.rpst_hydro17,2)
        vals2.rpst_hydro18 = round(vals2.rpst_hydro18,2)
        vals2.rpst_hydro19 = round(vals2.rpst_hydro19,2)
        vals2.rpst_hydro20 = round(vals2.rpst_hydro20,2)
        vals2.rpst_hydro21 = round(vals2.rpst_hydro21,2)
        vals2.rpst_hydro22 = round(vals2.rpst_hydro22,2)
        vals2.rpst_hydro23 = round(vals2.rpst_hydro23,2)
        vals2.rpst_hydro24 = round(vals2.rpst_hydro24,2)

        vals2.rpst_1ref15 = round(vals2.rpst_1ref15,2)        
        vals2.rpst_1ref16 = round(vals2.rpst_1ref16,2)
        vals2.rpst_1ref17 = round(vals2.rpst_1ref17,2)
        vals2.rpst_1ref18 = round(vals2.rpst_1ref18,2)
        vals2.rpst_1ref19 = round(vals2.rpst_1ref19,2)
        vals2.rpst_1ref20 = round(vals2.rpst_1ref20,2)
        vals2.rpst_1ref21 = round(vals2.rpst_1ref21,2)
        vals2.rpst_1ref22 = round(vals2.rpst_1ref22,2)
        vals2.rpst_1ref23 = round(vals2.rpst_1ref23,2)
        vals2.rpst_1ref24 = round(vals2.rpst_1ref24,2)

        vals2.rpst_2ref15 = round(vals2.rpst_2ref15,2)        
        vals2.rpst_2ref16 = round(vals2.rpst_2ref16,2)
        vals2.rpst_2ref17 = round(vals2.rpst_2ref17,2)
        vals2.rpst_2ref18 = round(vals2.rpst_2ref18,2)
        vals2.rpst_2ref19 = round(vals2.rpst_2ref19,2)
        vals2.rpst_2ref20 = round(vals2.rpst_2ref20,2)
        vals2.rpst_2ref21 = round(vals2.rpst_2ref21,2)
        vals2.rpst_2ref22 = round(vals2.rpst_2ref22,2)
        vals2.rpst_2ref23 = round(vals2.rpst_2ref23,2)
        vals2.rpst_2ref24 = round(vals2.rpst_2ref24,2)

        vals2.rpst_loadout15 = round(vals2.rpst_loadout15,2)        
        vals2.rpst_loadout16 = round(vals2.rpst_loadout16,2)
        vals2.rpst_loadout17 = round(vals2.rpst_loadout17,2)
        vals2.rpst_loadout18 = round(vals2.rpst_loadout18,2)
        vals2.rpst_loadout19 = round(vals2.rpst_loadout19,2)
        vals2.rpst_loadout20 = round(vals2.rpst_loadout20,2)
        vals2.rpst_loadout21 = round(vals2.rpst_loadout21,2)
        vals2.rpst_loadout22 = round(vals2.rpst_loadout22,2)
        vals2.rpst_loadout23 = round(vals2.rpst_loadout23,2)
        vals2.rpst_loadout24 = round(vals2.rpst_loadout24,2)

        vals2.rhpst_hydro15 = round(vals2.rhpst_hydro15,2)        
        vals2.rhpst_hydro16 = round(vals2.rhpst_hydro16,2)
        vals2.rhpst_hydro17 = round(vals2.rhpst_hydro17,2)
        vals2.rhpst_hydro18 = round(vals2.rhpst_hydro18,2)
        vals2.rhpst_hydro19 = round(vals2.rhpst_hydro19,2)
        vals2.rhpst_hydro20 = round(vals2.rhpst_hydro20,2)
        vals2.rhpst_hydro21 = round(vals2.rhpst_hydro21,2)
        vals2.rhpst_hydro22 = round(vals2.rhpst_hydro22,2)
        vals2.rhpst_hydro23 = round(vals2.rhpst_hydro23,2)
        vals2.rhpst_hydro24 = round(vals2.rhpst_hydro24,2)

        vals2.rhpst_1ref15 = round(vals2.rhpst_1ref15,2)        
        vals2.rhpst_1ref16 = round(vals2.rhpst_1ref16,2)
        vals2.rhpst_1ref17 = round(vals2.rhpst_1ref17,2)
        vals2.rhpst_1ref18 = round(vals2.rhpst_1ref18,2)
        vals2.rhpst_1ref19 = round(vals2.rhpst_1ref19,2)
        vals2.rhpst_1ref20 = round(vals2.rhpst_1ref20,2)
        vals2.rhpst_1ref21 = round(vals2.rhpst_1ref21,2)
        vals2.rhpst_1ref22 = round(vals2.rhpst_1ref22,2)
        vals2.rhpst_1ref23 = round(vals2.rhpst_1ref23,2)
        vals2.rhpst_1ref24 = round(vals2.rhpst_1ref24,2)

        vals2.rhpst_2ref15 = round(vals2.rhpst_2ref15,2)        
        vals2.rhpst_2ref16 = round(vals2.rhpst_2ref16,2)
        vals2.rhpst_2ref17 = round(vals2.rhpst_2ref17,2)
        vals2.rhpst_2ref18 = round(vals2.rhpst_2ref18,2)
        vals2.rhpst_2ref19 = round(vals2.rhpst_2ref19,2)
        vals2.rhpst_2ref20 = round(vals2.rhpst_2ref20,2)
        vals2.rhpst_2ref21 = round(vals2.rhpst_2ref21,2)
        vals2.rhpst_2ref22 = round(vals2.rhpst_2ref22,2)
        vals2.rhpst_2ref23 = round(vals2.rhpst_2ref23,2)
        vals2.rhpst_2ref24 = round(vals2.rhpst_2ref24,2)

        vals2.rhpst_loadout15 = round(vals2.rhpst_loadout15,2)        
        vals2.rhpst_loadout16 = round(vals2.rhpst_loadout16,2)
        vals2.rhpst_loadout17 = round(vals2.rhpst_loadout17,2)
        vals2.rhpst_loadout18 = round(vals2.rhpst_loadout18,2)
        vals2.rhpst_loadout19 = round(vals2.rhpst_loadout19,2)
        vals2.rhpst_loadout20 = round(vals2.rhpst_loadout20,2)
        vals2.rhpst_loadout21 = round(vals2.rhpst_loadout21,2)
        vals2.rhpst_loadout22 = round(vals2.rhpst_loadout22,2)
        vals2.rhpst_loadout23 = round(vals2.rhpst_loadout23,2)
        vals2.rhpst_loadout24 = round(vals2.rhpst_loadout24,2)

        vals2.rhcno_hydro15 = round(vals2.rhcno_hydro15,2)        
        vals2.rhcno_hydro16 = round(vals2.rhcno_hydro16,2)
        vals2.rhcno_hydro17 = round(vals2.rhcno_hydro17,2)
        vals2.rhcno_hydro18 = round(vals2.rhcno_hydro18,2)
        vals2.rhcno_hydro19 = round(vals2.rhcno_hydro19,2)
        vals2.rhcno_hydro20 = round(vals2.rhcno_hydro20,2)
        vals2.rhcno_hydro21 = round(vals2.rhcno_hydro21,2)
        vals2.rhcno_hydro22 = round(vals2.rhcno_hydro22,2)
        vals2.rhcno_hydro23 = round(vals2.rhcno_hydro23,2)
        vals2.rhcno_hydro24 = round(vals2.rhcno_hydro24,2)

        vals2.rhcno_1ref15 = round(vals2.rhcno_1ref15,2)        
        vals2.rhcno_1ref16 = round(vals2.rhcno_1ref16,2)
        vals2.rhcno_1ref17 = round(vals2.rhcno_1ref17,2)
        vals2.rhcno_1ref18 = round(vals2.rhcno_1ref18,2)
        vals2.rhcno_1ref19 = round(vals2.rhcno_1ref19,2)
        vals2.rhcno_1ref20 = round(vals2.rhcno_1ref20,2)
        vals2.rhcno_1ref21 = round(vals2.rhcno_1ref21,2)
        vals2.rhcno_1ref22 = round(vals2.rhcno_1ref22,2)
        vals2.rhcno_1ref23 = round(vals2.rhcno_1ref23,2)
        vals2.rhcno_1ref24 = round(vals2.rhcno_1ref24,2)

        vals2.rhcno_2ref15 = round(vals2.rhcno_2ref15,2)        
        vals2.rhcno_2ref16 = round(vals2.rhcno_2ref16,2)
        vals2.rhcno_2ref17 = round(vals2.rhcno_2ref17,2)
        vals2.rhcno_2ref18 = round(vals2.rhcno_2ref18,2)
        vals2.rhcno_2ref19 = round(vals2.rhcno_2ref19,2)
        vals2.rhcno_2ref20 = round(vals2.rhcno_2ref20,2)
        vals2.rhcno_2ref21 = round(vals2.rhcno_2ref21,2)
        vals2.rhcno_2ref22 = round(vals2.rhcno_2ref22,2)
        vals2.rhcno_2ref23 = round(vals2.rhcno_2ref23,2)
        vals2.rhcno_2ref24 = round(vals2.rhcno_2ref24,2)

        vals2.rhcno_loadout15 = round(vals2.rhcno_loadout15,2)        
        vals2.rhcno_loadout16 = round(vals2.rhcno_loadout16,2)
        vals2.rhcno_loadout17 = round(vals2.rhcno_loadout17,2)
        vals2.rhcno_loadout18 = round(vals2.rhcno_loadout18,2)
        vals2.rhcno_loadout19 = round(vals2.rhcno_loadout19,2)
        vals2.rhcno_loadout20 = round(vals2.rhcno_loadout20,2)
        vals2.rhcno_loadout21 = round(vals2.rhcno_loadout21,2)
        vals2.rhcno_loadout22 = round(vals2.rhcno_loadout22,2)
        vals2.rhcno_loadout23 = round(vals2.rhcno_loadout23,2)
        vals2.rhcno_loadout24 = round(vals2.rhcno_loadout24,2)

        vals2.rcno_hydro15 = round(vals2.rcno_hydro15,2)        
        vals2.rcno_hydro16 = round(vals2.rcno_hydro16,2)
        vals2.rcno_hydro17 = round(vals2.rcno_hydro17,2)
        vals2.rcno_hydro18 = round(vals2.rcno_hydro18,2)
        vals2.rcno_hydro19 = round(vals2.rcno_hydro19,2)
        vals2.rcno_hydro20 = round(vals2.rcno_hydro20,2)
        vals2.rcno_hydro21 = round(vals2.rcno_hydro21,2)
        vals2.rcno_hydro22 = round(vals2.rcno_hydro22,2)
        vals2.rcno_hydro23 = round(vals2.rcno_hydro23,2)
        vals2.rcno_hydro24 = round(vals2.rcno_hydro24,2)

        vals2.rcno_1ref15 = round(vals2.rcno_1ref15,2)        
        vals2.rcno_1ref16 = round(vals2.rcno_1ref16,2)
        vals2.rcno_1ref17 = round(vals2.rcno_1ref17,2)
        vals2.rcno_1ref18 = round(vals2.rcno_1ref18,2)
        vals2.rcno_1ref19 = round(vals2.rcno_1ref19,2)
        vals2.rcno_1ref20 = round(vals2.rcno_1ref20,2)
        vals2.rcno_1ref21 = round(vals2.rcno_1ref21,2)
        vals2.rcno_1ref22 = round(vals2.rcno_1ref22,2)
        vals2.rcno_1ref23 = round(vals2.rcno_1ref23,2)
        vals2.rcno_1ref24 = round(vals2.rcno_1ref24,2)

        vals2.rcno_2ref15 = round(vals2.rcno_2ref15,2)        
        vals2.rcno_2ref16 = round(vals2.rcno_2ref16,2)
        vals2.rcno_2ref17 = round(vals2.rcno_2ref17,2)
        vals2.rcno_2ref18 = round(vals2.rcno_2ref18,2)
        vals2.rcno_2ref19 = round(vals2.rcno_2ref19,2)
        vals2.rcno_2ref20 = round(vals2.rcno_2ref20,2)
        vals2.rcno_2ref21 = round(vals2.rcno_2ref21,2)
        vals2.rcno_2ref22 = round(vals2.rcno_2ref22,2)
        vals2.rcno_2ref23 = round(vals2.rcno_2ref23,2)
        vals2.rcno_2ref24 = round(vals2.rcno_2ref24,2)

        vals2.rcno_loadout15 = round(vals2.rcno_loadout15,2)        
        vals2.rcno_loadout16 = round(vals2.rcno_loadout16,2)
        vals2.rcno_loadout17 = round(vals2.rcno_loadout17,2)
        vals2.rcno_loadout18 = round(vals2.rcno_loadout18,2)
        vals2.rcno_loadout19 = round(vals2.rcno_loadout19,2)
        vals2.rcno_loadout20 = round(vals2.rcno_loadout20,2)
        vals2.rcno_loadout21 = round(vals2.rcno_loadout21,2)
        vals2.rcno_loadout22 = round(vals2.rcno_loadout22,2)
        vals2.rcno_loadout23 = round(vals2.rcno_loadout23,2)
        vals2.rcno_loadout24 = round(vals2.rcno_loadout24,2)

        vals2.rpko_hydro15 = round(vals2.rpko_hydro15,2)        
        vals2.rpko_hydro16 = round(vals2.rpko_hydro16,2)
        vals2.rpko_hydro17 = round(vals2.rpko_hydro17,2)
        vals2.rpko_hydro18 = round(vals2.rpko_hydro18,2)
        vals2.rpko_hydro19 = round(vals2.rpko_hydro19,2)
        vals2.rpko_hydro20 = round(vals2.rpko_hydro20,2)
        vals2.rpko_hydro21 = round(vals2.rpko_hydro21,2)
        vals2.rpko_hydro22 = round(vals2.rpko_hydro22,2)
        vals2.rpko_hydro23 = round(vals2.rpko_hydro23,2)
        vals2.rpko_hydro24 = round(vals2.rpko_hydro24,2)

        vals2.rpko_1ref15 = round(vals2.rpko_1ref15,2)        
        vals2.rpko_1ref16 = round(vals2.rpko_1ref16,2)
        vals2.rpko_1ref17 = round(vals2.rpko_1ref17,2)
        vals2.rpko_1ref18 = round(vals2.rpko_1ref18,2)
        vals2.rpko_1ref19 = round(vals2.rpko_1ref19,2)
        vals2.rpko_1ref20 = round(vals2.rpko_1ref20,2)
        vals2.rpko_1ref21 = round(vals2.rpko_1ref21,2)
        vals2.rpko_1ref22 = round(vals2.rpko_1ref22,2)
        vals2.rpko_1ref23 = round(vals2.rpko_1ref23,2)
        vals2.rpko_1ref24 = round(vals2.rpko_1ref24,2)

        vals2.rpko_2ref15 = round(vals2.rpko_2ref15,2)        
        vals2.rpko_2ref16 = round(vals2.rpko_2ref16,2)
        vals2.rpko_2ref17 = round(vals2.rpko_2ref17,2)
        vals2.rpko_2ref18 = round(vals2.rpko_2ref18,2)
        vals2.rpko_2ref19 = round(vals2.rpko_2ref19,2)
        vals2.rpko_2ref20 = round(vals2.rpko_2ref20,2)
        vals2.rpko_2ref21 = round(vals2.rpko_2ref21,2)
        vals2.rpko_2ref22 = round(vals2.rpko_2ref22,2)
        vals2.rpko_2ref23 = round(vals2.rpko_2ref23,2)
        vals2.rpko_2ref24 = round(vals2.rpko_2ref24,2)

        vals2.rpko_loadout15 = round(vals2.rpko_loadout15,2)        
        vals2.rpko_loadout16 = round(vals2.rpko_loadout16,2)
        vals2.rpko_loadout17 = round(vals2.rpko_loadout17,2)
        vals2.rpko_loadout18 = round(vals2.rpko_loadout18,2)
        vals2.rpko_loadout19 = round(vals2.rpko_loadout19,2)
        vals2.rpko_loadout20 = round(vals2.rpko_loadout20,2)
        vals2.rpko_loadout21 = round(vals2.rpko_loadout21,2)
        vals2.rpko_loadout22 = round(vals2.rpko_loadout22,2)
        vals2.rpko_loadout23 = round(vals2.rpko_loadout23,2)
        vals2.rpko_loadout24 = round(vals2.rpko_loadout24,2)

        vals2.apshortening_2ref15 = round(vals2.apshortening_2ref15,2)        
        vals2.apshortening_2ref16 = round(vals2.apshortening_2ref16,2)
        vals2.apshortening_2ref17 = round(vals2.apshortening_2ref17,2)
        vals2.apshortening_2ref18 = round(vals2.apshortening_2ref18,2)
        vals2.apshortening_2ref19 = round(vals2.apshortening_2ref19,2)
        vals2.apshortening_2ref20 = round(vals2.apshortening_2ref20,2)
        vals2.apshortening_2ref21 = round(vals2.apshortening_2ref21,2)
        vals2.apshortening_2ref22 = round(vals2.apshortening_2ref22,2)
        vals2.apshortening_2ref23 = round(vals2.apshortening_2ref23,2)
        vals2.apshortening_2ref24 = round(vals2.apshortening_2ref24,2)

        vals2.apshortening_perf15 = round(vals2.apshortening_perf15,2)        
        vals2.apshortening_perf16 = round(vals2.apshortening_perf16,2)
        vals2.apshortening_perf17 = round(vals2.apshortening_perf17,2)
        vals2.apshortening_perf18 = round(vals2.apshortening_perf18,2)
        vals2.apshortening_perf19 = round(vals2.apshortening_perf19,2)
        vals2.apshortening_perf20 = round(vals2.apshortening_perf20,2)
        vals2.apshortening_perf21 = round(vals2.apshortening_perf21,2)
        vals2.apshortening_perf22 = round(vals2.apshortening_perf22,2)
        vals2.apshortening_perf23 = round(vals2.apshortening_perf23,2)
        vals2.apshortening_perf24 = round(vals2.apshortening_perf24,2)

        vals2.rhpoc_2ref15 = round(vals2.rhpoc_2ref15,2)        
        vals2.rhpoc_2ref16 = round(vals2.rhpoc_2ref16,2)
        vals2.rhpoc_2ref17 = round(vals2.rhpoc_2ref17,2)
        vals2.rhpoc_2ref18 = round(vals2.rhpoc_2ref18,2)
        vals2.rhpoc_2ref19 = round(vals2.rhpoc_2ref19,2)
        vals2.rhpoc_2ref20 = round(vals2.rhpoc_2ref20,2)
        vals2.rhpoc_2ref21 = round(vals2.rhpoc_2ref21,2)
        vals2.rhpoc_2ref22 = round(vals2.rhpoc_2ref22,2)
        vals2.rhpoc_2ref23 = round(vals2.rhpoc_2ref23,2)
        vals2.rhpoc_2ref24 = round(vals2.rhpoc_2ref24,2)

        vals2.rhpoc_perf15 = round(vals2.rhpoc_perf15,2)        
        vals2.rhpoc_perf16 = round(vals2.rhpoc_perf16,2)
        vals2.rhpoc_perf17 = round(vals2.rhpoc_perf17,2)
        vals2.rhpoc_perf18 = round(vals2.rhpoc_perf18,2)
        vals2.rhpoc_perf19 = round(vals2.rhpoc_perf19,2)
        vals2.rhpoc_perf20 = round(vals2.rhpoc_perf20,2)
        vals2.rhpoc_perf21 = round(vals2.rhpoc_perf21,2)
        vals2.rhpoc_perf22 = round(vals2.rhpoc_perf22,2)
        vals2.rhpoc_perf23 = round(vals2.rhpoc_perf23,2)
        vals2.rhpoc_perf24 = round(vals2.rhpoc_perf24,2)

        vals2.rhsbo_2ref15 = round(vals2.rhsbo_2ref15,2)        
        vals2.rhsbo_2ref16 = round(vals2.rhsbo_2ref16,2)
        vals2.rhsbo_2ref17 = round(vals2.rhsbo_2ref17,2)
        vals2.rhsbo_2ref18 = round(vals2.rhsbo_2ref18,2)
        vals2.rhsbo_2ref19 = round(vals2.rhsbo_2ref19,2)
        vals2.rhsbo_2ref20 = round(vals2.rhsbo_2ref20,2)
        vals2.rhsbo_2ref21 = round(vals2.rhsbo_2ref21,2)
        vals2.rhsbo_2ref22 = round(vals2.rhsbo_2ref22,2)
        vals2.rhsbo_2ref23 = round(vals2.rhsbo_2ref23,2)
        vals2.rhsbo_2ref24 = round(vals2.rhsbo_2ref24,2)

        vals2.rhsbo_perf15 = round(vals2.rhsbo_perf15,2)        
        vals2.rhsbo_perf16 = round(vals2.rhsbo_perf16,2)
        vals2.rhsbo_perf17 = round(vals2.rhsbo_perf17,2)
        vals2.rhsbo_perf18 = round(vals2.rhsbo_perf18,2)
        vals2.rhsbo_perf19 = round(vals2.rhsbo_perf19,2)
        vals2.rhsbo_perf20 = round(vals2.rhsbo_perf20,2)
        vals2.rhsbo_perf21 = round(vals2.rhsbo_perf21,2)
        vals2.rhsbo_perf22 = round(vals2.rhsbo_perf22,2)
        vals2.rhsbo_perf23 = round(vals2.rhsbo_perf23,2)
        vals2.rhsbo_perf24 = round(vals2.rhsbo_perf24,2)

        vals2.ls_bibline15 = round(vals2.ls_bibline15,2)        
        vals2.ls_bibline16 = round(vals2.ls_bibline16,2)
        vals2.ls_bibline17 = round(vals2.ls_bibline17,2)
        vals2.ls_bibline18 = round(vals2.ls_bibline18,2)
        vals2.ls_bibline19 = round(vals2.ls_bibline19,2)
        vals2.ls_bibline20 = round(vals2.ls_bibline20,2)
        vals2.ls_bibline21 = round(vals2.ls_bibline21,2)
        vals2.ls_bibline22 = round(vals2.ls_bibline22,2)
        vals2.ls_bibline23 = round(vals2.ls_bibline23,2)
        vals2.ls_bibline24 = round(vals2.ls_bibline24,2)

        vals2.niscfl2_15 = round(vals2.niscfl2_15,2)        
        vals2.niscfl2_16 = round(vals2.niscfl2_16,2)
        vals2.niscfl2_17 = round(vals2.niscfl2_17,2)
        vals2.niscfl2_18 = round(vals2.niscfl2_18,2)
        vals2.niscfl2_19 = round(vals2.niscfl2_19,2)
        vals2.niscfl2_20 = round(vals2.niscfl2_20,2)
        vals2.niscfl2_21 = round(vals2.niscfl2_21,2)
        vals2.niscfl2_22 = round(vals2.niscfl2_22,2)
        vals2.niscfl2_23 = round(vals2.niscfl2_23,2)
        vals2.niscfl2_24 = round(vals2.niscfl2_24,2)

        vals2.nimcfl2_15 = round(vals2.nimcfl2_15,2)        
        vals2.nimcfl2_16 = round(vals2.nimcfl2_16,2)
        vals2.nimcfl2_17 = round(vals2.nimcfl2_17,2)
        vals2.nimcfl2_18 = round(vals2.nimcfl2_18,2)
        vals2.nimcfl2_19 = round(vals2.nimcfl2_19,2)
        vals2.nimcfl2_20 = round(vals2.nimcfl2_20,2)
        vals2.nimcfl2_21 = round(vals2.nimcfl2_21,2)
        vals2.nimcfl2_22 = round(vals2.nimcfl2_22,2)
        vals2.nimcfl2_23 = round(vals2.nimcfl2_23,2)
        vals2.nimcfl2_24 = round(vals2.nimcfl2_24,2)

        vals2.iscfl2_15 = round(vals2.iscfl2_15,2)        
        vals2.iscfl2_16 = round(vals2.iscfl2_16,2)
        vals2.iscfl2_17 = round(vals2.iscfl2_17,2)
        vals2.iscfl2_18 = round(vals2.iscfl2_18,2)
        vals2.iscfl2_19 = round(vals2.iscfl2_19,2)
        vals2.iscfl2_20 = round(vals2.iscfl2_20,2)
        vals2.iscfl2_21 = round(vals2.iscfl2_21,2)
        vals2.iscfl2_22 = round(vals2.iscfl2_22,2)
        vals2.iscfl2_23 = round(vals2.iscfl2_23,2)
        vals2.iscfl2_24 = round(vals2.iscfl2_24,2)

        vals2.imcfl2_15 = round(vals2.imcfl2_15,2)        
        vals2.imcfl2_16 = round(vals2.imcfl2_16,2)
        vals2.imcfl2_17 = round(vals2.imcfl2_17,2)
        vals2.imcfl2_18 = round(vals2.imcfl2_18,2)
        vals2.imcfl2_19 = round(vals2.imcfl2_19,2)
        vals2.imcfl2_20 = round(vals2.imcfl2_20,2)
        vals2.imcfl2_21 = round(vals2.imcfl2_21,2)
        vals2.imcfl2_22 = round(vals2.imcfl2_22,2)
        vals2.imcfl2_23 = round(vals2.imcfl2_23,2)
        vals2.imcfl2_24 = round(vals2.imcfl2_24,2)

        vals2.asm_perf15 = round(vals2.asm_perf15,2)        
        vals2.asm_perf16 = round(vals2.asm_perf16,2)
        vals2.asm_perf17 = round(vals2.asm_perf17,2)
        vals2.asm_perf18 = round(vals2.asm_perf18,2)
        vals2.asm_perf19 = round(vals2.asm_perf19,2)
        vals2.asm_perf20 = round(vals2.asm_perf20,2)
        vals2.asm_perf21 = round(vals2.asm_perf21,2)
        vals2.asm_perf22 = round(vals2.asm_perf22,2)
        vals2.asm_perf23 = round(vals2.asm_perf23,2)
        vals2.asm_perf24 = round(vals2.asm_perf24,2)

        vals2.asm_smp15 = round(vals2.asm_smp15,2)        
        vals2.asm_smp16 = round(vals2.asm_smp16,2)
        vals2.asm_smp17 = round(vals2.asm_smp17,2)
        vals2.asm_smp18 = round(vals2.asm_smp18,2)
        vals2.asm_smp19 = round(vals2.asm_smp19,2)
        vals2.asm_smp20 = round(vals2.asm_smp20,2)
        vals2.asm_smp21 = round(vals2.asm_smp21,2)
        vals2.asm_smp22 = round(vals2.asm_smp22,2)
        vals2.asm_smp23 = round(vals2.asm_smp23,2)
        vals2.asm_smp24 = round(vals2.asm_smp24,2)

        vals2.ieoil15 = round(vals2.ieoil15,2)        
        vals2.ieoil16 = round(vals2.ieoil16,2)
        vals2.ieoil17 = round(vals2.ieoil17,2)
        vals2.ieoil18 = round(vals2.ieoil18,2)
        vals2.ieoil19 = round(vals2.ieoil19,2)
        vals2.ieoil20 = round(vals2.ieoil20,2)
        vals2.ieoil21 = round(vals2.ieoil21,2)
        vals2.ieoil22 = round(vals2.ieoil22,2)
        vals2.ieoil23 = round(vals2.ieoil23,2)
        vals2.ieoil24 = round(vals2.ieoil24,2)

        vals2.hoil15 = round(vals2.hoil15,2)        
        vals2.hoil16 = round(vals2.hoil16,2)
        vals2.hoil17 = round(vals2.hoil17,2)
        vals2.hoil18 = round(vals2.hoil18,2)
        vals2.hoil19 = round(vals2.hoil19,2)
        vals2.hoil20 = round(vals2.hoil20,2)
        vals2.hoil21 = round(vals2.hoil21,2)
        vals2.hoil22 = round(vals2.hoil22,2)
        vals2.hoil23 = round(vals2.hoil23,2)
        vals2.hoil24 = round(vals2.hoil24,2)

        vals2.hoilh15 = round(vals2.hoilh15,2)        
        vals2.hoilh16 = round(vals2.hoilh16,2)
        vals2.hoilh17 = round(vals2.hoilh17,2)
        vals2.hoilh18 = round(vals2.hoilh18,2)
        vals2.hoilh19 = round(vals2.hoilh19,2)
        vals2.hoilh20 = round(vals2.hoilh20,2)
        vals2.hoilh21 = round(vals2.hoilh21,2)
        vals2.hoilh22 = round(vals2.hoilh22,2)
        vals2.hoilh23 = round(vals2.hoilh23,2)
        vals2.hoilh24 = round(vals2.hoilh24,2)

        vals2.hoilr15 = round(vals2.hoilr15,2)        
        vals2.hoilr16 = round(vals2.hoilr16,2)
        vals2.hoilr17 = round(vals2.hoilr17,2)
        vals2.hoilr18 = round(vals2.hoilr18,2)
        vals2.hoilr19 = round(vals2.hoilr19,2)
        vals2.hoilr20 = round(vals2.hoilr20,2)
        vals2.hoilr21 = round(vals2.hoilr21,2)
        vals2.hoilr22 = round(vals2.hoilr22,2)
        vals2.hoilr23 = round(vals2.hoilr23,2)
        vals2.hoilr24 = round(vals2.hoilr24,2)

        vals2.ieoild15 = round(vals2.ieoild15,2)        
        vals2.ieoild16 = round(vals2.ieoild16,2)
        vals2.ieoild17 = round(vals2.ieoild17,2)
        vals2.ieoild18 = round(vals2.ieoild18,2)
        vals2.ieoild19 = round(vals2.ieoild19,2)
        vals2.ieoild20 = round(vals2.ieoild20,2)
        vals2.ieoild21 = round(vals2.ieoild21,2)
        vals2.ieoild22 = round(vals2.ieoild22,2)
        vals2.ieoild23 = round(vals2.ieoild23,2)
        vals2.ieoild24 = round(vals2.ieoild24,2)

        vals2.neutral15 = round(vals2.neutral15,2)        
        vals2.neutral16 = round(vals2.neutral16,2)
        vals2.neutral17 = round(vals2.neutral17,2)
        vals2.neutral18 = round(vals2.neutral18,2)
        vals2.neutral19 = round(vals2.neutral19,2)
        vals2.neutral20 = round(vals2.neutral20,2)
        vals2.neutral21 = round(vals2.neutral21,2)
        vals2.neutral22 = round(vals2.neutral22,2)
        vals2.neutral23 = round(vals2.neutral23,2)
        vals2.neutral24 = round(vals2.neutral24,2)

        vals2.neutral_ecu15 = round(vals2.neutral_ecu15,2)        
        vals2.neutral_ecu16 = round(vals2.neutral_ecu16,2)
        vals2.neutral_ecu17 = round(vals2.neutral_ecu17,2)
        vals2.neutral_ecu18 = round(vals2.neutral_ecu18,2)
        vals2.neutral_ecu19 = round(vals2.neutral_ecu19,2)
        vals2.neutral_ecu20 = round(vals2.neutral_ecu20,2)
        vals2.neutral_ecu21 = round(vals2.neutral_ecu21,2)
        vals2.neutral_ecu22 = round(vals2.neutral_ecu22,2)
        vals2.neutral_ecu23 = round(vals2.neutral_ecu23,2)
        vals2.neutral_ecu24 = round(vals2.neutral_ecu24,2)

        vals2.dewaxing15 = round(vals2.dewaxing15,2)        
        vals2.dewaxing16 = round(vals2.dewaxing16,2)
        vals2.dewaxing17 = round(vals2.dewaxing17,2)
        vals2.dewaxing18 = round(vals2.dewaxing18,2)
        vals2.dewaxing19 = round(vals2.dewaxing19,2)
        vals2.dewaxing20 = round(vals2.dewaxing20,2)
        vals2.dewaxing21 = round(vals2.dewaxing21,2)
        vals2.dewaxing22 = round(vals2.dewaxing22,2)
        vals2.dewaxing23 = round(vals2.dewaxing23,2)
        vals2.dewaxing24 = round(vals2.dewaxing24,2)

        vals2.dewaxing_ecu15 = round(vals2.dewaxing_ecu15,2)        
        vals2.dewaxing_ecu16 = round(vals2.dewaxing_ecu16,2)
        vals2.dewaxing_ecu17 = round(vals2.dewaxing_ecu17,2)
        vals2.dewaxing_ecu18 = round(vals2.dewaxing_ecu18,2)
        vals2.dewaxing_ecu19 = round(vals2.dewaxing_ecu19,2)
        vals2.dewaxing_ecu20 = round(vals2.dewaxing_ecu20,2)
        vals2.dewaxing_ecu21 = round(vals2.dewaxing_ecu21,2)
        vals2.dewaxing_ecu22 = round(vals2.dewaxing_ecu22,2)
        vals2.dewaxing_ecu23 = round(vals2.dewaxing_ecu23,2)
        vals2.dewaxing_ecu24 = round(vals2.dewaxing_ecu24,2)

        vals2.firstref15 = round(vals2.firstref15,2)        
        vals2.firstref16 = round(vals2.firstref16,2)
        vals2.firstref17 = round(vals2.firstref17,2)
        vals2.firstref18 = round(vals2.firstref18,2)
        vals2.firstref19 = round(vals2.firstref19,2)
        vals2.firstref20 = round(vals2.firstref20,2)
        vals2.firstref21 = round(vals2.firstref21,2)
        vals2.firstref22 = round(vals2.firstref22,2)
        vals2.firstref23 = round(vals2.firstref23,2)
        vals2.firstref24 = round(vals2.firstref24,2)

        vals2.secondref15 = round(vals2.secondref15,2)        
        vals2.secondref16 = round(vals2.secondref16,2)
        vals2.secondref17 = round(vals2.secondref17,2)
        vals2.secondref18 = round(vals2.secondref18,2)
        vals2.secondref19 = round(vals2.secondref19,2)
        vals2.secondref20 = round(vals2.secondref20,2)
        vals2.secondref21 = round(vals2.secondref21,2)
        vals2.secondref22 = round(vals2.secondref22,2)
        vals2.secondref23 = round(vals2.secondref23,2)
        vals2.secondref24 = round(vals2.secondref24,2)

        vals2.tpd400ref15 = round(vals2.tpd400ref15,2)        
        vals2.tpd400ref16 = round(vals2.tpd400ref16,2)
        vals2.tpd400ref17 = round(vals2.tpd400ref17,2)
        vals2.tpd400ref18 = round(vals2.tpd400ref18,2)
        vals2.tpd400ref19 = round(vals2.tpd400ref19,2)
        vals2.tpd400ref20 = round(vals2.tpd400ref20,2)
        vals2.tpd400ref21 = round(vals2.tpd400ref21,2)
        vals2.tpd400ref22 = round(vals2.tpd400ref22,2)
        vals2.tpd400ref23 = round(vals2.tpd400ref23,2)
        vals2.tpd400ref24 = round(vals2.tpd400ref24,2)

        vals2.tpd400ref_ecu15 = round(vals2.tpd400ref_ecu15,2)        
        vals2.tpd400ref_ecu16 = round(vals2.tpd400ref_ecu16,2)
        vals2.tpd400ref_ecu17 = round(vals2.tpd400ref_ecu17,2)
        vals2.tpd400ref_ecu18 = round(vals2.tpd400ref_ecu18,2)
        vals2.tpd400ref_ecu19 = round(vals2.tpd400ref_ecu19,2)
        vals2.tpd400ref_ecu20 = round(vals2.tpd400ref_ecu20,2)
        vals2.tpd400ref_ecu21 = round(vals2.tpd400ref_ecu21,2)
        vals2.tpd400ref_ecu22 = round(vals2.tpd400ref_ecu22,2)
        vals2.tpd400ref_ecu23 = round(vals2.tpd400ref_ecu23,2)
        vals2.tpd400ref_ecu24 = round(vals2.tpd400ref_ecu24,2)

        vals2.hydro15 = round(vals2.hydro15,2)        
        vals2.hydro16 = round(vals2.hydro16,2)
        vals2.hydro17 = round(vals2.hydro17,2)
        vals2.hydro18 = round(vals2.hydro18,2)
        vals2.hydro19 = round(vals2.hydro19,2)
        vals2.hydro20 = round(vals2.hydro20,2)
        vals2.hydro21 = round(vals2.hydro21,2)
        vals2.hydro22 = round(vals2.hydro22,2)
        vals2.hydro23 = round(vals2.hydro23,2)
        vals2.hydro24 = round(vals2.hydro24,2)

        vals2.hydro_ecu15 = round(vals2.hydro_ecu15,2)        
        vals2.hydro_ecu16 = round(vals2.hydro_ecu16,2)
        vals2.hydro_ecu17 = round(vals2.hydro_ecu17,2)
        vals2.hydro_ecu18 = round(vals2.hydro_ecu18,2)
        vals2.hydro_ecu19 = round(vals2.hydro_ecu19,2)
        vals2.hydro_ecu20 = round(vals2.hydro_ecu20,2)
        vals2.hydro_ecu21 = round(vals2.hydro_ecu21,2)
        vals2.hydro_ecu22 = round(vals2.hydro_ecu22,2)
        vals2.hydro_ecu23 = round(vals2.hydro_ecu23,2)
        vals2.hydro_ecu24 = round(vals2.hydro_ecu24,2)

        vals2.ieoilb_ecu15 = round(vals2.ieoilb_ecu15,2)        
        vals2.ieoilb_ecu16 = round(vals2.ieoilb_ecu16,2)
        vals2.ieoilb_ecu17 = round(vals2.ieoilb_ecu17,2)
        vals2.ieoilb_ecu18 = round(vals2.ieoilb_ecu18,2)
        vals2.ieoilb_ecu19 = round(vals2.ieoilb_ecu19,2)
        vals2.ieoilb_ecu20 = round(vals2.ieoilb_ecu20,2)
        vals2.ieoilb_ecu21 = round(vals2.ieoilb_ecu21,2)
        vals2.ieoilb_ecu22 = round(vals2.ieoilb_ecu22,2)
        vals2.ieoilb_ecu23 = round(vals2.ieoilb_ecu23,2)
        vals2.ieoilb_ecu24 = round(vals2.ieoilb_ecu24,2)

        vals2.maxcap15 = round(vals2.maxcap15,2)        
        vals2.maxcap16 = round(vals2.maxcap16,2)
        vals2.maxcap17 = round(vals2.maxcap17,2)
        vals2.maxcap18 = round(vals2.maxcap18,2)
        vals2.maxcap19 = round(vals2.maxcap19,2)
        vals2.maxcap20 = round(vals2.maxcap20,2)
        vals2.maxcap21 = round(vals2.maxcap21,2)
        vals2.maxcap22 = round(vals2.maxcap22,2)
        vals2.maxcap23 = round(vals2.maxcap23,2)
        vals2.maxcap24 = round(vals2.maxcap24,2)

        vals2.perfectorb_ecu15 = round(vals2.perfectorb_ecu15,2)        
        vals2.perfectorb_ecu16 = round(vals2.perfectorb_ecu16,2)
        vals2.perfectorb_ecu17 = round(vals2.perfectorb_ecu17,2)
        vals2.perfectorb_ecu18 = round(vals2.perfectorb_ecu18,2)
        vals2.perfectorb_ecu19 = round(vals2.perfectorb_ecu19,2)
        vals2.perfectorb_ecu20 = round(vals2.perfectorb_ecu20,2)
        vals2.perfectorb_ecu21 = round(vals2.perfectorb_ecu21,2)
        vals2.perfectorb_ecu22 = round(vals2.perfectorb_ecu22,2)
        vals2.perfectorb_ecu23 = round(vals2.perfectorb_ecu23,2)
        vals2.perfectorb_ecu24 = round(vals2.perfectorb_ecu24,2)

        vals2.perfectorb15 = round(vals2.perfectorb15,2)        
        vals2.perfectorb16 = round(vals2.perfectorb16,2)
        vals2.perfectorb17 = round(vals2.perfectorb17,2)
        vals2.perfectorb18 = round(vals2.perfectorb18,2)
        vals2.perfectorb19 = round(vals2.perfectorb19,2)
        vals2.perfectorb20 = round(vals2.perfectorb20,2)
        vals2.perfectorb21 = round(vals2.perfectorb21,2)
        vals2.perfectorb22 = round(vals2.perfectorb22,2)
        vals2.perfectorb23 = round(vals2.perfectorb23,2)
        vals2.perfectorb24 = round(vals2.perfectorb24,2)

        vals2.perfectora_ecu15 = round(vals2.perfectora_ecu15,2)        
        vals2.perfectora_ecu16 = round(vals2.perfectora_ecu16,2)
        vals2.perfectora_ecu17 = round(vals2.perfectora_ecu17,2)
        vals2.perfectora_ecu18 = round(vals2.perfectora_ecu18,2)
        vals2.perfectora_ecu19 = round(vals2.perfectora_ecu19,2)
        vals2.perfectora_ecu20 = round(vals2.perfectora_ecu20,2)
        vals2.perfectora_ecu21 = round(vals2.perfectora_ecu21,2)
        vals2.perfectora_ecu22 = round(vals2.perfectora_ecu22,2)
        vals2.perfectora_ecu23 = round(vals2.perfectora_ecu23,2)
        vals2.perfectora_ecu24 = round(vals2.perfectora_ecu24,2)

        vals2.perfectora15 = round(vals2.perfectora15,2)        
        vals2.perfectora16 = round(vals2.perfectora16,2)
        vals2.perfectora17 = round(vals2.perfectora17,2)
        vals2.perfectora18 = round(vals2.perfectora18,2)
        vals2.perfectora19 = round(vals2.perfectora19,2)
        vals2.perfectora20 = round(vals2.perfectora20,2)
        vals2.perfectora21 = round(vals2.perfectora21,2)
        vals2.perfectora22 = round(vals2.perfectora22,2)
        vals2.perfectora23 = round(vals2.perfectora23,2)
        vals2.perfectora24 = round(vals2.perfectora24,2)

        vals2.petline_ecu15 = round(vals2.petline_ecu15,2)        
        vals2.petline_ecu16 = round(vals2.petline_ecu16,2)
        vals2.petline_ecu17 = round(vals2.petline_ecu17,2)
        vals2.petline_ecu18 = round(vals2.petline_ecu18,2)
        vals2.petline_ecu19 = round(vals2.petline_ecu19,2)
        vals2.petline_ecu20 = round(vals2.petline_ecu20,2)
        vals2.petline_ecu21 = round(vals2.petline_ecu21,2)
        vals2.petline_ecu22 = round(vals2.petline_ecu22,2)
        vals2.petline_ecu23 = round(vals2.petline_ecu23,2)
        vals2.petline_ecu24 = round(vals2.petline_ecu24,2)

        vals2.tbibline_ecu15 = round(vals2.tbibline_ecu15,2)        
        vals2.tbibline_ecu16 = round(vals2.tbibline_ecu16,2)
        vals2.tbibline_ecu17 = round(vals2.tbibline_ecu17,2)
        vals2.tbibline_ecu18 = round(vals2.tbibline_ecu18,2)
        vals2.tbibline_ecu19 = round(vals2.tbibline_ecu19,2)
        vals2.tbibline_ecu20 = round(vals2.tbibline_ecu20,2)
        vals2.tbibline_ecu21 = round(vals2.tbibline_ecu21,2)
        vals2.tbibline_ecu22 = round(vals2.tbibline_ecu22,2)
        vals2.tbibline_ecu23 = round(vals2.tbibline_ecu23,2)
        vals2.tbibline_ecu24 = round(vals2.tbibline_ecu24,2)

        vals2.tbibline15 = round(vals2.tbibline15,2)        
        vals2.tbibline16 = round(vals2.tbibline16,2)
        vals2.tbibline17 = round(vals2.tbibline17,2)
        vals2.tbibline18 = round(vals2.tbibline18,2)
        vals2.tbibline19 = round(vals2.tbibline19,2)
        vals2.tbibline20 = round(vals2.tbibline20,2)
        vals2.tbibline21 = round(vals2.tbibline21,2)
        vals2.tbibline22 = round(vals2.tbibline22,2)
        vals2.tbibline23 = round(vals2.tbibline23,2)
        vals2.tbibline24 = round(vals2.tbibline24,2)

        vals2.cfl1t15 = round(vals2.cfl1t15,2)        
        vals2.cfl1t16 = round(vals2.cfl1t16,2)
        vals2.cfl1t17 = round(vals2.cfl1t17,2)
        vals2.cfl1t18 = round(vals2.cfl1t18,2)
        vals2.cfl1t19 = round(vals2.cfl1t19,2)
        vals2.cfl1t20 = round(vals2.cfl1t20,2)
        vals2.cfl1t21 = round(vals2.cfl1t21,2)
        vals2.cfl1t22 = round(vals2.cfl1t22,2)
        vals2.cfl1t23 = round(vals2.cfl1t23,2)
        vals2.cfl1t24 = round(vals2.cfl1t24,2)

        vals2.cfl1t_ecu15 = round(vals2.cfl1t_ecu15,2)        
        vals2.cfl1t_ecu16 = round(vals2.cfl1t_ecu16,2)
        vals2.cfl1t_ecu17 = round(vals2.cfl1t_ecu17,2)
        vals2.cfl1t_ecu18 = round(vals2.cfl1t_ecu18,2)
        vals2.cfl1t_ecu19 = round(vals2.cfl1t_ecu19,2)
        vals2.cfl1t_ecu20 = round(vals2.cfl1t_ecu20,2)
        vals2.cfl1t_ecu21 = round(vals2.cfl1t_ecu21,2)
        vals2.cfl1t_ecu22 = round(vals2.cfl1t_ecu22,2)
        vals2.cfl1t_ecu23 = round(vals2.cfl1t_ecu23,2)
        vals2.cfl1t_ecu24 = round(vals2.cfl1t_ecu24,2)

        vals2.cfl2t15 = round(vals2.cfl2t15,2)        
        vals2.cfl2t16 = round(vals2.cfl2t16,2)
        vals2.cfl2t17 = round(vals2.cfl2t17,2)
        vals2.cfl2t18 = round(vals2.cfl2t18,2)
        vals2.cfl2t19 = round(vals2.cfl2t19,2)
        vals2.cfl2t20 = round(vals2.cfl2t20,2)
        vals2.cfl2t21 = round(vals2.cfl2t21,2)
        vals2.cfl2t22 = round(vals2.cfl2t22,2)
        vals2.cfl2t23 = round(vals2.cfl2t23,2)
        vals2.cfl2t24 = round(vals2.cfl2t24,2)

        vals2.cfl2t_ecu15 = round(vals2.cfl2t_ecu15,2)        
        vals2.cfl2t_ecu16 = round(vals2.cfl2t_ecu16,2)
        vals2.cfl2t_ecu17 = round(vals2.cfl2t_ecu17,2)
        vals2.cfl2t_ecu18 = round(vals2.cfl2t_ecu18,2)
        vals2.cfl2t_ecu19 = round(vals2.cfl2t_ecu19,2)
        vals2.cfl2t_ecu20 = round(vals2.cfl2t_ecu20,2)
        vals2.cfl2t_ecu21 = round(vals2.cfl2t_ecu21,2)
        vals2.cfl2t_ecu22 = round(vals2.cfl2t_ecu22,2)
        vals2.cfl2t_ecu23 = round(vals2.cfl2t_ecu23,2)
        vals2.cfl2t_ecu24 = round(vals2.cfl2t_ecu24,2)

        vals2.rhsbo_hydro15 = round(vals2.rhsbo_hydro15,2)        
        vals2.rhsbo_hydro16 = round(vals2.rhsbo_hydro16,2)
        vals2.rhsbo_hydro17 = round(vals2.rhsbo_hydro17,2)
        vals2.rhsbo_hydro18 = round(vals2.rhsbo_hydro18,2)
        vals2.rhsbo_hydro19 = round(vals2.rhsbo_hydro19,2)
        vals2.rhsbo_hydro20 = round(vals2.rhsbo_hydro20,2)
        vals2.rhsbo_hydro21 = round(vals2.rhsbo_hydro21,2)
        vals2.rhsbo_hydro22 = round(vals2.rhsbo_hydro22,2)
        vals2.rhsbo_hydro23 = round(vals2.rhsbo_hydro23,2)
        vals2.rhsbo_hydro24 = round(vals2.rhsbo_hydro24,2)





















































































































































































































        
        # save the object
        vals.save()
        vals2.save()
        return render(request, 'index.html', {'vals': vals , 'vals2': vals2})

    # context = {'form': form} --- if want to use forms
    return render(request, 'index.html', )