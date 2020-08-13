def get_formatted_city(city, country, population=""):

    if population:
        city_country = f"{city}, {country}: {population}"
    else:
        city_country = f"{city}, {country}"

    return city_country.title()