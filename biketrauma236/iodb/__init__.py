#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:36:03 2021

@author: llinares
"""
import os
url_db = "https://koumoul.com/s/data-fair/api/v1/datasets/accidents-velos/raw"
path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "bicycle_db.csv")
