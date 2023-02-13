car_models = [
    {
        "make": "Hyundai",
        "model": "Santa Fe",
        "submodels": [
            {"abbr": "SE", "full_name": "Santa Fe SE"}, # Santa Fe SE
            {"abbr": "SL", "full_name": "Santa Fe SEL"}, # Santa Fe SEL
            {"abbr": "LT", "full_name": "Santa Fe Limited"}, # Santa Fe Limited
            {"abbr": "CL", "full_name": "Santa Fe Calligraphy"}, # Santa Fe Calligraphy
            {"abbr": "NL", "full_name": "Santa Fe N Line"} # Santa Fe N Line
        ]
    },
    {
        "make": "Ford",
        "model": "Everest",
        "submodels": [
            {"abbr": "AM", "full_name": "Ford Everest Ambiente"}, # Ford Everest Ambiente
            {"abbr": "TR", "full_name": "Ford Everest Trend"}, # Ford Everest Trend
            {"abbr": "TT", "full_name": "Ford Everest Titanium"}, # Ford Everest Titanium
            {"abbr": "TH", "full_name": "Ford Everest Thunder"} # Ford Everest Thunder
        ]
    },
    {
        "make": "Mazda", 
        "model": "CX-9",
        "submodels": [
            {"abbr": "SP", "full_name": "Mazda CX-9 Sport"}, # Mazda CX-9 Sport
            {"abbr": "TR", "full_name": "Mazda CX-9 Touring"}, # Mazda CX-9 Touring
            {"abbr": "GT", "full_name": "Mazda CX-9 Grand Touring"}, # Mazda CX-9 Grand Touring
            {"abbr": "SG", "full_name": "Mazda CX-9 Signature"} # Mazda CX-9 Signature
        ]
    },
    {
        "make": "Mazda",
        "model": "CX-8",
        "submodels": [
            {"abbr": "SP", "full_name": "Mazda CX-8 Sport"}, # Mazda CX-8 Sport
            {"abbr": "TR", "full_name": "Mazda CX-8 Touring"}, # Mazda CX-8 Touring
            {"abbr": "AK", "full_name": "Mazda CX-8 Asaki"} # Mazda CX-8 Asaki
        ]
    },
    {
        "make": "Mitsubishi",
        "model": "Outlander",
        "submodels": [
            {"abbr": "ES", "full_name": "Mitsubishi Outlander ES"}, # Mitsubishi Outlander ES
            {"abbr": "SE", "full_name": "Mitsubishi Outlander SE"}, # Mitsubishi Outlander SE
            {"abbr": "LE", "full_name": "Mitsubishi Outlander LE"}, # Mitsubishi Outlander LE
            {"abbr": "GT", "full_name": "Mitsubishi Outlander GT"} # Mitsubishi Outlander GT
        ]
    },
    {
        "make": "Kia",
        "model": "Carnival",
        "submodels": [
            {"abbr": "LX", "full_name ": "Kia Carnival LX"}, # Kia Carnival LX
            {"abbr": "EX", "full_name": "Kia Carnival EX"}, # Kia Carnival EX
            {"abbr": "SX", "full_name": "Kia Carnival SX"}, # Kia Carnival SX
            {"abbr": "PL", "full_name": "Kia Carnival Platinum"} # Kia Carnival Platinum
]
},
{
        "make": "Kia",
        "model": "Sorento",
        "submodels": [
            {"abbr": "LX", "full_name": "Kia Sorento LX"}, # Kia Sorento LX
            {"abbr": "EX", "full_name": "Kia Sorento EX"}, # Kia Sorento EX
            {"abbr": "SX", "full_name": "Kia Sorento SX"}, # Kia Sorento SX
            {"abbr": "GT", "full_name": "Kia Sorento GT Line"} # Kia Sorento GT Line
]
}
]

class Vehicle:
    def __init__(self, make, model, submodel, year, import_status, listing, num_doors, fuel, engine_size, age, colour, num_seats, notes, numplate):
        self.make = make
        self.model = model
        self.submodel = submodel
        self.year = year
        self.import_status = import_status
        self.listing = listing
        self.num_doors = num_doors
        self.fuel = fuel
        self.engine_size = engine_size
        self.age = age
        self.colour = colour
        self.num_seats = num_seats
        self.notes = notes
        self.numplate = numplate
