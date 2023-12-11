import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def extent_per_year(df):
    """
    Bar chart of Arctic SIE measurements per year
    :param df: obj, pandas dataframe 
    :return barplot: plot,  
    """

    # Create year and month columns
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month

    # Count values per year
    df = df.groupby('year')['extent_million_sq_km'].count().reset_index(name='measurements_taken')

    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(10,4)})

    # Plot number of measurements taken per year
    plot_ = sns.barplot(df, x="year", y="measurements_taken")
    plt.title('Arctic Sea Ice Extent: Measurements Per Year', fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Count')

    for ind, label in enumerate(plot_.get_xticklabels()):
        if ind % 5 == 0:  # every 5th label is kept
            label.set_visible(True)
        else:
            label.set_visible(False)

    plt.savefig('figures/measurements_per_year.png')
    plt.show()

    print("Measurements were taken approximately every 2 days from 1978 to 1987.") 
    print("From 1988 to 2023, there is a daily measurement recorded, showing the recording frequency was increased two-fold.")

def seasonality(df):
    """
    Create time series plot to observe seasonality.
    :param df: obj, cleaned sea ice dataframe
    :return lineplot: plot,
    """

    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(10,4)})

    # Plot time series of SIE
    sns.lineplot(x="date", y="extent_million_sq_km", data=df)

    max_year = pd.DatetimeIndex(df['date']).year.max()

    plt.title(f"Arctic Sea Ice Extent: 1978-{max_year}")
    plt.xlabel("Year")
    plt.ylabel("Extent (M km^2)")

    # Save and plot figure
    plt.savefig(f'figures/ts_1978_{max_year}.png')
    plt.show()

    print("The above set is non-stationary as there are clear annual changes in sea ice extent.")

def period_comparison(df):
    """
    Comparing the period start & end seasons.
    :param df: obj, cleaned sea ice dataframe
    :return lineplot: plot,
    """
    sns.set_style('darkgrid')

    # Create year and month columns
    df['year'] = pd.DatetimeIndex(df['date']).year
    df['month'] = pd.DatetimeIndex(df['date']).month

    start_year = pd.DatetimeIndex(df['date']).year.min() + 1
    end_year = pd.DatetimeIndex(df['date']).year.max() - 1

    # Filtering data for start & end years
    sea_ice_start = df[df['year'] == start_year]
    sea_ice_end = df[df['year'] == end_year]

    # Create subplots with two rows and one column
    fig, axes = plt.subplots(1, 1, figsize=(10, 4))

    # Plot for 1978 on the first subplot
    sns.lineplot(x='month', y='extent_million_sq_km', data=sea_ice_start, hue='year', linestyle='dashed', palette='mako', ax=axes)
    # Plot for 2018 on the second subplot
    sns.lineplot(x='month', y='extent_million_sq_km', data=sea_ice_end, hue='year', linestyle='dashed', palette='flare', ax=axes)

    axes.set_title(f'Arctic Sea Ice Extent: Comparison of {start_year} & {end_year}', fontweight='bold')
    axes.set_xlabel('Month')
    axes.set_ylabel('Extent (M km^2)')

    # Save and show plot
    plt.savefig('figures/period_comparison.png')
    plt.show()

    print('By comparing the first full and final years of the set,') 
    print('we observe a decrased local maxima and mimina for the months March and September, respectively.') 
    print('The year 2017 shows an approximate 2 million square kilometer decrease in sea ice extent compared to 1979.')

def annual_changes(df):
    """
    Observing shift in annual sea ice extent
    :param df: obj, cleaned sea ice dataframe
    :return lineplot: plot,
    """

    # Plot annual changes in sea ice extent
    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(10,4)})

    max_year = pd.DatetimeIndex(df['date']).year.max()

    sns.lineplot(data=df, x="month", y="extent_million_sq_km", hue="year", palette="viridis", legend=False)
    plt.title("Annual Changes in Arctic Sea Extent: 1978-{max_year}")
    plt.xlabel("Month")
    plt.ylabel("Extent (M km^2)")

    # Save and show plot
    plt.savefig('figures/sie_annual_changes.png')
    plt.show()

    print('Furthermore, by including each year in the set, we observe a decrease in sea ice extent year-over-year') 
    print('with darker colors representing older years and shifting to younger years as the colors brighten.')

def avg_annual_sie(df):
    """
    Average annual sea ice extent per season.
    :param df: obj, cleaned sea ice dataframe
    :return lineplot: plot,
    """

    # Average Annual Arctic Sea Ice Extent
    df = df.groupby(df['year']).mean().drop(columns=["month"]).reset_index()
    df = df[1:-1]

    # Plot average annual sea ice extent
    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(10,4)})

    sns.lineplot(data=df, x="year", y="extent_million_sq_km", 
                palette="viridis", marker="o", legend=False)
    sns.regplot(data=df, x="year", y="extent_million_sq_km")

    max_year = pd.DatetimeIndex(df['year']).year.max()

    plt.title(f"Average Annual Arctic Sea Extent: 1978-{max_year}")
    plt.xlabel("Year")
    plt.ylabel("Extent (M km^2)")

    # Save and show plot
    plt.savefig('figures/sie_annual_avg.png')
    plt.show()

    print('The above chart displays the average annual sea ice extent where there is a clear decreasing linear trend')
    print('as we move to more current dates.')

def distribution_eval(df, dist_type='boxplot'):
    """
    Distribution evaluation using a boxplot.
    :param df: obj, cleaned sea ice dataframe
    :return boxplot: 
    """

    # Outlier detection
    plt.subplots(figsize=(10, 4))
    sns.set_style('darkgrid')

    if dist_type == 'boxplot':
        sns.boxplot(x=df['extent_million_sq_km'])

        plt.title("SIE Box Plot and Interquartile Range")
        plt.xlabel("Extent (M km^2)")

        plt.savefig("./figures/sie_boxplot.png")
        
        print('The above box plot shows a median line closer to the 75th Percentile, which indicates a negatively skewed distribution.') 
        print('Additionally, no outliers are observed beyond the box plot whiskers.')
    
    else:
        df['extent_million_sq_km'].hist()

        plt.title("SIE Measurement Distribution")
        plt.xlabel("Extent (M km^2)")
        plt.ylabel("Distribution")

        plt.savefig("./figures/sie_distribution.png")

    plt.show()

