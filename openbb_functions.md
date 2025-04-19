
```
.crypto.price.historical
.currency.price.historical
.derivatives.futures.curve
.derivatives.futures.historical
.derivatives.options.chains
.equity.discovery.active
.equity.discovery.aggressive_small_caps
.equity.discovery.gainers
.equity.discovery.growth_tech
.equity.discovery.losers
.equity.discovery.undervalued_growth
.equity.discovery.undervalued_large_caps
.equity.estimates.consensus
.equity.fundamental.balance
.equity.fundamental.cash
.equity.fundamental.dividends
.equity.fundamental.income
.equity.fundamental.management
.equity.fundamental.metrics
.equity.ownership.share_statistics
.equity.price.historical
.equity.price.quote
.equity.profile
.equity.screener
.etf.historical
.etf.info
.index.available
.index.price.historical
.news.company

```



```
.crypto.price.historical
Get historical price data for cryptocurrency pair(s) within a provider.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.crypto.price.historical(symbol='BTCUSD', provider='fmp')
        >>> obb.crypto.price.historical(symbol='BTCUSD', start_date='2024-01-01', end_date='2024-01-31', provider='fmp')
        >>> obb.crypto.price.historical(symbol='BTCUSD,ETHUSD', start_date='2024-01-01', end_date='2024-01-31', provider='polygon')
        >>> # Get monthly historical prices from Yahoo Finance for Ethereum.
        >>> obb.crypto.price.historical(symbol='ETH-USD', interval='1m', start_date='2024-01-01', end_date='2024-12-31', provider='yfinance')

Outputs:
date: The date of the data.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.
vwap: Volume Weighted Average Price over the period.
adj_close: The adjusted close price. (provider: fmp)
change: Change in the price from the previous close. (provider: fmp)
change_percent: Change in the price from the previous close, as a normalized percent. (provider: fmp)
transactions: Number of transactions for the symbol in the time period. (provider: polygon, tiingo)
volume_notional: The last size done for the asset on the specific date in the quote currency. The volume of the asset on the specific date in the quote currency. (provider: tiingo)

.currency.price.historical
    Currency Historical Price. Currency historical data.

        Currency historical prices refer to the past exchange rates of one currency against
        another over a specific period.
        This data provides insight into the fluctuations and trends in the foreign exchange market,
        helping analysts, traders, and economists understand currency performance,
        evaluate economic health, and make predictions about future movements.



        Examples
        --------
        >>> from openbb import obb
        >>> obb.currency.price.historical(symbol='EURUSD', provider='fmp')
        >>> # Filter historical data with specific start and end date.
        >>> obb.currency.price.historical(symbol='EURUSD', start_date='2023-01-01', end_date='2023-12-31', provider='fmp')
        >>> # Get data with different granularity.
        >>> obb.currency.price.historical(symbol='EURUSD', provider='polygon', interval='15m')

Outputs:
date: The date of the data.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.
vwap: Volume Weighted Average Price over the period.
adj_close: The adjusted close price. (provider: fmp)
change: Change in the price from the previous close. (provider: fmp)
change_percent: Change in the price from the previous close, as a normalized percent. (provider: fmp)
transactions: Number of transactions for the symbol in the time period. (provider: polygon)

.derivatives.futures.curve
Futures Term Structure, current or historical.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.derivatives.futures.curve(symbol='NG', provider='yfinance')

Outputs:
date: The date of the data.
expiration: Futures expiration month.
price: The price of the futures contract.

.derivatives.futures.historical
Historical futures prices.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.derivatives.futures.historical(symbol='ES', provider='yfinance')
        >>> # Enter multiple symbols.
        >>> obb.derivatives.futures.historical(symbol='ES,NQ', provider='yfinance')
        >>> # Enter expiration dates as "YYYY-MM".
        >>> obb.derivatives.futures.historical(symbol='ES', provider='yfinance', expiration='2025-12')

Outputs:
date: The date of the data.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.

.derivatives.options.chains
Get the complete options chain for a ticker.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.derivatives.options.chains(symbol='AAPL', provider='intrinio')
        >>> # Use the "date" parameter to get the end-of-day-data for a specific date, where supported.
        >>> obb.derivatives.options.chains(symbol='AAPL', date='2023-01-25', provider='intrinio')

Outputs:
underlying_symbol: Underlying symbol for the option.
underlying_price: Price of the underlying stock.
contract_symbol: Contract symbol for the option.
eod_date: Date for which the options chains are returned.
expiration: Expiration date of the contract.
dte: Days to expiration of the contract.
strike: Strike price of the contract.
option_type: Call or Put.
contract_size: Number of underlying units per contract.
open_interest: Open interest on the contract.
volume: The trading volume.
theoretical_price: Theoretical value of the option.
last_trade_price: Last trade price of the option.
last_trade_size: Last trade size of the option.
last_trade_time: The timestamp of the last trade.
tick: Whether the last tick was up or down in price.
bid: Current bid price for the option.
bid_size: Bid size for the option.
bid_time: The timestamp of the bid price.
bid_exchange: The exchange of the bid price.
ask: Current ask price for the option.
ask_size: Ask size for the option.
ask_time: The timestamp of the ask price.
ask_exchange: The exchange of the ask price.
mark: The mid-price between the latest bid and ask.
open: The open price.
open_bid: The opening bid price for the option that day.
open_ask: The opening ask price for the option that day.
high: The high price.
bid_high: The highest bid price for the option that day.
ask_high: The highest ask price for the option that day.
low: The low price.
bid_low: The lowest bid price for the option that day.
ask_low: The lowest ask price for the option that day.
close: The close price.
close_size: The closing trade size for the option that day.
close_time: The time of the closing price for the option that day.
close_bid: The closing bid price for the option that day.
close_bid_size: The closing bid size for the option that day.
close_bid_time: The time of the bid closing price for the option that day.
close_ask: The closing ask price for the option that day.
close_ask_size: The closing ask size for the option that day.
close_ask_time: The time of the ask closing price for the option that day.
prev_close: The previous close price.
change: The change in the price of the option.
change_percent: Change, in normalized percentage points, of the option.
implied_volatility: Implied volatility of the option.
delta: Delta of the option.
gamma: Gamma of the option.
theta: Theta of the option.
vega: Vega of the option.
rho: Rho of the option.
in_the_money: Whether the option is in the money. (provider: yfinance)
currency: Currency of the option. (provider: yfinance)

.equity.discovery.active
Get the most actively traded stocks based on volume.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.active(provider='yfinance')
        >>> obb.equity.discovery.active(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.discovery.aggressive_small_caps
Get top small cap stocks based on earnings growth.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.aggressive_small_caps(provider='yfinance')
        >>> obb.equity.discovery.aggressive_small_caps(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.discovery.gainers
Get the top price gainers in the stock market.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.gainers(provider='yfinance')
        >>> obb.equity.discovery.gainers(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.discovery.growth_tech
Get top tech stocks based on revenue and earnings growth.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.growth_tech(provider='yfinance')
        >>> obb.equity.discovery.growth_tech(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.discovery.losers
Get the top price losers in the stock market.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.losers(provider='yfinance')
        >>> obb.equity.discovery.losers(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.discovery.undervalued_growth
Get potentially undervalued growth stocks.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.undervalued_growth(provider='yfinance')
        >>> obb.equity.discovery.undervalued_growth(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.discovery.undervalued_large_caps
Get potentially undervalued large cap stocks.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.discovery.undervalued_large_caps(provider='yfinance')
        >>> obb.equity.discovery.undervalued_large_caps(sort='desc', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the entity.
price: Last price.
change: Change in price.
percent_change: Percent change.
volume: The trading volume.
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
market_cap: Market Cap. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange: Exchange where the stock is listed. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.equity.estimates.consensus
Get consensus price target and recommendation.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.estimates.consensus(symbol='AAPL', provider='fmp')
        >>> obb.equity.estimates.consensus(symbol='AAPL,MSFT', provider='yfinance')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: The company name
target_high: High target of the price target consensus.
target_low: Low target of the price target consensus.
target_consensus: Consensus target of the price target consensus.
target_median: Median target of the price target consensus.
standard_deviation: The standard deviation of target price estimates. (provider: intrinio)
total_anaylsts: The total number of target price estimates in consensus. (provider: intrinio)
raised: The number of analysts that have raised their target price estimates. (provider: intrinio)
lowered: The number of analysts that have lowered their target price estimates. (provider: intrinio)
most_recent_date: The date of the most recent estimate. (provider: intrinio)
industry_group_number: The Zacks industry group number. (provider: intrinio)
recommendation: Recommendation - buy, sell, etc. (provider: yfinance)
recommendation_mean: Mean recommendation score where 1 is strong buy and 5 is strong sell. (provider: yfinance)
number_of_analysts: Number of analysts providing opinions. (provider: yfinance)
current_price: Current price of the stock. (provider: yfinance)
currency: Currency the stock is priced in. (provider: yfinance)

.equity.fundamental.balance
Get the balance sheet for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.fundamental.balance(symbol='AAPL', provider='fmp')
        >>> obb.equity.fundamental.balance(symbol='AAPL', period='annual', limit=5, provider='intrinio')

Outputs:
period_ending: The end date of the reporting period.
fiscal_period: The fiscal period of the report.
fiscal_year: The fiscal year of the fiscal period.
filing_date: The date when the filing was made. (provider: fmp)
accepted_date: The date and time when the filing was accepted. (provider: fmp)
reported_currency: The currency in which the balance sheet was reported. (provider: fmp, intrinio)
cash_and_cash_equivalents: Cash and cash equivalents. (provider: fmp, intrinio)
short_term_investments: Short term investments. (provider: fmp, intrinio)
cash_and_short_term_investments: Cash and short term investments. (provider: fmp)
net_receivables: Net receivables. (provider: fmp)
inventory: Inventory. (provider: fmp, polygon)
other_current_assets: Other current assets. (provider: fmp, intrinio, polygon)
total_current_assets: Total current assets. (provider: fmp, intrinio, polygon)
plant_property_equipment_net: Plant property equipment net. (provider: fmp, intrinio)
goodwill: Goodwill. (provider: fmp, intrinio)
intangible_assets: Intangible assets. (provider: fmp, intrinio, polygon)
goodwill_and_intangible_assets: Goodwill and intangible assets. (provider: fmp)
long_term_investments: Long term investments. (provider: fmp, intrinio)
tax_assets: Tax assets. (provider: fmp)
other_non_current_assets: Other non current assets. (provider: fmp, polygon)
non_current_assets: Total non current assets. (provider: fmp)
other_assets: Other assets. (provider: fmp, intrinio)
total_assets: Total assets. (provider: fmp, intrinio, polygon)
accounts_payable: Accounts payable. (provider: fmp, intrinio, polygon)
short_term_debt: Short term debt. (provider: fmp, intrinio)
tax_payables: Tax payables. (provider: fmp)
current_deferred_revenue: Current deferred revenue. (provider: fmp, intrinio)
other_current_liabilities: Other current liabilities. (provider: fmp, intrinio, polygon)
total_current_liabilities: Total current liabilities. (provider: fmp, intrinio, polygon)
long_term_debt: Long term debt. (provider: fmp, intrinio, polygon)
deferred_revenue_non_current: Non current deferred revenue. (provider: fmp)
deferred_tax_liabilities_non_current: Deferred tax liabilities non current. (provider: fmp)
other_non_current_liabilities: Other non current liabilities. (provider: fmp, polygon)
total_non_current_liabilities: Total non current liabilities. (provider: fmp, intrinio, polygon)
other_liabilities: Other liabilities. (provider: fmp)
capital_lease_obligations: Capital lease obligations. (provider: fmp, intrinio)
total_liabilities: Total liabilities. (provider: fmp, intrinio, polygon)
preferred_stock: Preferred stock. (provider: fmp, intrinio, polygon)
common_stock: Common stock. (provider: fmp, intrinio)
retained_earnings: Retained earnings. (provider: fmp, intrinio)
accumulated_other_comprehensive_income: Accumulated other comprehensive income (loss). (provider: fmp, intrinio)
other_shareholders_equity: Other shareholders equity. (provider: fmp)
other_total_shareholders_equity: Other total shareholders equity. (provider: fmp)
total_common_equity: Total common equity. (provider: fmp, intrinio)
total_equity_non_controlling_interests: Total equity non controlling interests. (provider: fmp, intrinio)
total_liabilities_and_shareholders_equity: Total liabilities and shareholders equity. (provider: fmp, polygon)
minority_interest: Minority interest. (provider: fmp, polygon)
total_liabilities_and_total_equity: Total liabilities and total equity. (provider: fmp)
total_investments: Total investments. (provider: fmp)
total_debt: Total debt. (provider: fmp)
net_debt: Net debt. (provider: fmp)
link: Link to the filing. (provider: fmp)
final_link: Link to the filing document. (provider: fmp)
cash_and_due_from_banks: Cash and due from banks. (provider: intrinio)
restricted_cash: Restricted cash. (provider: intrinio)
federal_funds_sold: Federal funds sold. (provider: intrinio)
accounts_receivable: Accounts receivable. (provider: intrinio, polygon)
note_and_lease_receivable: Note and lease receivable. (Vendor non-trade receivables) (provider: intrinio)
inventories: Net Inventories. (provider: intrinio)
customer_and_other_receivables: Customer and other receivables. (provider: intrinio)
interest_bearing_deposits_at_other_banks: Interest bearing deposits at other banks. (provider: intrinio)
time_deposits_placed_and_other_short_term_investments: Time deposits placed and other short term investments. (provider: intrinio)
trading_account_securities: Trading account securities. (provider: intrinio)
loans_and_leases: Loans and leases. (provider: intrinio)
allowance_for_loan_and_lease_losses: Allowance for loan and lease losses. (provider: intrinio)
current_deferred_refundable_income_taxes: Current deferred refundable income taxes. (provider: intrinio)
loans_and_leases_net_of_allowance: Loans and leases net of allowance. (provider: intrinio)
accrued_investment_income: Accrued investment income. (provider: intrinio)
other_current_non_operating_assets: Other current non-operating assets. (provider: intrinio)
loans_held_for_sale: Loans held for sale. (provider: intrinio)
prepaid_expenses: Prepaid expenses. (provider: intrinio, polygon)
plant_property_equipment_gross: Plant property equipment gross. (provider: intrinio)
accumulated_depreciation: Accumulated depreciation. (provider: intrinio)
premises_and_equipment_net: Net premises and equipment. (provider: intrinio)
mortgage_servicing_rights: Mortgage servicing rights. (provider: intrinio)
unearned_premiums_asset: Unearned premiums asset. (provider: intrinio)
non_current_note_lease_receivables: Non-current note lease receivables. (provider: intrinio)
deferred_acquisition_cost: Deferred acquisition cost. (provider: intrinio)
separate_account_business_assets: Separate account business assets. (provider: intrinio)
non_current_deferred_refundable_income_taxes: Noncurrent deferred refundable income taxes. (provider: intrinio)
employee_benefit_assets: Employee benefit assets. (provider: intrinio)
other_non_current_operating_assets: Other noncurrent operating assets. (provider: intrinio)
other_non_current_non_operating_assets: Other noncurrent non-operating assets. (provider: intrinio)
interest_bearing_deposits: Interest bearing deposits. (provider: intrinio)
total_non_current_assets: Total noncurrent assets. (provider: intrinio, polygon)
non_interest_bearing_deposits: Non interest bearing deposits. (provider: intrinio)
federal_funds_purchased_and_securities_sold: Federal funds purchased and securities sold. (provider: intrinio)
bankers_acceptance_outstanding: Bankers acceptance outstanding. (provider: intrinio)
current_deferred_payable_income_tax_liabilities: Current deferred payable income tax liabilities. (provider: intrinio)
accrued_interest_payable: Accrued interest payable. (provider: intrinio)
accrued_expenses: Accrued expenses. (provider: intrinio)
other_short_term_payables: Other short term payables. (provider: intrinio)
customer_deposits: Customer deposits. (provider: intrinio)
dividends_payable: Dividends payable. (provider: intrinio)
claims_and_claim_expense: Claims and claim expense. (provider: intrinio)
future_policy_benefits: Future policy benefits. (provider: intrinio)
current_employee_benefit_liabilities: Current employee benefit liabilities. (provider: intrinio)
unearned_premiums_liability: Unearned premiums liability. (provider: intrinio)
other_taxes_payable: Other taxes payable. (provider: intrinio)
policy_holder_funds: Policy holder funds. (provider: intrinio)
other_current_non_operating_liabilities: Other current non-operating liabilities. (provider: intrinio)
separate_account_business_liabilities: Separate account business liabilities. (provider: intrinio)
other_long_term_liabilities: Other long term liabilities. (provider: intrinio)
non_current_deferred_revenue: Non-current deferred revenue. (provider: intrinio)
non_current_deferred_payable_income_tax_liabilities: Non-current deferred payable income tax liabilities. (provider: intrinio)
non_current_employee_benefit_liabilities: Non-current employee benefit liabilities. (provider: intrinio)
other_non_current_operating_liabilities: Other non-current operating liabilities. (provider: intrinio)
other_non_current_non_operating_liabilities: Other non-current, non-operating liabilities. (provider: intrinio)
asset_retirement_reserve_litigation_obligation: Asset retirement reserve litigation obligation. (provider: intrinio)
commitments_contingencies: Commitments contingencies. (provider: intrinio)
redeemable_non_controlling_interest: Redeemable non-controlling interest. (provider: intrinio, polygon)
treasury_stock: Treasury stock. (provider: intrinio)
participating_policy_holder_equity: Participating policy holder equity. (provider: intrinio)
other_equity_adjustments: Other equity adjustments. (provider: intrinio)
total_preferred_common_equity: Total preferred common equity. (provider: intrinio)
non_controlling_interest: Non-controlling interest. (provider: intrinio)
total_liabilities_shareholders_equity: Total liabilities and shareholders equity. (provider: intrinio)
marketable_securities: Marketable securities (provider: polygon)
property_plant_equipment_net: Property plant and equipment net (provider: polygon)
employee_wages: Employee wages (provider: polygon)
temporary_equity_attributable_to_parent: Temporary equity attributable to parent (provider: polygon)
equity_attributable_to_parent: Equity attributable to parent (provider: polygon)
temporary_equity: Temporary equity (provider: polygon)
redeemable_non_controlling_interest_other: Redeemable non-controlling interest other (provider: polygon)
total_shareholders_equity: Total stock holders equity (provider: polygon)
total_equity: Total equity (provider: polygon)

.equity.fundamental.cash
Get the cash flow statement for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.fundamental.cash(symbol='AAPL', provider='fmp')
        >>> obb.equity.fundamental.cash(symbol='AAPL', period='annual', limit=5, provider='intrinio')

Outputs:
period_ending: The end date of the reporting period.
fiscal_period: The fiscal period of the report.
fiscal_year: The fiscal year of the fiscal period.
filing_date: The date of the filing. (provider: fmp)
accepted_date: The date the filing was accepted. (provider: fmp)
reported_currency: The currency in which the cash flow statement was reported. (provider: fmp);
    The currency in which the balance sheet is reported. (provider: intrinio)
net_income: Net income. (provider: fmp);
    Consolidated Net Income. (provider: intrinio)
depreciation_and_amortization: Depreciation and amortization. (provider: fmp)
deferred_income_tax: Deferred income tax. (provider: fmp)
stock_based_compensation: Stock-based compensation. (provider: fmp)
change_in_working_capital: Change in working capital. (provider: fmp)
change_in_account_receivables: Change in account receivables. (provider: fmp)
change_in_inventory: Change in inventory. (provider: fmp)
change_in_account_payable: Change in account payable. (provider: fmp)
change_in_other_working_capital: Change in other working capital. (provider: fmp)
change_in_other_non_cash_items: Change in other non-cash items. (provider: fmp)
net_cash_from_operating_activities: Net cash from operating activities. (provider: fmp, intrinio)
purchase_of_property_plant_and_equipment: Purchase of property, plant and equipment. (provider: fmp, intrinio)
acquisitions: Acquisitions. (provider: fmp, intrinio)
purchase_of_investment_securities: Purchase of investment securities. (provider: fmp, intrinio)
sale_and_maturity_of_investments: Sale and maturity of investments. (provider: fmp, intrinio)
other_investing_activities: Other investing activities. (provider: fmp, intrinio)
net_cash_from_investing_activities: Net cash from investing activities. (provider: fmp, intrinio)
repayment_of_debt: Repayment of debt. (provider: fmp, intrinio)
issuance_of_common_equity: Issuance of common equity. (provider: fmp, intrinio)
repurchase_of_common_equity: Repurchase of common equity. (provider: fmp, intrinio)
payment_of_dividends: Payment of dividends. (provider: fmp, intrinio)
other_financing_activities: Other financing activities. (provider: fmp, intrinio)
net_cash_from_financing_activities: Net cash from financing activities. (provider: fmp, intrinio)
effect_of_exchange_rate_changes_on_cash: Effect of exchange rate changes on cash. (provider: fmp)
net_change_in_cash_and_equivalents: Net change in cash and equivalents. (provider: fmp, intrinio)
cash_at_beginning_of_period: Cash at beginning of period. (provider: fmp)
cash_at_end_of_period: Cash at end of period. (provider: fmp)
operating_cash_flow: Operating cash flow. (provider: fmp)
capital_expenditure: Capital expenditure. (provider: fmp)
free_cash_flow: None
link: Link to the filing. (provider: fmp)
final_link: Link to the filing document. (provider: fmp)
net_income_continuing_operations: Net Income (Continuing Operations) (provider: intrinio)
net_income_discontinued_operations: Net Income (Discontinued Operations) (provider: intrinio)
provision_for_loan_losses: Provision for Loan Losses (provider: intrinio)
provision_for_credit_losses: Provision for credit losses (provider: intrinio)
depreciation_expense: Depreciation Expense. (provider: intrinio)
amortization_expense: Amortization Expense. (provider: intrinio)
share_based_compensation: Share-based compensation. (provider: intrinio)
non_cash_adjustments_to_reconcile_net_income: Non-Cash Adjustments to Reconcile Net Income. (provider: intrinio)
changes_in_operating_assets_and_liabilities: Changes in Operating Assets and Liabilities (Net) (provider: intrinio)
net_cash_from_continuing_operating_activities: Net Cash from Continuing Operating Activities (provider: intrinio)
net_cash_from_discontinued_operating_activities: Net Cash from Discontinued Operating Activities (provider: intrinio)
divestitures: Divestitures (provider: intrinio)
sale_of_property_plant_and_equipment: Sale of Property, Plant, and Equipment (provider: intrinio)
purchase_of_investments: Purchase of Investments (provider: intrinio)
loans_held_for_sale: Loans Held for Sale (Net) (provider: intrinio)
net_cash_from_continuing_investing_activities: Net Cash from Continuing Investing Activities (provider: intrinio)
net_cash_from_discontinued_investing_activities: Net Cash from Discontinued Investing Activities (provider: intrinio)
repurchase_of_preferred_equity: Repurchase of Preferred Equity (provider: intrinio)
issuance_of_preferred_equity: Issuance of Preferred Equity (provider: intrinio)
issuance_of_debt: Issuance of Debt (provider: intrinio)
cash_interest_received: Cash Interest Received (provider: intrinio)
net_change_in_deposits: Net Change in Deposits (provider: intrinio)
net_increase_in_fed_funds_sold: Net Increase in Fed Funds Sold (provider: intrinio)
net_cash_from_continuing_financing_activities: Net Cash from Continuing Financing Activities (provider: intrinio)
net_cash_from_discontinued_financing_activities: Net Cash from Discontinued Financing Activities (provider: intrinio)
effect_of_exchange_rate_changes: Effect of Exchange Rate Changes (provider: intrinio)
other_net_changes_in_cash: Other Net Changes in Cash (provider: intrinio)
cash_income_taxes_paid: Cash Income Taxes Paid (provider: intrinio)
cash_interest_paid: Cash Interest Paid (provider: intrinio)
net_cash_flow_from_operating_activities_continuing: Net cash flow from operating activities continuing. (provider: polygon)
net_cash_flow_from_operating_activities_discontinued: Net cash flow from operating activities discontinued. (provider: polygon)
net_cash_flow_from_operating_activities: Net cash flow from operating activities. (provider: polygon)
net_cash_flow_from_investing_activities_continuing: Net cash flow from investing activities continuing. (provider: polygon)
net_cash_flow_from_investing_activities_discontinued: Net cash flow from investing activities discontinued. (provider: polygon)
net_cash_flow_from_investing_activities: Net cash flow from investing activities. (provider: polygon)
net_cash_flow_from_financing_activities_continuing: Net cash flow from financing activities continuing. (provider: polygon)
net_cash_flow_from_financing_activities_discontinued: Net cash flow from financing activities discontinued. (provider: polygon)
net_cash_flow_from_financing_activities: Net cash flow from financing activities. (provider: polygon)
net_cash_flow_continuing: Net cash flow continuing. (provider: polygon)
net_cash_flow_discontinued: Net cash flow discontinued. (provider: polygon)
exchange_gains_losses: Exchange gains losses. (provider: polygon)
net_cash_flow: Net cash flow. (provider: polygon)

.equity.fundamental.dividends
Get historical dividend data for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.fundamental.dividends(symbol='AAPL', provider='intrinio')

Outputs:
ex_dividend_date: The ex-dividend date - the date on which the stock begins trading without rights to the dividend.
amount: The dividend amount per share.
label: Label of the historical dividends. (provider: fmp)
adj_dividend: Adjusted dividend of the historical dividends. (provider: fmp)
record_date: Record date of the historical dividends. (provider: fmp)
payment_date: Payment date of the historical dividends. (provider: fmp)
declaration_date: Declaration date of the historical dividends. (provider: fmp)
factor: factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices. (provider: intrinio)
currency: The currency in which the dividend is paid. (provider: intrinio)
split_ratio: The ratio of the stock split, if a stock split occurred. (provider: intrinio)

.equity.fundamental.income
Get the income statement for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.fundamental.income(symbol='AAPL', provider='fmp')
        >>> obb.equity.fundamental.income(symbol='AAPL', period='annual', limit=5, provider='intrinio')

Outputs:
period_ending: The end date of the reporting period.
fiscal_period: The fiscal period of the report.
fiscal_year: The fiscal year of the fiscal period.
filing_date: The date when the filing was made. (provider: fmp)
accepted_date: The date and time when the filing was accepted. (provider: fmp)
reported_currency: The currency in which the balance sheet was reported. (provider: fmp, intrinio)
revenue: Total revenue. (provider: fmp, intrinio, polygon)
cost_of_revenue: Cost of revenue. (provider: fmp, intrinio, polygon)
gross_profit: Gross profit. (provider: fmp, intrinio, polygon)
gross_profit_margin: Gross profit margin. (provider: fmp);
    Gross margin ratio. (provider: intrinio)
general_and_admin_expense: General and administrative expenses. (provider: fmp)
research_and_development_expense: Research and development expenses. (provider: fmp, intrinio)
selling_and_marketing_expense: Selling and marketing expenses. (provider: fmp)
selling_general_and_admin_expense: Selling, general and administrative expenses. (provider: fmp, intrinio)
other_expenses: Other expenses. (provider: fmp)
total_operating_expenses: Total operating expenses. (provider: fmp, intrinio)
cost_and_expenses: Cost and expenses. (provider: fmp)
interest_income: Interest income. (provider: fmp)
total_interest_expense: Total interest expenses. (provider: fmp, intrinio);
    Interest Expense (provider: polygon)
depreciation_and_amortization: Depreciation and amortization. (provider: fmp, polygon)
ebitda: EBITDA. (provider: fmp);
    Earnings Before Interest, Taxes, Depreciation and Amortization. (provider: intrinio)
ebitda_margin: EBITDA margin. (provider: fmp);
    Margin on Earnings Before Interest, Taxes, Depreciation and Amortization. (provider: intrinio)
total_operating_income: Total operating income. (provider: fmp, intrinio)
operating_income_margin: Operating income margin. (provider: fmp)
total_other_income_expenses: Total other income and expenses. (provider: fmp)
total_pre_tax_income: Total pre-tax income. (provider: fmp, intrinio);
    Income Before Tax (provider: polygon)
pre_tax_income_margin: Pre-tax income margin. (provider: fmp, intrinio)
income_tax_expense: Income tax expense. (provider: fmp, intrinio, polygon)
consolidated_net_income: Consolidated net income. (provider: fmp, intrinio);
    Net Income/Loss (provider: polygon)
net_income_margin: Net income margin. (provider: fmp)
basic_earnings_per_share: Basic earnings per share. (provider: fmp, intrinio);
    Earnings Per Share (provider: polygon)
diluted_earnings_per_share: Diluted earnings per share. (provider: fmp, intrinio, polygon)
weighted_average_basic_shares_outstanding: Weighted average basic shares outstanding. (provider: fmp, intrinio);
    Basic Average Shares (provider: polygon)
weighted_average_diluted_shares_outstanding: Weighted average diluted shares outstanding. (provider: fmp, intrinio);
    Diluted Average Shares (provider: polygon)
link: Link to the filing. (provider: fmp)
final_link: Link to the filing document. (provider: fmp)
operating_revenue: Total operating revenue (provider: intrinio)
operating_cost_of_revenue: Total operating cost of revenue (provider: intrinio)
provision_for_credit_losses: Provision for credit losses (provider: intrinio)
salaries_and_employee_benefits: Salaries and employee benefits (provider: intrinio)
marketing_expense: Marketing expense (provider: intrinio)
net_occupancy_and_equipment_expense: Net occupancy and equipment expense (provider: intrinio)
other_operating_expenses: Other operating expenses (provider: intrinio, polygon)
depreciation_expense: Depreciation expense (provider: intrinio)
amortization_expense: Amortization expense (provider: intrinio)
amortization_of_deferred_policy_acquisition_costs: Amortization of deferred policy acquisition costs (provider: intrinio)
exploration_expense: Exploration expense (provider: intrinio)
depletion_expense: Depletion expense (provider: intrinio)
deposits_and_money_market_investments_interest_income: Deposits and money market investments interest income (provider: intrinio)
federal_funds_sold_and_securities_borrowed_interest_income: Federal funds sold and securities borrowed interest income (provider: intrinio)
investment_securities_interest_income: Investment securities interest income (provider: intrinio)
loans_and_leases_interest_income: Loans and leases interest income (provider: intrinio)
trading_account_interest_income: Trading account interest income (provider: intrinio)
other_interest_income: Other interest income (provider: intrinio)
total_non_interest_income: Total non-interest income (provider: intrinio)
interest_and_investment_income: Interest and investment income (provider: intrinio)
short_term_borrowings_interest_expense: Short-term borrowings interest expense (provider: intrinio)
long_term_debt_interest_expense: Long-term debt interest expense (provider: intrinio)
capitalized_lease_obligations_interest_expense: Capitalized lease obligations interest expense (provider: intrinio)
deposits_interest_expense: Deposits interest expense (provider: intrinio)
federal_funds_purchased_and_securities_sold_interest_expense: Federal funds purchased and securities sold interest expense (provider: intrinio)
other_interest_expense: Other interest expense (provider: intrinio)
net_interest_income: Net interest income (provider: intrinio);
    Interest Income Net (provider: polygon)
other_non_interest_income: Other non-interest income (provider: intrinio)
investment_banking_income: Investment banking income (provider: intrinio)
trust_fees_by_commissions: Trust fees by commissions (provider: intrinio)
premiums_earned: Premiums earned (provider: intrinio)
insurance_policy_acquisition_costs: Insurance policy acquisition costs (provider: intrinio)
current_and_future_benefits: Current and future benefits (provider: intrinio)
property_and_liability_insurance_claims: Property and liability insurance claims (provider: intrinio)
total_non_interest_expense: Total non-interest expense (provider: intrinio)
net_realized_and_unrealized_capital_gains_on_investments: Net realized and unrealized capital gains on investments (provider: intrinio)
other_gains: Other gains (provider: intrinio)
non_operating_income: Non-operating income (provider: intrinio);
    Non Operating Income/Loss (provider: polygon)
other_income: Other income (provider: intrinio)
other_revenue: Other revenue (provider: intrinio)
extraordinary_income: Extraordinary income (provider: intrinio)
total_other_income: Total other income (provider: intrinio)
ebit: Earnings Before Interest and Taxes. (provider: intrinio)
impairment_charge: Impairment charge (provider: intrinio)
restructuring_charge: Restructuring charge (provider: intrinio)
service_charges_on_deposit_accounts: Service charges on deposit accounts (provider: intrinio)
other_service_charges: Other service charges (provider: intrinio)
other_special_charges: Other special charges (provider: intrinio)
other_cost_of_revenue: Other cost of revenue (provider: intrinio)
net_income_continuing_operations: Net income (continuing operations) (provider: intrinio)
net_income_discontinued_operations: Net income (discontinued operations) (provider: intrinio)
other_adjustments_to_consolidated_net_income: Other adjustments to consolidated net income (provider: intrinio)
other_adjustment_to_net_income_attributable_to_common_shareholders: Other adjustment to net income attributable to common shareholders (provider: intrinio)
net_income_attributable_to_noncontrolling_interest: Net income attributable to noncontrolling interest (provider: intrinio)
net_income_attributable_to_common_shareholders: Net income attributable to common shareholders (provider: intrinio);
    Net Income/Loss Available To Common Stockholders Basic (provider: polygon)
basic_and_diluted_earnings_per_share: Basic and diluted earnings per share (provider: intrinio)
cash_dividends_to_common_per_share: Cash dividends to common per share (provider: intrinio)
preferred_stock_dividends_declared: Preferred stock dividends declared (provider: intrinio)
weighted_average_basic_and_diluted_shares_outstanding: Weighted average basic and diluted shares outstanding (provider: intrinio)
cost_of_revenue_goods: Cost of Revenue - Goods (provider: polygon)
cost_of_revenue_services: Cost of Revenue - Services (provider: polygon)
provisions_for_loan_lease_and_other_losses: Provisions for loan lease and other losses (provider: polygon)
income_tax_expense_benefit_current: Income tax expense benefit current (provider: polygon)
deferred_tax_benefit: Deferred tax benefit (provider: polygon)
benefits_costs_expenses: Benefits, costs and expenses (provider: polygon)
selling_general_and_administrative_expense: Selling, general and administrative expense (provider: polygon)
research_and_development: Research and development (provider: polygon)
costs_and_expenses: Costs and expenses (provider: polygon)
operating_expenses: Operating expenses (provider: polygon)
operating_income: Operating Income/Loss (provider: polygon)
interest_and_dividend_income: Interest and Dividend Income (provider: polygon)
interest_and_debt_expense: Interest and Debt Expense (provider: polygon)
interest_income_after_provision_for_losses: Interest Income After Provision for Losses (provider: polygon)
non_interest_expense: Non-Interest Expense (provider: polygon)
non_interest_income: Non-Interest Income (provider: polygon)
income_from_discontinued_operations_net_of_tax_on_disposal: Income From Discontinued Operations Net of Tax on Disposal (provider: polygon)
income_from_discontinued_operations_net_of_tax: Income From Discontinued Operations Net of Tax (provider: polygon)
income_before_equity_method_investments: Income Before Equity Method Investments (provider: polygon)
income_from_equity_method_investments: Income From Equity Method Investments (provider: polygon)
income_after_tax: Income After Tax (provider: polygon)
net_income_attributable_noncontrolling_interest: Net income (loss) attributable to noncontrolling interest (provider: polygon)
net_income_attributable_to_parent: Net income (loss) attributable to parent (provider: polygon)
participating_securities_earnings: Participating Securities Distributed And Undistributed Earnings Loss Basic (provider: polygon)
undistributed_earnings_allocated_to_participating_securities: Undistributed Earnings Allocated To Participating Securities (provider: polygon)
common_stock_dividends: Common Stock Dividends (provider: polygon)
preferred_stock_dividends_and_other_adjustments: Preferred stock dividends and other adjustments (provider: polygon)

.equity.fundamental.management
Get executive management team data for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.fundamental.management(symbol='AAPL', provider='fmp')

Outputs:
title: Designation of the key executive.
name: Name of the key executive.
pay: Pay of the key executive.
currency_pay: Currency of the pay.
gender: Gender of the key executive.
year_born: Birth year of the key executive.
title_since: Date the tile was held since.
exercised_value: Value of shares exercised. (provider: yfinance)
unexercised_value: Value of shares not exercised. (provider: yfinance)
fiscal_year: Fiscal year of the pay. (provider: yfinance)

.equity.fundamental.metrics
Get fundamental metrics for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.fundamental.metrics(symbol='AAPL', provider='fmp')
        >>> obb.equity.fundamental.metrics(symbol='AAPL', period='annual', limit=100, provider='intrinio')

Outputs:
symbol: Symbol representing the entity requested in the data.
market_cap: Market capitalization
pe_ratio: Price-to-earnings ratio (P/E ratio)
period_ending: Period ending date. (provider: fmp)
fiscal_period: Period of the data. (provider: fmp)
calendar_year: Calendar year for the fiscal period. (provider: fmp)
revenue_per_share: Revenue per share (provider: fmp, yfinance)
capex_per_share: Capital expenditures per share (provider: fmp)
net_income_per_share: Net income per share (provider: fmp)
operating_cash_flow_per_share: Operating cash flow per share (provider: fmp)
free_cash_flow_per_share: Free cash flow per share (provider: fmp)
cash_per_share: Cash per share (provider: fmp, yfinance)
book_value_per_share: Book value per share (provider: fmp)
tangible_book_value_per_share: Tangible book value per share (provider: fmp)
shareholders_equity_per_share: Shareholders equity per share (provider: fmp)
interest_debt_per_share: Interest debt per share (provider: fmp)
price_to_sales: Price-to-sales ratio (provider: fmp)
price_to_operating_cash_flow: Price-to-operating cash flow ratio (provider: fmp)
price_to_free_cash_flow: Price-to-free cash flow ratio (provider: fmp)
price_to_book: Price-to-book ratio (provider: fmp, intrinio, yfinance)
price_to_tangible_book: Price-to-tangible book ratio (provider: fmp, intrinio)
ev_to_sales: Enterprise value-to-sales ratio (provider: fmp)
ev_to_ebitda: Enterprise value-to-EBITDA ratio (provider: fmp)
ev_to_operating_cash_flow: Enterprise value-to-operating cash flow ratio (provider: fmp)
ev_to_free_cash_flow: Enterprise value-to-free cash flow ratio (provider: fmp)
earnings_yield: Earnings yield (provider: fmp);
    Earnings yield, as a normalized percent. (provider: intrinio)
free_cash_flow_yield: Free cash flow yield (provider: fmp)
debt_to_market_cap: Debt-to-market capitalization ratio (provider: fmp)
debt_to_equity: Debt-to-equity ratio (provider: fmp, yfinance)
debt_to_assets: Debt-to-assets ratio (provider: fmp)
net_debt_to_ebitda: Net debt-to-EBITDA ratio (provider: fmp)
current_ratio: Current ratio (provider: fmp, yfinance)
interest_coverage: Interest coverage (provider: fmp)
income_quality: Income quality (provider: fmp)
payout_ratio: Payout ratio (provider: fmp, yfinance)
sales_general_and_administrative_to_revenue: Sales general and administrative expenses-to-revenue ratio (provider: fmp)
research_and_development_to_revenue: Research and development expenses-to-revenue ratio (provider: fmp)
intangibles_to_total_assets: Intangibles-to-total assets ratio (provider: fmp)
capex_to_operating_cash_flow: Capital expenditures-to-operating cash flow ratio (provider: fmp)
capex_to_revenue: Capital expenditures-to-revenue ratio (provider: fmp)
capex_to_depreciation: Capital expenditures-to-depreciation ratio (provider: fmp)
stock_based_compensation_to_revenue: Stock-based compensation-to-revenue ratio (provider: fmp)
working_capital: Working capital (provider: fmp)
tangible_asset_value: Tangible asset value (provider: fmp)
net_current_asset_value: Net current asset value (provider: fmp)
enterprise_value: Enterprise value (provider: fmp, intrinio, yfinance)
invested_capital: Invested capital (provider: fmp)
average_receivables: Average receivables (provider: fmp)
average_payables: Average payables (provider: fmp)
average_inventory: Average inventory (provider: fmp)
days_sales_outstanding: Days sales outstanding (provider: fmp)
days_payables_outstanding: Days payables outstanding (provider: fmp)
days_of_inventory_on_hand: Days of inventory on hand (provider: fmp)
receivables_turnover: Receivables turnover (provider: fmp)
payables_turnover: Payables turnover (provider: fmp)
inventory_turnover: Inventory turnover (provider: fmp)
return_on_equity: Return on equity (provider: fmp);
    Return on equity, as a normalized percent. (provider: intrinio);
    Return on equity, as a normalized percent. (provider: yfinance)
return_on_invested_capital: Return on invested capital (provider: fmp);
    Return on invested capital, as a normalized percent. (provider: intrinio)
return_on_tangible_assets: Return on tangible assets (provider: fmp)
dividend_yield: Dividend yield, as a normalized percent. (provider: fmp, intrinio, yfinance)
graham_number: Graham number (provider: fmp)
graham_net_net: Graham net-net working capital (provider: fmp)
price_to_revenue: Price to revenue ratio. (provider: intrinio)
quick_ratio: Quick ratio. (provider: intrinio, yfinance)
gross_margin: Gross margin, as a normalized percent. (provider: intrinio, yfinance)
ebit_margin: EBIT margin, as a normalized percent. (provider: intrinio)
profit_margin: Profit margin, as a normalized percent. (provider: intrinio, yfinance)
eps: Basic earnings per share. (provider: intrinio)
eps_growth: EPS growth, as a normalized percent. (provider: intrinio)
revenue_growth: Revenue growth, as a normalized percent. (provider: intrinio, yfinance)
ebitda_growth: EBITDA growth, as a normalized percent. (provider: intrinio)
ebit_growth: EBIT growth, as a normalized percent. (provider: intrinio)
net_income_growth: Net income growth, as a normalized percent. (provider: intrinio)
free_cash_flow_to_firm_growth: Free cash flow to firm growth, as a normalized percent. (provider: intrinio)
invested_capital_growth: Invested capital growth, as a normalized percent. (provider: intrinio)
return_on_assets: Return on assets, as a normalized percent. (provider: intrinio, yfinance)
ebitda: Earnings before interest, taxes, depreciation, and amortization. (provider: intrinio)
ebit: Earnings before interest and taxes. (provider: intrinio)
long_term_debt: Long-term debt. (provider: intrinio)
total_debt: Total debt. (provider: intrinio)
total_capital: The sum of long-term debt and total shareholder equity. (provider: intrinio)
free_cash_flow_to_firm: Free cash flow to firm. (provider: intrinio)
altman_z_score: Altman Z-score. (provider: intrinio)
beta: Beta relative to the broad market (rolling three-year). (provider: intrinio);
    Beta relative to the broad market (5-year monthly). (provider: yfinance)
last_price: Last price of the stock. (provider: intrinio)
year_high: 52 week high (provider: intrinio)
year_low: 52 week low (provider: intrinio)
volume_avg: Average daily volume. (provider: intrinio)
short_interest: Number of shares reported as sold short. (provider: intrinio)
shares_outstanding: Weighted average shares outstanding (TTM). (provider: intrinio)
days_to_cover: Days to cover short interest, based on average daily volume. (provider: intrinio)
forward_pe: Forward price-to-earnings ratio. (provider: yfinance)
peg_ratio: PEG ratio (5-year expected). (provider: yfinance)
peg_ratio_ttm: PEG ratio (TTM). (provider: yfinance)
eps_ttm: Earnings per share (TTM). (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
enterprise_to_ebitda: Enterprise value to EBITDA ratio. (provider: yfinance)
earnings_growth: Earnings growth (Year Over Year), as a normalized percent. (provider: yfinance)
earnings_growth_quarterly: Quarterly earnings growth (Year Over Year), as a normalized percent. (provider: yfinance)
enterprise_to_revenue: Enterprise value to revenue ratio. (provider: yfinance)
operating_margin: Operating margin, as a normalized percent. (provider: yfinance)
ebitda_margin: EBITDA margin, as a normalized percent. (provider: yfinance)
dividend_yield_5y_avg: 5-year average dividend yield, as a normalized percent. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
overall_risk: Overall risk score. (provider: yfinance)
audit_risk: Audit risk score. (provider: yfinance)
board_risk: Board risk score. (provider: yfinance)
compensation_risk: Compensation risk score. (provider: yfinance)
shareholder_rights_risk: Shareholder rights risk score. (provider: yfinance)
price_return_1y: One-year price return, as a normalized percent. (provider: yfinance)
currency: Currency in which the data is presented. (provider: yfinance)

.equity.ownership.share_statistics
Get data about share float for a given company.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.ownership.share_statistics(symbol='AAPL', provider='fmp')

Outputs:
symbol: Symbol representing the entity requested in the data.
date: The date of the data.
free_float: Percentage of unrestricted shares of a publicly-traded company.
float_shares: Number of shares available for trading by the general public.
outstanding_shares: Total number of shares of a publicly-traded company.
source: Source of the received data.
adjusted_outstanding_shares: Total number of shares of a publicly-traded company, adjusted for splits. (provider: intrinio)
public_float: Aggregate market value of the shares of a publicly-traded company. (provider: intrinio)
implied_shares_outstanding: Implied Shares Outstanding of common equity, assuming the conversion of all convertible subsidiary equity into common. (provider: yfinance)
short_interest: Number of shares that are reported short. (provider: yfinance)
short_percent_of_float: Percentage of shares that are reported short, as a normalized percent. (provider: yfinance)
days_to_cover: Number of days to repurchase the shares as a ratio of average daily volume (provider: yfinance)
short_interest_prev_month: Number of shares that were reported short in the previous month. (provider: yfinance)
short_interest_prev_date: Date of the previous month's report. (provider: yfinance)
insider_ownership: Percentage of shares held by insiders, as a normalized percent. (provider: yfinance)
institution_ownership: Percentage of shares held by institutions, as a normalized percent. (provider: yfinance)
institution_float_ownership: Percentage of float held by institutions, as a normalized percent. (provider: yfinance)
institutions_count: Number of institutions holding shares. (provider: yfinance)

.equity.price.historical
Get historical price data for a given stock. This includes open, high, low, close, and volume.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.price.historical(symbol='AAPL', provider='fmp')
        >>> obb.equity.price.historical(symbol='AAPL', interval='1d', provider='intrinio')

Outputs:
date: The date of the data.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.
vwap: Volume Weighted Average Price over the period.
adj_close: The adjusted close price. (provider: fmp, intrinio, tiingo)
unadjusted_volume: Unadjusted volume of the symbol. (provider: fmp)
change: Change in the price from the previous close. (provider: fmp);
    Change in the price of the symbol from the previous day. (provider: intrinio)
change_percent: Change in the price from the previous close, as a normalized percent. (provider: fmp);
    Percent change in the price of the symbol from the previous day. (provider: intrinio)
average: Average trade price of an individual equity during the interval. (provider: intrinio)
adj_open: The adjusted open price. (provider: intrinio, tiingo)
adj_high: The adjusted high price. (provider: intrinio, tiingo)
adj_low: The adjusted low price. (provider: intrinio, tiingo)
adj_volume: The adjusted volume. (provider: intrinio, tiingo)
fifty_two_week_high: 52 week high price for the symbol. (provider: intrinio)
fifty_two_week_low: 52 week low price for the symbol. (provider: intrinio)
factor: factor by which to multiply equity prices before this date, in order to calculate historically-adjusted equity prices. (provider: intrinio)
split_ratio: Ratio of the equity split, if a split occurred. (provider: intrinio, tiingo, yfinance)
dividend: Dividend amount, if a dividend was paid. (provider: intrinio, tiingo, yfinance)
close_time: The timestamp that represents the end of the interval span. (provider: intrinio)
interval: The data time frequency. (provider: intrinio)
intra_period: If true, the equity price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period (provider: intrinio)
transactions: Number of transactions for the symbol in the time period. (provider: polygon)

.equity.price.quote
Get the latest quote for a given stock. Quote includes price, volume, and other data.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.price.quote(symbol='AAPL', provider='fmp')

Outputs:
symbol: Symbol representing the entity requested in the data.
asset_type: Type of asset - i.e, stock, ETF, etc.
name: Name of the company or asset.
exchange: The name or symbol of the venue where the data is from.
bid: Price of the top bid order.
bid_size: This represents the number of round lot orders at the given price. The normal round lot size is 100 shares. A size of 2 means there are 200 shares available at the given price.
bid_exchange: The specific trading venue where the purchase order was placed.
ask: Price of the top ask order.
ask_size: This represents the number of round lot orders at the given price. The normal round lot size is 100 shares. A size of 2 means there are 200 shares available at the given price.
ask_exchange: The specific trading venue where the sale order was placed.
quote_conditions: Conditions or condition codes applicable to the quote.
quote_indicators: Indicators or indicator codes applicable to the participant quote related to the price bands for the issue, or the affect the quote has on the NBBO.
sales_conditions: Conditions or condition codes applicable to the sale.
sequence_number: The sequence number represents the sequence in which message events happened. These are increasing and unique per ticker symbol, but will not always be sequential (e.g., 1, 2, 6, 9, 10, 11).
market_center: The ID of the UTP participant that originated the message.
participant_timestamp: Timestamp for when the quote was generated by the exchange.
trf_timestamp: Timestamp for when the TRF (Trade Reporting Facility) received the message.
sip_timestamp: Timestamp for when the SIP (Security Information Processor) received the message from the exchange.
last_price: Price of the last trade.
last_tick: Whether the last sale was an up or down tick.
last_size: Size of the last trade.
last_timestamp: Date and Time when the last price was recorded.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.
exchange_volume: Volume of shares exchanged during the trading day on the specific exchange.
prev_close: The previous close price.
change: Change in price from previous close.
change_percent: Change in price as a normalized percentage.
year_high: The one year high (52W High).
year_low: The one year low (52W Low).
price_avg50: 50 day moving average price. (provider: fmp)
price_avg200: 200 day moving average price. (provider: fmp)
avg_volume: Average volume over the last 10 trading days. (provider: fmp)
market_cap: Market cap of the company. (provider: fmp)
shares_outstanding: Number of shares outstanding. (provider: fmp)
eps: Earnings per share. (provider: fmp)
pe: Price earnings ratio. (provider: fmp)
earnings_announcement: Upcoming earnings announcement date. (provider: fmp)
is_darkpool: Whether or not the current trade is from a darkpool. (provider: intrinio)
source: Source of the Intrinio data. (provider: intrinio)
updated_on: Date and Time when the data was last updated. (provider: intrinio)
security: Security details related to the quote. (provider: intrinio)
ma_50d: 50-day moving average price. (provider: yfinance)
ma_200d: 200-day moving average price. (provider: yfinance)
volume_average: Average daily trading volume. (provider: yfinance)
volume_average_10d: Average daily trading volume in the last 10 days. (provider: yfinance)
currency: Currency of the price. (provider: yfinance)

.equity.profile
Get general information about a company. This includes company name, industry, sector and price data.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.profile(symbol='AAPL', provider='fmp')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Common name of the company.
cik: Central Index Key (CIK) for the requested entity.
cusip: CUSIP identifier for the company.
isin: International Securities Identification Number.
lei: Legal Entity Identifier assigned to the company.
legal_name: Official legal name of the company.
stock_exchange: Stock exchange where the company is traded.
sic: Standard Industrial Classification code for the company.
short_description: Short description of the company.
long_description: Long description of the company.
ceo: Chief Executive Officer of the company.
company_url: URL of the company's website.
business_address: Address of the company's headquarters.
mailing_address: Mailing address of the company.
business_phone_no: Phone number of the company's headquarters.
hq_address1: Address of the company's headquarters.
hq_address2: Address of the company's headquarters.
hq_address_city: City of the company's headquarters.
hq_address_postal_code: Zip code of the company's headquarters.
hq_state: State of the company's headquarters.
hq_country: Country of the company's headquarters.
inc_state: State in which the company is incorporated.
inc_country: Country in which the company is incorporated.
employees: Number of employees working for the company.
entity_legal_form: Legal form of the company.
entity_status: Status of the company.
latest_filing_date: Date of the company's latest filing.
irs_number: IRS number assigned to the company.
sector: Sector in which the company operates.
industry_category: Category of industry in which the company operates.
industry_group: Group of industry in which the company operates.
template: Template used to standardize the company's financial statements.
standardized_active: Whether the company is active or not.
first_fundamental_date: Date of the company's first fundamental.
last_fundamental_date: Date of the company's last fundamental.
first_stock_price_date: Date of the company's first stock price.
last_stock_price_date: Date of the company's last stock price.
is_etf: If the symbol is an ETF. (provider: fmp)
is_actively_trading: If the company is actively trading. (provider: fmp)
is_adr: If the stock is an ADR. (provider: fmp)
is_fund: If the company is a fund. (provider: fmp)
image: Image of the company. (provider: fmp)
currency: Currency in which the stock is traded. (provider: fmp, yfinance)
market_cap: Market capitalization of the company. (provider: fmp);
    The market capitalization of the asset. (provider: yfinance)
last_price: The last traded price. (provider: fmp)
year_high: The one-year high of the price. (provider: fmp)
year_low: The one-year low of the price. (provider: fmp)
volume_avg: Average daily trading volume. (provider: fmp)
annualized_dividend_amount: The annualized dividend payment based on the most recent regular dividend payment. (provider: fmp)
beta: Beta of the stock relative to the market. (provider: fmp, yfinance)
id: Intrinio ID for the company. (provider: intrinio)
thea_enabled: Whether the company has been enabled for Thea. (provider: intrinio)
exchange_timezone: The timezone of the exchange. (provider: yfinance)
issue_type: The issuance type of the asset. (provider: yfinance)
shares_outstanding: The number of listed shares outstanding. (provider: yfinance)
shares_float: The number of shares in the public float. (provider: yfinance)
shares_implied_outstanding: Implied shares outstanding of common equityassuming the conversion of all convertible subsidiary equity into common. (provider: yfinance)
shares_short: The reported number of shares short. (provider: yfinance)
dividend_yield: The dividend yield of the asset, as a normalized percent. (provider: yfinance)

.equity.screener
Screen for companies meeting various criteria.

        These criteria include market cap, price, beta, volume, and dividend yield.



        Examples
        --------
        >>> from openbb import obb
        >>> obb.equity.screener(provider='fmp')

Outputs:
symbol: Symbol representing the entity requested in the data.
name: Name of the company.
market_cap: The market cap of ticker. (provider: fmp);
    Market Cap. (provider: yfinance)
sector: The sector the ticker belongs to. (provider: fmp)
industry: The industry ticker belongs to. (provider: fmp)
beta: The beta of the ETF. (provider: fmp)
price: The current price. (provider: fmp)
last_annual_dividend: The last annual amount dividend paid. (provider: fmp)
volume: The current trading volume. (provider: fmp)
exchange: The exchange code the asset trades on. (provider: fmp);
    Exchange where the stock is listed. (provider: yfinance)
exchange_name: The full name of the primary exchange. (provider: fmp)
country: The two-letter country abbreviation where the head office is located. (provider: fmp)
is_etf: Whether the ticker is an ETF. (provider: fmp)
actively_trading: Whether the ETF is actively trading. (provider: fmp)
open: Open price for the day. (provider: yfinance)
high: High price for the day. (provider: yfinance)
low: Low price for the day. (provider: yfinance)
previous_close: Previous close price. (provider: yfinance)
ma50: 50-day moving average. (provider: yfinance)
ma200: 200-day moving average. (provider: yfinance)
year_high: 52-week high. (provider: yfinance)
year_low: 52-week low. (provider: yfinance)
shares_outstanding: Shares outstanding. (provider: yfinance)
book_value: Book value per share. (provider: yfinance)
price_to_book: Price to book ratio. (provider: yfinance)
eps_ttm: Earnings per share over the trailing twelve months. (provider: yfinance)
eps_forward: Forward earnings per share. (provider: yfinance)
pe_forward: Forward price-to-earnings ratio. (provider: yfinance)
dividend_yield: Trailing twelve month dividend yield. (provider: yfinance)
exchange_timezone: Timezone of the exchange. (provider: yfinance)
earnings_date: Most recent earnings date. (provider: yfinance)
currency: Currency of the price data. (provider: yfinance)

.etf.historical
ETF Historical Market Price.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.etf.historical(symbol='SPY', provider='fmp')
        >>> obb.etf.historical(symbol='SPY', provider='yfinance')
        >>> # This function accepts multiple tickers.
        >>> obb.etf.historical(symbol='SPY,IWM,QQQ,DJIA', provider='yfinance')

Outputs:
date: The date of the data.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.
vwap: Volume Weighted Average Price over the period.
adj_close: The adjusted close price. (provider: fmp, intrinio, tiingo)
unadjusted_volume: Unadjusted volume of the symbol. (provider: fmp)
change: Change in the price from the previous close. (provider: fmp);
    Change in the price of the symbol from the previous day. (provider: intrinio)
change_percent: Change in the price from the previous close, as a normalized percent. (provider: fmp);
    Percent change in the price of the symbol from the previous day. (provider: intrinio)
average: Average trade price of an individual equity during the interval. (provider: intrinio)
adj_open: The adjusted open price. (provider: intrinio, tiingo)
adj_high: The adjusted high price. (provider: intrinio, tiingo)
adj_low: The adjusted low price. (provider: intrinio, tiingo)
adj_volume: The adjusted volume. (provider: intrinio, tiingo)
fifty_two_week_high: 52 week high price for the symbol. (provider: intrinio)
fifty_two_week_low: 52 week low price for the symbol. (provider: intrinio)
factor: factor by which to multiply equity prices before this date, in order to calculate historically-adjusted equity prices. (provider: intrinio)
split_ratio: Ratio of the equity split, if a split occurred. (provider: intrinio, tiingo, yfinance)
dividend: Dividend amount, if a dividend was paid. (provider: intrinio, tiingo, yfinance)
close_time: The timestamp that represents the end of the interval span. (provider: intrinio)
interval: The data time frequency. (provider: intrinio)
intra_period: If true, the equity price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period (provider: intrinio)
transactions: Number of transactions for the symbol in the time period. (provider: polygon)

.etf.info
ETF Information Overview.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.etf.info(symbol='SPY', provider='fmp')
        >>> # This function accepts multiple tickers.
        >>> obb.etf.info(symbol='SPY,IWM,QQQ,DJIA', provider='fmp')

Outputs:
symbol: Symbol representing the entity requested in the data. (ETF)
name: Name of the ETF.
description: Description of the fund.
inception_date: Inception date of the ETF.
issuer: Company of the ETF. (provider: fmp);
    Issuer of the ETF. (provider: intrinio)
cusip: CUSIP of the ETF. (provider: fmp)
isin: ISIN of the ETF. (provider: fmp);
    International Securities Identification Number (ISIN). (provider: intrinio)
domicile: Domicile of the ETF. (provider: fmp);
    2 letter ISO country code for the country where the ETP is domiciled. (provider: intrinio)
asset_class: Asset class of the ETF. (provider: fmp);
    Captures the underlying nature of the securities in the Exchanged Traded Product (ETP). (provider: intrinio)
aum: Assets under management. (provider: fmp)
nav: Net asset value of the ETF. (provider: fmp)
nav_currency: Currency of the ETF's net asset value. (provider: fmp)
expense_ratio: The expense ratio, as a normalized percent. (provider: fmp)
holdings_count: Number of holdings. (provider: fmp)
avg_volume: Average daily trading volume. (provider: fmp)
website: Website of the issuer. (provider: fmp)
fund_listing_date: The date on which the Exchange Traded Product (ETP) or share class of the ETP is listed on a specific exchange. (provider: intrinio)
data_change_date: The last date on which there was a change in a classifications data field for this ETF. (provider: intrinio)
etn_maturity_date: If the product is an ETN, this field identifies the maturity date for the ETN. (provider: intrinio)
is_listed: If true, the ETF is still listed on an exchange. (provider: intrinio)
close_date: The date on which the ETF was de-listed if it is no longer listed. (provider: intrinio)
exchange: The exchange Market Identifier Code (MIC). (provider: intrinio);
    The exchange the fund is listed on. (provider: yfinance)
ric: Reuters Instrument Code (RIC). (provider: intrinio)
sedol: Stock Exchange Daily Official List (SEDOL). (provider: intrinio)
figi_symbol: Financial Instrument Global Identifier (FIGI) symbol. (provider: intrinio)
share_class_figi: Financial Instrument Global Identifier (FIGI). (provider: intrinio)
firstbridge_id: The FirstBridge unique identifier for the Exchange Traded Fund (ETF). (provider: intrinio)
firstbridge_parent_id: The FirstBridge unique identifier for the parent Exchange Traded Fund (ETF), if applicable. (provider: intrinio)
intrinio_id: Intrinio unique identifier for the security. (provider: intrinio)
intraday_nav_symbol: Intraday Net Asset Value (NAV) symbol. (provider: intrinio)
primary_symbol: The primary ticker field is used for Exchange Traded Products (ETPs) that have multiple listings and share classes. If an ETP has multiple listings or share classes, the same primary ticker is assigned to all the listings and share classes. (provider: intrinio)
etp_structure_type: Classifies Exchange Traded Products (ETPs) into very broad categories based on its legal structure. (provider: intrinio)
legal_structure: Legal structure of the fund. (provider: intrinio)
etn_issuing_bank: If the product is an Exchange Traded Note (ETN), this field identifies the issuing bank. (provider: intrinio)
fund_family: This field identifies the fund family to which the ETF belongs, as categorized by the ETF Sponsor. (provider: intrinio);
    The fund family. (provider: yfinance)
investment_style: Investment style of the ETF. (provider: intrinio)
derivatives_based: This field is populated if the ETF holds either listed or over-the-counter derivatives in its portfolio. (provider: intrinio)
income_category: Identifies if an Exchange Traded Fund (ETF) falls into a category that is specifically designed to provide a high yield or income (provider: intrinio)
other_asset_types: If 'asset_class' field is classified as 'Other Asset Types' this field captures the specific category of the underlying assets. (provider: intrinio)
single_category_designation: This categorization is created for those users who want every ETF to be 'forced' into a single bucket, so that the assets for all categories will always sum to the total market. (provider: intrinio)
beta_type: This field identifies whether an ETF provides 'Traditional' beta exposure or 'Smart' beta exposure. ETFs that are active (i.e. non-indexed), leveraged / inverse or have a proprietary quant model (i.e. that don't provide indexed exposure to a targeted factor) are classified separately. (provider: intrinio)
beta_details: This field provides further detail within the traditional and smart beta categories. (provider: intrinio)
market_cap_range: Equity ETFs are classified as falling into categories based on the description of their investment strategy in the prospectus. Examples ('Mega Cap', 'Large Cap', 'Mid Cap', etc.) (provider: intrinio)
market_cap_weighting_type: For ETFs that take the value 'Market Cap Weighted' in the 'index_weighting_scheme' field, this field provides detail on the market cap weighting type. (provider: intrinio)
index_weighting_scheme: For ETFs that track an underlying index, this field provides detail on the index weighting type. (provider: intrinio)
index_linked: This field identifies whether an ETF is index linked or active. (provider: intrinio)
index_name: This field identifies the name of the underlying index tracked by the ETF, if applicable. (provider: intrinio)
index_symbol: This field identifies the OpenFIGI ticker for the Index underlying the ETF. (provider: intrinio)
parent_index: This field identifies the name of the parent index, which represents the broader universe from which the index underlying the ETF is created, if applicable. (provider: intrinio)
index_family: This field identifies the index family to which the index underlying the ETF belongs. The index family is represented as categorized by the index provider. (provider: intrinio)
broader_index_family: This field identifies the broader index family to which the index underlying the ETF belongs. The broader index family is represented as categorized by the index provider. (provider: intrinio)
index_provider: This field identifies the Index provider for the index underlying the ETF, if applicable. (provider: intrinio)
index_provider_code: This field provides the First Bridge code for each Index provider, corresponding to the index underlying the ETF if applicable. (provider: intrinio)
replication_structure: The replication structure of the Exchange Traded Product (ETP). (provider: intrinio)
growth_value_tilt: Classifies equity ETFs as either 'Growth' or Value' based on the stated style tilt in the ETF prospectus. Equity ETFs that do not have a stated style tilt are classified as 'Core / Blend'. (provider: intrinio)
growth_type: For ETFs that are classified as 'Growth' in 'growth_value_tilt', this field further identifies those where the stocks in the ETF are both selected and weighted based on their growth (style factor) scores. (provider: intrinio)
value_type: For ETFs that are classified as 'Value' in 'growth_value_tilt', this field further identifies those where the stocks in the ETF are both selected and weighted based on their value (style factor) scores. (provider: intrinio)
sector: For equity ETFs that aim to provide targeted exposure to a sector or industry, this field identifies the Sector that it provides the exposure to. (provider: intrinio)
industry: For equity ETFs that aim to provide targeted exposure to an industry, this field identifies the Industry that it provides the exposure to. (provider: intrinio)
industry_group: For equity ETFs that aim to provide targeted exposure to a sub-industry, this field identifies the sub-Industry that it provides the exposure to. (provider: intrinio)
cross_sector_theme: For equity ETFs that aim to provide targeted exposure to a specific investment theme that cuts across GICS sectors, this field identifies the specific cross-sector theme. Examples ('Agri-business', 'Natural Resources', 'Green Investing', etc.) (provider: intrinio)
natural_resources_type: For ETFs that are classified as 'Natural Resources' in the 'cross_sector_theme' field, this field provides further detail on the type of Natural Resources exposure. (provider: intrinio)
us_or_excludes_us: Takes the value of 'Domestic' for US exposure, 'International' for non-US exposure and 'Global' for exposure that includes all regions including the US. (provider: intrinio)
developed_emerging: This field identifies the stage of development of the markets that the ETF provides exposure to. (provider: intrinio)
specialized_region: This field is populated if the ETF provides targeted exposure to a specific type of geography-based grouping that does not fall into a specific country or continent grouping. Examples ('BRIC', 'Chindia', etc.) (provider: intrinio)
continent: This field is populated if the ETF provides targeted exposure to a specific continent or country within that Continent. (provider: intrinio)
latin_america_sub_group: For ETFs that are classified as 'Latin America' in the 'continent' field, this field provides further detail on the type of regional exposure. (provider: intrinio)
europe_sub_group: For ETFs that are classified as 'Europe' in the 'continent' field, this field provides further detail on the type of regional exposure. (provider: intrinio)
asia_sub_group: For ETFs that are classified as 'Asia' in the 'continent' field, this field provides further detail on the type of regional exposure. (provider: intrinio)
specific_country: This field is populated if the ETF provides targeted exposure to a specific country. (provider: intrinio)
china_listing_location: For ETFs that are classified as 'China' in the 'country' field, this field provides further detail on the type of exposure in the underlying securities. (provider: intrinio)
us_state: Takes the value of a US state if the ETF provides targeted exposure to the municipal bonds or equities of companies. (provider: intrinio)
real_estate: For ETFs that provide targeted real estate exposure, this field is populated if the ETF provides targeted exposure to a specific segment of the real estate market. (provider: intrinio)
fundamental_weighting_type: For ETFs that take the value 'Fundamental Weighted' in the 'index_weighting_scheme' field, this field provides detail on the fundamental weighting methodology. (provider: intrinio)
dividend_weighting_type: For ETFs that take the value 'Dividend Weighted' in the 'index_weighting_scheme' field, this field provides detail on the dividend weighting methodology. (provider: intrinio)
bond_type: For ETFs where 'asset_class_type' is 'Bonds', this field provides detail on the type of bonds held in the ETF. (provider: intrinio)
government_bond_types: For bond ETFs that take the value 'Treasury & Government' in 'bond_type', this field provides detail on the exposure. (provider: intrinio)
municipal_bond_region: For bond ETFs that take the value 'Municipal' in 'bond_type', this field provides additional detail on the geographic exposure. (provider: intrinio)
municipal_vrdo: For bond ETFs that take the value 'Municipal' in 'bond_type', this field identifies those ETFs that specifically provide exposure to Variable Rate Demand Obligations. (provider: intrinio)
mortgage_bond_types: For bond ETFs that take the value 'Mortgage' in 'bond_type', this field provides additional detail on the type of underlying securities. (provider: intrinio)
bond_tax_status: For all US bond ETFs, this field provides additional detail on the tax treatment of the underlying securities. (provider: intrinio)
credit_quality: For all bond ETFs, this field helps to identify if the ETF provides targeted exposure to securities of a specific credit quality range. (provider: intrinio)
average_maturity: For all bond ETFs, this field helps to identify if the ETF provides targeted exposure to securities of a specific maturity range. (provider: intrinio)
specific_maturity_year: For all bond ETFs that take the value 'Specific Maturity Year' in the 'average_maturity' field, this field specifies the calendar year. (provider: intrinio)
commodity_types: For ETFs where 'asset_class_type' is 'Commodities', this field provides detail on the type of commodities held in the ETF. (provider: intrinio)
energy_type: For ETFs where 'commodity_type' is 'Energy', this field provides detail on the type of energy exposure provided by the ETF. (provider: intrinio)
agricultural_type: For ETFs where 'commodity_type' is 'Agricultural', this field provides detail on the type of agricultural exposure provided by the ETF. (provider: intrinio)
livestock_type: For ETFs where 'commodity_type' is 'Livestock', this field provides detail on the type of livestock exposure provided by the ETF. (provider: intrinio)
metal_type: For ETFs where 'commodity_type' is 'Gold & Metals', this field provides detail on the type of exposure provided by the ETF. (provider: intrinio)
inverse_leveraged: This field is populated if the ETF provides inverse or leveraged exposure. (provider: intrinio)
target_date_multi_asset_type: For ETFs where 'asset_class_type' is 'Target Date / MultiAsset', this field provides detail on the type of commodities held in the ETF. (provider: intrinio)
currency_pair: This field is populated if the ETF's strategy involves providing exposure to the movements of a currency or involves hedging currency exposure. (provider: intrinio)
social_environmental_type: This field is populated if the ETF's strategy involves providing exposure to a specific social or environmental theme. (provider: intrinio)
clean_energy_type: This field is populated if the ETF has a value of 'Clean Energy' in the 'social_environmental_type' field. (provider: intrinio)
dividend_type: This field is populated if the ETF has an intended investment objective of holding dividend-oriented stocks as stated in the prospectus. (provider: intrinio)
regular_dividend_payor_type: This field is populated if the ETF has a value of'Dividend - Regular Payors' in the 'dividend_type' field. (provider: intrinio)
quant_strategies_type: This field is populated if the ETF has either an index-linked or active strategy that is based on a proprietary quantitative strategy. (provider: intrinio)
other_quant_models: For ETFs where 'quant_strategies_type' is 'Other Quant Model', this field provides the name of the specific proprietary quant model used as the underlying strategy for the ETF. (provider: intrinio)
hedge_fund_type: For ETFs where 'other_asset_types' is 'Hedge Fund Replication', this field provides detail on the type of hedge fund replication strategy. (provider: intrinio)
excludes_financials: For equity ETFs, identifies those ETFs where the underlying fund holdings will not hold financials stocks, based on the funds intended objective. (provider: intrinio)
excludes_technology: For equity ETFs, identifies those ETFs where the underlying fund holdings will not hold technology stocks, based on the funds intended objective. (provider: intrinio)
holds_only_nyse_stocks: If true, the ETF is an equity ETF and holds only stocks listed on NYSE. (provider: intrinio)
holds_only_nasdaq_stocks: If true, the ETF is an equity ETF and holds only stocks listed on Nasdaq. (provider: intrinio)
holds_mlp: If true, the ETF's investment objective explicitly specifies that it holds MLPs as an intended part of its investment strategy. (provider: intrinio)
holds_preferred_stock: If true, the ETF's investment objective explicitly specifies that it holds preferred stock as an intended part of its investment strategy. (provider: intrinio)
holds_closed_end_funds: If true, the ETF's investment objective explicitly specifies that it holds closed end funds as an intended part of its investment strategy. (provider: intrinio)
holds_adr: If true, he ETF's investment objective explicitly specifies that it holds American Depositary Receipts (ADRs) as an intended part of its investment strategy. (provider: intrinio)
laddered: For bond ETFs, this field identifies those ETFs that specifically hold bonds in a laddered structure, where the bonds are scheduled to mature in an annual, sequential structure. (provider: intrinio)
zero_coupon: For bond ETFs, this field identifies those ETFs that specifically hold zero coupon Treasury Bills. (provider: intrinio)
floating_rate: For bond ETFs, this field identifies those ETFs that specifically hold floating rate bonds. (provider: intrinio)
build_america_bonds: For municipal bond ETFs, this field identifies those ETFs that specifically hold Build America Bonds. (provider: intrinio)
dynamic_futures_roll: If the product holds futures contracts, this field identifies those products where the roll strategy is dynamic (rather than entirely rules based), so as to minimize roll costs. (provider: intrinio)
currency_hedged: This field is populated if the ETF's strategy involves hedging currency exposure. (provider: intrinio)
includes_short_exposure: This field is populated if the ETF has short exposure in any of its holdings e.g. in a long/short or inverse ETF. (provider: intrinio)
ucits: If true, the Exchange Traded Product (ETP) is Undertakings for the Collective Investment in Transferable Securities (UCITS) compliant (provider: intrinio)
registered_countries: The list of countries where the ETF is legally registered for sale. This may differ from where the ETF is domiciled or traded, particularly in Europe. (provider: intrinio)
issuer_country: 2 letter ISO country code for the country where the issuer is located. (provider: intrinio)
listing_country: 2 letter ISO country code for the country of the primary listing. (provider: intrinio)
listing_region: Geographic region in the country of the primary listing falls. (provider: intrinio)
bond_currency_denomination: For all bond ETFs, this field provides additional detail on the currency denomination of the underlying securities. (provider: intrinio)
base_currency: Base currency in which NAV is reported. (provider: intrinio)
listing_currency: Listing currency of the Exchange Traded Product (ETP) in which it is traded. Reported using the 3-digit ISO currency code. (provider: intrinio)
number_of_holdings: The number of holdings in the ETF. (provider: intrinio)
month_end_assets: Net assets in millions of dollars as of the most recent month end. (provider: intrinio)
net_expense_ratio: Gross expense net of Fee Waivers, as a percentage of net assets as published by the ETF issuer. (provider: intrinio)
etf_portfolio_turnover: The percentage of positions turned over in the last 12 months. (provider: intrinio)
fund_type: The legal type of fund. (provider: yfinance)
category: The fund category. (provider: yfinance)
exchange_timezone: The timezone of the exchange. (provider: yfinance)
currency: The currency in which the fund is listed. (provider: yfinance)
nav_price: The net asset value per unit of the fund. (provider: yfinance)
total_assets: The total value of assets held by the fund. (provider: yfinance)
trailing_pe: The trailing twelve month P/E ratio of the fund's assets. (provider: yfinance)
dividend_yield: The dividend yield of the fund, as a normalized percent. (provider: yfinance)
dividend_rate_ttm: The trailing twelve month annual dividend rate of the fund, in currency units. (provider: yfinance)
dividend_yield_ttm: The trailing twelve month annual dividend yield of the fund, as a normalized percent. (provider: yfinance)
year_high: The fifty-two week high price. (provider: yfinance)
year_low: The fifty-two week low price. (provider: yfinance)
ma_50d: 50-day moving average price. (provider: yfinance)
ma_200d: 200-day moving average price. (provider: yfinance)
return_ytd: The year-to-date return of the fund, as a normalized percent. (provider: yfinance)
return_3y_avg: The three year average return of the fund, as a normalized percent. (provider: yfinance)
return_5y_avg: The five year average return of the fund, as a normalized percent. (provider: yfinance)
beta_3y_avg: The three year average beta of the fund. (provider: yfinance)
volume_avg: The average daily trading volume of the fund. (provider: yfinance)
volume_avg_10d: The average daily trading volume of the fund over the past ten days. (provider: yfinance)
bid: The current bid price. (provider: yfinance)
bid_size: The current bid size. (provider: yfinance)
ask: The current ask price. (provider: yfinance)
ask_size: The current ask size. (provider: yfinance)
open: The open price of the most recent trading session. (provider: yfinance)
high: The highest price of the most recent trading session. (provider: yfinance)
low: The lowest price of the most recent trading session. (provider: yfinance)
volume: The trading volume of the most recent trading session. (provider: yfinance)
prev_close: The previous closing price. (provider: yfinance)

.index.available
All indices available from a given provider.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.index.available(provider='fmp')
        >>> obb.index.available(provider='yfinance')

Outputs:
name: Name of the index.
currency: Currency the index is traded in.
stock_exchange: Stock exchange where the index is listed. (provider: fmp)
exchange_short_name: Short name of the stock exchange where the index is listed. (provider: fmp)
code: ID code for keying the index in the OpenBB Terminal. (provider: yfinance)
symbol: Symbol for the index. (provider: yfinance)

.index.price.historical
Historical Index Levels.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.index.price.historical(symbol='^GSPC', provider='fmp')
        >>> # Not all providers have the same symbols.
        >>> obb.index.price.historical(symbol='SPX', provider='intrinio')

Outputs:
date: The date of the data.
open: The open price.
high: The high price.
low: The low price.
close: The close price.
volume: The trading volume.
vwap: Volume Weighted Average Price over the period. (provider: fmp)
change: Change in the price from the previous close. (provider: fmp)
change_percent: Change in the price from the previous close, as a normalized percent. (provider: fmp)
transactions: Number of transactions for the symbol in the time period. (provider: polygon)

.news.company
Company News. Get news for one or more companies.


        Examples
        --------
        >>> from openbb import obb
        >>> obb.news.company(provider='benzinga')
        >>> obb.news.company(limit=100, provider='benzinga')
        >>> # Get news on the specified dates.
        >>> obb.news.company(symbol='AAPL', start_date='2024-02-01', end_date='2024-02-07', provider='intrinio')
        >>> # Display the headlines of the news.
        >>> obb.news.company(symbol='AAPL', display='headline', provider='benzinga')
        >>> # Get news for multiple symbols.
        >>> obb.news.company(symbol='aapl,tsla', provider='fmp')
        >>> # Get news company's ISIN.
        >>> obb.news.company(symbol='NVDA', isin='US0378331005', provider='benzinga')

Outputs:
date: The date of the data. Here it is the published date of the article.
title: Title of the article.
text: Text/body of the article.
images: Images associated with the article.
url: URL to the article.
symbols: Symbols associated with the article.
id: Article ID. (provider: benzinga, intrinio, polygon)
author: Author of the article. (provider: benzinga)
teaser: Teaser of the news. (provider: benzinga)
channels: Channels associated with the news. (provider: benzinga)
stocks: Stocks associated with the news. (provider: benzinga)
tags: Tags associated with the news. (provider: benzinga, polygon, tiingo)
updated: Updated date of the news. (provider: benzinga)
source: Name of the news source. (provider: fmp);
    The source of the news article. (provider: intrinio);
    Source of the article. (provider: polygon);
    News source. (provider: tiingo);
    Source of the news article (provider: yfinance)
summary: The summary of the news article. (provider: intrinio)
topics: The topics related to the news article. (provider: intrinio)
word_count: The word count of the news article. (provider: intrinio)
business_relevance:  	How strongly correlated the news article is to the business (provider: intrinio)
sentiment: The sentiment of the news article - i.e, negative, positive. (provider: intrinio)
sentiment_confidence: The confidence score of the sentiment rating. (provider: intrinio)
language: The language of the news article. (provider: intrinio)
spam: Whether the news article is spam. (provider: intrinio)
copyright: The copyright notice of the news article. (provider: intrinio)
security: The Intrinio Security object. Contains the security details related to the news article. (provider: intrinio)
amp_url: AMP URL. (provider: polygon)
publisher: Publisher of the article. (provider: polygon)
article_id: Unique ID of the news article. (provider: tiingo)
crawl_date: Date the news article was crawled. (provider: tiingo)

```