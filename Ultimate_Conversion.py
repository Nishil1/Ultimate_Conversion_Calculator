# Title - Invitation + decoration
def num_check(number):
    if number < 1:
        return False;
    else: 
        return True;


def convert_to_unit(number,unit, unitc):

    hours = {"hrs", "hr", "hours", "hour"}
    minutes = {"min","mins", "minutes"}
    seconds = {"sec", "secs", "second", "seconds"}

    if unit == 'mm'and unitc == "m":
        return number/1000
        
    elif unit == 'km' and unitc == "m":
        return number * 1000;
    elif unit == 'cm' and unitc == "m":
        return number /100;
    elif unit == "mm" and unitc == "km":
        return number/1000000
    elif unit == "cm" and unitc == "km":
        return number/100000
    elif unit == "m" and unitc == "km":
        return number/1000
    elif unit == "km" and unitc == "cm":
        return number*100000
    elif unit == "m" and unitc == "cm":
        return number*100
    elif unit == "mm" and unitc == "cm":
        return number/100
    elif unit == "cm" and unitc == "mm":
        return number*10
    elif unit == "m" and unitc == "mm":
        return number*1000
    elif unit == "km" and unitc == "mm":
        return number*1000000
    elif unit == "km" and unitc == "km":
        return number
    elif unit == "mm" and unitc == "mm":
        return number
    elif unit == "m" and unitc == "m":
        return number
    elif unit == "cm" and unitc == "cm":
        return number
    elif unit == "kg" and unitc == "mg":
        return number*1000000
    elif unit == "g" and unitc == "mg":
        return number/1000
    elif unit == "mg" and unitc == "mg":
        return number
    elif unit == "mg" and unitc == "kg":
        return number/1000000
    elif unit == "g" and unitc == "kg":
        return number/1000
    elif unit == "kg" and unitc == "kg":
        return number
    elif unit == 'mg' and unitc == "g":
        return number*1000
    elif unit == "kg" and unitc == "g":
        return number*1000
    elif unit == "g" and unitc == "g":
        return number
    elif unit  in hours and unitc in minutes:
        return number*60
    elif unit in seconds and unitc in minutes:
        return number/60
    elif unit in minutes and unitc in minutes:
        return number
    elif unit in seconds and unitc in seconds:
        return number
    elif unit in minutes and unitc in seconds:
        return number*60
    elif unit in hours and unitc in seconds:
        return number*3600
    elif unit in seconds and unitc in hours:
        return number/3600
    elif unit  in hours and unitc in hours:
        return number
    elif unit in minutes and unitc in hours:
        return number/60

  


def is_conversion_valid(existing_unit,conversion_unit):

    distance = {"km","mm","m","cm"}
    time = {"hours", "hour", "hr", "hrs", "min", "minutes", "sec", "seconds"}
    weight = {"g","kg","mg"}

    
    if existing_unit in distance and conversion_unit  in distance:
       
        return True
    elif existing_unit in time and conversion_unit  in time:
        
        return True
    elif existing_unit in weight and conversion_unit  in weight:
       
        return True
    else: 
        
        return False;
    

    
        
           

       



def captureNumber():
     while True:
        try:
            amount = float(input("Enter the integer value: "))
            if (num_check(amount)) is True:
                return amount;
            else:
                print('Please enter a value more than 0 ') 
        except ValueError:
            print('Please enter a valid integer')     


def capture_existing_Unit():
    while True:
        try:
            unit = input("Enter conversion unit: ")
            if (unit != 'km' and unit != 'mm' and unit != 'cm' and unit != "m" and unit != "kg" and unit != "g" and unit != "mg" and unit != "min" and unit != "minutes" and unit != "sec" and unit != "seconds" and unit != "hours" and unit != "hrs" and unit != "hour" and unit != "hr"):
                print('Please enter valid conversion unit') 
            else:
                return unit;
        except ValueError:
            print('Please enter valid conversion unit')   

def capture_conversion_unit(existingUnit):
     while True:
        try:
            unit = input("Enter unit to convert to:  ")
            if (unit != 'km' and unit != 'mm' and unit != 'cm' and unit != "m" and unit != "kg" and unit != "g" and unit != "mg"and unit != "min" and unit != "minutes" and unit != "sec" and unit != "seconds" and unit != "hours" and unit != "hrs" and unit != "hour" and unit != "hr"):
                print('Please enter valid unit to convert to') 
            elif is_conversion_valid(existingUnit, unit ) is False:
                print("Please enter a valid conversion unit")
            else:
                return unit;
        except ValueError:
            print('Please enter valid conversion unit')   

  
# decoration + instruction
print("**** Ultimate Conversion Calculator ****")
instruction = input("Press <enter> for instructions or any other key to skip: ")

read_instructions = "Ultimate Conversion Calculator is extremely efficient for calculating things such as distance(km, cm, m, mm), time(hours, minutes, seconds) and weights(g, kg, mg)"

if instruction == "":
    print(read_instructions)

    



def main_routine ():
    while True:
        
        inputAmount = captureNumber();
        existingunit = capture_existing_Unit(); 
        conversionUnit = capture_conversion_unit(existingunit)
        
        unitConversionResult = convert_to_unit(inputAmount,existingunit, conversionUnit);
        print(inputAmount ,existingunit , "is" , unitConversionResult , conversionUnit);
        repeat = input("Press <Enter> to make another calculation or anything else to quit")
        if repeat != "": break;


    print("Thanks for using Ultimate Conversion Calculator")


# main routine starts here
main_routine();


        