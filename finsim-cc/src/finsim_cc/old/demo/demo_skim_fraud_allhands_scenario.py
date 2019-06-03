#!/usr/bin/python3

#  FinSim
#  Copyright 2018 Carnegie Mellon University. All Rights Reserved.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Released under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.

import requests, random, time

atm_user = 'atm_000_0'
atm_pw = 'tartans@1'

ccUrl = "http://localhost:5000/"
baseUrl  = "http://localhost:10000/"
baseUrl2 = "http://localhost:10100/"

userAccts = [ '0001222233334879', '0001222233334880', '0001222233334881', '0004332221111670', '0004332221111671', '0003987145123486', '0003987145123487', '0005431235531224', '0005431235531225', '0008712351421301', '0008712351421302', '0007531438312391', '0007531438312392', '0007531438312393', '0005111122223333' ]

compromisedAccts = [ ( 'jjones', '0001222233334879' ),
                     ( 'ckent', '0003987145123487' ),
                     ( 'pmitchell', '0007531438312391' ),
                     ( 'pmitchell', '0007531438312393' ),
                     ( 'vgs', '0005111122223333' ) 
                   ]
'''
for user, account in compromisedAccts:
    loginForm = {"username": atm_user, "password": atm_pw}
    token = requests.post( baseUrl + "login", json = loginForm ).json()
    header = { "Authorization": "Bearer " + token['access_token'], "Content-Type": "application/json" }
    transactionResponse = requests.post( baseUrl + "bank/withdrawal", json = { 'amount': 12345.00, 'account': account, 'counterpart_name': 'atm_000_0', 'counterpart_acct': 'atm0', 'fraud_flag': 0 }, headers = header )
    print( transactionResponse.text )

time.sleep(300)
'''
counter = 762
for user, account in compromisedAccts:
    loginForm = {"username": user, "password": 'tartans@1'}
    token = requests.post( baseUrl + "login", json = loginForm ).json()
    header = { "Authorization": "Bearer " + token['access_token'], "Content-Type": "application/json" }
    flagResponse = requests.post( baseUrl + 'flag/fraud', json = { 'account':account, 'transaction': counter }, headers = header )
    print( "Response Text: " + flagResponse.text )
    counter+=1
