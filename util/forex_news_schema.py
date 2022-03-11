def forex_news_schema(date, title, article):
    date_temp = date.split("/")
    if len(date_temp) != 3:
        raise Exception("Error in date format")
    for i in date_temp:
        int(i)
    if title == None:
        title = ""
    title = str(title)
    if article == None:
        article = ""
    article = str(article)
    return date, title, article