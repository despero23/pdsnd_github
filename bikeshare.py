# -*- coding: utf-8 -*-
"""
Created on Wed May 14 13:36:59 2025

@author: MAOSUCH
"""

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Select city to analyze: Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name. ")

    #get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Which month are you interested? (january, february, ... june, or all: ').lower()
        if month in months:
            break
        else:
            print('Invalid input. Please enter valid month (january, february, ... june, or all)')
    #get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input('Which day of week are you interested? (Monday to Sunday or all): ').lower()
        if day in days:
            break
        else:
            print('Invalid input. Please enter valid day (Monday to Sunday or all')
        


    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        df = df[df['month_name'] == months[month]]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    most_common_month = df['month'].mode()[0]
    print(f"The most common month is: {most_common_month}")

    #display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of week is: {most_common_day}")

    #display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # Histogram of start hours distribution
    plt.figure(figsize=(12,8))
    df['hour'].hist(bins=24, edgecolor = 'black')
    plt.title('Distribution of Trips Start Hours')
    plt.xlabel('Hour')
    plt.ylabel('Frequency')
    plt.show()

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {most_common_start_station}")
    
    # Plot bar chart of start stations
    plt.figure(figsize=(12, 8))
    df['Start Station'].value_counts().head(10).plot(kind='bar', edgecolor='black')
    plt.title('Top 10 Start Stations')
    plt.xlabel('Start Station')
    plt.ylabel('Frequency')
    plt.show()
    
    #display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {most_common_end_station}")
    
    # Plot bar chart of start stations
    plt.figure(figsize=(12, 8))
    df['End Station'].value_counts().head(10).plot(kind='bar', edgecolor='black')
    plt.title('Top 10 End Stations')
    plt.xlabel('End Station')
    plt.ylabel('Frequency')
    plt.show()
    
    #display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station trip is: {most_common_trip}") 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_hours = total_travel_time/3600
    print(f"Total travel time is: {total_travel_time} seconds")
    print(f"Which is equal to: {total_travel_time_hours} hours")

    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")
    
    # Distribution of trip durations for all trips:
    plt.figure(figsize=(12,8))
    # df['Trip Duration'].plot(kind='hist', bins=100, edgecolor='black')
    plt.hist(np.clip(df['Trip Duration'], 0, 3600), bins=100, edgecolor='black')
    plt.title('Distribution of Trip Durations - for trips shorter than 1 hour')
    plt.xlabel('Trip Duration (seconds)')
    plt.ylabel('Frequency')
    plt.show()
    
    # Distribution of trip durations for trips shorter than 1 hour:
    plt.figure(figsize=(12,8))
    df['Trip Duration'].plot(kind='hist', bins=100, edgecolor='black')
    plt.title('Distribution of Trip Durations - for trips shorter than 1 hour')
    plt.xlabel('Trip Duration (seconds)')
    plt.ylabel('Frequency')
    plt.show()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Counts of user types:\n{user_types}")
    
    # Plot bar chart of user types
    plt.figure(figsize=(12, 8))
    user_types.plot(kind='bar', edgecolor='black')
    plt.title('Counts of User Types')
    plt.xlabel('User Type')
    plt.ylabel('Count')
    plt.show()
    
    #Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Counts of gender:\n{gender_counts}")
        
        # Plot bar chart of gender counts
        plt.figure(figsize=(12, 8))
        gender_counts.plot(kind='bar', edgecolor='black')
        plt.title('Counts of Gender')
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.show()
    else:
        print("Gender data is not available for selected city")

    #Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {most_recent_year}")
        print(f"Most common year of birth: {most_common_year}")
        
        #Plot distribution of birht years
        plt.figure(figsize=(12,6))
        df['Birth Year'].plot(kind='hist', bins=50, edgecolor='black')
        plt.title('Distribution of users birth years')
        plt.xlabel('Birth Year')
        plt.ylabel('Count')
        plt.show()
    else:
        print("Birth year data is not available for selected city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
