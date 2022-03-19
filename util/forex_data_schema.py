from flask_sqlalchemy import SQLAlchemy
def forex_data_schema(date, price, open, high, low, change_percent, difference, label, sma, ema, macd, macd_s, macd_h, roc, rsi, bollinger_up, bollinger_down, cci):
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
    if sma == None:
        sma = 0
    sma = float(sma)
    if ema == None:
        ema = 0
    ema = float(ema)
    if macd == None:
        macd = 0
    macd = float(macd)
    if macd_s == None:
        macd_s = 0
    macd_s = float(macd_s)
    if macd_h == None:
        macd_h = 0
    macd_h = float(macd_h)
    if roc == None:
        roc = 0
    roc = float(roc)
    if rsi == None:
        rsi = 0
    rsi = float(rsi)
    if bollinger_up == None:
        bollinger_up = 0
    bollinger_up = float(bollinger_up)
    if bollinger_down == None:
        bollinger_down = 0
    bollinger_down = float(bollinger_down)
    if cci == None:
        cci = 0
    cci = float(cci)
    return date, price, open, high, low, change_percent, difference, label, sma, ema, macd, macd_s, macd_h, roc, rsi, bollinger_up, bollinger_down, cci
    
    