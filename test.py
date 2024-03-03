from flask import *
import realEstateAPI
import weatherAPI
import googleAPI
import mainCalcs

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/result.html" , methods = ['GET' , 'POST'])
def result():
    S = ""
    address1 = request.form["address1"]
    address2 = request.form["address2"]
    distance = request.form["distance"]
    minLandAcres = request.form["minLandAcres"]
    time = float(request.form["time"])
    apiKey = "2cda45d56b334172fa0f715c45148a54"  
    county , properties = realEstateAPI.find_properties_with_more_land(address1, address2, distance, minLandAcres, apiKey)
    time, best_model, max_energy = mainCalcs.main(county,time)
    

    line1 = "County: " + county
    line2= f" The turbine model with the highest energy production for an address in {county} county is: {best_model} and it produces {max_energy/1000000} MW in the time period of {time} hours."

    if properties:
        S += f"Properties with more than  {minLandAcres} acre of land within {distance} miles of {address1}:"
        for propertyInfo in properties:
            S += str(propertyInfo)
    else:
        line3 = "No properties found."
    return render_template('result.html',  line1 = line1 , line2 = line2)