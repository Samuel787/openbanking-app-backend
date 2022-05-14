# Open Banking Deep Backend

This project houses the deep backend for NUS FinTech Openbanking project. It consists of PostgreSQL db to store news and fx data and exposes some APIs for other components of the project to interact with the database. This project is developed using Python, Flask, PostgreSQL and Heroku.

## Setting up the project locally
The set up was done by following this tutorial: 
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

### Requirements
1. PostgreSQL installed in your system
2. Heroku CLI installed in your system
3. virtualenv installed in your system

### Set up
1. `source env/Scripts/activate`
2. export the variables in `.env` file by copy pasting the export commands into terminal and running them
3. `py app.py`

## Viewing content in remote heroku db
1. `heroku pg:psql --app openbanking-application`
2. View all relations: `\dt`
3. View schema for a relation `\d relation_name`

## Pushing code to production (Initiate build in Heroku)
1. `git checkout main`
2. `git push prod main`

## Exposed APIs
The following APIs are exposed to interact with the database for the project. The deployed base live link for the API:
https://openbanking-application.herokuapp.com
### Adding forex data
A `POST` request has to be made to https://openbanking-application.herokuapp.com/data with the content in JSON format.

| Attribute  | Example | Required |
| ------------- | ------------- |--|
| "token"  | `api access secret`  | yes|
| "date"  | "2023-01-02" | yes |
| "price" | "1.3186" | yes |
|"open"| "1.3205" | yes |
| "high"| "1.3302" | yes|
|"low" | "1.3157"| yes|
| "change_percent" | "-0.14%" | yes|
|"difference"|"-0.0019000000000000128"| yes|
|"label" | "0.0"| yes|
|"sma"| "0.0"| yes|
|"ema"| "0.0"| yes|
|"macd"| "0.0"| yes|
|"macd_s"| "0.0"| yes|
|"macd_h"| "0.0"| yes|
|"roc"| "0.0"| yes|
|"rsi"| "0.0"| yes|
|"bollinger_up"| "0.0"| yes|
|"bollinger_down"| "0.0" | yes|
|"cci"| "0.0" | yes|

Example of JSON body of POST request:

```
{
    "secret": "auth secret here",
    "date": "2023-01-02",
    "price": "1.3186",
    "open": "1.3205",
    "high": "1.3302",
    "low": "1.3157",
    "change_percent": "-0.14%",
    "difference": "-0.0019000000000000128",
    "label": "0.0",
    "sma": "0.0",
    "ema": "0.0",
    "macd": "0.0",
    "macd_s": "0.0",
    "macd_h": "0.0",
    "roc": "0.0",
    "rsi": "0.0",
    "bollinger_up": "0.0",
    "bollinger_down": "0.0",
    "cci": "0.0"
}
```

### Retrieving Forex Data
A `GET` request has to be made to https://openbanking-application.herokuapp.com/fx with the following URL parameters.

| Attribute  | Example | Required |
| ------------- | ------------- |--|
| "token"  | `api access secret`  | yes|
| "start"  | `yyyy-mm-dd`  | yes|
| "end"  | `yyyy-mm-dd`  | yes|

Example:
https://openbanking-application.herokuapp.com/fx?start=2019-01-02&end=2019-10-03&token=api_auth_secret

Example response:
```
[
    {
        "bollinger_down": 1.0900977873372888,
        "bollinger_up": 1.1110922126627112,
        "cci": -123.40850818163595,
        "change_percent": 0.29,
        "date": "Tue, 01 Oct 2019 00:00:00 GMT",
        "difference": 0.0031999999999998,
        "ema": 1.09246407611737,
        "high": 1.0943,
        "id": 7,
        "label": 2.0,
        "low": 1.0878,
        "macd": -0.004171043402388941,
        "macd_h": -0.0008004647311926679,
        "open": 1.09,
        "price": 1.093,
        "roc": -0.007986930477400544,
        "rsi": 39.15647079428078,
        "sma": 1.100595
    },
    {
        "bollinger_down": 1.0895945885527645,
        "bollinger_up": 1.1108454114472355,
        "cci": -81.0173870404364,
        "change_percent": 0.26,
        "date": "Wed, 02 Oct 2019 00:00:00 GMT",
        "difference": 0.0028000000000001,
        "ema": 1.095030171411701,
        "high": 1.0964,
        "id": 11,
        "label": 2.0,
        "low": 1.0904,
        "macd": -0.003953990951522268,
        "macd_h": -0.00046672982426079583,
        "open": 1.0933,
        "price": 1.0958,
        "roc": 0.0015537885019651172,
        "rsi": 46.15598827764058,
        "sma": 1.10022
    },
    {
        "bollinger_down": 1.0892226219604852,
        "bollinger_up": 1.110527378039515,
        "cci": -41.952549861821694,
        "change_percent": 0.05,
        "date": "Thu, 03 Oct 2019 00:00:00 GMT",
        "difference": 0.0005999999999999,
        "ema": 1.0960838857103925,
        "high": 1.1,
        "id": 13,
        "label": 0.0,
        "low": 1.0941,
        "macd": -0.003691012638717517,
        "macd_h": -0.00016300120916483548,
        "open": 1.0959,
        "price": 1.0964,
        "roc": 0.003937368372859601,
        "rsi": 47.6451829623959,
        "sma": 1.0998750000000002
    }
]
```
### Deleting Forex Data
A `DELETE` request has to be made to https://openbanking-application.herokuapp.com/fx with the following URL parameters.

| Attribute  | Example | Required |
| ------------- | ------------- |--|
| "token"  | `api access secret`  | yes|
| "date"  | `yyyy-mm-dd`  | yes|

Example:
https://openbanking-application.herokuapp.com/fx?date=2023-01-01&token=api_auth_secret

Success response:
```
ok
```

### Get News Data
A `GET` request has to be made to https://openbanking-application.herokuapp.com/news with the following URL parameters.

| Attribute  | Example | Required |
| ------------- | ------------- |--|
| "token"  | `api access secret`  | yes|
| "limit"  | 10  | yes|

Example:
https://openbanking-application.herokuapp.com/news?limit=10&token=api_auth_secret

Success response:
```
[
    {
        "article": "© Reuters.\r\nInvesting.com - The greenback picked up steam on Friday despite U.S. consumer optimism hitting its lowest level since Donald Trump was elected president and the government shutdown moving into its 28th day.\r\nThe dollar was supported by a stronger-than-expected report for U.S. industrial production in December, in which manufacturing posted an impressive 1.1% gain from November. Such positive surprises relieve some of the worries about the strength of the economy after the slowdown at the end of last year. They also underline the relative strength of the U.S. compared to the Euro zone, where the Bank of Italy warned Friday that the country may have slid into recession with a second straight decline in GDP in the fourth quarter of last year.\r\nHowever, the negatives for dollar sentiment haven't gone away: Congress and Trump continue to struggle with their impasse over the budget and over 800,000 federal workers remain furloughed. The shutdown could have negative impacts on the economy, business leaders have warned this week as they presented their quarterly earnings.\r\nThe shutdown is clearly having an effect on U.S. consumers already: the University of Michigan's Consumer Survey Center that consumer sentiment plummeted to a two-year low of 90.7 in January from 98.3 a month earlier.\r\nThe , which measures the greenback’s strength against a basket of six major currencies, rose 0.17% to 95.875 as of 10:19 AM ET (15:19 GMT).\r\nThe dollar also continued to be supported by a Wall Street Journal report that U.S. Treasury Secretary Steven Mnuchin is in favor of easing tariffs on Chinese products. That sent U.S. stocks and the dollar higher late on Thursday, despite the Treasury Department denying the news.\r\nMeanwhile, sterling retreated from its recent highs after weak retail sales data for December. decreased 0.51% to 1.2914. It's still holding to most of the gains made in recent weeks, as the risk of an economically harmful 'hard' Brexit appears to recede.\r\nThe yen, typically sought by investors as a safe haven during times of economic or market stress, was lower against the dollar, with rising 0.19% to 109.42.\r\nElsewhere, the euro dipped with falling 0.18% to 1.1374.",
        "date": "Fri, 18 Jan 2019 00:00:00 GMT",
        "id": 4,
        "title": "Forex - U.S. Dollar Rises as Consumer Optimism Falls"
    },
    {
        "article": "© Reuters.\r\nInvesting.com – The U.S. dollar little changed Thursday as mostly upbeat economic data was offset by strong rise in sterling on bets the U.K. will avoid leaving the EU without a trade deal.\r\nThe , which measures the greenback against a trade-weighted basket of six major currencies, rose by 0.08% to 95.76.\r\nAs U.K. Prime Minister Theresa May seeks cross-party consensus on a Brexit deal after her government won a vote of confidence on Wednesday, traders continue to bet on the UK securing a withdrawal deal, pushing the pound higher against the greenback.\r\nThe way forward on Brexit, however, is paved with uncertainty as Labor leader, Jeremy Corbyn, has refused to enter cross-party talks demanding May rule out a no-deal Brexit. That is a demand which May has stressed is “impossible.”\r\nrose 0.76% to $1.2979.\r\nThe pound's strength kept a lid on gains in the greenback even as a key manufacturing report and labor data topped economists’ estimates.\r\nThe Philadelphia Fed said Thursday its rose to a reading of 17 in January from a revised 9.1 last month.\r\nThe U.S. Department of Labor reported Thursday that dropped by 3,000 to a seasonally adjusted 213,000, beating economists’ forecast for a drop to 216,000.\r\nThe upbeat regional manufacturing report comes a day after the Fed’s Beige Book – an economic report, based on anecdotal information collected by the Fed’s 12 reserve banks – highlighted concerns about manufacturing growth amid rising costs, trade and political uncertainty.\r\nElsewhere, fell 0.14% $1.1381, while rose 0.34% to C$1.3299 as falling oil prices weighed on the loonie, supporting gains in the pair.\r\nfell 0.02% to Y109.06.",
        "date": "Fri, 18 Jan 2019 00:00:00 GMT",
        "id": 8,
        "title": "Forex - Upbeat U.S. Data Can't Help Dollar as Sterling Reigns Supreme"
    }
]
```

### Add News Data
A `POST` request has to be made to https://openbanking-application.herokuapp.com/news with the content in JSON format.

| Attribute  | Example | Required |
| ------------- | ------------- |--|
| "token"  | `api access secret`  | yes|
| "date"  | "2023-01-02" | yes |
| "title" | "Some title" | yes |
| "article" | "Some article" | yes |
| "sentiment"| 1 (float and -1 is default) | yes|

Example of JSON content:
```
{
    "token": "f13785bcd296e49e14706164d1983be531492d5c92b3523204812014ae79941a",
    "date": "2025-01-19",
    "title": "Dummy news title",
    "article": "Dummy article content"
}
```

Success Response
```
Forex News Added. news id=2
```

### Delete News Data
A `DELETE` request has to be made to https://openbanking-application.herokuapp.com/news with the following URL parameters.

| Attribute  | Example | Required |
| ------------- | ------------- |--|
| "token"  | `api access secret`  | yes|
| "date"  | `yyyy-mm-dd`  | yes|

Example:
https://openbanking-application.herokuapp.com/news?date=2023-01-01&token=api_auth_secret

Success response:
```
ok
```

## Encounter problems/bugs?
Report it under issues in this github repo and we will look into it.