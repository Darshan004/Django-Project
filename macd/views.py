from django.shortcuts import render, redirect
from django.http import HttpResponse
from macd.models import values
import numpy as np
from .forms import InputsForm


def index(request):
    if request.method == 'POST':
        # create new 'values' object
        vals = values()
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
        vals.rhpo15 = float(request.POST['rhpo15'])
        vals.rhsbo15 = float(request.POST['rhsbo15'])
        vals.subtotal_15 = vals.apshortening15 + vals.rhsbo15 + vals.rhpo15
        vals.sf_total15 = vals.subtotal_15 + vals.subtotal15

        vals.apshortening16 = float(request.POST['apshortening16'])
        vals.rhpo16 = float(request.POST['rhpo16'])
        vals.rhsbo16 = float(request.POST['rhsbo16'])
        vals.subtotal_16 = vals.apshortening16 + vals.rhsbo16 + vals.rhpo16
        vals.sf_total16 = vals.subtotal_16 + vals.subtotal16

        vals.apshortening17 = float(request.POST['apshortening17'])
        vals.rhpo17 = float(request.POST['rhpo17'])
        vals.rhsbo17 = float(request.POST['rhsbo17'])
        vals.subtotal_17 = vals.apshortening17 + vals.rhsbo17 + vals.rhpo17
        vals.sf_total17 = vals.subtotal_17 + vals.subtotal17

        vals.apshortening18 = float(request.POST['apshortening18'])
        vals.rhpo18 = float(request.POST['rhpo18'])
        vals.rhsbo18 = float(request.POST['rhsbo18'])
        vals.subtotal_18 = vals.apshortening18 + vals.rhsbo18 + vals.rhpo18
        vals.sf_total18 = vals.subtotal_18 + vals.subtotal18

        vals.apshortening19 = float(request.POST['apshortening19'])
        vals.rhpo19 = float(request.POST['rhpo19'])
        vals.rhsbo19 = float(request.POST['rhsbo19'])
        vals.subtotal_19 = vals.apshortening19 + vals.rhsbo19 + vals.rhpo19
        vals.sf_total19 = vals.subtotal_19 + vals.subtotal19

        vals.apshortening20 = float(request.POST['apshortening20'])
        vals.rhpo20 = float(request.POST['rhpo20'])
        vals.rhsbo20 = float(request.POST['rhsbo20'])
        vals.subtotal_20 = vals.apshortening20 + vals.rhsbo20 + vals.rhpo20
        vals.sf_total20 = vals.subtotal_20 + vals.subtotal20

        vals.apshortening21 = float(request.POST['apshortening21'])
        vals.rhpo21 = float(request.POST['rhpo21'])
        vals.rhsbo21 = float(request.POST['rhsbo21'])
        vals.subtotal_21 = vals.apshortening21 + vals.rhsbo21 + vals.rhpo21
        vals.sf_total21 = vals.subtotal_21 + vals.subtotal21

        vals.apshortening22 = float(request.POST['apshortening22'])
        vals.rhpo22 = float(request.POST['rhpo22'])
        vals.rhsbo22 = float(request.POST['rhsbo22'])
        vals.subtotal_22 = vals.apshortening22 + vals.rhsbo22 + vals.rhpo22
        vals.sf_total22 = vals.subtotal_22 + vals.subtotal22

        vals.apshortening23 = float(request.POST['apshortening23'])
        vals.rhpo23 = float(request.POST['rhpo23'])
        vals.rhsbo23 = float(request.POST['rhsbo23'])
        vals.subtotal_23 = vals.apshortening23 + vals.rhsbo23 + vals.rhpo23
        vals.sf_total23 = vals.subtotal_23 + vals.subtotal23

        vals.apshortening24 = float(request.POST['apshortening24'])
        vals.rhpo24 = float(request.POST['rhpo24'])
        vals.rhsbo24 = float(request.POST['rhsbo24'])
        vals.subtotal_24 = vals.apshortening24 + vals.rhsbo24 + vals.rhpo24
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

        # save the object
        vals.save()
        return render(request, 'index.html', {'vals': vals})

    # context = {'form': form} --- if want to use forms
    return render(request, 'index.html', )


# def calculate(request):
#     # vals = values.objects.all()  this will return all the objects, i dont think that is what you want
#     vals = values()
#     vals.hocan15 = float(request.POST['hocan15'])
#     vals.g1sb015 = float(request.POST['g1sb015'])
#     vals.corn15 = float(request.POST['corn15'])
#     vals.hsbo15 = float(request.POST['hsbo15'])

#     vals.stote_oil_blend15 = vals.g1sb015/(16.5*100)
#     vals.chicken_par_fry15 = (
#         vals.corn15 - vals.stote_oil_blend15*20/100)/(45/100)
#     vals.save()

#     return render(request, 'index.html', {'vals': vals})
