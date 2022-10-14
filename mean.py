import datetime
import json

import pandas as pd


def get_mean(start_date, end_date):
    dtypes = {
        'date': 'string',
        'first_name': 'string',
        'last_name': 'string',
        'transaction_id': 'int',
        'amount': 'float',
        'currency': 'string'
    }
    ts = pd.read_csv(
        'transactions.csv',
        dtype=dtypes,
        parse_dates=['date'],
        dayfirst=True,
        iterator=True,
        chunksize=1000
    )
    df = pd.concat([chunk[(chunk['date'] > start_date) & (chunk['date'] < end_date)] for chunk in ts])
    df.index = pd.to_datetime(df['date'], format='%d/%m/%y')
    mean_by_curr_month = df.groupby([pd.Grouper(freq='M'), 'currency'])["amount"].mean()
    res = json.loads(mean_by_curr_month.to_json())
    return res


if __name__ == '__main__':
    date = datetime.datetime(2022, 8, 1)
    date2 = datetime.datetime(2022, 10, 11)
    print(get_mean(date, date2))
    date = datetime.datetime(2022, 7, 1)
    date2 = datetime.datetime(2022, 9, 11)
    print(get_mean(date, date2))
