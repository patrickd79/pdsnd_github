def main():
    import time
    import pandas as pd
    import numpy as np
    from dateutil.relativedelta import relativedelta
    from datetime import date

    CITY_DATA = { 'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv' }

    cities = ['chicago','new york city','washington']
    #day_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


    print('Hello! Let\'s explore some US bikeshare data!')

    def get_city():
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city_answer = input("Which city would you like to know about? Please type 'chicago', 'new york', or 'washington'?: ")
        while True: 
            if city_answer.lower() not in cities:
                print("Please enter a valid city name: 'chicago','new york city','washington'")
                city_answer = input("Which city would you like to know about? Please type 'chicago', 'new york', or 'washington'?: ")

            elif city_answer.lower() in cities:
                city = city_answer
                return city
            else:
                break
            return city

    

        
        
        
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        
    #months = ['1','2','3','4','5','6']
        
        # get user input for month (all, january, february, ... , june)
        #months = ['1','2','3','4','5','6']
    def get_month():
        month_answer = input("Which month would you like data for? Please enter number for month(1-January, 2-February, 3-March, 4-April, 5-May,  or 6-June) or 'all' to return data for all months.: ")

        while month_answer not in ('all','1','2','3','4','5','6'):
            print('Please enter a number 1-6 that corresponds to a month Jan - June.')
            month_answer = input("Which month would you like data for? Please enter number for month(1-January, 2-February, 3-March, 4-April, 5-May,  or 6-June) or 'all' to return data for all months.: ")
            if month_answer in ('1','2','3','4','5','6'):
                return month_answer
            elif month_answer == 'all':
                month_answer = (1,2,3,4,5,6)
                return month_answer    
            #month_answer = input("Which month would you like data for? Please enter number for month(1-January, 2-February, 3-March, 4-April, 5-May,  or 6-June) or 'all' to return data for all months.: ")
            else:
                break
        return month_answer
        # get user input for day of week (all, monday, tuesday, ... sunday)
        #days_of_week = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        #day_answer = input("Which day of the week do you want data for?(all lowercase): ")
    def get_day():
        day_answer = input("Which day of the week do you want data for?: ")

        while day_answer.lower() not in ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Please enter a day of the week or all.')
            day_answer = input("Which day of the week do you want data for?: ")
            if day_answer.lower() in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                return day_answer
            elif day_answer.lower() == 'all':
                day_answer = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
                return day_answer
            else:
                break
        return day_answer



    


    print('-'*40)

    city = get_city()
    month_answer = get_month()
    day_answer = get_day()

    print("OK, we'll look at",city.title(), "during month #", month_answer, "on ", day_answer,'.' )


    if city == 'washington':
        print('ATTENTION: The data for WASHINGTON does not contain user gender or birth year.')

    def load_data(city, month_answer, day_answer):
        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['weekday'] = df['Start Time'].dt.dayofweek
        if month_answer != 'all':
            months = ('1','2','3','4','5','6')
            month_answer = months.index(month_answer) +1
            df = (df[df['month'] == month_answer])
        if day_answer != 'all':
            days_of_week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
            day_answer = days_of_week.index(day_answer) + 1
            df = (df[df['weekday']== day_answer])

        return(df)    
        
            
        
            
        

    df = load_data(city,month_answer,day_answer)

        

    def time_stats(df):
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()
        # display the most common month
        most_common_month = df['month'].mode()[0]
        print('The most common month for rentals is:')
        
        print(most_common_month)
        
        # display the most common day of week
        most_common_day_of_week = df['weekday'].mode()[0]
        print('The most common day of the week for rentals is:')
        
        print(most_common_day_of_week)
        # display the most common start hour
        df['start_hour'] = df['Start Time'].dt.hour
        most_common_start_hour = df['start_hour'].mode()[0]
        print('The most common start hour is:')
        
        print(most_common_start_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    print(time_stats(df))


    def station_stats(df):
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()
        #display most commonly used start station
        most_common_beginning_station = df['Start Station'].mode()[0]
        print('The most common station to start a trip is:') 
        
        print(most_common_beginning_station)

        #display most commonly used end station
        most_common_end_station = df['End Station'].mode()[0]
        print('The most common station to end a trip is:') 
        
        print(most_common_end_station)

        #display most frequent combination of start station and end station trip
        most_common_combination_of_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head()
        print('The most common combinations of starting stations and ending stations are:') 
        
        print(most_common_combination_of_stations)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    print(station_stats(df))

    def trip_duration_stats(df):
        

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()
        #duration = datetime.combine(date.min, end) - datetime.combine(date.min, beginning)
        
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        start_trip = df['Start Time']
        end_trip = df['End Time']
        df['travel_time'] = end_trip - start_trip
        print('The total amount of time spent travelling during the period requested is:')
        print(df['travel_time'].sum())
        print('The mean duration of each trip is:')
        print(df['travel_time'].mean())
        
        #display total travel time
        #print(travel_time)
        #print(total_travel_time)
        # display mean travel time


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    print(trip_duration_stats(df))

    def user_stats(df):
        

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print(user_types)
        # Display counts of gender
        user_by_gender = df['Gender'].value_counts()
        print(user_by_gender)
        # Display earliest, most recent, and most common year of birth
        birth_year_earliest = df['Birth Year'].min()
        birth_year_recent = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        print('The earliest year of birth for a user is:')
        print(birth_year_earliest)
        print('The most recent year of birth for a user is:')
        print(birth_year_recent)
        print('The most common year of birth for users is:')
        print(most_common_birth_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    print(user_stats(df))



    def  start_over():  
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while True:
            if restart == 'yep':
                main()
            elif restart == 'nope':
                exit()
            else:
                print("Please enter either 'yep', or 'nope'.")
                start_over()
                break
    start_over()            
main()


        

