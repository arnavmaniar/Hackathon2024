import pandas as pd
import math
import weatherAPI
import realEstateAPI
import random

apiKey1 = '2cda45d56b334172fa0f715c45148a54'
apiKey2 = '70f56f1c5ef54c92b6e143052240303'

def calc_power(windSpeed, bladeLength):
    airDensity = 1.225 
    sweptArea = math.pi * bladeLength ** 2
    power = 0.5 * airDensity * sweptArea * (windSpeed ** 3) * 0.42
    return power

def unit_change(windSpeedKMH):
    return windSpeedKMH * (1000 / 3600)

def calc_energy_production(power, time):
    energy = power * time
    return energy

def main(county, time):
    windSpeedKMH = weatherAPI.get_wind_data(apiKey2, county)[0]
    windSpeed = unit_change(windSpeedKMH)
    #time = float(input("Enter time (hours): "))

    models = find_unique_models("USTurbineData.csv")

    max_energy = float('-10000000')
    best_model = None

    for model, radius in models.items():
        bladeLength = radius 
        sweptArea = math.pi * bladeLength ** 2

        power = calc_power(windSpeed, bladeLength)
        energy = calc_energy_production(power, time)

        if energy > max_energy:
            max_energy = energy
            best_model = model
    
    max_energy = round(max_energy , 4)
    #print("The model with the highest energy production in" , time , "hours is:" , best_model , "with" ,  max_energy/1000000 , "MW.")
    return (time, best_model, max_energy)


def find_unique_models(file):
    data = pd.read_csv(file)
    diameters = data[['t_model', 't_rd']]

    models = {}
    for idx in diameters.index:
        model = diameters['t_model'][idx]
        dia = diameters['t_rd'][idx]

        if not math.isnan(dia):
            models[model] = dia

    return models

if __name__ == "__main__":
    address1 = input("Enter the street address: ")
    address2 = input("Enter the City, State: ")
    distance = input("Enter the search distance (miles): ")
    minLand = float(input("Enter the minimum land area (acres): "))

    county,properties = realEstateAPI.find_properties_with_more_land(address1 , address2, distance, minLand , apiKey1)

    if county != None:
        main(county)
    else:
        print("County missing")
