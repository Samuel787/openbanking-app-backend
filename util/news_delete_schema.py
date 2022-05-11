def news_delete_schema(date):
    date_temp = date.split("-")
    if len(date_temp) != 3:
        raise Exception("Error in date format. Format is yyyy-mm-dd")
    for i in date_temp:
        int(i)
    return date