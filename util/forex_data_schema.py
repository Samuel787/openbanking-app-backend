def forex_data_schema(date, price, open, high, low, change_percent, difference, label):
    # simple check for date format
    date_temp = date.split("-")
    if len(date_temp) != 3:
        raise Exception("Error in date format")
    for i in date_temp:
        int(i)
    if price == None:
        price = 0
    price = float(price)
    if open == None:
        open = 0
    open = float(open)
    if high == None:
        high = 0
    high = float(high)
    if low == None:
        low = 0
    low = float(low)
    if change_percent == None:
        change_percent = 0
    if "%" in change_percent:
        change_percent = change_percent.replace("%", "")
    change_percent = float(change_percent)
    if difference == None:
        difference = 0
    difference = float(difference)
    if label == None:
        label = 0
    label = float(label)
    return date, price, open, high, low, change_percent, difference, label
    
    