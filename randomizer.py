import xml.etree.ElementTree as ET
import random
import os

# Route to your 'CustomAIDrivers' directory
file_base = r"D:\SteamLibrary\steamapps\common\Automobilista 2\UserData\CustomAIDrivers"

# Add/Remove any files you would like to be randomizing
files = [
    "Group C.xml",
    "Group C mod.xml",
    "GT1.xml",
    "GT1 mod.xml",
    "GT3.xml",
    "GT3_Gen2.xml",
    "GT4.xml",
    "GT5.xml",
    "GTE.xml",
    "GTE Mod.xml",
    "LMDh.xml",
    "LMP2.xml",
    "World_GT_Challenge.xml"
]

def get_ratings():
    # Assign driver a random overall (This value isn't directly used)
    ovr = random.randint(1, 100)
    min_value = max(1, ovr - 5)
    max_value = min(100, ovr + 5)

    core_attrs = ["race_skill", "qualifying_skill", "defending", "stamina",
                  "consistency", "start_reactions", "wet_skill",
                  "tyre_management", "fuel_management", "weather_tyre_changes",
                  "avoidance_of_mistakes", "avoidance_of_forced_mistakes"]

    # All core attributes are generated within +/- 5 of the driver's overall
    ratings = {attr: random.randint(min_value, max_value) * 0.01 for attr in core_attrs}
    # These 3 attributes are generated separately, as they are 
    # independent from skill in my opinion
    ratings["aggression"] = random.randint(1, 100) * 0.01
    ratings["blue_flag_conceding"] = random.randint(30, 70) * 0.01
    ratings["vehicle_reliability"] = random.randint(65, 75) * 0.01

    return ratings



def main():
    for file in files:
        file_path = os.path.join(file_base, file)

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
        except ET.ParseError:
            print(f"Failed to parse {file}")
            continue
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            continue

        for driver in root.findall("driver"):
            ratings = get_ratings()

            for key, value in ratings.items():
                elem = driver.find(key)
                if elem is not None:
                    elem.text = f"{value:.2f}"
                else:
                    ET.SubElement(driver, key).text = f"{value:.2f}"

        tree.write(file_path)
        print(f"Randomized drivers for class: {file}")
    
    print("Done.")


if __name__ == "__main__":
    main()