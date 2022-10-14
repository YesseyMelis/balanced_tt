import datetime

from pandas._libs.tslibs.ccalendar import MONTH_ALIASES


def get_refactored_result(dict_means: dict):
    result = {}
    for k, v in dict_means.items():
        currency = k.split(',')[1].split("'")[1].split("'")[0]
        date = datetime.datetime.strptime(k.split("'")[1].split("'")[0].split()[0], '%Y-%m-%d')
        month_name = MONTH_ALIASES.get(date.month)
        year = str(date.year)
        if year in result:
            if month_name in result[year]:
                result[year][month_name][currency] = v
            else:
                result[year][month_name] = {currency: v}
        else:
            result[year] = {month_name: {currency: v}}
    return result
