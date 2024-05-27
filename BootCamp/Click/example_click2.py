import click # type: ignore


print (click.__doc__)
@click.command()
@click.option('--days', default=7, help='Number of days.')
@click.option('--months', default=0, help='Number of months')
@click.option('--years', default=0, help='Number of Years')


def calculateWeekends(days, months, years):
    """Calculate the Number of Weekends"""
    totalDays= (days+months*30+years*12*30)
    GetWeeksEnds= totalDays/7*2
    print(f"The Number of Weekends in {years} Years {months} Months & {days} Days is : {GetWeeksEnds}")
    


if __name__ == '__main__':
    calculateWeekends()
## Usage python3  example_click2.py --days 365  --months 0 --years 0 ##