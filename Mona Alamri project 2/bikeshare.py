# Hello , this is project 2 of my Udacity course in programing for data science. 
# now i am updating these changes in github repo. 
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, 
        "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # here i used while True  as a loop then add the if condition inside so avoid code breaks too . 

     # while loop for a city filter    
    while True:
        city= input('please choose a city between chicago, new york city, washington to see its data: ').lower()
    
        if city in CITY_DATA :
          break   
        else : 
            print('please write a correct city name between chicago, new york city, washington:  \n ')

    # while loop for a months filter    

   
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']

    while True :
      month = input('please write the name of the month to filter by, or write (all) :').lower()
      if month in months : 
           break
      else:
          print('please enter invalid input like : all,january, february, march, april, may, june: ')
        
            
    # while loop for a days filter    


    days = ['all','monday', 'tuesday','wednesday','sunday','thursday','friday','saturday']

    while True : 
        
        day = input('please write the name of the day you want to filter by,or write (all): ').lower()
        
        if day in days :
            break
        else:
         print('please enter a valid input like : monday, tuesday, wednesday, thursday, friday, saturday, and Sunday')  

            
    

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
    # load data using panda 

    df = pd.read_csv(CITY_DATA[city])

    
    # transform Start Time into a date time type 

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Then transform Start Time into monshs
    df['month'] = df['Start Time'].dt.month

    # Then transform Start Time into days name  
    df['day_of_week'] = df['Start Time'].dt.day_name()
   
   # used if function and a list to make it act like a filter 
    if month != 'all':
        # used index function +1 to count months from 1 to 6 :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
   
   # used 'title' to convert the fisrt letter into capital letter . 

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # using month_name  and mode to extract the most common value : 

    # for month 

    df['month'] = df['Start Time'].dt.month_name()
    Most_Common_Month = df['month'].mode()[0]
    print('the most common month is:  ',Most_Common_Month)

    # for a day 

    df['day_of_week'] = df['Start Time'].dt.day_name()
    Most_Common_Day = df['day_of_week'].mode()[0]
    print('the most common day is:  ',Most_Common_Day)


    # for an hour : 

    df['hour'] = df['Start Time'].dt.hour
    Most_Common_Hour = df['hour'].mode()[0]
    print('the most common hour is:  ',Most_Common_Hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # using 'mode' to find out the most common used stations :

    # start station 

    MC_start = df['Start Station'].mode()[0]
    print('data shows that the most commonly used start station is:  ',MC_start)

    # end station

    MC_end = df['End Station'].mode()[0]
    print('data shows that the most commonly used end station is:',MC_end)

    # most frequent combination of start station and end station trip

    MC_start_END= (df['Start Station']+' & '+df['End Station']).mode()[0]
    print('the most frequent combination of start station and end station trip is :  ',MC_start_END)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # counting trips statistics using 'sum' and 'mean' to find the total & average trip duration
    # transformed second to hour (sec / 3600 ) 

    # total travel time : 

    Total_Travel_Time= df['Trip Duration'].sum() / 3600
    print('total travel time is : ',Total_Travel_Time,' Hour.')

    # mean travel time

    Mean_Trip_Duration= df['Trip Duration'].mean() / 3600
    print('the mean of trip duration is:  ',Mean_Trip_Duration, ' Hour.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #using value_counts to count number of user and gender types :
    

    # counts of user types
    User_Type =df['User Type'].value_counts()
    print('the counts of user types are :  ',User_Type)


    # sense there is no GENDER column in washington i will use if function. 

    if 'Gender' in df:
        Gender_Counts= df['Gender'].value_counts()
        print('counts of gender are :  ',Gender_Counts)

    
    
    # sense there is no 'birth year' column in washington too i will use if function here again. 

    # i used 'int' so i can count Birth Year data using min , max   : 

    #  i used 'min' to find the earliest BY , 'max' to find the recent BY , 'mode' to find the most common . 
    if 'Birth Year' in df : 
        Earliest_BY =int(df['Birth Year'].min())
        print('the earlist year of birth is :  ',Earliest_BY)

        Recent_BY = int(df['Birth Year'].max())
        print('the most recent year of birth is :  ',Recent_BY)

        Common_BY = int(df['Birth Year'].mode()[0])
        print('the common year of birth is :  ',Common_BY)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_display(df):
 """ here i used while loop and i loc() function to ask the user if they want so show the 10 rows of the data divided 5 and 5 dataframes """
    
  
      
  #print(user_answer)
    
 while True : 

    user_answer =   input('would like to show tha data in a dataframe ? \n , write yes on no  :  ')

    dataframe=0 

    if user_answer == 'yes':
     
        print(df.iloc[0:5])
        dataframe += 5
    else:
         
        user_answer == 'no'
        break  
        
    user_answer =   input('would like to show tha data in a dataframe ? \n , write yes on no  :  ')

    if user_answer == 'yes':
        
        print(df.iloc[5:10])
        dataframe += 5
        return df

    else:
         
        user_answer == 'no'
        break  
 return df      




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
