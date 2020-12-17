d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
f = e | d
print(f)

def pivot():
    Flexmonster = {
        'container' : 'pivot',
        'componentFolder': "https://cdn.flexmonster.com/",
        'height': 600,
        'toolbar': True,
        'report': {
            "dataSource": {
                "type": "api",
                "url": "http://localhost:9204/mongo", # the url where our connector is running
                "index": "marketing", # specify the collection’s name
            },
            "slice": {
                "rows": [
                {
                    "uniqueName": "Country",
                }
            ],
            "columns": [
                {
                    "uniqueName": "[Measures]",
                }
            ],
            "measures": [
                {
                    "uniqueName": "Leads",
                    "aggregation": "sum",
                },
                {
                    "uniqueName": "Opportunities",
                    "aggregation": "sum",
                }
            ],
            }
        }
    }
def pivot_charts():
    Flexmonster = {
        'container' : 'pivot_charts',
        'componentFolder': "https://cdn.flexmonster.com/",
        'height': 600,
        'toolbar': True,
        'report': {}
    }