import xml.etree.ElementTree as ET
import random
import numpy as np

def get_ratings():
    ovr = int(random.triangular(1, 100, 50))
    min_value = max(1, ovr - 5)
    max_value = min(100, ovr + 5)

    values = {
        "race_skill": random.randint(min_value, max_value) * .01,
        "qualifying_skill": random.randint(min_value, max_value) * .01,
        "aggression": random.randint(min_value, max_value) * .01,
        "defending": random.randint(min_value, max_value) * .01,
        "stamina": random.randint(min_value, max_value) * .01,
        "consistency": random.randint(min_value, max_value) * .01,
        "start_reactions": random.randint(min_value, max_value) * .01,
        "wet_skill": random.randint(min_value, max_value) * .01,
        "tyre_management": random.randint(min_value, max_value) * .01,
        "fuel_management": random.randint(min_value, max_value) * .01,
        "blue_flag_conceding": random.randint(40, 60) * .01,
        "weather_tyre_changes": random.randint(min_value, max_value) * .01,
        "avoidance_of_mistakes": random.randint(min_value, max_value) * .01,
        "avoidance_of_forced_mistakes": random.randint(min_value, max_value) * .01,
        "vehicle_reliability": random.randint(65, 75) * .01,
    }
    
    return values


def main(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for driver in root.findall("driver"):
        ratings = get_ratings()

        for key, value in ratings.items():
            elem = driver.find(key)
            if elem is not None:
                elem.text = f"{value:.2f}"
            else:
                ET.SubElement(driver, key).text = f"{value:.2f}"

    tree.write(file_path)


if __name__ == "__main__":
    file_path = input("Paste the XML file path: ").strip().strip('"')
    main(file_path)