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

for i, rows in belgium_df.iterrows():
    if rows["Province"] in flanders:
        flanders_i.append(i)
    elif rows["Province"] in brussels:
        brussels_i.append(i)
    elif rows["Province"] in walloon:
        walloon_i.append(i)
    else:
        print(F"ERROR {rows}")

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
        most_expensive = max(municipality_average_price, key=municipality_average_price.get)
        return most_expensive, municipality_average_price[most_expensive]
    if least:
        least_expensive = min(municipality_average_price, key=municipality_average_price.get)
        return least_expensive, municipality_average_price[least_expensive]
    else:
        return municipality_average_price

def median_price_municipality(data, most=False, least=False):
    municipality_median_price = {}
    for group in data:
        locality = group['Locality'].iloc[0]
        temp_df = group[group['Locality'] == locality]
        municipality_median_price[locality] = int(temp_df['Price'].median())
    if most:
        most_expensive = max(municipality_median_price, key=municipality_median_price.get)
        return most_expensive, municipality_median_price[most_expensive]
    if least:
        least_expensive = min(municipality_median_price, key=municipality_median_price.get)
        return least_expensive, municipality_median_price[least_expensive]
    else:
        return municipality_median_price



def price_m2_municipality(data, terrace:bool=False,garden:bool=False,land_surface:bool=False, most=False, least=False):
    municipality_price_m2 = {}
    for group in data:
        meter_squared = 0
        price = 0
        locality = group['Locality'].iloc[0]
        for _, row in group.iterrows():
            meter_squared += row['Livable Space (m2)']
            if terrace:
                meter_squared += row["Terrace Area (m2)"]
            if garden:
                meter_squared += row["Garden Area (m2)"]
            if land_surface:
                meter_squared += row["Surface of the Land (m2)"]
            price += row['Price']
        price_m2 = (price/meter_squared)
        price_m2 = round(price_m2,2)
        municipality_price_m2[locality] = price_m2
    if most:
        most_expensive = max(municipality_price_m2, key=municipality_price_m2.get)
        return most_expensive, municipality_price_m2[most_expensive]
    if least:
        least_expensive = min(municipality_price_m2, key=municipality_price_m2.get)
        return least_expensive, municipality_price_m2[least_expensive]
    else:
        return municipality_price_m2


municipality_voi = {"most_expensive_belgium": {},
                    "least_expensive_belgium": {},
                    "most_expensive_flanders": {},
                    "least_expensive_flanders": {},
                    "most_expensive_walloons": {},
                    "least_expensive_walloons": {},
                    "most_expensive_brussels": {},
                    "least_expensive_brussels": {}}

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

molenbeek = brussels_df.groupby('Locality').get_group('Molenbeek')
Ixelles = brussels_df.groupby('Locality').get_group('Ixelles-chatelain')
schuiferskapelle = flanders_df.groupby('Locality').get_group('Schuiferskapelle')
gravenwezel = flanders_df.groupby('Locality').get_group('S-gravenwezel-schilde')
lasne = walloon_df.groupby('Locality').get_group('Lasne-ohain')
bouillon = walloon_df.groupby('Locality').get_group('Bouillon-ucimont')

def subtype(df, name):
    counts = df['Subtype of Property'].value_counts(normalize=True) * 100
    counts_subtype = round(counts,1)

    results = counts_subtype.reset_index()
    results.columns = ['subtype of properties', 'percentage']

    print(results)

    results.to_csv(F'csv-data/municipalities/{name}.csv', index=False)

    return results

molenbeek_subtype = subtype(molenbeek, 'Molenbeek')
ixelles_subtype = subtype(Ixelles, 'Ixelles-chatelain')
schuiferskapelle_subtype = subtype(schuiferskapelle, 'Schuiferskapelle')
gravenwezel_subtype = subtype(gravenwezel, 'S-gravenwezel-schilde')
lasne_subtype = subtype(lasne, 'Lasne-ohain')
bouillon_subtype = subtype(bouillon, 'Bouillon-ucimont')

