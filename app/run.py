from api import app
from waitress import serve


if __name__ == "__main__":
    app.run(debug=True, port=8610, host="0.0.0.0")
    # Please use waitress serve for the production deployement
    # serve(app=app, host='0.0.0.0', port='8601')
