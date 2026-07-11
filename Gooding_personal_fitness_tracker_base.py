# Author: Omario Gooding
# Date: July 8, 2026
# Assignment: Personal Fitness Tracker
# Version Attempted: Base Level
# I attempted the Base Level version of this assignment. This program collects three workouts,
# calculates calories burned per minute, gives each workout an intensity label, and prints a
# short report for each workout.



# This function calculates calories burned per minute
def calories_per_minute(calories, duration):
    rate = calories / duration
    return round(rate, 1)


# This function decides the workout intensity based on the rate
def get_intensity(rate):
    if rate < 5.0:
        intensity = "Low"
    elif rate < 10.0:
        intensity = "Moderate"
    else:
        intensity = "High"

    return intensity


# Start of the main program
print("Welcome to the Personal Fitness Tracker!")
print("You will log 3 workouts.")

# This list stores the workout information entered by the user
workouts = []

# Ask the user for three workouts
for workout_number in range(1, 4):
    print()
    print(f"--- Workout {workout_number} ---")

    workout_name = input("Workout name: ").strip().title()
    duration = int(input("Duration (minutes): ").strip())
    calories = int(input("Calories burned: ").strip())

    # Store the workout name, duration, and calories in a list
    workout = [workout_name, duration, calories]
    workouts.append(workout)

    # Call the functions to calculate the rate and intensity
    rate = calories_per_minute(calories, duration)
    intensity = get_intensity(rate)

    # Print a summary for this workout
    print(f"Result: {workout_name} | {duration} min | {calories} cal | {rate} cal/min | Intensity: {intensity}")

print()
print("All workouts logged. Great job staying active!")
