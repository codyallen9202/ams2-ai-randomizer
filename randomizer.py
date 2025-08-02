import xml.etree.ElementTree as ET
import random
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_ratings():
    # Assign driver a random overall (This value isn't directly used)
    ovr = random.randint(45, 100)
    min_value = ovr - 5
    max_value = min(100, ovr + 5)

    core_attrs = ["race_skill", "qualifying_skill", "defending", "stamina",
                  "consistency", "start_reactions", "wet_skill",
                  "tyre_management", "fuel_management", "weather_tyre_changes",
                  "avoidance_of_mistakes", "avoidance_of_forced_mistakes"]

    # All core attributes are generated within +/- 5 of the driver's overall
    ratings = {attr: random.randint(min_value, max_value) * 0.01 for attr in core_attrs}
    # These 3 attributes are generated separately, as they are 
    # independent from skill in my opinion
    ratings["aggression"] = random.randint(0, 100) * 0.01
    ratings["blue_flag_conceding"] = random.randint(30, 100) * 0.01
    ratings["vehicle_reliability"] = random.randint(65, 75) * 0.01

    return ratings

def get_files():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("showinfo", "Select all .xml files you wish to edit in \\steamapps\\common\\Automobilista 2\\UserData\\CustomAIDrivers")
    files = filedialog.askopenfilenames(title="Select all .xml files you wish to edit in \\steamapps\\common\\Automobilista 2\\UserData\\CustomAIDrivers")
    return files

def main():
    files = get_files()

    for file in files:
        try:
            tree = ET.parse(file)
            root = tree.getroot()
        except ET.ParseError:
            errormsg = "Failed to parse: " + file
            messagebox.showerror("showerror", errormsg)
            continue
        except FileNotFoundError:
            errormsg = "File not found: " + file
            messagebox.showerror("showerror", errormsg)
            continue

        for driver in root.findall("driver"):
            ratings = get_ratings()

            for key, value in ratings.items():
                elem = driver.find(key)
                if elem is not None:
                    elem.text = f"{value:.2f}"
                else:
                    ET.SubElement(driver, key).text = f"{value:.2f}"

        tree.write(file)
    
    messagebox.showinfo("showinfo", "Done")


if __name__ == "__main__":
    main()