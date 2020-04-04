

# main function
def main():
    
    miles = float(input("\nPlease tell me how many miles you want converted to kilometers: "))
    milesToKm(miles)
    
    gallons = float(input("\nPlease tell me how many gallons you want converted to liters: "))
    galToLit(gallons)
    
    pounds = float(input("\nPlease tell me how many pounds you want converted to kilograms: "))
    poundsToKg(pounds)
    
    inches = float(input("\nPlease tell me how many inches you want converted to centimeters: "))
    inchesToCm(inches)
    
    fahrenheit = float(input("\nPlease tell me how many fahrenheit you want converted to celsius: "))
    fahToCel(fahrenheit)

    
#  function to convert miles to kilometers
def milesToKm(miles):
    kilometers = miles * 1.6
    print(miles, " miles is equal to ", 
        format(kilometers,'.2f'), " kilometers.", sep ='') 
    
# function to convert gallons to liters
def galToLit(gallons):
    liters = gallons * 3.9
    print(gallons, " gallons is equal to ", 
        format(liters,'.2f'), " liters.", sep ='')
    
# function to convert pounds to kilograms
def poundsToKg(pounds):
    kilograms = pounds * 0.45
    print(pounds, " pounds is equal to ", 
        format(kilograms,'.2f'), " kilograms.", sep ='')

# function to convert inches to centimeters 
def inchesToCm(inches):
    centimeters = inches * 2.54
    print( inches, " inches is equal to ", 
        format(centimeters, '.2f'), " centimeters.", sep ='')

# function to convert fahrenheit to celsius
def fahToCel(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, " fahrenheit is equal to ", 
        format(celsius, '.2f'), " celsius.", sep ='')

# call to main function
main()