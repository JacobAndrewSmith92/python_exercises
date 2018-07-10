# # A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

# stock_dict = {
# 'GM': 'General Motors',
# 'CAT':'Caterpillar',
# 'AAPL': "Apple" }

# # Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# purchases = [
# ('GM', 481231, '10-sep-2001', 142 ),
# ('CAT', 32534, '1-apr-1999', 103 ),
# ('GM', 2524, '1-jul-1998', 56 ),
# ('AAPL', 5432, '2-dec-2018', 1600)]

# # Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stock_dict to look up the full company name. This is the basic relational database join algorithm between two tables.




# def calculate_stock():
#     for purchase in purchases:
#         for ticker, name in stock_dict.items():
#             if purchase[0] == ticker:
#                 total = purchase[1] * purchase[3]
#                 print(f"There were {purchase[1]} {name} shares purchased at ${purchase[3]} a share totaling ${total} on {purchase[2]}.")

# calculate_stock()

# def portfolio():
#     company_dict = {}
#     for ticker, name in stock_dict.items():
#         total = 0
#         for purchase in purchases:
#             if ticker == purchase[0]:
#                 total += purchase[1] * purchase[3]
#             company_dict[name] = total
#     return company_dict


# def create_report(dict):
#     for name, price in dict.items():
#         print(f"{name} has a total investment of ${price}.")

# create_report(portfolio())

stockDict = { 'GE': 'General Electric',
 'MSFT': 'Microsoft',
 'APPL': 'Apple',
 'CAT':'Caterpillar', 'EK':'Eastman Kodak' }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'MSFT', 1000, '1-apr-1999', 198 ),
 ( 'MSFT', 250, '1-apr-1999', 75 ),
 ( 'MSFT', 333, '1-apr-1999', 100 ),
 ( 'APPL', 50, '1-apr-1999', 144 ),
 ( 'EK', 300, '5-apr-2017', 9 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]


portfolio = dict()
for purchase in purchases:
    ticker = purchase[0]

    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1]
    purchase_price = purchase[3]
    full_purchase_price = number_of_shares * purchase_price

    minimal_purchase = (purchase[1], purchase[2], purchase[3])

    try:
        portfolio[ticker].append(purchase) # Append the purchase to the ticker list
    except KeyError:
        portfolio[ticker] = list() # If the key doesn't exist yet, create it
        portfolio[ticker].append(purchase)


    print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

print(portfolio)

for ticker,purchases in portfolio.items():
    print("------ {} ------".format(ticker))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print("    {}".format(purchase))
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))