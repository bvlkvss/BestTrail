import requests
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="BestTrail, an app that finds the best trails in Boulton for your needs")
    parser.add_argument('--bike', action='store_true', help='Filter for parks with bike trails.')
    parser.add_argument('--fishing', action='store_true', help='Filter for parks with fishing.')
    return parser.parse_args()

def fetch_data(bike_parameter, fishing_parameter):
    url = "http://127.0.0.1/api/trails"
    params = {}

    if bike_parameter:
        params['has_bike'] = bike_parameter
    if fishing_parameter:
        params['authorize_fishing'] = fishing_parameter

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    args = parse_arguments()
    data = fetch_data(args.bike, args.fishing)
    if data is not None:
        print("The following parks respect your criterias: \n\n")
        for row in data:
            print(f"The park {row.get('AccessName')} at {row.get('Address')}")
    else:
        print("Unfortunately our service is currently unavailable. Try again later.")

if __name__ == "__main__":
    main()