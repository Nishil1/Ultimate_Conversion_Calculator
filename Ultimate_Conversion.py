# All valid units and individual lists containing several valid inputs for that conversion(eg. hours)
hours = ["hrs", "hr", "hours", "hour"]
minutes = ["min","mins", "minutes"]
seconds = ["sec", "secs", "second", "seconds"]
distance = ["km","mm","m","cm"]
time = ["hours", "hour", "hr", "hrs", "min", "minutes", "sec", "seconds", "mins"]
weight = ["g","kg","mg"]
valid_units = ["km", "mm", "cm", "m", "kg", "g", "mg" , "min", "minutes", "sec", "seconds", "hours", "hrs", "hour", "hr", "mins"]
for_distance = {"distance", "d", "dis", "Distance"}
for_time = {"time", "t", "Time"}
for_weights = {"Weights", "weight", "weights", "w", "Weights"}
# number checking function
def num_check(number):
    if number <= 0:
        return False;
    else: 
        return True;
# gets input from lists in like 1-3 and returns a string so that conversion table works
def getDerivedUnit(inputUnit) :
    if( inputUnit in hours):
        return "hrs";
    elif (inputUnit in minutes):
        return "min";
    elif (inputUnit in seconds):
        return "sec";
    else:
        return inputUnit;
# function to convert one measurement to another
    # base unit is cm
def convert_to(number, existing_unit, conversion_unit):
    dis = {
        "cm" :  1,
        "mm" :  1/10,
        "km" :  100000,
        "m" :  100,}
    # base unit is minutes
    time = {
        "min" :  1,
        "hrs" :  60,
        "sec" : 1/60}
    # base unit is kg
    weigh = {
        "kg":  1,
        "g" :  1/1000,
        "mg" :  1/1e+6}
    values = dis | time | weigh
    convert_to_base = number * values[existing_unit]
    converted = convert_to_base/values[conversion_unit]
    print(number, existing_unit, "is" ,convertToInteger(converted), conversion_unit )
# checks whether the 2 entered conversions match and are valid to convert
def is_conversion_valid(existing_unit,conversion_unit):
    if existing_unit in distance and conversion_unit  in distance:
        return True
    elif existing_unit in time and conversion_unit  in time:
        return True
    elif existing_unit in weight and conversion_unit  in weight:
        return True
    else: 
        return False;
# function that checks whether result of conversion is an integer, in that case print whole number
def convertToInteger(inputNumber):
    if (float(inputNumber).is_integer()):
        return int(inputNumber);
    else:
        return inputNumber;
# checks that value of conversion is a valid input
def captureNumber():
     while True:
        try:
            amount = convertToInteger(float(input("Enter value of conversion: ")))
            if (num_check(amount)) is True:
                return amount;
            else:
                print('Please enter a value more than 0 ') 
        except ValueError:
            print('please enter a valid number')     
# checks whether inputted conversion unit is a valid unit
def capture_existing_Unit():
    while True:      
            unit = (input("Enter conversion unit: "))
            if (unit) not in valid_units:
                print('Please enter a valid unit to convert from') 
            else:              
                return getDerivedUnit(unit);
# checks whether inputted convert to unit is a valid unit to convert to
def capture_conversion_unit(existingUnit):
     while True:      
            unit = input("Enter unit to convert to:  ")
            if unit not in valid_units:
                print('Please enter valid unit to convert to') 
            elif is_conversion_valid(existingUnit, unit ) is False:
                print("Please enter a valid conversion unit")
            else:
                return getDerivedUnit(unit);
# main routine function
def main_routine ():
    # decoration + instruction
    print("**** Ultimate Conversion Calculator ****")
    instruction = input("Press <enter> for instructions or any other key to skip: ")
    read_instructions = "Ultimate Conversion Calculator is extremely efficient for calculating things such as distance(km, cm, m, mm), time(hrs, min, sec) and weights(g, kg, mg)"
    if instruction == "":
        print(read_instructions)
    while True:        
        inputAmount = captureNumber()
        existingunit = capture_existing_Unit()
        conversionUnit = capture_conversion_unit(existingunit)
        convert_to(inputAmount, existingunit, conversionUnit)
        repeat = input("Press <Enter> to make another calculation or anything else to quit")
        if repeat != "": break;
    print("Thanks for using Ultimate Conversion Calculator")
# main routine starts here
main_routine()       