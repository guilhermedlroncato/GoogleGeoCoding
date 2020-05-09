import requests

def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    api_key = 'AIzaSyDIcve1_XU_0op6b15YrFLW54uyyKAbrxc'
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    # see how our endpoint includes our API key? Yes this is yet another reason to restrict the key
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return lat, lng

print(extract_lat_long_via_address(89042299))
print(extract_lat_long_via_address('Johann Ohf, 1445, Blumenau- SC'))