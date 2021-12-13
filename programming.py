#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 02:46:39 2021

@author: abbeyswanner
"""
    
"""
This program was created to run everyday and check to see if you have a friend with a birthday coming up, I have not included the code to make it do so so that you can run it on a sepaerte server. 
Before this program will run for you, you will have to install and set up ezgmail
"""
import datetime, ezgmail
current_date = datetime.datetime.now()    
month=current_date.month
day=current_date.day
import pandas as pd
idk = pd.read_excel('Birthdays.xlsx')
"""
you should either name your file the same thing, or change the name here to what you named your file
also, make sure your file is stored in the same folder as your program
also, this program is set to run assuming your file is set up the same way mine is, that is with row 1 being a header, with coulumn A having the title "names", B the title "day", and C the title "month". The A column should simply state their first and last name, the B column should simply state the numerical value for the day of the month, and the C coulmun should state the numerical value for the month
"""
bdays=idk.to_numpy()
length=len(bdays)
i=0
while i<length:
    bmonth = bdays[i,2]
    bday = bdays[i,1]

    if bmonth==current_date.month:
        if bday==current_date.day:
            ezgmail.send('8652550428@email.uscc.net', 'Birthday', 'Hey, dont forget that you know someone that was born today!')
            print ("message sent")
            "you should consider replacing my phone number here with your phone number, or it is going to text me, you may also have to change the carrier"
            
    i=i+1
    
leapyear=current_date.year%4
"this variable was created to account for leap year, adding one day to all the months after February if the year is divisible by 4"
if leapyear!=0:
    month_changed=0
    if current_date.month==1:
        month_changed=0
    if current_date.month==2:
        month_changed=31
    if current_date.month==3:
        month_changed=59
    if current_date.month==4:
        month_changed=90
    if current_date.month==5:
        month_changed=120
    if current_date.month==6:
        month_changed=151
    if current_date.month==7:
        month_changed=181
    if current_date.month==8:
        month_changed=212
    if current_date.month==9:
        month_changed=243
    if current_date.month==10:
        month_changed=273
    if current_date.month==11:
        month_changed=304
    if current_date.month==12:
        month_changed=334
    current=month_changed+current_date.day

    l=0
    while l<length:
        bmonth = bdays[l,2]
        bday = bdays[l,1]
        bmonth_changed=0
        if bmonth==1:
            bmonth_changed=0
        if bmonth==2:
            bmonth_changed=31
        if bmonth==3:
            bmonth_changed=59
        if bmonth==4:
            bmonth_changed=90
        if bmonth==5:
            bmonth_changed=120
        if bmonth==6:
            bmonth_changed=151
        if bmonth==7:
            bmonth_changed=181
        if bmonth==8:
            bmonth_changed=212
        if bmonth==9:
            bmonth_changed=243
        if bmonth==10:
            bmonth_changed=273
        if bmonth==11:
            bmonth_changed=304
        if bmonth==12:
            bmonth_changed=334   
        birthday=bmonth_changed+bday-14
        "this is subracting 14 in order to alert you 2 weeks before your friend's birthday, if you wanted to do one week, change it to 7"
        if birthday==current:
            ezgmail.send('8652550428@email.uscc.net', 'Birthday', 'Hey, one of your friends has a birthday in two weeks')
            print('message sent')
            "Once again, change your number here"
        l=l+1
        
if leapyear==0:
    month_changed=0
    if current_date.month==1:
        month_changed=0
    if current_date.month==2:
        month_changed=31
    if current_date.month==3:
        month_changed=60
    if current_date.month==4:
        month_changed=91
    if current_date.month==5:
        month_changed=121
    if current_date.month==6:
        month_changed=152
    if current_date.month==7:
        month_changed=182
    if current_date.month==8:
        month_changed=213
    if current_date.month==9:
        month_changed=244
    if current_date.month==10:
        month_changed=274
    if current_date.month==11:
        month_changed=305
    if current_date.month==12:
        month_changed=335
    current=month_changed+current_date.day

    l=0
    while l<length:
        bmonth = bdays[l,2]
        bday = bdays[l,1]
        bmonth_changed=0
        if bmonth==1:
            bmonth_changed=0
        if bmonth==2:
            bmonth_changed=31
        if bmonth==3:
            bmonth_changed=60
        if bmonth==4:
            bmonth_changed=91
        if bmonth==5:
            bmonth_changed=121
        if bmonth==6:
            bmonth_changed=152
        if bmonth==7:
            bmonth_changed=182
        if bmonth==8:
            bmonth_changed=213
        if bmonth==9:
            bmonth_changed=244
        if bmonth==10:
            bmonth_changed=274
        if bmonth==11:
            bmonth_changed=305
        if bmonth==12:
            bmonth_changed=335  
        birthday=bmonth_changed+bday-14
        "this is subracting 14 in order to alert you 2 weeks before your friend's birthday, if you wanted to do one week, change it to 7"
        if birthday==current:
            ezgmail.send('8652550428@email.uscc.net', 'Birthday', 'Hey, one of your friends has a birthday in two weeks')
            print('message sent')
            "Once again, change your number here"
        l=l+1
print("program complete")
"This is here as the main output of the program is to text you if it is someone's birthday or if a birthday is coming up, but otherwise it has no output, so this lets you know it ran"








