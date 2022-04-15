from alpaca_historical_extract import hub

def pullData(api, credentials):
    #hub.update_dbs(credentials, api, tckrs='', modeling=True, forceFDataPull=False, forceMDataPull=False, verbose=True)
    hub.update_dbs(credentials, api, tckrs=['TSLA', 'AAPL', 'MSFT','TWTR'], modeling=True, forceFDataPull=False, forceMDataPull=False, verbose=False)

print('hello')