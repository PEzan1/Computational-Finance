#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:49:58 2024

@author: paolezan
"""

import yfinance as yf 
import pandas as pd
import numpy as np

sp500 = yf.download("ES=F")
print(f"sp500 {sp500}")

prices=sp500['Adj Close']
sp500['Log Returns']=np.log(prices).diff()
Annual_Vol = sp500['Log Returns'].std() * np.sqrt(252)

print()
print(f"Annualized Vol {Annual_Vol}")