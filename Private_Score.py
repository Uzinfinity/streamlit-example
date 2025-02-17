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
        return 0.35 * calArrGrowth('$10-$25M', arrGrowth) + 0.25 * calNDR('$10-$25M', NDR) + 0.15 * calNMN('$10-$25M', NMN) + 0.15 * calARRFTE('$10-$25M',ARRFTE) + 0.1 * calBurnRate('$10-$25M',burnRate)
    elif arrScale == '$25-$50M':
        return 0.3 * calArrGrowth('$25-$50M', arrGrowth) + 0.2 * calNDR('$25-$50M', NDR) + 0.1 * calR40('$25-$50M', R40) + 0.2 * calNMN('$25-$50M', NMN) + 0.1 * calARRFTE('$25-$50M',ARRFTE) + 0.1 * calBurnRate('$25-$50M',burnRate)
    elif arrScale == '$50-$100M':
        return 0.3 * calArrGrowth('$50-$100M', arrGrowth) + 0.2 * calNDR('$50-$100M', NDR) + 0.1 * calR40('$50-$100M', R40) + 0.2 * calNMN('$50-$100M', NMN) + 0.1 * calARRFTE('$50-$100M',ARRFTE) + 0.1 * calBurnRate('$50-$100M',burnRate)
    elif arrScale == '$100M+':
        return 0.25 * calArrGrowth('$100M+', arrGrowth) + 0.15 * calNDR('$100M+', NDR) + 0.15 * calR40('$100M+', R40) + 0.15 * calNMN('$100M+', NMN) + 0.15 * calARRFTE('$100M+',ARRFTE) + 0.15 * calBurnRate('$100M+',burnRate)

    return 

def calArrGrowth(arrScale, arrGrowth):

    if arrScale == '<$10M':

        if not arrGrowth:
            return 0

        if arrGrowth <= 75:
            return arrGrowth / 100 * 25
        elif 75 < arrGrowth <= 150:
            return 25 + (arrGrowth - 75) / (150 - 75) * 25
        elif 150 < arrGrowth <= 225:
            return 50 + (arrGrowth - 150) / (225 - 150) * 25
        elif 225 < arrGrowth <= 325:
            return 75 + (arrGrowth - 225) / (325 - 225) * 25
        else:
            return 100
        

    elif arrScale == '$10-$25M':

        if not arrGrowth:
            return 0

        if arrGrowth <= 50:
            return 0
        elif 50 < arrGrowth <= 75:
            return (arrGrowth - 50) / (75 - 50) * 25
        elif 75 < arrGrowth <= 125:
            return 25 + (arrGrowth - 75) / (125 - 75) * 25
        elif 125 < arrGrowth <= 175:
            return 50 + (arrGrowth - 125) / (175 - 125) * 25
        elif 175 < arrGrowth <= 225:
            return 75 + (arrGrowth - 175) / (225 - 175) * 25
        else:
            return 100


    elif arrScale == '$25-$50M':

        if arrGrowth <= 15:
            return 0
        elif 15 < arrGrowth <= 40:
            return (arrGrowth - 15) / (40 - 15) * 25
        elif 40 < arrGrowth <= 65:
            return 25 + (arrGrowth - 40) / (65 - 40) * 25
        elif 65 < arrGrowth <= 90:
            return 50 + (arrGrowth - 65) / (90 - 65) * 25
        elif 90 < arrGrowth <= 115:
            return 75 + (arrGrowth - 90) / (115 - 90) * 25
        else:
            return 100
       
    elif arrScale == '$50-$100M':

        if arrGrowth <= 15:
            return 0
        elif 15 < arrGrowth <= 30:
            return (arrGrowth - 15) / (30 - 15) * 25
        elif 30 < arrGrowth <= 55:
            return 25 + (arrGrowth - 30) / (55 - 30) * 25
        elif 55 < arrGrowth <= 80:
            return 50 + (arrGrowth - 55) / (80 - 55) * 25
        else:
            return 75 + (arrGrowth - 80) / (105 - 80) * 25

       
    elif arrScale == '$100M+':

        if arrGrowth <= 10:
            return arrGrowth / 10 * 25
        elif 10 < arrGrowth <= 25:
            return 25 + (arrGrowth - 10) / (25 - 10) * 25
        elif 25 < arrGrowth <= 50:
            return 50 + (arrGrowth - 25) / (50 - 25) * 25
        elif 50 < arrGrowth <= 75:
            return 75 + (arrGrowth - 50) / (75 - 50) * 25
        else:
            100
       
    return 0

def calNDR(arrScale, NDR):

    if arrScale == '<$10M':

        if NDR < 80:
            return 0

        if 80 <= NDR <= 93:
            return (NDR - 80) / (93 - 80) * 25
        elif 93 < NDR <= 105:
            return 25 + (NDR - 93) / (105 - 93) * 25
        elif 105 < NDR <= 117:
            return 50 + (NDR - 105) / (117 - 105) * 25
        elif 117 < NDR <=130:
            return 75 + (NDR - 117) / (130 - 117) * 25
        else:
            return 100

    elif arrScale == '$10-$25M':

        if NDR < 80:
            return 0

        if 80 <= NDR <= 93:
            return (NDR - 80) / (93 - 80) * 25
        elif 93 < NDR <= 105:
            return 25 + (NDR - 93) / (105 - 93) * 25
        elif 105 < NDR <= 117:
            return 50 + (NDR - 105) / (117 - 105) * 25
        elif 117 < NDR <=130:
            return 75 + (NDR - 117) / (130 - 117) * 25
        else:
            return 100

    elif arrScale == '$25-$50M':

        if NDR < 70:
            return 0

        if 70 <= NDR <= 80:
            return (NDR - 70) / (80 - 70) * 25
        elif 80 < NDR <= 90:
            return 25 + (NDR - 80) / (90 - 80) * 25
        elif 90 < NDR <= 110:
            return 50 + (NDR - 90) / (110 - 90) * 25
        elif 110 < NDR <= 130:
            return 75 + (NDR - 110) / (130 - 110) * 25
        else:
            return 100
       
    elif arrScale == '$50-$100M':

        if NDR < 70:
            return 0

        if 70 <= NDR <= 80:
            return (NDR - 70) / (80 - 70) * 25
        elif 80 < NDR <= 90:
            return 25 + (NDR - 80) / (90 - 80) * 25
        elif 90 < NDR <= 110:
            return 50 + (NDR - 90) / (110 - 90) * 25
        elif 110 < NDR <= 130:
            return 75 + (NDR - 110) / (130 - 110) * 25
        else:
            return 100

       
    elif arrScale == '$100M+':

        if NDR < 70:
            return 0

        if 70 <= NDR <= 80:
            return (NDR - 70) / (80 - 70) * 25
        elif 80 < NDR <= 90:
            return 25 + (NDR - 80) / (90 - 80) * 25
        elif 90 < NDR <= 110:
            return 50 + (NDR - 90) / (110 - 90) * 25
        elif 110 < NDR <= 130:
            return 75 + (NDR - 110) / (130 - 110) * 25
        else:
            return 100
       
    return 0


def calR40(arrScale, R40):

    if arrScale == '<$10M' or arrScale == '$10-$25M':
        return 0

    elif arrScale == '$25-$50M':
        
        if R40 < 10:
            return 0

        if 10 <= R40 <= 20:
            return (R40 - 10) / (20 - 10) * 25
        elif 20 < R40 <= 30:
            return 25 + (R40 - 20) / (30 - 20) * 25
        elif 30 < R40 <= 40:
            return 50 + (R40 - 30) / (40 - 30) * 25
        elif 40 < R40 <= 60:
            return 75 + (R40 - 40) / (60 - 40) * 25
        else:
            return 100
       
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

        if NMN < 0.2:
            return 0
    
        if 0.2 <= NMN <= 0.5:
            return (NMN - 0.2) / (0.5 - 0.2) * 25
        elif 0.5 < NMN <= 0.8:
            return 25 + (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.4:
            return 50 + (NMN - 0.8) / (1.4 - 0.8) * 25
        elif 1 < NMN <= 1.3:
            return 75 + (NMN - 1.4) / (2.4 - 1.4) * 25
        else:
            return 100
    
    elif arrScale == '$10-$25M':

        if NMN < 0.2:
            return 0
    
        if 0.2 <= NMN <= 0.5:
            return (NMN - 0.2) / (0.5 - 0.2) * 25
        elif 0.5 < NMN <= 0.8:
            return 25 + (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.4:
            return 50 + (NMN - 0.8) / (1.4 - 0.8) * 25
        elif 1 < NMN <= 1.3:
            return 75 + (NMN - 1.4) / (2.4 - 1.4) * 25
        else:
            return 100


    elif arrScale == '$25-$50M':

        if NMN < 0.2:
            return 0
    
        if 0.2 <= NMN <= 0.5:
            return (NMN - 0.2) / (0.5 - 0.2) * 25
        elif 0.5 < NMN <= 0.8:
            return 25 + (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.4:
            return 50 + (NMN - 0.8) / (1.4 - 0.8) * 25
        elif 1 < NMN <= 1.3:
            return 75 + (NMN - 1.4) / (2.4 - 1.4) * 25
        else:
            return 100
       
    elif arrScale == '$50-$100M':

        if NMN < 0.2:
            return 0
    
        if 0.2 <= NMN <= 0.5:
            return (NMN - 0.2) / (0.5 - 0.2) * 25
        elif 0.5 < NMN <= 0.8:
            return 25 + (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.4:
            return 50 + (NMN - 0.8) / (1.4 - 0.8) * 25
        elif 1 < NMN <= 1.3:
            return 75 + (NMN - 1.4) / (2.4 - 1.4) * 25
        else:
            return 100
       
    elif arrScale == '$100M+':

        if NMN < 0.2:
            return 0
    
        if 0.2 <= NMN <= 0.5:
            return (NMN - 0.2) / (0.5 - 0.2) * 25
        elif 0.5 < NMN <= 0.8:
            return 25 + (NMN - 0.5) / (0.8 - 0.5) * 25
        elif 0.8 < NMN <= 1.4:
            return 50 + (NMN - 0.8) / (1.4 - 0.8) * 25
        elif 1 < NMN <= 1.3:
            return 75 + (NMN - 1.4) / (2.4 - 1.4) * 25
        else:
            return 100
       
    return 0

def calARRFTE(arrScale, ARRFTE):

    if arrScale == '<$10M':

        if ARRFTE < 30000:
            return 0
    
        if 30000 <= ARRFTE <= 43000:
            return (ARRFTE - 30000) / (43000 - 30000) * 25
        elif 43000 < ARRFTE <= 55000:
            return 25 + (ARRFTE - 43000) / (55000 - 43000) * 25
        elif 55000 < ARRFTE <= 68000:
            return 50 + (ARRFTE - 55000) / (68000 - 55000) * 25
        elif 68000 < ARRFTE <= 80000:
            return 75 + (ARRFTE - 68000) / (80000 - 68000) * 25
        else:
            return 100
    
    elif arrScale == '$10-$25M':

        if ARRFTE < 25000:
            return 0
    
        if 25000 <= ARRFTE <= 50000:
            return (ARRFTE - 25000) / (50000 - 25000) * 25
        elif 50000 < ARRFTE <= 75000:
            return 25 + (ARRFTE - 50000) / (75000 - 50000) * 25
        elif 75000 < ARRFTE <= 100000:
            return 50 + (ARRFTE - 75000) / (100000 - 75000) * 25
        elif 100000 < ARRFTE <= 125000:
            return 75 + (ARRFTE - 100000) / (125000 - 100000) * 25
        else:
            return 100

    elif arrScale == '$25-$50M':

        if ARRFTE < 50000:
            return 0
    
        if 50000 <= ARRFTE <= 75000:
            return (ARRFTE - 50000) / (75000 - 50000) * 25
        elif 75000 < ARRFTE <= 100000:
            return 25 + (ARRFTE - 75000) / (100000 - 75000) * 25
        elif 100000 < ARRFTE <= 125000:
            return 50 + (ARRFTE - 100000) / (125000 - 100000) * 25
        elif 125000 < ARRFTE <= 150000:
            return 75 + (ARRFTE - 125000) / (150000 - 125000) * 25
        else:
            return 100

       
    elif arrScale == '$50-$100M':

        if ARRFTE < 750000:
            return 0
    
        if 75000 <= ARRFTE <= 100000:
            return (ARRFTE - 75000) / (75000 - 100000) * 25
        elif 100000 < ARRFTE <= 125000:
            return 25 + (ARRFTE - 100000) / (125000 - 100000) * 25
        elif 125000 < ARRFTE <= 150000:
            return 50 + (ARRFTE - 125000) / (150000 - 125000) * 25
        elif 150000 < ARRFTE <= 175000:
            return 75 + (ARRFTE - 150000) / (175000 - 150000) * 25
        else:
            return 100



       
    elif arrScale == '$100M+':

        if ARRFTE < 75000:
            return 0
    
        if 75000 <= ARRFTE <= 100000:
            return (ARRFTE - 30000) / (43000 - 30000) * 25
        elif 43000 < ARRFTE <= 55000:
            return 25 + (ARRFTE - 43000) / (55000 - 43000) * 25
        elif 55000 < ARRFTE <= 68000:
            return 50 + (ARRFTE - 55000) / (68000 - 55000) * 25
        elif 68000 < ARRFTE <= 80000:
            return 75 + (ARRFTE - 68000) / (80000 - 68000) * 25
        else:
            return 100
       
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
        elif 0.6 < burnRate <= 0.8:
            return 75 + (burnRate - 0.6) / (0.8 - 0.6) * 25
        else:
            return 100

    elif arrScale == '$10-$25M':

        if not burnRate:
            return 0

        if  burnRate <= 0.2:
            return burnRate / 0.2 * 25
        elif 0.2 < burnRate <= 0.4:
            return 25 + (burnRate - 0.2) / (0.4 - 0.2) * 25
        elif 0.4 < burnRate <= 0.6:
            return 50 + (burnRate - 0.4) / (0.6 - 0.4) * 25
        elif 0.6 < burnRate <= 0.8:
            return 75 + (burnRate - 0.6) / (0.8 - 0.6) * 25
        else:
            return 100

    elif arrScale == '$25-$50M':

        if burnRate < 0.2:
            return 0

        if  0.2 <= burnRate <= 0.4:
            return (burnRate - 0.2) / (0.4 - 0.2) * 25
        elif 0.4 < burnRate <= 0.6:
            return 25 + (burnRate - 0.4) / (0.6 - 0.4) * 25
        elif 0.6 < burnRate <= 0.8:
            return 50 + (burnRate - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < burnRate <= 1.0:
            return 75 + (burnRate - 0.8) / (1.0 - 0.8) * 25
        else:
            return 100

    elif arrScale == '$50-$100M':

        if burnRate < 0.4:
            return 0

        if  0.4 <= burnRate <= 0.6:
            return (burnRate - 0.4) / (0.6 - 0.4) * 25
        elif 0.6 < burnRate <= 0.8:
            return 25 + (burnRate - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < burnRate <= 1.0:
            return 50 + (burnRate - 0.8) / (1.0 - 0.8) * 25
        elif 1.0 < burnRate <= 1.2:
            return 75 + (burnRate - 1.0) / (1.2 - 1.0) * 25
        else:
            return 100
       
    elif arrScale == '$100M+':

        if burnRate < 0.6:
            return 0

        if  0.6 <= burnRate <= 0.8:
            return (burnRate - 0.6) / (0.8 - 0.6) * 25
        elif 0.8 < burnRate <= 1.0:
            return 25 + (burnRate - 0.8) / (1.0 - 0.8) * 25
        elif 1.0 < burnRate <= 1.2:
            return 50 + (burnRate - 1.0) / (1.2 - 1.0) * 25
        elif 1.2 < burnRate <= 1.4:
            return 75 + (burnRate - 1.2) / (1.4 - 1.2) * 25
        else:
            return 100
       
    return 0

st.metric(label = 'ARR scale', value = arrScale)
# st.text('You selected: ' + arrScale)
# st.write('You selected:')

arrGrowth = st.number_input('ARR Growth (in %)', step = 1)
st.metric(label = 'ARR Growth Score', value = round(calArrGrowth(arrScale, arrGrowth),2))
# st.text('ARR Growth Score is ' + str(calArrGrowth(arrScale, arrGrowth)))
st.write('ARR Growth is ', int(arrGrowth), '%')

NDR = st.number_input('NDR (in %)', step = 1)
st.metric(label = 'Net Dollar Retention Score', value = round(calNDR(arrScale, NDR),2))
# st.text('Net Dollar Retention Score is ' + str(calNDR(arrScale, NDR)))
st.write('Net Dollar Retention is ', int(NDR), '%')

R40 = st.number_input('Rule of 40 (in %)')
st.metric(label = 'Rule of 40 Score' , value = round(calR40(arrScale, R40),2))
# st.text('Rule of 40 Score is ' +  str(calR40(arrScale,R40)))
st.write('Rule of 40 is ', R40)

NMN = st.number_input('Net Magic Number')
st.metric(label = 'Net Magic Number Score', value = round(calNMN(arrScale, NMN),2))
# st.write('Net Magic Number Score is ', calNMN(arrScale,NMN))
st.write('Net Magic Number is ', NMN)

ARRFTE = st.number_input('ARR per FTE (in k)') * 1000
st.metric(label = 'ARR per FTE Score', value = round(calARRFTE(arrScale, ARRFTE)))
st.write('ARR per FTE is ', ARRFTE,'k')

burnRate = st.number_input('Burn Rate', max_value=1.0)
st.metric(label = 'Burn Rate Score ', value = round(calBurnRate(arrScale, burnRate),2))
st.write('Burn Rate is ', round(burnRate, 2))

score = int(calScore(arrScale, arrGrowth,NDR,R40,NMN,ARRFTE,burnRate))



# st.write('Composite score is', calScore(arrScale, arrGrowth,NDR,R40,NMN,ARRFTE,burnRate))
st.header('Composite Score is ' + str(score))

if score >= 75:
    st.header('Passing')
else:
    st.header('No Passing')



# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
