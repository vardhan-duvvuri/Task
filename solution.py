#!/usr/bin/python

class FootTraffic():
    def __init__(self,filename):
        self._filename = filename
        self.d={}
        self.sorted_d={}
    def read(self):
        temp_data = [line.split() for line in open(self._filename)]
        data=temp_data[1:]

        for _, room_number, direction, time in data:
            if not room_number in self.d:
                self.d[room_number] = []
            self.d[room_number].append(-int(time) if direction == 'I' else int(time))
    def sort(self):
        self.sorted_d = sorted(self.d, key=lambda x: int(x))
    def display(self):
        for key in self.sorted_d:
            visitors = len(self.d[key]) / 2
            print("Room %s, %d minute average visit, %d visitor(s) total" % 
                (key, sum(self.d[key])/visitors, visitors))

if __name__ == "__main__":
    filename=raw_input("Enter Test file name : ")
    f=FootTraffic(filename)
    f.read()
    f.sort()
    f.display()

