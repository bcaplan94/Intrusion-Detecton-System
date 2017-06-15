"""
Datastore class

Class to provide the datastore.
This should be the interface to the data storage method
Whether that is in memory, flat file, or database.

Changes to backend datastore shouldn't affect API
"""


class DataStore:
    data_dict = {}

    def save(self, data, i):
        for key in data:
            if key in self.data_dict:
                #This will now take the correct average based on how many entries there are.
                self.data_dict[key] = (self.data_dict[key] * (i-1) + data[key]) / i
            else:
                self.data_dict.update(data)
