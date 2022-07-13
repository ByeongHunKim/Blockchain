from exchange import CurrencyPair
from exchange import ExchangeAPI

Huobi = ExchangeAPI().create_exchange('Huobi')

pando_usdt = Huobi.get_ticker(CurrencyPair('USDT', 'PANDO'))
print(f"1. pando_usdt 조회결과는 >>>> {pando_usdt}")

pando_price = pando_usdt.price
print(f"2. pando_usdt 가격 조회결과는 >>>> {pando_price}")


btc_usdt = Huobi.get_ticker(CurrencyPair('USDT', 'BTC'))
print(f"3. btc_usdt 조회결과는 >>>> {btc_usdt}")

btc_price = btc_usdt.price
print(f"4. btc_usdt 가격 조회결과는 >>>> {btc_price}")


eth_usdt = Huobi.get_ticker(CurrencyPair('USDT', 'ETH'))
print(f"5. eth_usdt 조회결과는 >>>> {eth_usdt}")

eth_price = eth_usdt.price
print(f"6. eth_usdt 가격 조회결과는 >>>> {eth_price}")


# for pair in Huobi.get_currency_pairs():
#     print(pair)
# market_currency: BTC, currency: ETH
# market_currency: BTC, currency: LTC
# market_currency: BTC, currency: BNB
# market_currency: BTC, currency: NEO
# market_currency: ETH, currency: QTUM
# ...

# print(Huobi.get_ticker(CurrencyPair('USDT', 'PANDO')))
# currency_pair: market_currency: USDT, currency: BTC, price: 7505.27, timestamp: 1533219056

# print(Huobi.get_orderbook(CurrencyPair('USDT', 'PANDO')))
# Orderbook(1533219081)-(market_currency: USDT, currency: BTC)
# Bids -
#         price: 7504.00000, amount: 0.14538
#         price: 7502.00000, amount: 0.23498
#         price: 7501.00000, amount: 0.62473
#         price: 7500.38000, amount: 0.05693
#         price: 7500.06000, amount: 0.34357
# ...
# Bids -
#         price: 7504.00000, amount: 0.14538
#         price: 7502.00000, amount: 0.23498
#         price: 7501.00000, amount: 0.62473
#         price: 7500.38000, amount: 0.05693
#         price: 7500.06000, amount: 0.34357
# '''
