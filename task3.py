def convert_temperature():
    initial_temp = float(input("Please enter the temperature "))
    unit = input("is this temperature in celsius (c) or fahrenheit (F)? ")

    if unit.upper() == "C":
        final_temp = (initial_temp * 9/5) + 32
        print(
            f"{initial_temp} degrees Celsius is equal to {final_temp} degrees Fahrenheit")

    elif unit.upper() == "F":
         final_temp = (initial_temp - 32) * 5/9
         print(f"{initial_temp} degrees Fahrenheit is equal to {final_temp} degrees Celsius.")
    else:
        print("Invalid unit. Please enter either C for Celsius or F for Fahrenheit.")

convert_temperature()
        
    
