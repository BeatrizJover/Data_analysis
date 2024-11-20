import copy

import pandas as pd

belgium_df = pd.read_csv('csv-data/cleaned_dataset_analysis.csv')
belgium_df_list = [group for _, group in belgium_df.groupby('Locality')]

province_of = "Province of"
flanders = ["Province of West Flanders", "Province of East Flanders", "Province of Antwerp", "Province of Flemish Brabant", "Province of Limburg"]
brussels = ["Brussels-Capital Region"]
walloon = ["Province of Liège", "Province of Luxembourg", "Province of Hainaut", "Province of Namur", "Province of Walloon Brabant"]

flanders_i = []
brussels_i = []
walloon_i = []

for i, row in belgium_df.iterrows():
    if row["Province"] in flanders:
        flanders_i.append(i)
    elif row["Province"] in brussels:
        brussels_i.append(i)
    elif row["Province"] in walloon:
        walloon_i.append(i)
    else:
        print(F"ERROR {row}")

flanders_df = belgium_df.iloc[flanders_i,:]
brussels_df = belgium_df.iloc[brussels_i,:]
walloon_df = belgium_df.iloc[walloon_i,:]

flanders_df_list = [group for _, group in flanders_df.groupby('Locality')]
brussels_df_list = [group for _, group in brussels_df.groupby('Locality')]
walloon_df_list = [group for _, group in walloon_df.groupby('Locality')]

flanders_df.to_csv('csv-data/flanders_dataset.csv')
brussels_df.to_csv('csv-data/brussels_dataset.csv')
walloon_df.to_csv('csv-data/walloon_dataset.csv')



def average_price_municipality(data, most=False, least=False):
    municipality_average_price = {}
    for group in data:
        total = 0
        count = 0
        locality = group['Locality'].iloc[0]
        for _, row in group.iterrows():
            total += row['Price']
            count += 1
        average_price = total / count
        municipality_average_price[locality] = average_price
    if most:
        return max(municipality_average_price, key=municipality_average_price.get)
    if least:
        return min(municipality_average_price, key=municipality_average_price.get)
    else:
        return municipality_average_price

def median_price_municipality(data, most=False, least=False):
    municipality_median_price = {}
    for group in data:
        locality = group['Locality'].iloc[0]
        temp_df = group[group['Locality'] == locality]
        municipality_median_price[locality] = temp_df['Price'].median()
    if most:
        return max(municipality_median_price, key=municipality_median_price.get)
    if least:
        return min(municipality_median_price, key=municipality_median_price.get)
    else:
        return municipality_median_price



def price_m2_municipality(data, terrace:bool=False,garden:bool= False, most=False, least=False):
    municipality_price_m2 = {}
    for group in data:
        meter_squared = 0
        price = 0
        count = 0
        locality = group['Locality'].iloc[0]
        for _, row in group.iterrows():
            meter_squared += row['Livable Space (m2)']
            if terrace:
                meter_squared += row["Terrace Area (m2)"]
            if garden:
                meter_squared += row["Garden Area (m2)"]
            price += row['Price']
            count += 1
        price_m2 = (meter_squared / price) * count
        municipality_price_m2[locality] = price_m2
    if most:
        return max(municipality_price_m2, key=municipality_price_m2.get)
    if least:
        return min(municipality_price_m2, key=municipality_price_m2.get)
    else:
        return municipality_price_m2




voi_dict = {"average_price": None, "median_price": None, "price_m2": None}

municipality_voi = {"most_expensive_belgium": copy.deepcopy(voi_dict),
                    "least_expensive_belgium": copy.deepcopy(voi_dict),
                    "most_expensive_flanders": copy.deepcopy(voi_dict),
                    "least_expensive_flanders": copy.deepcopy(voi_dict),
                    "most_expensive_walloons": copy.deepcopy(voi_dict),
                    "least_expensive_walloons": copy.deepcopy(voi_dict),
                    "most_expensive_brussels": copy.deepcopy(voi_dict),
                    "least_expensive_brussels": copy.deepcopy(voi_dict),}

municipality_voi["most_expensive_belgium"]["average_price"] = average_price_municipality(belgium_df_list, most=True)
municipality_voi["most_expensive_belgium"]["median_price"] = median_price_municipality(belgium_df_list, most=True)
municipality_voi["most_expensive_belgium"]["price_m2"] = price_m2_municipality(belgium_df_list, most=True)

municipality_voi["least_expensive_belgium"]["average_price"] = average_price_municipality(belgium_df_list, least=True)
municipality_voi["least_expensive_belgium"]["median_price"] = median_price_municipality(belgium_df_list, least=True)
municipality_voi["least_expensive_belgium"]["price_m2"] = price_m2_municipality(belgium_df_list, least=True)

municipality_voi["most_expensive_flanders"]["average_price"] = average_price_municipality(flanders_df_list, most=True)
municipality_voi["most_expensive_flanders"]["median_price"] = median_price_municipality(flanders_df_list, most=True)
municipality_voi["most_expensive_flanders"]["price_m2"] = price_m2_municipality(flanders_df_list, most=True)

municipality_voi["least_expensive_flanders"]["average_price"] = average_price_municipality(flanders_df_list, least=True)
municipality_voi["least_expensive_flanders"]["median_price"] = median_price_municipality(flanders_df_list, least=True)
municipality_voi["least_expensive_flanders"]["price_m2"] = price_m2_municipality(flanders_df_list, least=True)

municipality_voi["most_expensive_walloons"]["average_price"] = average_price_municipality(walloon_df_list, most=True)
municipality_voi["most_expensive_walloons"]["median_price"] = median_price_municipality(walloon_df_list, most=True)
municipality_voi["most_expensive_walloons"]["price_m2"] = price_m2_municipality(walloon_df_list, most=True)

municipality_voi["least_expensive_walloons"]["average_price"] = average_price_municipality(walloon_df_list, least=True)
municipality_voi["least_expensive_walloons"]["median_price"] = median_price_municipality(walloon_df_list, least=True)
municipality_voi["least_expensive_walloons"]["price_m2"] = price_m2_municipality(walloon_df_list, least=True)

municipality_voi["most_expensive_brussels"]["average_price"] = average_price_municipality(brussels_df_list, most=True)
municipality_voi["most_expensive_brussels"]["median_price"] = median_price_municipality(brussels_df_list, most=True)
municipality_voi["most_expensive_brussels"]["price_m2"] = price_m2_municipality(brussels_df_list, most=True)

municipality_voi["least_expensive_brussels"]["average_price"] = average_price_municipality(brussels_df_list, least=True)
municipality_voi["least_expensive_brussels"]["median_price"] = median_price_municipality(brussels_df_list, least=True)
municipality_voi["least_expensive_brussels"]["price_m2"] = price_m2_municipality(brussels_df_list, least=True)

print(municipality_voi)

municipality_voi_df = pd.DataFrame(municipality_voi)
print(municipality_voi_df)

municipality_voi_df.to_csv('csv-data/result.csv')