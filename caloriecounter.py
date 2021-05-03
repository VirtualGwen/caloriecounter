''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

''' Type your code here. '''
years_age = float(input())
weight_pounds = float(input())
heart_rate = float(input())
time_minutes = float(input())

men_calories = ((years_age * 0.2017) + (weight_pounds * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time_minutes / 4.184
women_calories = ((years_age * 0.074) - (weight_pounds * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time_minutes / 4.184


print('Women: {:.2f} calories'.format(women_calories))
print('Men: {:.2f} calories'.format(men_calories))