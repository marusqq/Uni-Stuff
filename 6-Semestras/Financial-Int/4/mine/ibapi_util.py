#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script to test the capabilities of interactive brokers api'''

from ibapi.contract import Contract
from ibapi.order import Order

def create_contract(symbol, exchange, currency, secType):
    '''function to create contract'''
    contract = Contract()
    contract.symbol = symbol
    contract.exchange = exchange
    contract.secType = secType
    contract.currency = currency

    return contract

def print_contract(contract, symbol = True, exchange = False, secType = False, currency = False):
    
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('Contract: ')
    if symbol:
        print('Symbol:', contract.symbol)
    if exchange:
        print('Exchange:', contract.exchange)
    if secType:
        print('secType:', contract.secType)
    if currency:
        print('Currency:', contract.currency)

    print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\n')
    return

def create_order(order_type, total_quantity, action, limit = None):
    '''function to create custom limit order'''
    order = Order()
    order.orderType = order_type
    order.totalQuantity = total_quantity 
    order.action = action
    if order_type == 'LMT':
        order.lmtPrice = limit

    return order

def print_order(order, order_type = False, total_quantity = False, action = True, limit = False):
    
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('Order: ')
    if order_type:
        print('Order type:', order.orderType)
    if total_quantity:
        print('Total quantity:', order.totalQuantity)
    if action:
        print('Action:', order.action)
    if limit:
        print('Limit:', order.lmtPrice)

    print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\n')
    return



