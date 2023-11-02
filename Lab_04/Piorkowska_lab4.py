import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane temperatur i wyznacz średnią temperaturę, minimalną i maksymalną temperaturę w danym regionie.
def zadanie_1():
    temperatures = pd.read_csv("city_temperature.csv", low_memory=False)
    pd.set_option('display.max_columns', None)
    region = temperatures.groupby('Region')
    print(region['AvgTemperature'].mean())
    print(region['AvgTemperature'].min())
    print(region['AvgTemperature'].max())

# Następnie wyznacz te same wskazania dla poszczególnych miesięcy
def zadanie_1_2():
    temperatures = pd.read_csv("city_temperature.csv", low_memory=False)
    pd.set_option('display.max_columns', None)
    result = temperatures.groupby(['Region', 'Month'])['AvgTemperature'].aggregate(['mean', 'min', 'max'])
    print(result)

def pivot_table():
    data = pd.read_csv("city_temperature.csv", low_memory=False)
    df = data.drop(columns=['Day']).pivot_table(columns='Region', index=['Year', 'Month'],
                                                aggfunc=['min', 'max', 'mean'], values='AvgTemperature')
    pd.set_option('display.max_columns', None)
    print(df)
    df.to_csv("pivot_table_test.csv")

def zadanie_2():
    original_data = pd.read_csv("city_temperature.csv", low_memory=False)
    df = original_data.drop(columns=['Day']).pivot_table(columns='Region', index=['Year', 'Month'], aggfunc='mean', values='AvgTemperature')
    # df.to_csv("zadanie_2_obribka.csv")
    june_data = df.loc[df.index.get_level_values('Month') == 6]
    december_data = df.loc[df.index.get_level_values('Month') == 12]
    # Removig 200 and 201 years
    december_data_drop_redundant_data = (december_data.index.get_level_values('Year') >= 1995)
    filtered_december_data = december_data[december_data_drop_redundant_data]
    print(filtered_december_data)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for region in june_data.columns:
        axes[0].plot(june_data.index.get_level_values('Year'), june_data[region], label=region)
    axes[0].set_title('Average Temperatures in June')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Average Temperature')
    axes[0].legend()

    for region in december_data.columns:
        axes[1].plot(filtered_december_data.index.get_level_values('Year'), filtered_december_data[region], label=region)

    axes[1].set_title('Average Temperatures in December')
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Average Temperature')
    axes[1].legend()

    plt.tight_layout()
    plt.show()

def zadanie_3():
    titanic_data = pd.read_csv("titanic_train.csv", low_memory=False)
    # Używając grupowania lub tabeli przestawnej spróbuj stworzyć dataset zawierający informację o liczbie osób które
    # przeżyły katastrofę z podziałem na płeć i klasę w której podróżowały

    # Removing redundant columns from dataset
    titanic_removed_redundant_data = titanic_data.drop(columns=['PassengerId', 'Name', 'Age', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked', 'SibSp'])

    amount_of_people_by_sex_and_class = titanic_removed_redundant_data.groupby(['Sex', 'Pclass']).count()
    survived_sum_by_sex_and_class = titanic_removed_redundant_data.groupby(['Sex', 'Pclass']).sum()

    # Wyznacz udział procentowy osób, które przeżyły z uwzględnieniem płci i klasy biletu
    percentage_survived = (survived_sum_by_sex_and_class / amount_of_people_by_sex_and_class) * 100
    percentage_survived = percentage_survived.reset_index()
    percentage_survived = percentage_survived.rename(columns={'Survived': 'Percentage Survived'})

    # Wyniki wyświetl w formie wykresu słupkowego
    grouped = percentage_survived.pivot(index='Pclass', columns='Sex', values='Percentage Survived')
    ax = grouped.plot(kind='bar', figsize=(10, 6), color=['blue', 'green'])
    plt.xlabel("Class")
    plt.ylabel("Percentage Survived")
    plt.title("Percentage of Survivors by Class and Sex")
    plt.legend(title="Sex")

    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',va='center')

    plt.show()


    print(percentage_survived)
def main():
    # zadanie_1()
    # zadanie_1_2()
    # pivot_table()
    # zadanie_2()
    zadanie_3()

if __name__ == "__main__":
    main()