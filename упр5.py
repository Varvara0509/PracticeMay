import datetime


def date_in_future(number_day = None) -> str:
    current_datetime = datetime.datetime.now()

    if not isinstance(number_day, int) or number_day is None:
        return current_datetime.strftime("%d-%m-%Y %H:%M:%S")

    number_day_in_future = current_datetime + datetime.timedelta(days=number_day)

    return number_day_in_future.strftime("%d-%m-%Y %H:%M:%S")


def tests():
    print(date_in_future([]))  # => текущая дата
    print(date_in_future(2))  # => текущая дата + 2 дня


tests()