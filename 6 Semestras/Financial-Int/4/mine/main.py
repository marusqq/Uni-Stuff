#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script to test the capabilities of interactive brokers api'''

#ibapi libraries
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.ticktype import TickTypeEnum

#for threading
from threading import Thread

#my util files
import ibapi_util as iu

#for sleeping and date
import time
import datetime

#test IDS:
# ID: 1 <===== TSLA current data
# ID: 2 <===== Historical USD-EUR data
# ID: 3 <===== TSLA MKT Order for BUY 15
# ID: 4 <===== TSLA LMT Order for BUY 15 @ 100 USD


class App(EWrapper, EClient):
    oid = 0

    def __init__(self, ip, port, client):
        EClient.__init__(self, self)
        EWrapper.__init__(self)

        self.connect(ip, port, client)

        thread = Thread(target=self.run)
        thread.start()

    def getNextID(self):
        self.oid = self.oid + 1
        return self.oid

    def get_market_data(self, contract, orderID = None):
        #check for ID or generate
        orderID = self.checkForID(orderID)
        #print contract
        iu.print_contract(contract, symbol = True, currency = True)

        #account for frozen data only
        self.reqMarketDataType(4)
        self.reqMktData(orderID, contract, '', False, False, [])

    def place_order(self, contract, order, orderID = None):
        #check for ID or generate
        orderID = self.checkForID(orderID)

        #print order with contract
        iu.print_contract(contract, symbol = True, currency = True)
        if order.orderType == 'LMT':
            iu.print_order(order, order_type = True, total_quantity = True, action = True, limit = True)
        else:
            iu.print_order(order, order_type = True, total_quantity = True, action = True, limit = False)
        
        
        #place the order
        self.placeOrder(orderID, contract, order)
        return orderID

    def checkForID(self, orderID):
        if orderID is None:
            orderID = self.getNextID()
            print('ID:', orderID)
        return orderID

    def tickPrice(self, TickerId, tickType, price,
                   attrib):
            if tickType in [66, 67]:
                print("Stock Price: Tick ID: [", TickerId, '], Type: [', TickTypeEnum.to_str(tickType), '] Price: ', price)
            return

    def cancel_order(self, orderID):

        print('Cancelling order:', orderID)
        self.cancelOrder(orderID)
        
        return
    
    def cancel_all_orders(self):
        print('Cancelling all offers')
        self.reqGlobalCancel()
        return

    def get_historical_data(self, contract, orderID = None):
        #check for ID or generate
        orderID = self.checkForID(orderID)

        queryTime = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime("%Y%m%d %H:%M:%S")
        self.reqHistoricalData(
            orderID, 
            contract, 
            queryTime,
            "1 M", 
            "1 day",
            "MIDPOINT",
            0, 
            1, 
            False, 
            [])
        
        #print contract
        iu.print_contract(contract, symbol = True, currency = True)

    def historicalData(self, orderID, bar):
        print('ID:', orderID, ', Date:', bar.date, ', Price:', bar.close)

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        print('---------------------------------------------------------------')
        print('[ORDER STATUS] ID:', orderId, 'Information:  status:', status, ', fill', filled, ', remaining', remaining, ', lastFillPrice', lastFillPrice)
        print('---------------------------------------------------------------\n') 

    def openOrder(self, orderId, contract, order, orderState):
        print('---------------------------------------------------------------')
        print('[ORDER OPENED] ID:', orderId, 'Information: ', order.orderType, order.action, order.totalQuantity, contract.symbol, ' - ', orderState.status)
        print('---------------------------------------------------------------\n')

    def execDetails(self, reqId, contract, execution):
        print('---------------------------------------------------------------')
        print('[ORDER EXECUTED] ID:', execution.orderId, 'Information', execution.shares, contract.symbol, contract.currency)
        print('---------------------------------------------------------------\n')
    

def main():
    #create app and connect to localhost:4001
    #Understand and connect to broker API ✓
    app = App("127.0.0.1", 4002, 0)

    time.sleep(1)   

    #Get current and historic data
    #Get current data ✓
    print('Getting market data:')
    app.get_market_data(
        iu.create_contract(
            symbol = 'TSLA',
            currency = 'USD',
            exchange = 'SMART',
            secType = 'STK'
        ), 
        orderID = 1
    )

    #Get historic data ✓
    #TODO: https://github.com/softwarespartan/IB4m/issues/60
    print('Getting historic data:')
    app.get_historical_data(
        iu.create_contract(
            symbol = 'EUR',
            currency = 'USD',
            exchange = 'IDEALPRO',
            secType = 'CASH'
        ),
        orderID = 2
    )

    print('Placing MKT order:')
    #Send market orders ✓
    app.place_order(
        iu.create_contract(
            symbol = 'TSLA',
            currency = 'USD',
            exchange = 'SMART',
            secType = 'STK'
        ), 
        
        iu.create_order(
            order_type = 'MKT',
            total_quantity = 15,
            action = 'BUY'
        ),
        orderID = 3
    )

    #Send limit orders ✓
    print('Placing LMT order:')
    app.place_order(
        iu.create_contract(
            symbol = 'TSLA',
            currency = 'USD',
            exchange = 'SMART',
            secType = 'STK'
        ), 
    
        iu.create_order(
            order_type = 'LMT',
            total_quantity = 15,
            action = 'BUY',
            limit = 100
        ),
        orderID = 4
    )

    #Cancel offers ✓
    print('Cancelling LMT order')
    app.cancel_order(orderID = 4)

    #possible to cancel all offers
    #app.cancel_all_orders()
    
    #throws [WinError 10038] but its after disconnection
    #app.disconnect()
    #app.done = True

if __name__ == "__main__":
    main()