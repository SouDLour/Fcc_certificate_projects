import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas 
    # series with race names as the index labels.
    rc = pd.Series(df['race'])
    
    race_count = rc.value_counts()

    # What is the average age of men?
    filt_df = df.loc[(df['sex'] == 'Male'),['sex','age']]
    avg_age_men = filt_df['age'].mean().round()
    
    average_age_men = int(avg_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    total_edu = df['education'].value_counts().sum()
    total_education = total_edu
    total_bach = df[df['education']=='Bachelors']['education']
    total_bach_count = total_bach.count()
    percent_of_bach = (total_bach_count/ total_education) * 100
    
    percentage_bachelors = percent_of_bach 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    ###RICH ADVANCED EDUCATION HIGHER EDUCATION
    higher_education_rich = pd.DataFrame(df)
    higher_education_rich.loc[higher_education_rich['education'].isin(['Bachelors','Masters','Doctorate']),['salary','education']]
    total_higher_edu = higher_education_rich.education.value_counts().sum()

    smart_rich = higher_education_rich.loc[(higher_education_rich['education'].isin(['Bachelors','Masters','Doctorate'])) & (higher_education_rich['salary'] == '<=50K'),['salary','education']]
    total_high_50 = smart_rich.value_counts().sum()
    
    percent_rich = total_high_50 / total_higher_edu * 100
    high_edu_rich_perc = percent_rich.round() 

    ###POOR PERCENTAGE PEOPLE ADVANCE EDUCATION LESS THAN 50K

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = high_edu_rich_perc
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()