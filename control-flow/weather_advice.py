# Ask the user for the current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Give clothing recommendation based on the weather condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("on't forget your umbrella and a raincoat.")
elif weather == "dry":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")