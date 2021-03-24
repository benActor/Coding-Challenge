from flask import Flask, request, jsonify
import utils.helpers
import utils.pwp_helpers as pwp_helper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
"""
TODO

1 - get request params 

2 - get all the combinations of pwp

3 - get the total load of each combination

4 - get load higher or equal to target value

5 - choose the optimal load based on cost 


{
  "load": 910,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 16
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 36
    }
  ]
}

"""
@app.route('/productionplan', methods=["GET", "POST"])
def production_plan():
    types = {
        "one": "gasfired",
        "two": "turbojet",
        "three": "windturbine"
    }
    fuels = {}
    load = {}
    power_plants = []

    # get request params
    if request.is_json:
        try:
            fuels = request.json["fuels"]
            load = request.json["load"]
            power_plants = request.json["powerplants"]
        except:
            fuels = {}
            load = {}
            power_plants = []

        # get all combination of power_plants
        if power_plants and fuels and load:
            all_combinations = utils.helpers.all_n_combinations(power_plants)

            # get combinition with load higher than target load
            matching_comb = [comb for comb in all_combinations if
                             (pwp_helper.total_pmax_pwp_set(pwp_set=comb, fuels_json=fuels, types=types) >= load)]

            optimal_composition = max(matching_comb, key=lambda x: pwp_helper.pmax_over_cost(pwp_set=x, fuels_json=fuels, types=types))

            result = [{"name" : x["name"], "p": 0} for x in power_plants if x not in optimal_composition] + \
                     [{"name": y["name"], "p": y["pmax"]} for y in optimal_composition]
            return jsonify(result)
    return 'hoho'





if __name__ == '__main__':
    app.run()
