def Sensitivity_direct(States,Parameters):
    EP = States['EP']
    En = States['En']
    Es = States['Es']
    EsQ = States['EsQ']
    PP = States['PP']
    PQ = States['PQ']
    SA = States['SA']
    SB = States['SB']

    k1 = Parameters['k1']
    k1m = Parameters['k1m']
    k2 = Parameters['k2']
    k2m = Parameters['k2m']
    k3 = Parameters['k3']
    k3m = Parameters['k3m']
    k4 = Parameters['k4']
    k4m = Parameters['k4m']

    dEPdk1 = 0
    dEPdk1m = 0
    dEPdk2 = 0
    dEPdk2m = 0
    dEPdk3 = 0
    dEPdk3m = 0
    dEPdk4 = En*PP*k4
    dEPdk4m = -EP*k4m
    dEndk1 = -En*SA*k1
    dEndk1m = Es*PP*k1m
    dEndk2 = Es*SB*k2
    dEndk2m = -En*PQ*k2m
    dEndk3 = 0
    dEndk3m = 0
    dEndk4 = k4*(EP - En*PP)
    dEndk4m = 0
    dEsdk1 = En*SA*k1
    dEsdk1m = -Es*PP*k1m
    dEsdk2 = -Es*SB*k2
    dEsdk2m = En*PQ*k2m
    dEsdk3 = k3*(-Es + EsQ)
    dEsdk3m = 0
    dEsdk4 = 0
    dEsdk4m = 0
    dEsQdk1 = 0
    dEsQdk1m = 0
    dEsQdk2 = 0
    dEsQdk2m = 0
    dEsQdk3 = Es*PQ*k3
    dEsQdk3m = -EsQ*k3m
    dEsQdk4 = 0
    dEsQdk4m = 0
    dPPdk1 = En*SA*k1
    dPPdk1m = -Es*PP*k1m
    dPPdk2 = 0
    dPPdk2m = 0
    dPPdk3 = 0
    dPPdk3m = 0
    dPPdk4 = -En*PP*k4
    dPPdk4m = EP*k4m
    dPQdk1 = 0
    dPQdk1m = 0
    dPQdk2 = En*SB*k2
    dPQdk2m = -En*PQ*k2m
    dPQdk3 = -Es*PQ*k3
    dPQdk3m = EsQ*k3m
    dPQdk4 = 0
    dPQdk4m = 0
    dSAdk1 = -En*SA*k1
    dSAdk1m = Es*PP*k1m
    dSAdk2 = 0
    dSAdk2m = 0
    dSAdk3 = 0
    dSAdk3m = 0
    dSAdk4 = 0
    dSAdk4m = 0
    dSBdk1 = 0
    dSBdk1m = 0
    dSBdk2 = -Es*SB*k2
    dSBdk2m = En*PQ*k2m
    dSBdk3 = 0
    dSBdk3m = 0
    dSBdk4 = 0
    dSBdk4m = 0
    Output = {}
    Output['dEPdk1'] = dEPdk1
    Output['dEPdk1m'] = dEPdk1m
    Output['dEPdk2'] = dEPdk2
    Output['dEPdk2m'] = dEPdk2m
    Output['dEPdk3'] = dEPdk3
    Output['dEPdk3m'] = dEPdk3m
    Output['dEPdk4'] = dEPdk4
    Output['dEPdk4m'] = dEPdk4m
    Output['dEndk1'] = dEndk1
    Output['dEndk1m'] = dEndk1m
    Output['dEndk2'] = dEndk2
    Output['dEndk2m'] = dEndk2m
    Output['dEndk3'] = dEndk3
    Output['dEndk3m'] = dEndk3m
    Output['dEndk4'] = dEndk4
    Output['dEndk4m'] = dEndk4m
    Output['dEsdk1'] = dEsdk1
    Output['dEsdk1m'] = dEsdk1m
    Output['dEsdk2'] = dEsdk2
    Output['dEsdk2m'] = dEsdk2m
    Output['dEsdk3'] = dEsdk3
    Output['dEsdk3m'] = dEsdk3m
    Output['dEsdk4'] = dEsdk4
    Output['dEsdk4m'] = dEsdk4m
    Output['dEsQdk1'] = dEsQdk1
    Output['dEsQdk1m'] = dEsQdk1m
    Output['dEsQdk2'] = dEsQdk2
    Output['dEsQdk2m'] = dEsQdk2m
    Output['dEsQdk3'] = dEsQdk3
    Output['dEsQdk3m'] = dEsQdk3m
    Output['dEsQdk4'] = dEsQdk4
    Output['dEsQdk4m'] = dEsQdk4m
    Output['dPPdk1'] = dPPdk1
    Output['dPPdk1m'] = dPPdk1m
    Output['dPPdk2'] = dPPdk2
    Output['dPPdk2m'] = dPPdk2m
    Output['dPPdk3'] = dPPdk3
    Output['dPPdk3m'] = dPPdk3m
    Output['dPPdk4'] = dPPdk4
    Output['dPPdk4m'] = dPPdk4m
    Output['dPQdk1'] = dPQdk1
    Output['dPQdk1m'] = dPQdk1m
    Output['dPQdk2'] = dPQdk2
    Output['dPQdk2m'] = dPQdk2m
    Output['dPQdk3'] = dPQdk3
    Output['dPQdk3m'] = dPQdk3m
    Output['dPQdk4'] = dPQdk4
    Output['dPQdk4m'] = dPQdk4m
    Output['dSAdk1'] = dSAdk1
    Output['dSAdk1m'] = dSAdk1m
    Output['dSAdk2'] = dSAdk2
    Output['dSAdk2m'] = dSAdk2m
    Output['dSAdk3'] = dSAdk3
    Output['dSAdk3m'] = dSAdk3m
    Output['dSAdk4'] = dSAdk4
    Output['dSAdk4m'] = dSAdk4m
    Output['dSBdk1'] = dSBdk1
    Output['dSBdk1m'] = dSBdk1m
    Output['dSBdk2'] = dSBdk2
    Output['dSBdk2m'] = dSBdk2m
    Output['dSBdk3'] = dSBdk3
    Output['dSBdk3m'] = dSBdk3m
    Output['dSBdk4'] = dSBdk4
    Output['dSBdk4m'] = dSBdk4m
    return Output

def Sensitivity_indirect(States,Parameters):
    EP = States['EP']
    En = States['En']
    Es = States['Es']
    EsQ = States['EsQ']
    PP = States['PP']
    PQ = States['PQ']
    SA = States['SA']
    SB = States['SB']

    k1 = Parameters['k1']
    k1m = Parameters['k1m']
    k2 = Parameters['k2']
    k2m = Parameters['k2m']
    k3 = Parameters['k3']
    k3m = Parameters['k3m']
    k4 = Parameters['k4']
    k4m = Parameters['k4m']

    dEPdEPXdEPdk1 = 0
    dEPdEPXdEPdk1m = 0
    dEPdEPXdEPdk2 = 0
    dEPdEPXdEPdk2m = 0
    dEPdEPXdEPdk3 = 0
    dEPdEPXdEPdk3m = 0
    dEPdEPXdEPdk4 = En*PP*k4
    dEPdEPXdEPdk4m = -(k4*En*PP-k4m*EP)*k4m
    dEndEPXdEPdk1 = -En*SA*k1
    dEndEPXdEPdk1m = Es*PP*k1m
    dEndEPXdEPdk2 = Es*SB*k2
    dEndEPXdEPdk2m = -En*PQ*k2m
    dEndEPXdEPdk3 = 0
    dEndEPXdEPdk3m = 0
    dEndEPXdEPdk4 = k4*((k4*En*PP-k4m*EP) - En*PP)
    dEndEPXdEPdk4m = 0
    dEsdEPXdEPdk1 = En*SA*k1
    dEsdEPXdEPdk1m = -Es*PP*k1m
    dEsdEPXdEPdk2 = -Es*SB*k2
    dEsdEPXdEPdk2m = En*PQ*k2m
    dEsdEPXdEPdk3 = k3*(-Es + EsQ)
    dEsdEPXdEPdk3m = 0
    dEsdEPXdEPdk4 = 0
    dEsdEPXdEPdk4m = 0
    dEsQdEPXdEPdk1 = 0
    dEsQdEPXdEPdk1m = 0
    dEsQdEPXdEPdk2 = 0
    dEsQdEPXdEPdk2m = 0
    dEsQdEPXdEPdk3 = Es*PQ*k3
    dEsQdEPXdEPdk3m = -EsQ*k3m
    dEsQdEPXdEPdk4 = 0
    dEsQdEPXdEPdk4m = 0
    dPPdEPXdEPdk1 = En*SA*k1
    dPPdEPXdEPdk1m = -Es*PP*k1m
    dPPdEPXdEPdk2 = 0
    dPPdEPXdEPdk2m = 0
    dPPdEPXdEPdk3 = 0
    dPPdEPXdEPdk3m = 0
    dPPdEPXdEPdk4 = -En*PP*k4
    dPPdEPXdEPdk4m = (k4*En*PP-k4m*EP)*k4m
    dPQdEPXdEPdk1 = 0
    dPQdEPXdEPdk1m = 0
    dPQdEPXdEPdk2 = En*SB*k2
    dPQdEPXdEPdk2m = -En*PQ*k2m
    dPQdEPXdEPdk3 = -Es*PQ*k3
    dPQdEPXdEPdk3m = EsQ*k3m
    dPQdEPXdEPdk4 = 0
    dPQdEPXdEPdk4m = 0
    dSAdEPXdEPdk1 = -En*SA*k1
    dSAdEPXdEPdk1m = Es*PP*k1m
    dSAdEPXdEPdk2 = 0
    dSAdEPXdEPdk2m = 0
    dSAdEPXdEPdk3 = 0
    dSAdEPXdEPdk3m = 0
    dSAdEPXdEPdk4 = 0
    dSAdEPXdEPdk4m = 0
    dSBdEPXdEPdk1 = 0
    dSBdEPXdEPdk1m = 0
    dSBdEPXdEPdk2 = -Es*SB*k2
    dSBdEPXdEPdk2m = En*PQ*k2m
    dSBdEPXdEPdk3 = 0
    dSBdEPXdEPdk3m = 0
    dSBdEPXdEPdk4 = 0
    dSBdEPXdEPdk4m = 0
    dEPdEnXdEndk1 = 0
    dEPdEnXdEndk1m = 0
    dEPdEnXdEndk2 = 0
    dEPdEnXdEndk2m = 0
    dEPdEnXdEndk3 = 0
    dEPdEnXdEndk3m = 0
    dEPdEnXdEndk4 = (k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PP*k4
    dEPdEnXdEndk4m = -EP*k4m
    dEndEnXdEndk1 = -(k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*SA*k1
    dEndEnXdEndk1m = Es*PP*k1m
    dEndEnXdEndk2 = Es*SB*k2
    dEndEnXdEndk2m = -(k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PQ*k2m
    dEndEnXdEndk3 = 0
    dEndEnXdEndk3m = 0
    dEndEnXdEndk4 = k4*(-(k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PP + EP)
    dEndEnXdEndk4m = 0
    dEsdEnXdEndk1 = (k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*SA*k1
    dEsdEnXdEndk1m = -Es*PP*k1m
    dEsdEnXdEndk2 = -Es*SB*k2
    dEsdEnXdEndk2m = (k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PQ*k2m
    dEsdEnXdEndk3 = k3*(-Es + EsQ)
    dEsdEnXdEndk3m = 0
    dEsdEnXdEndk4 = 0
    dEsdEnXdEndk4m = 0
    dEsQdEnXdEndk1 = 0
    dEsQdEnXdEndk1m = 0
    dEsQdEnXdEndk2 = 0
    dEsQdEnXdEndk2m = 0
    dEsQdEnXdEndk3 = Es*PQ*k3
    dEsQdEnXdEndk3m = -EsQ*k3m
    dEsQdEnXdEndk4 = 0
    dEsQdEnXdEndk4m = 0
    dPPdEnXdEndk1 = (k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*SA*k1
    dPPdEnXdEndk1m = -Es*PP*k1m
    dPPdEnXdEndk2 = 0
    dPPdEnXdEndk2m = 0
    dPPdEnXdEndk3 = 0
    dPPdEnXdEndk3m = 0
    dPPdEnXdEndk4 = -(k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PP*k4
    dPPdEnXdEndk4m = EP*k4m
    dPQdEnXdEndk1 = 0
    dPQdEnXdEndk1m = 0
    dPQdEnXdEndk2 = (k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*SB*k2
    dPQdEnXdEndk2m = -(k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PQ*k2m
    dPQdEnXdEndk3 = -Es*PQ*k3
    dPQdEnXdEndk3m = EsQ*k3m
    dPQdEnXdEndk4 = 0
    dPQdEnXdEndk4m = 0
    dSAdEnXdEndk1 = -(k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*SA*k1
    dSAdEnXdEndk1m = Es*PP*k1m
    dSAdEnXdEndk2 = 0
    dSAdEnXdEndk2m = 0
    dSAdEnXdEndk3 = 0
    dSAdEnXdEndk3m = 0
    dSAdEnXdEndk4 = 0
    dSAdEnXdEndk4m = 0
    dSBdEnXdEndk1 = 0
    dSBdEnXdEndk1m = 0
    dSBdEnXdEndk2 = -Es*SB*k2
    dSBdEnXdEndk2m = (k1m*Es*PP+k4*EP+k2*Es*SB-k1*En*SA-k4*En*PP-k2m*En*PQ)*PQ*k2m
    dSBdEnXdEndk3 = 0
    dSBdEnXdEndk3m = 0
    dSBdEnXdEndk4 = 0
    dSBdEnXdEndk4m = 0
    dEPdEsXdEsdk1 = 0
    dEPdEsXdEsdk1m = 0
    dEPdEsXdEsdk2 = 0
    dEPdEsXdEsdk2m = 0
    dEPdEsXdEsdk3 = 0
    dEPdEsXdEsdk3m = 0
    dEPdEsXdEsdk4 = En*PP*k4
    dEPdEsXdEsdk4m = -EP*k4m
    dEndEsXdEsdk1 = -En*SA*k1
    dEndEsXdEsdk1m = (-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*PP*k1m
    dEndEsXdEsdk2 = (-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*SB*k2
    dEndEsXdEsdk2m = -En*PQ*k2m
    dEndEsXdEsdk3 = 0
    dEndEsXdEsdk3m = 0
    dEndEsXdEsdk4 = k4*(EP - En*PP)
    dEndEsXdEsdk4m = 0
    dEsdEsXdEsdk1 = En*SA*k1
    dEsdEsXdEsdk1m = -(-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*PP*k1m
    dEsdEsXdEsdk2 = -(-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*SB*k2
    dEsdEsXdEsdk2m = En*PQ*k2m
    dEsdEsXdEsdk3 = k3*(-(-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ) + EsQ)
    dEsdEsXdEsdk3m = 0
    dEsdEsXdEsdk4 = 0
    dEsdEsXdEsdk4m = 0
    dEsQdEsXdEsdk1 = 0
    dEsQdEsXdEsdk1m = 0
    dEsQdEsXdEsdk2 = 0
    dEsQdEsXdEsdk2m = 0
    dEsQdEsXdEsdk3 = (-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*PQ*k3
    dEsQdEsXdEsdk3m = -EsQ*k3m
    dEsQdEsXdEsdk4 = 0
    dEsQdEsXdEsdk4m = 0
    dPPdEsXdEsdk1 = En*SA*k1
    dPPdEsXdEsdk1m = -(-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*PP*k1m
    dPPdEsXdEsdk2 = 0
    dPPdEsXdEsdk2m = 0
    dPPdEsXdEsdk3 = 0
    dPPdEsXdEsdk3m = 0
    dPPdEsXdEsdk4 = -En*PP*k4
    dPPdEsXdEsdk4m = EP*k4m
    dPQdEsXdEsdk1 = 0
    dPQdEsXdEsdk1m = 0
    dPQdEsXdEsdk2 = En*SB*k2
    dPQdEsXdEsdk2m = -En*PQ*k2m
    dPQdEsXdEsdk3 = -(-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*PQ*k3
    dPQdEsXdEsdk3m = EsQ*k3m
    dPQdEsXdEsdk4 = 0
    dPQdEsXdEsdk4m = 0
    dSAdEsXdEsdk1 = -En*SA*k1
    dSAdEsXdEsdk1m = (-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*PP*k1m
    dSAdEsXdEsdk2 = 0
    dSAdEsXdEsdk2m = 0
    dSAdEsXdEsdk3 = 0
    dSAdEsXdEsdk3m = 0
    dSAdEsXdEsdk4 = 0
    dSAdEsXdEsdk4m = 0
    dSBdEsXdEsdk1 = 0
    dSBdEsXdEsdk1m = 0
    dSBdEsXdEsdk2 = -(-k1m*Es*PP+k3*EsQ-k2*Es*SB+k1*En*SA-k3*Es+k2m*En*PQ)*SB*k2
    dSBdEsXdEsdk2m = En*PQ*k2m
    dSBdEsXdEsdk3 = 0
    dSBdEsXdEsdk3m = 0
    dSBdEsXdEsdk4 = 0
    dSBdEsXdEsdk4m = 0
    dEPdEsQXdEsQdk1 = 0
    dEPdEsQXdEsQdk1m = 0
    dEPdEsQXdEsQdk2 = 0
    dEPdEsQXdEsQdk2m = 0
    dEPdEsQXdEsQdk3 = 0
    dEPdEsQXdEsQdk3m = 0
    dEPdEsQXdEsQdk4 = En*PP*k4
    dEPdEsQXdEsQdk4m = -EP*k4m
    dEndEsQXdEsQdk1 = -En*SA*k1
    dEndEsQXdEsQdk1m = Es*PP*k1m
    dEndEsQXdEsQdk2 = Es*SB*k2
    dEndEsQXdEsQdk2m = -En*PQ*k2m
    dEndEsQXdEsQdk3 = 0
    dEndEsQXdEsQdk3m = 0
    dEndEsQXdEsQdk4 = k4*(EP - En*PP)
    dEndEsQXdEsQdk4m = 0
    dEsdEsQXdEsQdk1 = En*SA*k1
    dEsdEsQXdEsQdk1m = -Es*PP*k1m
    dEsdEsQXdEsQdk2 = -Es*SB*k2
    dEsdEsQXdEsQdk2m = En*PQ*k2m
    dEsdEsQXdEsQdk3 = k3*((k3*Es*PQ-k3m*EsQ) - Es)
    dEsdEsQXdEsQdk3m = 0
    dEsdEsQXdEsQdk4 = 0
    dEsdEsQXdEsQdk4m = 0
    dEsQdEsQXdEsQdk1 = 0
    dEsQdEsQXdEsQdk1m = 0
    dEsQdEsQXdEsQdk2 = 0
    dEsQdEsQXdEsQdk2m = 0
    dEsQdEsQXdEsQdk3 = Es*PQ*k3
    dEsQdEsQXdEsQdk3m = -(k3*Es*PQ-k3m*EsQ)*k3m
    dEsQdEsQXdEsQdk4 = 0
    dEsQdEsQXdEsQdk4m = 0
    dPPdEsQXdEsQdk1 = En*SA*k1
    dPPdEsQXdEsQdk1m = -Es*PP*k1m
    dPPdEsQXdEsQdk2 = 0
    dPPdEsQXdEsQdk2m = 0
    dPPdEsQXdEsQdk3 = 0
    dPPdEsQXdEsQdk3m = 0
    dPPdEsQXdEsQdk4 = -En*PP*k4
    dPPdEsQXdEsQdk4m = EP*k4m
    dPQdEsQXdEsQdk1 = 0
    dPQdEsQXdEsQdk1m = 0
    dPQdEsQXdEsQdk2 = En*SB*k2
    dPQdEsQXdEsQdk2m = -En*PQ*k2m
    dPQdEsQXdEsQdk3 = -Es*PQ*k3
    dPQdEsQXdEsQdk3m = (k3*Es*PQ-k3m*EsQ)*k3m
    dPQdEsQXdEsQdk4 = 0
    dPQdEsQXdEsQdk4m = 0
    dSAdEsQXdEsQdk1 = -En*SA*k1
    dSAdEsQXdEsQdk1m = Es*PP*k1m
    dSAdEsQXdEsQdk2 = 0
    dSAdEsQXdEsQdk2m = 0
    dSAdEsQXdEsQdk3 = 0
    dSAdEsQXdEsQdk3m = 0
    dSAdEsQXdEsQdk4 = 0
    dSAdEsQXdEsQdk4m = 0
    dSBdEsQXdEsQdk1 = 0
    dSBdEsQXdEsQdk1m = 0
    dSBdEsQXdEsQdk2 = -Es*SB*k2
    dSBdEsQXdEsQdk2m = En*PQ*k2m
    dSBdEsQXdEsQdk3 = 0
    dSBdEsQXdEsQdk3m = 0
    dSBdEsQXdEsQdk4 = 0
    dSBdEsQXdEsQdk4m = 0
    dEPdPPXdPPdk1 = 0
    dEPdPPXdPPdk1m = 0
    dEPdPPXdPPdk2 = 0
    dEPdPPXdPPdk2m = 0
    dEPdPPXdPPdk3 = 0
    dEPdPPXdPPdk3m = 0
    dEPdPPXdPPdk4 = (k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*En*k4
    dEPdPPXdPPdk4m = -EP*k4m
    dEndPPXdPPdk1 = -En*SA*k1
    dEndPPXdPPdk1m = (k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*Es*k1m
    dEndPPXdPPdk2 = Es*SB*k2
    dEndPPXdPPdk2m = -En*PQ*k2m
    dEndPPXdPPdk3 = 0
    dEndPPXdPPdk3m = 0
    dEndPPXdPPdk4 = k4*(-(k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*En + EP)
    dEndPPXdPPdk4m = 0
    dEsdPPXdPPdk1 = En*SA*k1
    dEsdPPXdPPdk1m = -(k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*Es*k1m
    dEsdPPXdPPdk2 = -Es*SB*k2
    dEsdPPXdPPdk2m = En*PQ*k2m
    dEsdPPXdPPdk3 = k3*(-Es + EsQ)
    dEsdPPXdPPdk3m = 0
    dEsdPPXdPPdk4 = 0
    dEsdPPXdPPdk4m = 0
    dEsQdPPXdPPdk1 = 0
    dEsQdPPXdPPdk1m = 0
    dEsQdPPXdPPdk2 = 0
    dEsQdPPXdPPdk2m = 0
    dEsQdPPXdPPdk3 = Es*PQ*k3
    dEsQdPPXdPPdk3m = -EsQ*k3m
    dEsQdPPXdPPdk4 = 0
    dEsQdPPXdPPdk4m = 0
    dPPdPPXdPPdk1 = En*SA*k1
    dPPdPPXdPPdk1m = -(k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*Es*k1m
    dPPdPPXdPPdk2 = 0
    dPPdPPXdPPdk2m = 0
    dPPdPPXdPPdk3 = 0
    dPPdPPXdPPdk3m = 0
    dPPdPPXdPPdk4 = -(k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*En*k4
    dPPdPPXdPPdk4m = EP*k4m
    dPQdPPXdPPdk1 = 0
    dPQdPPXdPPdk1m = 0
    dPQdPPXdPPdk2 = En*SB*k2
    dPQdPPXdPPdk2m = -En*PQ*k2m
    dPQdPPXdPPdk3 = -Es*PQ*k3
    dPQdPPXdPPdk3m = EsQ*k3m
    dPQdPPXdPPdk4 = 0
    dPQdPPXdPPdk4m = 0
    dSAdPPXdPPdk1 = -En*SA*k1
    dSAdPPXdPPdk1m = (k1*En*SA-k1m*Es*PP-k4*En*PP+k4m*EP)*Es*k1m
    dSAdPPXdPPdk2 = 0
    dSAdPPXdPPdk2m = 0
    dSAdPPXdPPdk3 = 0
    dSAdPPXdPPdk3m = 0
    dSAdPPXdPPdk4 = 0
    dSAdPPXdPPdk4m = 0
    dSBdPPXdPPdk1 = 0
    dSBdPPXdPPdk1m = 0
    dSBdPPXdPPdk2 = -Es*SB*k2
    dSBdPPXdPPdk2m = En*PQ*k2m
    dSBdPPXdPPdk3 = 0
    dSBdPPXdPPdk3m = 0
    dSBdPPXdPPdk4 = 0
    dSBdPPXdPPdk4m = 0
    dEPdPQXdPQdk1 = 0
    dEPdPQXdPQdk1m = 0
    dEPdPQXdPQdk2 = 0
    dEPdPQXdPQdk2m = 0
    dEPdPQXdPQdk3 = 0
    dEPdPQXdPQdk3m = 0
    dEPdPQXdPQdk4 = En*PP*k4
    dEPdPQXdPQdk4m = -EP*k4m
    dEndPQXdPQdk1 = -En*SA*k1
    dEndPQXdPQdk1m = Es*PP*k1m
    dEndPQXdPQdk2 = Es*SB*k2
    dEndPQXdPQdk2m = -(k2*En*SB-k2m*En*PQ-k3*Es*PQ+k3m*EsQ)*En*k2m
    dEndPQXdPQdk3 = 0
    dEndPQXdPQdk3m = 0
    dEndPQXdPQdk4 = k4*(EP - En*PP)
    dEndPQXdPQdk4m = 0
    dEsdPQXdPQdk1 = En*SA*k1
    dEsdPQXdPQdk1m = -Es*PP*k1m
    dEsdPQXdPQdk2 = -Es*SB*k2
    dEsdPQXdPQdk2m = (k2*En*SB-k2m*En*PQ-k3*Es*PQ+k3m*EsQ)*En*k2m
    dEsdPQXdPQdk3 = k3*(-Es + EsQ)
    dEsdPQXdPQdk3m = 0
    dEsdPQXdPQdk4 = 0
    dEsdPQXdPQdk4m = 0
    dEsQdPQXdPQdk1 = 0
    dEsQdPQXdPQdk1m = 0
    dEsQdPQXdPQdk2 = 0
    dEsQdPQXdPQdk2m = 0
    dEsQdPQXdPQdk3 = (k2*En*SB-k2m*En*PQ-k3*Es*PQ+k3m*EsQ)*Es*k3
    dEsQdPQXdPQdk3m = -EsQ*k3m
    dEsQdPQXdPQdk4 = 0
    dEsQdPQXdPQdk4m = 0
    dPPdPQXdPQdk1 = En*SA*k1
    dPPdPQXdPQdk1m = -Es*PP*k1m
    dPPdPQXdPQdk2 = 0
    dPPdPQXdPQdk2m = 0
    dPPdPQXdPQdk3 = 0
    dPPdPQXdPQdk3m = 0
    dPPdPQXdPQdk4 = -En*PP*k4
    dPPdPQXdPQdk4m = EP*k4m
    dPQdPQXdPQdk1 = 0
    dPQdPQXdPQdk1m = 0
    dPQdPQXdPQdk2 = En*SB*k2
    dPQdPQXdPQdk2m = -(k2*En*SB-k2m*En*PQ-k3*Es*PQ+k3m*EsQ)*En*k2m
    dPQdPQXdPQdk3 = -(k2*En*SB-k2m*En*PQ-k3*Es*PQ+k3m*EsQ)*Es*k3
    dPQdPQXdPQdk3m = EsQ*k3m
    dPQdPQXdPQdk4 = 0
    dPQdPQXdPQdk4m = 0
    dSAdPQXdPQdk1 = -En*SA*k1
    dSAdPQXdPQdk1m = Es*PP*k1m
    dSAdPQXdPQdk2 = 0
    dSAdPQXdPQdk2m = 0
    dSAdPQXdPQdk3 = 0
    dSAdPQXdPQdk3m = 0
    dSAdPQXdPQdk4 = 0
    dSAdPQXdPQdk4m = 0
    dSBdPQXdPQdk1 = 0
    dSBdPQXdPQdk1m = 0
    dSBdPQXdPQdk2 = -Es*SB*k2
    dSBdPQXdPQdk2m = (k2*En*SB-k2m*En*PQ-k3*Es*PQ+k3m*EsQ)*En*k2m
    dSBdPQXdPQdk3 = 0
    dSBdPQXdPQdk3m = 0
    dSBdPQXdPQdk4 = 0
    dSBdPQXdPQdk4m = 0
    dEPdSAXdSAdk1 = 0
    dEPdSAXdSAdk1m = 0
    dEPdSAXdSAdk2 = 0
    dEPdSAXdSAdk2m = 0
    dEPdSAXdSAdk3 = 0
    dEPdSAXdSAdk3m = 0
    dEPdSAXdSAdk4 = En*PP*k4
    dEPdSAXdSAdk4m = -EP*k4m
    dEndSAXdSAdk1 = -(-k1*En*SA+k1m*Es*PP)*En*k1
    dEndSAXdSAdk1m = Es*PP*k1m
    dEndSAXdSAdk2 = Es*SB*k2
    dEndSAXdSAdk2m = -En*PQ*k2m
    dEndSAXdSAdk3 = 0
    dEndSAXdSAdk3m = 0
    dEndSAXdSAdk4 = k4*(EP - En*PP)
    dEndSAXdSAdk4m = 0
    dEsdSAXdSAdk1 = (-k1*En*SA+k1m*Es*PP)*En*k1
    dEsdSAXdSAdk1m = -Es*PP*k1m
    dEsdSAXdSAdk2 = -Es*SB*k2
    dEsdSAXdSAdk2m = En*PQ*k2m
    dEsdSAXdSAdk3 = k3*(-Es + EsQ)
    dEsdSAXdSAdk3m = 0
    dEsdSAXdSAdk4 = 0
    dEsdSAXdSAdk4m = 0
    dEsQdSAXdSAdk1 = 0
    dEsQdSAXdSAdk1m = 0
    dEsQdSAXdSAdk2 = 0
    dEsQdSAXdSAdk2m = 0
    dEsQdSAXdSAdk3 = Es*PQ*k3
    dEsQdSAXdSAdk3m = -EsQ*k3m
    dEsQdSAXdSAdk4 = 0
    dEsQdSAXdSAdk4m = 0
    dPPdSAXdSAdk1 = (-k1*En*SA+k1m*Es*PP)*En*k1
    dPPdSAXdSAdk1m = -Es*PP*k1m
    dPPdSAXdSAdk2 = 0
    dPPdSAXdSAdk2m = 0
    dPPdSAXdSAdk3 = 0
    dPPdSAXdSAdk3m = 0
    dPPdSAXdSAdk4 = -En*PP*k4
    dPPdSAXdSAdk4m = EP*k4m
    dPQdSAXdSAdk1 = 0
    dPQdSAXdSAdk1m = 0
    dPQdSAXdSAdk2 = En*SB*k2
    dPQdSAXdSAdk2m = -En*PQ*k2m
    dPQdSAXdSAdk3 = -Es*PQ*k3
    dPQdSAXdSAdk3m = EsQ*k3m
    dPQdSAXdSAdk4 = 0
    dPQdSAXdSAdk4m = 0
    dSAdSAXdSAdk1 = -(-k1*En*SA+k1m*Es*PP)*En*k1
    dSAdSAXdSAdk1m = Es*PP*k1m
    dSAdSAXdSAdk2 = 0
    dSAdSAXdSAdk2m = 0
    dSAdSAXdSAdk3 = 0
    dSAdSAXdSAdk3m = 0
    dSAdSAXdSAdk4 = 0
    dSAdSAXdSAdk4m = 0
    dSBdSAXdSAdk1 = 0
    dSBdSAXdSAdk1m = 0
    dSBdSAXdSAdk2 = -Es*SB*k2
    dSBdSAXdSAdk2m = En*PQ*k2m
    dSBdSAXdSAdk3 = 0
    dSBdSAXdSAdk3m = 0
    dSBdSAXdSAdk4 = 0
    dSBdSAXdSAdk4m = 0
    dEPdSBXdSBdk1 = 0
    dEPdSBXdSBdk1m = 0
    dEPdSBXdSBdk2 = 0
    dEPdSBXdSBdk2m = 0
    dEPdSBXdSBdk3 = 0
    dEPdSBXdSBdk3m = 0
    dEPdSBXdSBdk4 = En*PP*k4
    dEPdSBXdSBdk4m = -EP*k4m
    dEndSBXdSBdk1 = -En*SA*k1
    dEndSBXdSBdk1m = Es*PP*k1m
    dEndSBXdSBdk2 = (-k2*Es*SB+k2m*En*PQ)*Es*k2
    dEndSBXdSBdk2m = -En*PQ*k2m
    dEndSBXdSBdk3 = 0
    dEndSBXdSBdk3m = 0
    dEndSBXdSBdk4 = k4*(EP - En*PP)
    dEndSBXdSBdk4m = 0
    dEsdSBXdSBdk1 = En*SA*k1
    dEsdSBXdSBdk1m = -Es*PP*k1m
    dEsdSBXdSBdk2 = -(-k2*Es*SB+k2m*En*PQ)*Es*k2
    dEsdSBXdSBdk2m = En*PQ*k2m
    dEsdSBXdSBdk3 = k3*(-Es + EsQ)
    dEsdSBXdSBdk3m = 0
    dEsdSBXdSBdk4 = 0
    dEsdSBXdSBdk4m = 0
    dEsQdSBXdSBdk1 = 0
    dEsQdSBXdSBdk1m = 0
    dEsQdSBXdSBdk2 = 0
    dEsQdSBXdSBdk2m = 0
    dEsQdSBXdSBdk3 = Es*PQ*k3
    dEsQdSBXdSBdk3m = -EsQ*k3m
    dEsQdSBXdSBdk4 = 0
    dEsQdSBXdSBdk4m = 0
    dPPdSBXdSBdk1 = En*SA*k1
    dPPdSBXdSBdk1m = -Es*PP*k1m
    dPPdSBXdSBdk2 = 0
    dPPdSBXdSBdk2m = 0
    dPPdSBXdSBdk3 = 0
    dPPdSBXdSBdk3m = 0
    dPPdSBXdSBdk4 = -En*PP*k4
    dPPdSBXdSBdk4m = EP*k4m
    dPQdSBXdSBdk1 = 0
    dPQdSBXdSBdk1m = 0
    dPQdSBXdSBdk2 = (-k2*Es*SB+k2m*En*PQ)*En*k2
    dPQdSBXdSBdk2m = -En*PQ*k2m
    dPQdSBXdSBdk3 = -Es*PQ*k3
    dPQdSBXdSBdk3m = EsQ*k3m
    dPQdSBXdSBdk4 = 0
    dPQdSBXdSBdk4m = 0
    dSAdSBXdSBdk1 = -En*SA*k1
    dSAdSBXdSBdk1m = Es*PP*k1m
    dSAdSBXdSBdk2 = 0
    dSAdSBXdSBdk2m = 0
    dSAdSBXdSBdk3 = 0
    dSAdSBXdSBdk3m = 0
    dSAdSBXdSBdk4 = 0
    dSAdSBXdSBdk4m = 0
    dSBdSBXdSBdk1 = 0
    dSBdSBXdSBdk1m = 0
    dSBdSBXdSBdk2 = -(-k2*Es*SB+k2m*En*PQ)*Es*k2
    dSBdSBXdSBdk2m = En*PQ*k2m
    dSBdSBXdSBdk3 = 0
    dSBdSBXdSBdk3m = 0
    dSBdSBXdSBdk4 = 0
    dSBdSBXdSBdk4m = 0
    Output = {}
    dEPdk1 = dEPdEPXdEPdk1 + dEPdEnXdEndk1 + dEPdEsXdEsdk1 + dEPdEsQXdEsQdk1 + dEPdPPXdPPdk1 + dEPdPQXdPQdk1 + dEPdSAXdSAdk1 + dEPdSBXdSBdk1
    dEPdk1m = dEPdEPXdEPdk1m + dEPdEnXdEndk1m + dEPdEsXdEsdk1m + dEPdEsQXdEsQdk1m + dEPdPPXdPPdk1m + dEPdPQXdPQdk1m + dEPdSAXdSAdk1m + dEPdSBXdSBdk1m
    dEPdk2 = dEPdEPXdEPdk2 + dEPdEnXdEndk2 + dEPdEsXdEsdk2 + dEPdEsQXdEsQdk2 + dEPdPPXdPPdk2 + dEPdPQXdPQdk2 + dEPdSAXdSAdk2 + dEPdSBXdSBdk2
    dEPdk2m = dEPdEPXdEPdk2m + dEPdEnXdEndk2m + dEPdEsXdEsdk2m + dEPdEsQXdEsQdk2m + dEPdPPXdPPdk2m + dEPdPQXdPQdk2m + dEPdSAXdSAdk2m + dEPdSBXdSBdk2m
    dEPdk3 = dEPdEPXdEPdk3 + dEPdEnXdEndk3 + dEPdEsXdEsdk3 + dEPdEsQXdEsQdk3 + dEPdPPXdPPdk3 + dEPdPQXdPQdk3 + dEPdSAXdSAdk3 + dEPdSBXdSBdk3
    dEPdk3m = dEPdEPXdEPdk3m + dEPdEnXdEndk3m + dEPdEsXdEsdk3m + dEPdEsQXdEsQdk3m + dEPdPPXdPPdk3m + dEPdPQXdPQdk3m + dEPdSAXdSAdk3m + dEPdSBXdSBdk3m
    dEPdk4 = dEPdEPXdEPdk4 + dEPdEnXdEndk4 + dEPdEsXdEsdk4 + dEPdEsQXdEsQdk4 + dEPdPPXdPPdk4 + dEPdPQXdPQdk4 + dEPdSAXdSAdk4 + dEPdSBXdSBdk4
    dEPdk4m = dEPdEPXdEPdk4m + dEPdEnXdEndk4m + dEPdEsXdEsdk4m + dEPdEsQXdEsQdk4m + dEPdPPXdPPdk4m + dEPdPQXdPQdk4m + dEPdSAXdSAdk4m + dEPdSBXdSBdk4m
    dEndk1 = dEndEPXdEPdk1 + dEndEnXdEndk1 + dEndEsXdEsdk1 + dEndEsQXdEsQdk1 + dEndPPXdPPdk1 + dEndPQXdPQdk1 + dEndSAXdSAdk1 + dEndSBXdSBdk1
    dEndk1m = dEndEPXdEPdk1m + dEndEnXdEndk1m + dEndEsXdEsdk1m + dEndEsQXdEsQdk1m + dEndPPXdPPdk1m + dEndPQXdPQdk1m + dEndSAXdSAdk1m + dEndSBXdSBdk1m
    dEndk2 = dEndEPXdEPdk2 + dEndEnXdEndk2 + dEndEsXdEsdk2 + dEndEsQXdEsQdk2 + dEndPPXdPPdk2 + dEndPQXdPQdk2 + dEndSAXdSAdk2 + dEndSBXdSBdk2
    dEndk2m = dEndEPXdEPdk2m + dEndEnXdEndk2m + dEndEsXdEsdk2m + dEndEsQXdEsQdk2m + dEndPPXdPPdk2m + dEndPQXdPQdk2m + dEndSAXdSAdk2m + dEndSBXdSBdk2m
    dEndk3 = dEndEPXdEPdk3 + dEndEnXdEndk3 + dEndEsXdEsdk3 + dEndEsQXdEsQdk3 + dEndPPXdPPdk3 + dEndPQXdPQdk3 + dEndSAXdSAdk3 + dEndSBXdSBdk3
    dEndk3m = dEndEPXdEPdk3m + dEndEnXdEndk3m + dEndEsXdEsdk3m + dEndEsQXdEsQdk3m + dEndPPXdPPdk3m + dEndPQXdPQdk3m + dEndSAXdSAdk3m + dEndSBXdSBdk3m
    dEndk4 = dEndEPXdEPdk4 + dEndEnXdEndk4 + dEndEsXdEsdk4 + dEndEsQXdEsQdk4 + dEndPPXdPPdk4 + dEndPQXdPQdk4 + dEndSAXdSAdk4 + dEndSBXdSBdk4
    dEndk4m = dEndEPXdEPdk4m + dEndEnXdEndk4m + dEndEsXdEsdk4m + dEndEsQXdEsQdk4m + dEndPPXdPPdk4m + dEndPQXdPQdk4m + dEndSAXdSAdk4m + dEndSBXdSBdk4m
    dEsdk1 = dEsdEPXdEPdk1 + dEsdEnXdEndk1 + dEsdEsXdEsdk1 + dEsdEsQXdEsQdk1 + dEsdPPXdPPdk1 + dEsdPQXdPQdk1 + dEsdSAXdSAdk1 + dEsdSBXdSBdk1
    dEsdk1m = dEsdEPXdEPdk1m + dEsdEnXdEndk1m + dEsdEsXdEsdk1m + dEsdEsQXdEsQdk1m + dEsdPPXdPPdk1m + dEsdPQXdPQdk1m + dEsdSAXdSAdk1m + dEsdSBXdSBdk1m
    dEsdk2 = dEsdEPXdEPdk2 + dEsdEnXdEndk2 + dEsdEsXdEsdk2 + dEsdEsQXdEsQdk2 + dEsdPPXdPPdk2 + dEsdPQXdPQdk2 + dEsdSAXdSAdk2 + dEsdSBXdSBdk2
    dEsdk2m = dEsdEPXdEPdk2m + dEsdEnXdEndk2m + dEsdEsXdEsdk2m + dEsdEsQXdEsQdk2m + dEsdPPXdPPdk2m + dEsdPQXdPQdk2m + dEsdSAXdSAdk2m + dEsdSBXdSBdk2m
    dEsdk3 = dEsdEPXdEPdk3 + dEsdEnXdEndk3 + dEsdEsXdEsdk3 + dEsdEsQXdEsQdk3 + dEsdPPXdPPdk3 + dEsdPQXdPQdk3 + dEsdSAXdSAdk3 + dEsdSBXdSBdk3
    dEsdk3m = dEsdEPXdEPdk3m + dEsdEnXdEndk3m + dEsdEsXdEsdk3m + dEsdEsQXdEsQdk3m + dEsdPPXdPPdk3m + dEsdPQXdPQdk3m + dEsdSAXdSAdk3m + dEsdSBXdSBdk3m
    dEsdk4 = dEsdEPXdEPdk4 + dEsdEnXdEndk4 + dEsdEsXdEsdk4 + dEsdEsQXdEsQdk4 + dEsdPPXdPPdk4 + dEsdPQXdPQdk4 + dEsdSAXdSAdk4 + dEsdSBXdSBdk4
    dEsdk4m = dEsdEPXdEPdk4m + dEsdEnXdEndk4m + dEsdEsXdEsdk4m + dEsdEsQXdEsQdk4m + dEsdPPXdPPdk4m + dEsdPQXdPQdk4m + dEsdSAXdSAdk4m + dEsdSBXdSBdk4m
    dEsQdk1 = dEsQdEPXdEPdk1 + dEsQdEnXdEndk1 + dEsQdEsXdEsdk1 + dEsQdEsQXdEsQdk1 + dEsQdPPXdPPdk1 + dEsQdPQXdPQdk1 + dEsQdSAXdSAdk1 + dEsQdSBXdSBdk1
    dEsQdk1m = dEsQdEPXdEPdk1m + dEsQdEnXdEndk1m + dEsQdEsXdEsdk1m + dEsQdEsQXdEsQdk1m + dEsQdPPXdPPdk1m + dEsQdPQXdPQdk1m + dEsQdSAXdSAdk1m + dEsQdSBXdSBdk1m
    dEsQdk2 = dEsQdEPXdEPdk2 + dEsQdEnXdEndk2 + dEsQdEsXdEsdk2 + dEsQdEsQXdEsQdk2 + dEsQdPPXdPPdk2 + dEsQdPQXdPQdk2 + dEsQdSAXdSAdk2 + dEsQdSBXdSBdk2
    dEsQdk2m = dEsQdEPXdEPdk2m + dEsQdEnXdEndk2m + dEsQdEsXdEsdk2m + dEsQdEsQXdEsQdk2m + dEsQdPPXdPPdk2m + dEsQdPQXdPQdk2m + dEsQdSAXdSAdk2m + dEsQdSBXdSBdk2m
    dEsQdk3 = dEsQdEPXdEPdk3 + dEsQdEnXdEndk3 + dEsQdEsXdEsdk3 + dEsQdEsQXdEsQdk3 + dEsQdPPXdPPdk3 + dEsQdPQXdPQdk3 + dEsQdSAXdSAdk3 + dEsQdSBXdSBdk3
    dEsQdk3m = dEsQdEPXdEPdk3m + dEsQdEnXdEndk3m + dEsQdEsXdEsdk3m + dEsQdEsQXdEsQdk3m + dEsQdPPXdPPdk3m + dEsQdPQXdPQdk3m + dEsQdSAXdSAdk3m + dEsQdSBXdSBdk3m
    dEsQdk4 = dEsQdEPXdEPdk4 + dEsQdEnXdEndk4 + dEsQdEsXdEsdk4 + dEsQdEsQXdEsQdk4 + dEsQdPPXdPPdk4 + dEsQdPQXdPQdk4 + dEsQdSAXdSAdk4 + dEsQdSBXdSBdk4
    dEsQdk4m = dEsQdEPXdEPdk4m + dEsQdEnXdEndk4m + dEsQdEsXdEsdk4m + dEsQdEsQXdEsQdk4m + dEsQdPPXdPPdk4m + dEsQdPQXdPQdk4m + dEsQdSAXdSAdk4m + dEsQdSBXdSBdk4m
    dPPdk1 = dPPdEPXdEPdk1 + dPPdEnXdEndk1 + dPPdEsXdEsdk1 + dPPdEsQXdEsQdk1 + dPPdPPXdPPdk1 + dPPdPQXdPQdk1 + dPPdSAXdSAdk1 + dPPdSBXdSBdk1
    dPPdk1m = dPPdEPXdEPdk1m + dPPdEnXdEndk1m + dPPdEsXdEsdk1m + dPPdEsQXdEsQdk1m + dPPdPPXdPPdk1m + dPPdPQXdPQdk1m + dPPdSAXdSAdk1m + dPPdSBXdSBdk1m
    dPPdk2 = dPPdEPXdEPdk2 + dPPdEnXdEndk2 + dPPdEsXdEsdk2 + dPPdEsQXdEsQdk2 + dPPdPPXdPPdk2 + dPPdPQXdPQdk2 + dPPdSAXdSAdk2 + dPPdSBXdSBdk2
    dPPdk2m = dPPdEPXdEPdk2m + dPPdEnXdEndk2m + dPPdEsXdEsdk2m + dPPdEsQXdEsQdk2m + dPPdPPXdPPdk2m + dPPdPQXdPQdk2m + dPPdSAXdSAdk2m + dPPdSBXdSBdk2m
    dPPdk3 = dPPdEPXdEPdk3 + dPPdEnXdEndk3 + dPPdEsXdEsdk3 + dPPdEsQXdEsQdk3 + dPPdPPXdPPdk3 + dPPdPQXdPQdk3 + dPPdSAXdSAdk3 + dPPdSBXdSBdk3
    dPPdk3m = dPPdEPXdEPdk3m + dPPdEnXdEndk3m + dPPdEsXdEsdk3m + dPPdEsQXdEsQdk3m + dPPdPPXdPPdk3m + dPPdPQXdPQdk3m + dPPdSAXdSAdk3m + dPPdSBXdSBdk3m
    dPPdk4 = dPPdEPXdEPdk4 + dPPdEnXdEndk4 + dPPdEsXdEsdk4 + dPPdEsQXdEsQdk4 + dPPdPPXdPPdk4 + dPPdPQXdPQdk4 + dPPdSAXdSAdk4 + dPPdSBXdSBdk4
    dPPdk4m = dPPdEPXdEPdk4m + dPPdEnXdEndk4m + dPPdEsXdEsdk4m + dPPdEsQXdEsQdk4m + dPPdPPXdPPdk4m + dPPdPQXdPQdk4m + dPPdSAXdSAdk4m + dPPdSBXdSBdk4m
    dPQdk1 = dPQdEPXdEPdk1 + dPQdEnXdEndk1 + dPQdEsXdEsdk1 + dPQdEsQXdEsQdk1 + dPQdPPXdPPdk1 + dPQdPQXdPQdk1 + dPQdSAXdSAdk1 + dPQdSBXdSBdk1
    dPQdk1m = dPQdEPXdEPdk1m + dPQdEnXdEndk1m + dPQdEsXdEsdk1m + dPQdEsQXdEsQdk1m + dPQdPPXdPPdk1m + dPQdPQXdPQdk1m + dPQdSAXdSAdk1m + dPQdSBXdSBdk1m
    dPQdk2 = dPQdEPXdEPdk2 + dPQdEnXdEndk2 + dPQdEsXdEsdk2 + dPQdEsQXdEsQdk2 + dPQdPPXdPPdk2 + dPQdPQXdPQdk2 + dPQdSAXdSAdk2 + dPQdSBXdSBdk2
    dPQdk2m = dPQdEPXdEPdk2m + dPQdEnXdEndk2m + dPQdEsXdEsdk2m + dPQdEsQXdEsQdk2m + dPQdPPXdPPdk2m + dPQdPQXdPQdk2m + dPQdSAXdSAdk2m + dPQdSBXdSBdk2m
    dPQdk3 = dPQdEPXdEPdk3 + dPQdEnXdEndk3 + dPQdEsXdEsdk3 + dPQdEsQXdEsQdk3 + dPQdPPXdPPdk3 + dPQdPQXdPQdk3 + dPQdSAXdSAdk3 + dPQdSBXdSBdk3
    dPQdk3m = dPQdEPXdEPdk3m + dPQdEnXdEndk3m + dPQdEsXdEsdk3m + dPQdEsQXdEsQdk3m + dPQdPPXdPPdk3m + dPQdPQXdPQdk3m + dPQdSAXdSAdk3m + dPQdSBXdSBdk3m
    dPQdk4 = dPQdEPXdEPdk4 + dPQdEnXdEndk4 + dPQdEsXdEsdk4 + dPQdEsQXdEsQdk4 + dPQdPPXdPPdk4 + dPQdPQXdPQdk4 + dPQdSAXdSAdk4 + dPQdSBXdSBdk4
    dPQdk4m = dPQdEPXdEPdk4m + dPQdEnXdEndk4m + dPQdEsXdEsdk4m + dPQdEsQXdEsQdk4m + dPQdPPXdPPdk4m + dPQdPQXdPQdk4m + dPQdSAXdSAdk4m + dPQdSBXdSBdk4m
    dSAdk1 = dSAdEPXdEPdk1 + dSAdEnXdEndk1 + dSAdEsXdEsdk1 + dSAdEsQXdEsQdk1 + dSAdPPXdPPdk1 + dSAdPQXdPQdk1 + dSAdSAXdSAdk1 + dSAdSBXdSBdk1
    dSAdk1m = dSAdEPXdEPdk1m + dSAdEnXdEndk1m + dSAdEsXdEsdk1m + dSAdEsQXdEsQdk1m + dSAdPPXdPPdk1m + dSAdPQXdPQdk1m + dSAdSAXdSAdk1m + dSAdSBXdSBdk1m
    dSAdk2 = dSAdEPXdEPdk2 + dSAdEnXdEndk2 + dSAdEsXdEsdk2 + dSAdEsQXdEsQdk2 + dSAdPPXdPPdk2 + dSAdPQXdPQdk2 + dSAdSAXdSAdk2 + dSAdSBXdSBdk2
    dSAdk2m = dSAdEPXdEPdk2m + dSAdEnXdEndk2m + dSAdEsXdEsdk2m + dSAdEsQXdEsQdk2m + dSAdPPXdPPdk2m + dSAdPQXdPQdk2m + dSAdSAXdSAdk2m + dSAdSBXdSBdk2m
    dSAdk3 = dSAdEPXdEPdk3 + dSAdEnXdEndk3 + dSAdEsXdEsdk3 + dSAdEsQXdEsQdk3 + dSAdPPXdPPdk3 + dSAdPQXdPQdk3 + dSAdSAXdSAdk3 + dSAdSBXdSBdk3
    dSAdk3m = dSAdEPXdEPdk3m + dSAdEnXdEndk3m + dSAdEsXdEsdk3m + dSAdEsQXdEsQdk3m + dSAdPPXdPPdk3m + dSAdPQXdPQdk3m + dSAdSAXdSAdk3m + dSAdSBXdSBdk3m
    dSAdk4 = dSAdEPXdEPdk4 + dSAdEnXdEndk4 + dSAdEsXdEsdk4 + dSAdEsQXdEsQdk4 + dSAdPPXdPPdk4 + dSAdPQXdPQdk4 + dSAdSAXdSAdk4 + dSAdSBXdSBdk4
    dSAdk4m = dSAdEPXdEPdk4m + dSAdEnXdEndk4m + dSAdEsXdEsdk4m + dSAdEsQXdEsQdk4m + dSAdPPXdPPdk4m + dSAdPQXdPQdk4m + dSAdSAXdSAdk4m + dSAdSBXdSBdk4m
    dSBdk1 = dSBdEPXdEPdk1 + dSBdEnXdEndk1 + dSBdEsXdEsdk1 + dSBdEsQXdEsQdk1 + dSBdPPXdPPdk1 + dSBdPQXdPQdk1 + dSBdSAXdSAdk1 + dSBdSBXdSBdk1
    dSBdk1m = dSBdEPXdEPdk1m + dSBdEnXdEndk1m + dSBdEsXdEsdk1m + dSBdEsQXdEsQdk1m + dSBdPPXdPPdk1m + dSBdPQXdPQdk1m + dSBdSAXdSAdk1m + dSBdSBXdSBdk1m
    dSBdk2 = dSBdEPXdEPdk2 + dSBdEnXdEndk2 + dSBdEsXdEsdk2 + dSBdEsQXdEsQdk2 + dSBdPPXdPPdk2 + dSBdPQXdPQdk2 + dSBdSAXdSAdk2 + dSBdSBXdSBdk2
    dSBdk2m = dSBdEPXdEPdk2m + dSBdEnXdEndk2m + dSBdEsXdEsdk2m + dSBdEsQXdEsQdk2m + dSBdPPXdPPdk2m + dSBdPQXdPQdk2m + dSBdSAXdSAdk2m + dSBdSBXdSBdk2m
    dSBdk3 = dSBdEPXdEPdk3 + dSBdEnXdEndk3 + dSBdEsXdEsdk3 + dSBdEsQXdEsQdk3 + dSBdPPXdPPdk3 + dSBdPQXdPQdk3 + dSBdSAXdSAdk3 + dSBdSBXdSBdk3
    dSBdk3m = dSBdEPXdEPdk3m + dSBdEnXdEndk3m + dSBdEsXdEsdk3m + dSBdEsQXdEsQdk3m + dSBdPPXdPPdk3m + dSBdPQXdPQdk3m + dSBdSAXdSAdk3m + dSBdSBXdSBdk3m
    dSBdk4 = dSBdEPXdEPdk4 + dSBdEnXdEndk4 + dSBdEsXdEsdk4 + dSBdEsQXdEsQdk4 + dSBdPPXdPPdk4 + dSBdPQXdPQdk4 + dSBdSAXdSAdk4 + dSBdSBXdSBdk4
    dSBdk4m = dSBdEPXdEPdk4m + dSBdEnXdEndk4m + dSBdEsXdEsdk4m + dSBdEsQXdEsQdk4m + dSBdPPXdPPdk4m + dSBdPQXdPQdk4m + dSBdSAXdSAdk4m + dSBdSBXdSBdk4m
    Output['dEPdk1'] = dEPdk1
    Output['dEPdk1m'] = dEPdk1m
    Output['dEPdk2'] = dEPdk2
    Output['dEPdk2m'] = dEPdk2m
    Output['dEPdk3'] = dEPdk3
    Output['dEPdk3m'] = dEPdk3m
    Output['dEPdk4'] = dEPdk4
    Output['dEPdk4m'] = dEPdk4m
    Output['dEndk1'] = dEndk1
    Output['dEndk1m'] = dEndk1m
    Output['dEndk2'] = dEndk2
    Output['dEndk2m'] = dEndk2m
    Output['dEndk3'] = dEndk3
    Output['dEndk3m'] = dEndk3m
    Output['dEndk4'] = dEndk4
    Output['dEndk4m'] = dEndk4m
    Output['dEsdk1'] = dEsdk1
    Output['dEsdk1m'] = dEsdk1m
    Output['dEsdk2'] = dEsdk2
    Output['dEsdk2m'] = dEsdk2m
    Output['dEsdk3'] = dEsdk3
    Output['dEsdk3m'] = dEsdk3m
    Output['dEsdk4'] = dEsdk4
    Output['dEsdk4m'] = dEsdk4m
    Output['dEsQdk1'] = dEsQdk1
    Output['dEsQdk1m'] = dEsQdk1m
    Output['dEsQdk2'] = dEsQdk2
    Output['dEsQdk2m'] = dEsQdk2m
    Output['dEsQdk3'] = dEsQdk3
    Output['dEsQdk3m'] = dEsQdk3m
    Output['dEsQdk4'] = dEsQdk4
    Output['dEsQdk4m'] = dEsQdk4m
    Output['dPPdk1'] = dPPdk1
    Output['dPPdk1m'] = dPPdk1m
    Output['dPPdk2'] = dPPdk2
    Output['dPPdk2m'] = dPPdk2m
    Output['dPPdk3'] = dPPdk3
    Output['dPPdk3m'] = dPPdk3m
    Output['dPPdk4'] = dPPdk4
    Output['dPPdk4m'] = dPPdk4m
    Output['dPQdk1'] = dPQdk1
    Output['dPQdk1m'] = dPQdk1m
    Output['dPQdk2'] = dPQdk2
    Output['dPQdk2m'] = dPQdk2m
    Output['dPQdk3'] = dPQdk3
    Output['dPQdk3m'] = dPQdk3m
    Output['dPQdk4'] = dPQdk4
    Output['dPQdk4m'] = dPQdk4m
    Output['dSAdk1'] = dSAdk1
    Output['dSAdk1m'] = dSAdk1m
    Output['dSAdk2'] = dSAdk2
    Output['dSAdk2m'] = dSAdk2m
    Output['dSAdk3'] = dSAdk3
    Output['dSAdk3m'] = dSAdk3m
    Output['dSAdk4'] = dSAdk4
    Output['dSAdk4m'] = dSAdk4m
    Output['dSBdk1'] = dSBdk1
    Output['dSBdk1m'] = dSBdk1m
    Output['dSBdk2'] = dSBdk2
    Output['dSBdk2m'] = dSBdk2m
    Output['dSBdk3'] = dSBdk3
    Output['dSBdk3m'] = dSBdk3m
    Output['dSBdk4'] = dSBdk4
    Output['dSBdk4m'] = dSBdk4m
    return Output
