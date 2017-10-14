# stock_advisor
This repo will contain following:
* Data analytics for recommanding buying and selling stocks
* A simple web portal for presenting the recommandations

Both the analytics and web portal will use MongoDB.

### Data Analytics
* `Stock Recommender` process to pull historical prices from Google Finance for ticker symbols found in our MongoDB, and using various models to determine buy/sell signals
* Process for analyzing news and social media for determining real-time market sentiment.
* Process for analyzing historical news and how it correlated to historical market prices.

### Daemon and Cron Processes
* `Stock Watcher` cron process (every 5 mins) that gets current stock prices of configured stocks to watch and adds events to MongoDB for those stocks that have achieved new levels.

### Web Portal
* `Stock Recommender` page to display results of the `Stock Recommender` analytic process with one card per data model, listing the stocks that model recommends buying.
* `Stock Watcher` page to display the last 3 events created by the `Stock Watcher` process for each stock we are watching.

### Cloud Resources
We will use the following AWS resources:
* Two 4 cores servers for running high performance distributed data analytics routines, where we will also run the web portal which will use very little resource and thereby not compete with the analytics routines for processing power.
* One server for standing up MongoDB instance, launching data analytics on the high performance servers, and any cron jobs that do simple scheduling and ETL.

### MongoDB Collections
`Stock Recommender`
* Ticker symbols for use in data analytics. This will include most of the SP500 and any other stocks we are interested in.
* Model Results

`Stock Watcher`
* Ticker symbols and price levels (Support, Resistance) for automatic notification when stocks approch specific levels.
* Events: each time a configured stock reaches a new level.



