import pandas as pd
arrays = [[1,2,3],["xyz", "abc", "pqr"]]
mi = pd.MultiIndex.from_arrays(arrays, names = ("ids", "student"))
print("The MultiIndex:\n", mi)
print("Names of levels in Multi-Index:\n", mi.names)

#multiindex-ex.2
cities = [["Punjab", "Hyderaba", "Bombay", "Kerala"], ["Melbourne", "Zurich", "Chicago", "Berlin"]]
mi = pd.MultiIndex.from_arrays(cities, names=("india_cities", "usa_cities"))
print("\n\nMultiIndex - 2:\n", mi)
print("Levels in Multi-Index-2:\n", mi.levels)
print("Names of levels in Multi-Index-2:\n", mi.names)

#Multi-index-ex.3
employees = [["E101", "E102", "E103", "E104"], ["emp1", "emp2", "emp3", "emp4"]]
mi = pd.MultiIndex.from_arrays(employees, names = ("emp_ids", "names"))
print("\n\nMultiIndex - 3:\n", mi)
print()
print("Levels in Multi-Index-3:\n", mi.levels)
print()
new_levels = [["E1", "E2", "E3", "E4"],
              ["abc", "pqr", "xyz", "def"]]
newmi = mi.set_levels(new_levels)
print("Setting new levels:\n", newmi)
print("Updated names of levels in Multi-Index-3:\n", mi.names)