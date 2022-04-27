import streamlit as st
import time
import numpy as np

# Dropdown for ARR scale selection
arrScale = st.selectbox(
     'What is the company current ARR scale?',
     ('<$10M', '$10-$25M', '$25-$50M','$50-$100M','$100M+' ))


def calScore(arrScale, arrGrowth, NDR, R40, NMN, ARRFTE, burnRate):

    if arrScale == '<$10M':
        return 0.4 * calArrGrowth('<$10M', arrGrowth) + 0.2 * calNDR('<$10M', NDR) + 0.15 * calNMN('<$10M', NMN) + 0.15 * calARRFTE('<$10M',ARRFTE) + 0.1 * calBurnRate('<$10M',burnRate)
    elif arrScale == '$10-$25M':
        return 0.3 * calArrGrowth('$10-$25M', arrGrowth) + 0.3 * calNDR('$10-$25M', NDR) + 0.15 * calNMN('$10-$25M', NMN) + 0.15 * calARRFTE('$10-$25M',ARRFTE) + 0.1 * calBurnRate('$10-$25M',burnRate)
    elif arrScale == '$25-$50M':
        return 0.25 * calArrGrowth('$25-$50M', arrGrowth) + 0.2 * calNDR('$25-$50M', NDR) + 0.15 * calR40('$25-$50M', R40) + 0.15 * calNMN('$25-$50M', NMN) + 0.15 * calARRFTE('$25-$50M',ARRFTE) + 0.1 * calBurnRate('$25-$50M',burnRate)
    elif arrScale == '$50-$100M':
        return 0.25 * calArrGrowth('$50-$100M', arrGrowth) + 0.15 * calNDR('$50-$100M', NDR) + 0.15 * calR40('$50-$100M', R40) + 0.15 * calNMN('$50-$100M', NMN) + 0.15 * calARRFTE('$50-$100M',ARRFTE) + 0.1 * calBurnRate('$50-$100M',burnRate)
    elif arrScale == '$100M+':
        return 0.25 * calArrGrowth('$100M+', arrGrowth) + 0.15 * calNDR('$100M+', NDR) + 0.15 * calR40('$100M+', R40) + 0.15 * calNMN('$100M+', NMN) + 0.15 * calARRFTE('$100M+',ARRFTE) + 0.1 * calBurnRate('$100M+',burnRate)

    return 

def calArrGrowth(arrScale, arrGrowth):

    if arrScale == '<$10M':

        if not arrGrowth:
            return 0

        if arrGrowth <= 100:
            return arrGrowth / 100 * 25
        elif 100 < arrGrowth <= 210:
            return 25 + (arrGrowth - 100) / (210 - 100) * 25
        elif 210 < arrGrowth <= 325:
            return 50 + (arrGrowth - 210) / (325 - 210) * 25
        else:
            return 75 + (arrGrowth - 325) / (400 - 325) * 25

    elif arrScale == '$10-$25M':

        if not arrGrowth:
            return 0

        if arrGrowth <= 80:
            return 0
        elif 80 < arrGrowth <= 100:
            return (arrGrowth - 80) / (100 - 80) * 25
        elif 100 < arrGrowth <= 135:
            return 25 + (arrGrowth - 100) / (135 - 100) * 25
        elif 135 < arrGrowth <= 175:
            return 50 + (arrGrowth - 135) / (175 - 135) * 25
        else:
            return 75 + (arrGrowth - 175) / (300 - 175) * 25

    elif arrScale == '$25-$50M':

        if arrGrowth <= 30:
            return 0
        elif 30 < arrGrowth <= 60:
            return (arrGrowth - 30) / (60 - 30) * 25
        elif 60 < arrGrowth <= 90:
            return 25 + (arrGrowth - 60) / (90 - 60) * 25
        elif 90 < arrGrowth <= 115:
            return 50 + (arrGrowth - 90) / (115 - 90) * 25
        else:
            return 75 + (arrGrowth - 115) / (150 - 115) * 25
       
    elif arrScale == '$50-$100M':

        if arrGrowth <= 10:
            return 0
        elif 10 < arrGrowth <= 30:
            return (arrGrowth - 10) / (30 - 10) * 25
        elif 30 < arrGrowth <= 65:
            return 25 + (arrGrowth - 30) / (65 - 30) * 25
        elif 65 < arrGrowth <= 105:
            return 50 + (arrGrowth - 65) / (105 - 65) * 25
        else:
            return 75 + (arrGrowth - 105) / (120 - 105) * 25

       
    elif arrScale == '$100M+':

        if arrGrowth <= 10:
            return 0
        elif 10 < arrGrowth <= 30:
            return (arrGrowth - 10) / (30 - 10) * 25
        elif 30 < arrGrowth <= 45:
            return 25 + (arrGrowth - 30) / (45 - 30) * 25
        elif 45 < arrGrowth <= 70:
            return 50 + (arrGrowth - 45) / (70 - 45) * 25
        else:
            return 75 + (arrGrowth - 70) / (90 - 70) * 25
       
    return 0

def calNDR(arrScale, NDR):

    if arrScale == '<$10M':

        if not NDR:
            return 0

        if 80 < NDR <= 100:
            return NDR / 100 * 25
        elif 100 < NDR <= 115:
            return 25 + (NDR - 100) / (115 - 100) * 25
        elif 115 < NDR <= 130:
            return 50 + (NDR - 115) / (130 - 115) * 25
        else:
            return 75 + (NDR - 130) / (150 - 130) * 25

    elif arrScale == '$10-$25M':

        if 80 < NDR <= 100:
            return (NDR - 80) / (100 - 80) * 25
        elif 100 < NDR <= 115:
            return 25 + (NDR - 100) / (115 - 100) * 25
        elif 115 < NDR <= 130:
            return 50 + (NDR - 115) / (130 - 115) * 25
        else:
            return 75 + (NDR - 130) / (140 - 130) * 25

    elif arrScale == '$25-$50M':

        if 80 < NDR <= 100:
            return (NDR - 80) / (100 - 80) * 25
        elif 100 < NDR <= 110:
            return 25 + (NDR - 100) / (110 - 100) * 25
        elif 110 < NDR <= 125:
            return 50 + (NDR - 110) / (125 - 110) * 25
        else:
            return 75 + (NDR - 125) / (130 - 125) * 25
       
    elif arrScale == '$50-$100M':

        if 80 < NDR <= 100:
            return (NDR - 80) / (100 - 80) * 25
        elif 100 < NDR <= 110:
            return 25 + (NDR - 100) / (110 - 100) * 25
        elif 110 < NDR <= 125:
            return 50 + (NDR - 110) / (125 - 110) * 25
        else:
            return 75 + (NDR - 125) / (130 - 125) * 25

       
    elif arrScale == '$100M+':

        if 80 < NDR <= 100:
            return (NDR - 80) / (100 - 80) * 25
        elif 100 < NDR <= 110:
            return 25 + (NDR - 100) / (110 - 100) * 25
        elif 110 < NDR <= 125:
            return 50 + (NDR - 110) / (125 - 110) * 25
        else:
            return 75 + (NDR - 125) / (130 - 125) * 25
       
    return 0

def calR40(arrScale, R40):

    if arrScale == '<$10M' or arrScale == '$10-$25M':
        return 0

    elif arrScale == '$25-$50M':

        if R40 <= 40:
            return R40 / 40 * 25
        elif 40 < R40 <= 60:
            return 25 + (R40 - 40) / (60 - 40) * 25
        elif 60 < R40 <= 105:
            return 50 + (R40 - 60) / (105 - 60) * 25
        else:
            return 75 + (R40 - 105) / (120 - 105) * 25
       
    elif arrScale == '$50-$100M':

        if R40 <= 40:
            return R40 / 40 * 25
        elif 40 < R40 <= 52:
            return 25 + (R40 - 40) / (52 - 40) * 25
        elif 52 < R40 <= 80:
            return 50 + (R40 - 52) / (80 - 52) * 25
        else:
            return 75 + (R40 - 80) / (100 - 80) * 25

       
    elif arrScale == '$100M+':

        if R40 <= 20:
            return R40 / 40 * 25
        elif 20 < R40 <= 40:
            return 25 + (R40 - 20) / (40 - 20) * 25
        elif 40 < R40 <= 65:
            return 50 + (R40 - 40) / (65 - 40) * 25
        else:
            return 75 + (R40 - 65) / (75 - 65) * 25
       
    return 0

def calNMN(arrScale, NMN):

    if arrScale == '<$10M':

        if not NMN:
            return 0
    
        if 0.2 < NMN <= 0.5:
            return (NMN - 0.2) / (0.5 - 0.2) * 25
        elif 0.5 < NMN <= 0.8:
            return 25 + (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.4:
            return 50 + (NMN - 0.8) / (1.4 - 0.8) * 25
        else:
            return 75 + (NMN - 1.4) / (2.4 - 1.4) * 25
    
    elif arrScale == '$10-$25M':

        if 0.5 < NMN <= 0.8:
            return (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.0:
            return 25 + (NMN - 0.8) / (1.0 - 0.8) * 25
        elif 1.0 < NMN <= 1.4:
            return 50 + (NMN - 1.0) / (1.4 - 1.0) * 25
        else:
            return 75 + (NMN - 1.4) / (2.0 - 1.4) * 25

    elif arrScale == '$25-$50M':

        if 0.6 < NMN <= 0.8:
            return (NMN - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < NMN <= 1.0:
            return 25 + (NMN - 0.8) / (1.0 - 0.8) * 25
        elif 1.0 < NMN <= 1.3:
            return 50 + (NMN - 1.0) / (1.3 - 1.0) * 25
        else:
            return 75 + (NMN - 1.3) / (1.5 - 1.3) * 25
       
    elif arrScale == '$50-$100M':

        if 0.4 < NMN <= 0.6:
            return (NMN - 0.4) / (0.6 - 0.4) * 25
        elif 0.6 < NMN <= 0.8:
            return 25 + (NMN - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < NMN <= 1.1:
            return 50 + (NMN - 0.8) / (1.1 - 0.8) * 25
        else:
            return 75 + (NMN - 1.1) / (1.3 - 1.1) * 25

       
    elif arrScale == '$100M+':

        if 0.3 < NMN <= 0.5:
            return (NMN - 0.3) / (0.5 - 0.3) * 25
        elif 0.5 < NMN <= 0.7:
            return 25 + (NMN - 0.5) / (0.7 - 0.5) * 25
        elif 0.7 < NMN <= 1.0:
            return 50 + (NMN - 0.7) / (1.0 - 0.7) * 25
        else:
            return 75 + (NMN - 1.0) / (1.2 - 1.0) * 25
       
    return 0

def calARRFTE(arrScale, ARRFTE):

    if arrScale == '<$10M':

        if not ARRFTE:
            return 0
    
        if 10000 < ARRFTE <= 30000:
            return (ARRFTE - 10000) / (30000 - 10000) * 25
        elif 30000 < ARRFTE <= 50000:
            return 25 + (ARRFTE - 30000) / (50000 - 30000) * 25
        elif 50000 < ARRFTE <= 73000:
            return 50 + (ARRFTE - 50000) / (73000 - 50000) * 25
        else:
            return 75 + (ARRFTE - 73000) / (105000 - 73000) * 25
    
    elif arrScale == '$10-$25M':

        if 60000 < ARRFTE <= 90000:
            return (ARRFTE - 60000) / (90000 - 60000) * 25
        elif 90000 < ARRFTE <= 120000:
            return 25 + (ARRFTE - 90000) / (120000 - 90000) * 25
        elif 120000 < ARRFTE <= 150000:
            return 50 + (ARRFTE - 120000) / (150000 - 120000) * 25
        else:
            return 75 + (ARRFTE - 150000) / (170000 - 150000) * 25

    elif arrScale == '$25-$50M':

        if 60000 < ARRFTE <= 80000:
            return (ARRFTE - 60000) / (80000 - 60000) * 25
        elif 80000 < ARRFTE <= 120000:
            return 25 + (ARRFTE - 80000) / (120000 - 80000) * 25
        elif 120000 < ARRFTE <= 150000:
            return 50 + (ARRFTE - 120000) / (150000 - 120000) * 25
        else:
            return 75 + (ARRFTE - 150000) / (195000 - 150000) * 25


       
    elif arrScale == '$50-$100M':

        if 80000 < ARRFTE <= 120000:
            return (ARRFTE - 80000) / (120000 - 80000) * 25
        elif 120000 < ARRFTE <= 150000:
            return 25 + (ARRFTE - 120000) / (150000 - 120000) * 25
        elif 150000 < ARRFTE <= 175000:
            return 50 + (ARRFTE - 150000) / (175000 - 150000) * 25
        else:
            return 75 + (ARRFTE - 175000) / (230000 - 175000) * 25



       
    elif arrScale == '$100M+':

        if 100000 < ARRFTE <= 120000:
            return (ARRFTE - 100000) / (120000 - 100000) * 25
        elif 120000 < ARRFTE <= 150000:
            return 25 + (ARRFTE - 120000) / (150000 - 120000) * 25
        elif 150000 < ARRFTE <= 175000:
            return 50 + (ARRFTE - 150000) / (175000 - 150000) * 25
        else:
            return 75 + (ARRFTE - 175000) / (230000 - 175000) * 25
       
    return 0

def calBurnRate(arrScale, burnRate):
    
    if arrScale == '<$10M':

        if not burnRate:
            return 0

        if  burnRate <= 0.2:
            return burnRate / 0.2 * 25
        elif 0.2 < burnRate <= 0.4:
            return 25 + (burnRate - 0.2) / (0.4 - 0.2) * 25
        elif 0.4 < burnRate <= 0.6:
            return 50 + (burnRate - 0.4) / (0.6 - 0.4) * 25
        else:
            return 75 + (burnRate - 0.6) / (0.8 - 0.6) * 25

    elif arrScale == '$10-$25M':

        if  0.2 < burnRate <= 0.4:
            return (burnRate - 0.2) / (0.4 - 0.2) * 25
        elif 0.4 < burnRate <= 0.6:
            return 25 + (burnRate - 0.4) / (0.6 - 0.4) * 25
        elif 0.6 < burnRate <= 0.8:
            return 50 + (burnRate - 0.6) / (0.8 - 0.6) * 25
        else:
            return 75 + (burnRate - 0.8) / (1.0 - 0.8) * 25

    elif arrScale == '$25-$50M':

        if  0.4 < burnRate <= 0.6:
            return (burnRate - 0.4) / (0.6 - 0.4) * 25
        elif 0.6 < burnRate <= 0.8:
            return 25 + (burnRate - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < burnRate <= 1.0:
            return 50 + (burnRate - 0.8) / (1.0 - 0.8) * 25
        else:
            return 75 + (burnRate - 1.0) / (1.2 - 1.0) * 25
       
    elif arrScale == '$50-$100M':

        if  0.6 < burnRate <= 0.8:
            return (burnRate - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < burnRate <= 1.0:
            return 25 + (burnRate - 0.8) / (1.0 - 0.8) * 25
        elif 1.0 < burnRate <= 1.2:
            return 50 + (burnRate - 1.0) / (1.2 - 1.0) * 25
        else:
            return 75 + (burnRate - 1.2) / (1.4 - 1.2) * 25

       
    elif arrScale == '$100M+':

        if 0.8 < burnRate <= 1.0:
            return (burnRate - 0.8) / (1.0 - 0.8) * 25
        elif 1.0 < burnRate <= 1.2:
            return 25 + (burnRate - 1.0) / (1.2 - 1.0) * 25
        elif 1.2 < burnRate <= 1.4:
            return 50 + (burnRate - 1.2) / (1.4 - 1.2) * 25
        else:
            return 75 + (burnRate - 1.4) / (1.6 - 1.4) * 25
       
    return 0

st.write('You selected:', arrScale)

arrGrowth = st.number_input('ARR Gorwth')
st.write('ARR Growth is ', arrGrowth)

NDR = st.number_input('NDR')
st.write('Net Dollar Retention is ', NDR)

R40 = st.number_input('Rule of 40')
st.write('Rule of 40 is ', R40)

NMN = st.number_input('Net Magic Number')
st.write('Net Magic Number is ', NMN)

ARRFTE = st.number_input('ARR per FTE') * 1000
st.write('ARR per FTE is ', ARRFTE)

burnRate = st.number_input('burnRate', max_value=1.0)
st.write('Burn Rate is ', burnRate)

score = 'Composite score is ' + str(calScore(arrScale, arrGrowth,NDR,R40,NMN,ARRFTE,burnRate))

# st.write('Composite score is', calScore(arrScale, arrGrowth,NDR,R40,NMN,ARRFTE,burnRate))
st.header(score)


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
