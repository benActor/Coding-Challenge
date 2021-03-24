#from .helpers import first_of, rest_of
from utils.helpers import first_of, rest_of


def pwp_pmax(power_plant_json, fuels_json, types):
    """

    :param power_plant_json: {
                              "name": "gasfiredbig1",
                              "type": "gasfired",
                              "efficiency": 0.53,
                              "pmin": 100,
                              "pmax": 460
                            }
    :param fuels_json:{
                        "gas(euro/MWh)": 13.4,
                        "kerosine(euro/MWh)": 50.8,
                        "co2(euro/ton)": 20,
                        "wind(%)": 60
                      }
    :param types:types = {
                            "one" : "gasfired",
                            "two" : "turbojet",
                            "three": "windturbine"
                        }


    :return: 460
    """
    if power_plant_json["type"] == types["three"]:
        return power_plant_json["pmax"] * fuels_json["wind(%)"]/100
    return power_plant_json["pmax"]


def pwp_cost(power_plant_json, fuels_json, types):
    """

    :param power_plant_json:{
                              "name": "windpark2",
                              "type": "windturbine",
                              "efficiency": 1,
                              "pmin": 0,
                              "pmax": 36
                            }
    :param fuels_json:{
                        "gas(euro/MWh)": 13.4,
                        "kerosine(euro/MWh)": 50.8,
                        "co2(euro/ton)": 20,
                        "wind(%)": 60
                      }

    :param types:{
                    "one" : "gasfired",
                    "two" : "turbojet",
                    "three": "windturbine"
                }
    :return: 0
    """
    if power_plant_json["type"] == types["one"]:
        return fuels_json["gas(euro/MWh)"] * 1/power_plant_json["efficiency"]
    if power_plant_json["type"] == types["two"]:
        return fuels_json["kerosine(euro/MWh)"] * 1/power_plant_json["efficiency"]
    return 0


def total_pmax_pwp_set(pwp_set, fuels_json, types):
    """

    :param pwp_set:
    :param fuels_json:
    :return:
    """
    if pwp_set == []:
        return 0
    else:
        return pwp_pmax(first_of(pwp_set), fuels_json, types) + total_pmax_pwp_set(rest_of(pwp_set), fuels_json, types)


def total_cost(pwp_set, fuels_json, types):
    if pwp_set == []:
        return 0
    else:
        return pwp_cost(first_of(pwp_set), fuels_json, types) + total_cost(rest_of(pwp_set), fuels_json, types)


def pmax_over_cost(pwp_set, fuels_json, types):
    return total_pmax_pwp_set(pwp_set, fuels_json, types)/total_cost(pwp_set, fuels_json, types)




print(min([1, 2, 3, 5, 9, 21, 18], key=lambda x:abs(x-15)))