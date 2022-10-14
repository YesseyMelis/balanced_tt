import json

import pandas as pd

from utils import get_refactored_result


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
    dict_means = json.loads(mean_by_curr_month.to_json())
    return get_refactored_result(dict_means)
