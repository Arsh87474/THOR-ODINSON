pizza = input("How many pizzas do you want?\n")
pizza = eval(pizza)
price = input("What's the menu $ cost of each pizza?\n$")
price = eval(price)
subtotal = price * pizza
tax = 0.08 * subtotal
print(" subtotal = $", subtotal)
print(" tax = $", tax)
total = subtotal + tax
print(" total = $", total)
