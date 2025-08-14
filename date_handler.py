import datetime
from dateutil.relativedelta import relativedelta
from functools import lru_cache

DEFAULT_DATE = datetime.date(2020,1,1)

@lru_cache(maxsize=None)
def format_date(month : int):
    new_date = DEFAULT_DATE + relativedelta(months=month-1)
    return new_date.strftime("%m/%d/%Y")