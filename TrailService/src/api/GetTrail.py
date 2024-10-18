from flask import request, jsonify

def register_get_routes(app, db_handler):
    @app.route('/api/trails', methods=['GET'])
    def get_filtered_trails():
        bike_parameter = request.args.get('has_bike')
        fishing_parameter = request.args.get('authorize_fishing')

        predicates = []
        print("INFO: Recieved GET request on trails endpoint", flush = True)
        
        if bike_parameter == "True":
            print("INFO: User wants to filter with bike trails", flush=True)
            def has_bike_trail(row):
                return row.get('BikeTrail') == 'Yes'  
            predicates.append(has_bike_trail)

        if fishing_parameter == "True":
            print("INFO: User wants to filter with fishing authorized", flush=True)
            def is_fishing_authorized(row):
                return row.get('FISHING') == 'Yes' 
            predicates.append(is_fishing_authorized)

        filtered_data = db_handler.get_filtered_data(predicates)
        return jsonify(filtered_data)