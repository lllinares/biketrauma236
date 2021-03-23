#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 08:29:36 2021

@author: llinares
"""

def format_date(df_bikes):
    df = df_bikes.drop(columns = ['date', 'mois','jour','heure'])
    df.insert(0,"date_formated", df_bikes['date']+"T"+df_bikes['heure']+":00:00+01:00")
    #autre méthode : df.to_date_time(...)
    return df