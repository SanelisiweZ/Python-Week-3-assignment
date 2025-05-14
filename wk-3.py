# Function to calculate the discount
def calculate_discount(price, discount_percent):
    # If discount_percent is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
    print(f"No discount applied. The original price is: ${price:.2f}")
else:
    print(f"After applying the discount, the final price is: ${final_price:.2f}")
