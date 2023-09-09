products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", 
            "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#calculate the total price average for all products
total_price = sum(prices)/len(prices)
print("The total_price of all products is:" ,total_price)


#create a new price list that reduces the old prices by $ 5
new_prices= []
for price in prices:
    new_price = price - 5
    new_prices.append(new_price)
print("The new price list is :" ,new_prices)


#calculate the total revenue generated from the products
total_revenue = 0
for i in range(len(prices)):
    total_revenue += prices[i] * last_week[i]
print("Total revenue generated from the products last week is:", total_revenue)


#calculate the average daily revenue generated from the products
average_daily = total_revenue/sum(last_week)
print("The average daily revenue is:", average_daily)


#based on the new prices, which products are less than $ 30 
products_less_than_30 =[]
for i in range(len(products)):
    if new_prices[i] <30:
        products_less_than_30.append(products[i])

print("The products less than $30 are:", products_less_than_30)

