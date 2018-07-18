# Big Car Database Thing

## Installation steps
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. Done!

## Usage
```
python gen.py [number of cars (default:10)]
python gen.py [number of cars (default:10)] > cars.csv
```
Outputs a CSV file

### Example
`python gen.py 100000 > cars.csv`

## To-Do

* Make the auto-generated cars make sense
* Ingest into a DB
* Create a RESTful API to access the cars
    * Include search and sort operations
* Make a web frontend to access information about the cars
* Scale smoothly to 10,000,000+ cars and > 3 requests/second


