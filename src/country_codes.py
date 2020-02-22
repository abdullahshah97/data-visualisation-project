from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the 2 digit pygal country code for given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
