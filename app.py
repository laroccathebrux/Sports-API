from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/f1/circuits',methods=['GET'])
def circuits():
    df = pd.read_csv('csv/f1/circuits.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/constructor_results',methods=['GET'])
def constructor_results():
    df = pd.read_csv('csv/f1/constructor_results.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/constructor_standings',methods=['GET'])
def constructor_standings():
    df = pd.read_csv('csv/f1/constructor_standings.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/constructors',methods=['GET'])
def constructors():
    df = pd.read_csv('csv/f1/constructors.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/driver_standings',methods=['GET'])
def driver_standings():
    df = pd.read_csv('csv/f1/driver_standings.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/drivers',methods=['GET'])
def drivers():
    df = pd.read_csv('csv/f1/drivers.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/lap_times',methods=['GET'])
def lap_times():
    df = pd.read_csv('csv/f1/lap_times.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/pit_stops',methods=['GET'])
def pit_stops():
    df = pd.read_csv('csv/f1/pit_stops.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/qualifying',methods=['GET'])
def qualifying():
    df = pd.read_csv('csv/f1/qualifying.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/races',methods=['GET'])
def races():
    df = pd.read_csv('csv/f1/races.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/results',methods=['GET'])
def results():
    df = pd.read_csv('csv/f1/results.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/seasons',methods=['GET'])
def seasons():
    df = pd.read_csv('csv/f1/seasons.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/sprint_results',methods=['GET'])
def sprint_results():
    df = pd.read_csv('csv/f1/sprint_results.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/f1/status',methods=['GET'])
def status():
    df = pd.read_csv('csv/f1/status.csv')
    return jsonify(df.to_dict(orient='records'))



app.run(debug=True)