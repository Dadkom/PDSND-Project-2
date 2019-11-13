import time
import pandas as pd
import numpy as np

CITY_DATA ={ 'chicago': 'chicago.csv',
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
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n')
        citys = ['chicago', 'new york city', 'washington']
        if city.lower() in citys:
            break
        else:
                invalid_a = "It is invalid, please enter another name"
                print(invalid_a)
                
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWould you like to filter the data by month?\n'
                      'Which month - January, February, March, April, May, or June?\n')
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month.lower() in months:
            break
        else:
                invalid_b = "It is invalid, please enter another month"
                print(invalid_b)
                
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input('\nWould you like to filter the data by day?\n'
                    'Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        if day.lower() in days:
            break
        else:
                invalid_c = "It is invalid, please enter another day"
                print(invalid_c)

                
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city], index_col = 0)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # filter by month if applicable
    if month != 'all':

   # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month


   # use the index of the months list to get the corresponding int
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1
   # filter by month to create the new dataframe
    df = df.loc[df['month'] == month]
    
    #filter by day of week if applicable
    if day!='all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['start_hour'] = df['Start Time'].dt.hour
        
    #filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
        return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

  
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].value_counts().idxmax() - 1
    month_title = months[most_common_month].title()
    print("The most common month with bike travel is:", month_title)


    # TO DO: display the most common day of week
    most_common_day_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week with bike travel is:", most_common_day_week)
    

    # TO DO: display the most common start hour
    most_common_start_hour = df['start_hour'].value_counts().idxmax()
    print("The most common day of the week with bike travel is:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station= df['Start Station'].value_counts().idxmax()
    print("The most common used start station is:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common used end station is:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_combination_start_end = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most most frequent combination of start station and end station trip are : {}, {}".format(most_combination_start_end[0], most_combination_start_end[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total time travel is:", total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The total mean travel is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_types = df["User Type"].value_counts()
    print("Count of user types: ", counts_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("\nThe Counts of Gender")
        print("Male : ", df.query("Gender == 'Male'").Gender.count())
        print("Female : ", df.query("Gender == 'Female'").Gender.count())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Brith Year' in df:
        earliest_brith = df['Birth Year'].min()
        recent_brith = df['Birth Year'].max()
        common_brith = df['Birth Year'].value_counts().idxmax()
        print("The most earliest year of brith is:", earliest_brith)
        print("The most recent year of birth is:" , recent_brith)
        print("The most common year of birth is:", common_brith)
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
        # TO DO: Display the data rows 5 x 11
def raw_data(df):
    user = input('Do you want to see raw data? Enter yes or no. \n')
    line_num = 0
    while True:
        if user.lower() != 'no':
            print(df.iloc[line_num : line_num +5])
            line_num += 5
            user = input('\nDo you want to see raw data? Enter yes or no. \n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
