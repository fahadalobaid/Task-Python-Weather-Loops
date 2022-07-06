# printer(elements)
# - Accepts a list
# - Prints every element of the list
def printer(elements):
    for element in elements:
        print(element)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    c_temp=[]
    for temp in temperatures:
    
        c = (temp - 32) * (5/9)
        c_temp.append(c)
        
    return (c_temp)

# print(to_celsius([50,60,70]))

# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    temp_list =[]
    for temp in temperatures:
       if temp > threshold:
        temp_list.append(temp)
    return temp_list
# print(hottest_days([50,80,45,90,100],75))


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshold):
    printer(to_celsius(hottest_days([30,40,50],35)))
print_hottest_days([30,40,50],35)  
# 
