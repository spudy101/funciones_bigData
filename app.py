from flask import Flask, jsonify, render_template
from google.cloud import bigquery

app = Flask(__name__)

# Configura tu cliente de BigQuery
client = bigquery.Client()

@app.route('/api/routes')
def get_routes():
    query = """
        SELECT
            r.route_long_name,
            COUNT(*) AS route_count
        FROM
            `dulcet-bucksaw-425222-h3.transporte_us.frequencies` f
        INNER JOIN
            `dulcet-bucksaw-425222-h3.transporte_us.trips` t
        ON
            t.trip_id = f.trip_id
        INNER JOIN
            `dulcet-bucksaw-425222-h3.transporte_us.routes` r
        ON
            r.route_id = t.route_id
        GROUP BY
            r.route_long_name
        ORDER BY
            route_count DESC
    """
    query_job = client.query(query)
    results = query_job.result()

    routes = []
    for row in results:
        routes.append({"route_long_name": row.route_long_name, "route_count": row.route_count})

    return jsonify(routes)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200, debug=True)
