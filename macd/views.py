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


        

        # save the object
        vals.save()
        vals2.save()
        return render(request, 'index.html', {'vals': vals , 'vals2': vals2})

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
