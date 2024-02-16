from datetime import datetime, timedelta


class Times:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._datetime = datetime.now()
        return cls._instance

    @property
    def today(self):
        return str(self._instance._datetime.date())

    @property
    def period(self):
        return self._instance._datetime.strftime('%Y%m')

    @property
    def pre_period(self):
        last_month_date = self._instance._datetime - timedelta(days=self._instance._datetime.day)
        return last_month_date.strftime('%Y%m')
