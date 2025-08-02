# AMS2 Driver Stat Randomizer

A simple Python app that randomizes all AI driver stats in Automobilista 2 for users with the **Real Names Mod**. Great for creating unpredictable offline grids and varied racing experiences.

## Features

* Randomizes all relevant AI driver stats within reasonable ranges
* Uses tkinter GUI to select one or more `.xml` driver files
* Ensures each stat is adjusted independently for realistic variation
* Preserves original file structure and updates in-place

## Randomization Logic

* Core driving attributes (e.g., `race_skill`, `wet_skill`, `consistency`) are centered around a randomized "overall" score.
* Behavioral stats like `aggression`, `blue_flag_conceding`, and `vehicle_reliability` are randomized separately to reflect personality differences.

## Usage

1. Make sure you have Python installed (preferably 3.8+).
2. Run the .exe
3. A file picker will appear. Select one or more driver `.xml` files from:
    ```
   steamapps\common\Automobilista 2\UserData\CustomAIDrivers
   ```
4. Wait for confirmation — the files will be overwritten with new randomized stats.

## Requirements

* Python 3
* No external libraries required — uses built-in `tkinter`, `os`, and `xml.etree.ElementTree`.

## Notes

* Always back up your original `.xml` files before using the tool.
* Designed specifically for the Real Names Mod, but can work with any valid AMS2 AI driver XMLs.