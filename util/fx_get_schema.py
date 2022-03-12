def fx_get_schema(start_date, end_date):
    date_temp = start_date.split("-")
    if len(date_temp) != 3:
        raise Exception("Error in date format. Format is yyyy-mm-dd")
    for i in date_temp:
        int(i)
    date_temp = end_date.split("-")
    if len(date_temp) != 3:
        raise Exception("Error in date format. Format is yyyy-mm-dd")
    for i in date_temp:
        int(i)
    return start_date, end_date