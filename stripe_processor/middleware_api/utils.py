def parse_date(data):
    exp_date = data.pop('exp_date')
    data['exp_month'] = int(exp_date[:2])
    data['exp_year'] = 2000 + int(exp_date[2:])
    return data


def mask(value):
    if len(value) <= 4:
        value = "*" * len(value)
    else:
        value = value[-4:].rjust(len(value), "*")
    return value
