hours = ["hrs", "hr", "hours", "hour"]
minutes = ["min","mins", "minutes"]
seconds = ["sec", "secs", "second", "seconds"]
distance = ["km","mm","m","cm"]
time = ["hours", "hour", "hr", "hrs", "min", "minutes", "sec", "seconds"]
weight = ["g","kg","mg"]
valid_units = ["km", "mm", "cm", "m", "kg", "g", "mg" , "min", "minutes", "sec", "seconds", "hours", "hrs", "hour", "hr"]

def num_check(number):
    if number < 0.1:
        return False;
    else: 
        return True;

def getDerivedUnit(inputUnit) :
    if( inputUnit in hours):
        return "hrs";
    elif (inputUnit in minutes):
        return "min";
    elif (inputUnit in seconds):
        return "sec";
    else:
        return inputUnit;


def convert_to_unit(number,unit, unitc):
    convertionTable = {
            "m_to_km" : number/1000,
            "km_to_m" : number*1000,
            "cm_to_km" : number*100000,
            "cm_to_m" : number/100,
            "mm_to_km" : number/1000000,
            "km_to_cm" : number*100000,
            "m_to_cm" : number*100,
            "mm_to_cm" : number/100,
            "cm_to_mm" : number*10,
            "m_to_mm" : number*1000,
            "km_to_mm" : number*1000000,
            "km_to_km" : number,
            "mm_to_mm" : number,
            "m_to_m" : number,
            "cm_to_cm": number,
            "kg_to_mg" : number*1000000,
            "g_to_mg" : number*1000,
            "mg_to_mg": number,
            "mg_to_kg" : number/1000000,
            "g_to_kg" : number/1000,
            "kg_to_kg" : number,
            "g_to_g" : number,
             "kg_to_g" : number*1000,
             "mg_to_g" : number/1000,
            "hrs_to_min":number/60,
            "min_to_sec":number*60,
            "hrs_to_sec" : number*3600,
            "hrs_to_hrs" : number,
            "min_to_hrs" : number/60,
            "min_to_min" : number,
            "sec_to_hrs" : number/3600,
            "sec_to_min" : number/60,
            "sec_to_sec" : number,
           
    };
    return convertionTable[unit+"_to_"+unitc]


def is_conversion_valid(existing_unit,conversion_unit):
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
            amount = float(input("Enter value of conversion: "))
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
            if unit not in valid_units:
                print('Please enter a valif unit to convert from') 
            else:
              
                return getDerivedUnit(unit);
        except ValueError:
            print('Please enter a valif unit to convert from')   

def capture_conversion_unit(existingUnit):
     while True:
        try:
            unit = input("Enter unit to convert to:  ")
            if unit not in valid_units:
                print('Please enter valid unit to convert to') 
            elif is_conversion_valid(existingUnit, unit ) is False:
                print("Please enter a valid conversion unit")
            else:
                return getDerivedUnit(unit);
        except ValueError:
            print('Please enter valid conversion unit')   


def convertToInteger(inputNumber):
    if (float(inputNumber).is_integer()):
        return int(inputNumber);
    else:
        return inputNumber;

def main_routine ():
    # decoration + instruction
    print("**** Ultimate Conversion Calculator ****")
    instruction = input("Press <enter> for instructions or any other key to skip: ")
    read_instructions = "Ultimate Conversion Calculator is extremely efficient for calculating things such as distance(km, cm, m, mm), time(hrs, min, sec) and weights(g, kg, mg)"

    if instruction == "":
        print(read_instructions)

    while True:
        
        inputAmount = captureNumber();
        existingunit = capture_existing_Unit(); 
        conversionUnit = capture_conversion_unit(existingunit)
        
        unitConversionResult = convert_to_unit(inputAmount,existingunit, conversionUnit);
        print(convertToInteger(inputAmount) ,existingunit , "is" , convertToInteger(unitConversionResult) , conversionUnit);
        repeat = input("Press <Enter> to make another calculation or anything else to quit")
        if repeat != "": break;
    print("Thanks for using Ultimate Conversion Calculator")

# main routine starts here
main_routine()


        