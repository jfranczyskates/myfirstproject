from alpaca_historical_extract import hub

def pullData(api, credentials):
    #hub.update_dbs(credentials, api, tckrs='', modeling=True, forceFDataPull=False, forceMDataPull=False, verbose=True)
    hub.update_dbs(credentials, api, tckrs=['TSLA', 'AAPL', 'MSFT','TWTR'], modeling=True, forceFDataPull=False, forceMDataPull=False, verbose=False)


def run_stock_analysis():
    loginSuccessful = False
    api=''
    credentials=''
    loginSuccessful, api, credentials = hub.init()
    # print(loginSuccessful,api,credentials)

    if loginSuccessful:
        # print(api.get_account())
        pullData(api, credentials)

        # dataset = hub.get_table(dataset='DAILY MARKET DATA', raw=True)
    keys = hub.get_datasets()
    print(keys)
    dataset = hub.get_table(dataset=hub.get_datasets(), raw=False)
    # print(dataset['marketData'])
    dailyDf = dataset['marketData']['DAILY MARKET DATA']['STAT DATA']
    print(dailyDf.head(10).to_string())
    # print(dataset['DAILY MARKET DATA']['RAW DATA'].to_string())
    print(dailyDf.describe(include="all").to_string())
    print(dailyDf.info())

if __name__ == '__main__':
    run_stock_analysis()