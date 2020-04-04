

# importing Conversions function
import Conversions

# main function
def main():
    
    miles = float(input("\nPlease tell me how many miles you want converted to kilometers: "))
    kilometers = Conversions.milesToKm(miles)
    print(miles, " miles is equal to ", 
        format(kilometers,'.2f'), " kilometers.", sep ='') 

    
    gallons = float(input("\nPlease tell me how many gallons you want converted to liters: "))
    liters = Conversions.galToLit(gallons)
    print(gallons, " gallons is equal to ",
        format(liters,'.2f'), " liters.", sep ='')
    
    
    pounds = float(input("\nPlease tell me how many pounds you want converted to kilograms: "))
    kilograms = Conversions.poundsToKg(pounds)
    print(pounds, " pounds is equal to ", 
        format(kilograms,'.2f'), " kilograms.", sep ='')

    
    inches = float(input("\nPlease tell me how many inches you want converted to centimeters: "))
    centimeters = Conversions.inchesToCm(inches)
    print( inches, " inches is equal to ", 
        format(centimeters, '.2f'), " centimeters.", sep ='')
    
    fahrenheit = float(input("\nPlease tell me how many fahrenheit you want converted to celsius: "))
    celsius = Conversions.fahToCel(fahrenheit)
    print(fahrenheit, " fahrenheit is equal to ", 
        format(celsius, '.2f'), " celsius.", sep ='')
    
# call to main function
main()