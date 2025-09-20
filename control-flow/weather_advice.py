userResponse = str(input("What's the weather like today? (sunny/rainy/cold): "))
userResponseLow = userResponse.lower()

if userResponseLow == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif userResponseLow == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif userResponseLow == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")