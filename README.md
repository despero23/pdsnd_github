## Date created
06.06.2025

## Project Title
US Bikeshare Study

## Description

Welcome to the US Bikeshare Data Analysis project! 

This Python-based application allows users to explore and analyze bikeshare data from three major cities: Chicago, New York City, and Washington. By leveraging the power of Pandas and Matplotlib, the project provides insightful statistics and visualizations on bikeshare usage patterns.

### Key Features:

* City Selection: Choose from Chicago, New York City, or Washington to analyze bikeshare data.
* Flexible Filtering: Filter data by month and day to focus on specific time periods.
* Comprehensive Statistics: Discover the most frequent times of travel, popular stations, trip durations, and user demographics.
* Interactive Visualizations: View histograms and bar charts that illustrate the distribution of trips, start hours, station usage, and user types.

## How to

### Prerequisites:

Ensure that you have the following installed:
* Python 3.x
* Pandas
* NumPy
* Matplotlib

You can install the required libraries using pip:

`pip install pandas numpy matplotlib`

### Steps to Use:

1. **Prepare the Data:** Ensure you have the CSV files (chicago.csv, new_york_city.csv, washington.csv) in the same directory as the script.
2. **Run the script:** Execute the Python script to start the analysis:

`python bikeshare.py`

3. **Interact with the Program:**

    * **City Selection:** When prompted, enter the name of the city you want to analyze (Chicago, New York City, Washington).
    > Note: Capital letter does not matter, i.e.: Script will accept 'ChIcAgO' as valid input.
    * **Month Selection:** Choose the month you are interested in (January, February, ..., June or all)
    * **Day selection:** Specify the day of the week (Monday, Tuesday, ..., Sunday, or all)

4. **View results:**: The program will display various statistics and visualizations based on your selections.

5. **Restart or Exit**:  After viewing the results, you can choose to restart the analysis with different filters or exit the program.

## Files used
* bikeshare.py - main python script
* Data base files:
    * chicago.csv
    * new_york_city.csv
    * washington.csv
    > Note: Data base files are excluded from the repository via the .gitignore file.

## Credits
This repository and the whole project was done as part of Data Science course provided by Udacity. 
Big credits to whole Udacity team!
