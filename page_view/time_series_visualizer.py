import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'],index_col= 'date')
# Clean data
# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))&
    (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot 
    fig, axe = plt.subplots(figsize=(16,5))
    axe.plot(df.index, df['value'], 'r', linewidth=1)
    axe.set_title('Daily FreeCodeCamp Daily Forum Views 5/2016-12/2019')
    axe.set_xlabel('Date')
    axe.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year','month'])['value'].mean()
    df_bar = df_bar.unstack() 
    
    # Draw bar plot
    
    fig = df_bar.plot.bar(legend=True, figsize = (10,5), ylabel='Average Page views',xlabel='Years').figure 
    plt.legend(['january','febuary','march','April','May','june',
                'july','august','september','november','December'])

 
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

        # Draw box plots (using Seaborn)
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
        
    fig, axe = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    axe[0] = sns.boxplot(x=df_box['year'],y=df_box['value'], ax=axe[0])
    axe[1] = sns.boxplot(x=df_box['month'],y=df_box['value'], ax=axe[1])

    axe[0].set_title('year wise box plot')
    axe[0].set_xlabel('year')
    axe[0].set_ylabel('page views')


    axe[1].set_title('month wise box plot')
    axe[1].set_xlabel('monthly')
    axe[1].set_ylabel('page views')

        
        # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
