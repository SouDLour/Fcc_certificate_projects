import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    ddf = pd.read_csv('adult_data.csv')

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
    
    percentage_bachelors = percent_of_bach.round()

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    main_edu = df['education']
    main_tot = main_edu.value_counts().sum()
    higher_education_rich_m = pd.DataFrame(df)
    filt_high_edu = higher_education_rich_m.loc[(higher_education_rich_m.education.isin(['Bachelors','Masters','Doctorate']) & (higher_education_rich_m['salary']=='<=50K')),['salary','education']]
    high_total = filt_high_edu.value_counts().sum()
    percent_back = (high_total / main_tot) * 100
    
    # [REDO THIS ONE ]What percentage of people without advanced education make more than 50K? NO NEED
    lower_education_rich_m = pd.DataFrame(df)
    filt_lower_edu = lower_education_rich_m.loc[(lower_education_rich_m.education.isin(['Bachelors','Masters','Doctorate']) & (lower_education_rich_m['salary']=='>50K')),['salary','education']]
    lower_total = filt_lower_edu.value_counts().sum()
    percent_back_low = (lower_total / main_tot) * 100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = percent_back
    lower_education = percent_back_low
    
    # Highed Education but less > 50K
    high_less = pd.DataFrame(df)
    filt_high_less = high_less.loc[(high_less.education.isin(['Bachelors','Masters','Doctoate']) & (high_less['salary'] == '>50K')),['salary','education']]
    fhl = filt_high_less.value_counts().sum()
    high_less_percent = (fhl/main_tot)*100
    high_less_percent
    
    #Lower Education Rich Code:
    original_amount = pd.DataFrame(df)
    dividen_amount = original_amount['education'].value_counts().sum()
    dividen_amount
    
    # Turning Any cell that has the string_data into '' <= making it a new value for the column
    without_edu_low = pd.DataFrame(df)
    string_data = ['Bachelors','Doctorate','Masters']
    without_edu_low['education'] = without_edu_low['education'].apply(lambda x: ''.join([word for word in x.split() if word not in string_data]))
    without_edu_low
    
    # Dropping the '' Data from the column thus removing every row
    for x in without_edu_low.index:
        if without_edu_low.loc[x,'education'] == '':
            without_edu_low.drop(x, inplace=True)

    # Getting Percent of people with less education less than 50K
    num_no_high_less = without_edu_low['education'].value_counts().sum()
    calc_non_less = (num_no_high_less/dividen_amount) * 100
    


    # percentage with salary >50K
    higher_education_rich = high_less_percent.round()
    lower_education_rich = calc_non_less.round()

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    df['hours-per-week'].info()
    df['hours-per-week'].describe()
    min_hr = df['hours-per-week'].min()
    min_work_hours = min_hr

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    ppl_work_1hr =  df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K'),['hours-per-week','salary']]
    total_ppl = df['hours-per-week'].value_counts().sum()
    
    percentag_sum = (ppl_work_1hr.value_counts().sum()/total_ppl) * 100
    
    num_min_workers = ppl_work_1hr.value_counts()

    rich_percentage = percentag_sum

    # What Country with highest percentage of rich & Highest percentage of rich people in country?
    richest_country = df[['salary','native-country']].value_counts()
    highest_earning_country = richest_country
    
    ppl_united_plus50 = df.loc[(df['native-country']=='United-States') & (df['salary']=='<=50K'),['salary','native-country']]
    ppl_united_plus50.isna().any()
    a_ppl = ppl_united_plus50.value_counts().sum()
    percentageRichPpl = (a_ppl / 32561) * 100
    percentageRichPpl
    highest_earning_country_percentage = percentageRichPpl

    # Identify the most popular occupation for those who earn >50K in India.
    ddf[['occupation','native-country','salary']].value_counts()
    ddf['native-country'].value_counts()
    top_IN = ddf.loc[(ddf['native-country']=='India') & (ddf['education']==ddf['education']),['salary','occupation']].value_counts().idxmax()
    
    top_IN_occupation = top_IN



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