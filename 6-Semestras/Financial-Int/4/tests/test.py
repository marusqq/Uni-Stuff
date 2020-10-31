from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class App(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    # EWrapper function
    def contractDetails(self, reqId, contractDetails):
        print("contractDetails: ", reqId, " ", contractDetails)


def main():
    app = App()

    #connection on localhost:4001
    app.connect("127.0.0.1", 4001, 0)


    # In production application, we would wait for acknowledgement connection is complete.
    # Typically this is done by waiting for nextValidID callback.

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    print(contract)

    # EClient function
    app.reqContractDetails(1, contract)

    app.contractDetails(contract.symbol, contract.currency)

    app.run()


if __name__ == "__main__":
    main()