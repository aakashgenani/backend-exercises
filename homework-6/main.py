from flowers import Red, Blue, Yellow
from weather import Sunny, Cloudy, Rain
import random


def main():
    no_of_flowers = 4                                   # Set number of flowers
    no_of_days = 100
    flowers_in_garden = list()                          # Initialize list of flowers in the garden
    weathers = [Sunny(), Cloudy(), Rain()]              # List of weather types

    #  Set number and random types of flowers in the garden
    for i in range(0, no_of_flowers):
        flowers = [Red(), Yellow(), Blue()]
        random_flower = flowers[random.randint(0, 2)]   # Randomize the flower
        flowers_in_garden.append(random_flower)

    for day in range(1, no_of_days):
        weather = weathers[random.randint(0, 2)]        # Choosing a random weather for each day
        flowers_names = list(map(lambda x: x.get_type(), flowers_in_garden))
        hydration_list = list(map(lambda x: x.get_hydration(), flowers_in_garden))
        height_list = list(map(lambda x: x.get_height(), flowers_in_garden))

        # Print flowers' stats
        print(f'\nDay: {day}. Weather: {weather.get_name()}.\nFlowers:')
        for i in range(len(flowers_in_garden)):
            print(
                f'\t{i + 1}. {flowers_names[i]} (Hydration: {round(hydration_list[i], 1)}% Height: {round(height_list[i], 1)}cm)')

        # Print status of dead flowers each day
        dead_flowers = list(filter(lambda x: x.is_dead(), flowers_in_garden))
        for i in range(len(dead_flowers)):
            print(f'\t{dead_flowers[i].get_type()} flower at {flowers_in_garden.index(dead_flowers[i])+1}. is dead')

        # Check if all flowers are dead
        if all(map(lambda x: x.is_dead(), flowers_in_garden)):
            print('All flowers dead!!')
            break

        # Calculations for height and hydration for each flower object in a given day
        for curr_flower in flowers_in_garden:
            if not curr_flower.is_dead():
                curr_flower.set_hydration(weather)
                curr_flower.set_height(weather)


if __name__ == '__main__':
    main()
