from random import randrange
import sys

def string_gen(*opts):
    return opts[randrange(0,len(opts))]

def int_gen(i_min, i_max):
    return randrange(i_min, i_max)

def car_gen():
    cars = [
        ("Honda",["Civic", "S2000", "Accord"]),
        ("Jeep", ["Liberty", "Wrangler", "Cherokee", "Grand Cherokee"]),
        ("Kia", ["Rio", "Sportage", "Spectra"]),
        ("Ford", ["F150", "F250", "Fiesta", "Mustang"]),
        ("Chrysler", ["Town and Country"]),
        ("Toyota", ["Camry", "Corolla"]),
        ("Suburu", ["Outback", "Forester", "WRX"]),
        ("Hyundai", ["Sonata", "Allegro", "Fortissimo"]),
        ("VW", ["Beetle", "Beetle 2", "Beetle 3", "Jetta"]),
    ]

    x = randrange(0, len(cars))
    y = randrange(0, len(cars[x][1]))
    return "{}, {}".format(cars[x][0], cars[x][1][y])

class DataRow:
    rows = [
        ("Year", int_gen, (1995, 2018)),
        ("Miles",int_gen, (0, 1000000)),
        ("Make, Model", car_gen, ()),
        ("Condition", string_gen, ("Excellent","Good","Fair","Poor")),
        ("Color", string_gen, ("Red", "Green", "Blue", "Black", "White")),
        ("Transmission", string_gen, ("Automatic", "Manual")),
        ("Drive type", string_gen, ("AWD", "FWD", "RWD")),
    ]

    def print_csv(self, num_rows):
        num_cols = len(self.rows)
        fmt_str = "{}, ".join("" for i in self.rows) + "{}"

        print(fmt_str.format(*[row[0] for row in self.rows]))
        for _ in range(num_rows):
            row_line = [
                x[1](*x[2])
                for x in self.rows
            ]
            print(fmt_str.format(*row_line))

if __name__=="__main__":
    generator = DataRow()
    try:
        generator.print_csv(int(sys.argv[1]))
    except ValueError:
        print("{} is not a number".format(sys.argv[1]))
    except IndexError:
        generator.print_csv(10)

