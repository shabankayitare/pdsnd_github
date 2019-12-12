import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city=input('Please enter the data of a city which  you wish to navigate. Choose: Chicago, New York City, or Washington')
      if city.lower() not in ['chicago','new york city','washington']:
             print("Please select one of the three cities")
     
      else: 
             city=city.lower()
             break
    print('You select {}'.format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=['jan','feb','mar','apr','may','jun','all']
        month=input("select a month you want to observe: Jan, Feb, Mar, Apr, May, Jun or \"All\"")
        if month[:3].lower() not in months:
            print("Please Choose one of the available months, or \"All\"")
        else:
            month=month[:3].lower
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
while True:
        day=input("please Enter the three alphabets expression for the days of the week\
                  :Mon, Tue, Wed , etc. ; or \"All\"")
        days=['mon','tue','wed','thu','fri','sat','sun','all']
        day=day[:3].lower()
        if day not in days:
            print("Please select an available day, or \"All")
        else:
            day=days.index(day)
            break
    
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
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
mostly_common_month=df['month'].mode()
    print ("The Mostly Common Month")
    print(mostly_common_month)

    # TO DO: display the most common day of week
mostly_common_day=df['day_of_week'].mode()
    print ('The Mostly Common Weekday')
    print(mostly_common_day)

    # TO DO: display the most common start hour
mostly_starting_hour=df['hour'].mode()
    print('The Mostly Common Hour')
    print(mostly_starting_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the popularity stations and travel."""

    print('\nCalculating The Popularity Stations and Travel...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
popular_starting_station=df['Starting Station'].mode()[0]
    print('Mostly Popular Starting Station: {}'.format(popular_starting_station))

    # TO DO: display most commonly used end station
 popular_ending_station=df['Ending Station'].mode()[0]
    print('Most Popular Ending Station: {}'.format(popular_ending_station))

    # TO DO: display most frequent combination of start station and end station trip
dfa=df.groupby(['Starting Station','Ending Station']).size().sort_values(ascending=False)
    a=dfa['Starting Station'].iloc[0]
    b=dfa['Ending Station'].iloc[0]
    print('Mostly Popular Combination of Starting and Ending Stations: Starting: {} Ending {}'.format(a,b))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
total_travelling_time=df['Trip Duration'].sum()
    print("Total Travel Time is: {}".format(total_travelling_time))

    # TO DO: display mean travel time
mean_travelling_time=df['Trip Duration'].mean()
    print('Mean Travelling Time is: {}'.format(mean_travelling_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    starting_time = time.time()

    # TO DO: Display counts of user types
 user_types=df.groupby(['User Type']).sum()
    print('User Types\n',user_types)

    # TO DO: Display counts of gender
if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print("Gender Counts")
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
if 'Birth Year' in df.columns:
        early_year=df['Birth Year'].max()
        late_year=df['Birth Year'].min()
        common_year=df['Birth Year'].mode()
        print('The earliest birth year is: {}'.format(early_year))
        print('The mostly recent birth year is: {}'.format(late_year))
        print('The mostly common birth year is: {}'.format(common_year))

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
    def display_data(df):
        prompt = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n')
        s = 0
        e = 5
        if prompt.lower() == 'yes':
        df2 = df.iloc[s:e]
        print(df2)

        more = input('Do you want to see more five lines? yes or no')
        while more.lower() == 'yes':
            s = 0
            e += 5
            df2 = df.iloc[s:e]
            print(df2)

            more = input('Do you want to see more five lines? yes or no')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
