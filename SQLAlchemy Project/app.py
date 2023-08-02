# Import the dependencies.
from datetime import datetime, timedelta
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False, connect_args={"check_same_thread": False},)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    #Return all available links, some in anchor form and other is manually typed.
    return (
        """
        <div>
        <h1>Welcome to the homepage!</h1>

        <h3>Available Routes: </h3>
        <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a>
        <br />
        <a href='/api/v1.0/stations'>/api/v1.0/stations</a>
        <br />
        <a href='/api/v1.0/tobs'>/api/v1.0/tobs</a>
        
        <p>You can also query with /api/v1.0/<start> where start is a specified start date or /api/v1.0/<start>/<end> where you also can input an end date. </p>
        </div>
        """
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    #Get Recent Date
    recent_Date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    #Calculate Time Difference
    difference_Date = datetime.strptime(recent_Date[0], "%Y-%m-%d") - timedelta(weeks=52)
    # Create Query where date is greater than or equal to differenceDate
    scores = session.query(measurement.date, measurement.prcp).filter(measurement.date >= difference_Date).all()
    result = {}
    for score in scores:
        result[score[0]] = score[1]
    return (
        jsonify(result)
    )

@app.route("/api/v1.0/stations")
def stations():
    stations = {}
    i=0
    #Create query for all stations and place in result
    for place in session.query(station.station).all():
        stations.__setitem__(i, place[0])
        i+=1
    return (
        jsonify(stations)
    )

@app.route("/api/v1.0/tobs")
def tobs():
    #Create query for date and tobs for the most active station
    active_Station_Temps = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').order_by(measurement.date.desc()).all()
    result = {}
    for activeStats in active_Station_Temps:
        result[activeStats[0]] = activeStats[1]
    return (
        jsonify(result)
    )

@app.route("/api/v1.0/<start>")
def startDate(start):
    #Convert Date
    start = datetime.strptime(start, "%Y-%m-%d")

    #Create Query
    stats = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).all()
    #mostActiveStats contains our result in tuple form so we can extract as such.
    result = {
        "min": stats[0][0],
        "max": stats[0][1],
        "avg": stats[0][2]
    }
    return (
        jsonify(result)
    )

@app.route("/api/v1.0/<start>/<end>")
def startEndDate(start, end):
    #Convert Dates
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    # Check if we have a valid start-end
    if (start > end):
        return "Error: Please enter a valid start date. Start date exceeds end date."
    #Create Query
    stats = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()
    #mostActiveStats contains our result in tuple form so we can extract as such.
    result = {
        "min": stats[0][0],
        "max": stats[0][1],
        "avg": stats[0][2]
    }
    return (
        jsonify(result)
    )

if __name__ == '__main__':
    app.run(debug=True)