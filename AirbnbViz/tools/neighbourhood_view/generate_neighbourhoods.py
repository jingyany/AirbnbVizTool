def generate_neighbourhoods():
    data1 = pd.read_csv("../../data/listings.csv")
    data2 = pd.read_csv("../../data/listings2.csv")
    neighbourhood = data1['neighbourhood'].tolist()
    price = data1['price'].tolist()
    rating = data2['review_scores_rating'].tolist()

    # neighourhood name list
    name_list = [data1['neighbourhood'][0]]
    n = len(neighbourhood)
    for i in range(1, n):
        if neighbourhood[i] != neighbourhood[i - 1]:
            name_list.append(neighbourhood[i])

    # avg price, avg rating by neighbourhood
    price_list = data1.groupby(data1.neighbourhood).mean()['price']
    rating_list = data2.groupby(data1.neighbourhood).mean()['review_scores_rating']

    avg_price = []
    avg_rating = []

    d = len(name_list)
    for i in range(0, d):
        price_target = price_list[name_list[i]]
        rating_target = rating_list[name_list[i]]
        avg_price.append(price_target)
        avg_rating.append(rating_target)

    with open('../../data/neighbourhoods.geojson') as f:
        data = json.load(f)
    for i in range(0, 91):
        a_dict = {'price': avg_price[i], 'rating': avg_rating[i]}
        data["features"][i]["properties"].update(a_dict)

    with open('../../js/neighbourhoods.json', 'w') as f:
        json.dump(data, f)

    file = open('../../js/neighbourhoods.json')
    data = json.load(file)

    with open('../../js/neighbourhoods.js', 'w') as f:
        f.write("var neighbourhoods = " + str(data));
        f.close()

