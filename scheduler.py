from pq import PriorityQueue
from entry import entry
from date import date

class scheduler:
    def __init__(self):
        self.pq = PriorityQueue()
        self.read_from_file()

    def read_from_file(self):
        file = open('entries.txt','r')
        for line in file:
            task_entry = self.strng_to_entry(line[:-2])
            self.pq.insert(task_entry, task_entry.date.find_priority())
        file.close()

    def strng_to_entry(self,strng):
        # used to convert information from txt file into entry class
        entry_list = strng.split('/')
        entry_date = date(entry_list[2],entry_list[3],entry_list[4],entry_list[5],entry_list[6],entry_list[7])
        ret_entry = entry(entry_list[0],entry_list[1],entry_date)
        return ret_entry

    def delete_entry(self, task_name):
        # first find the entry with the task_name in the assignment_name and then deletes
        pass

    def print_schedule(self):
        new_pq = PriorityQueue(self.pq.getentries())
        while len(new_pq) > 0:
            print(new_pq.removemin())

    def write_pq_to_file(self):
        # gets the entries from the pq and writes them to the txt file
        for entry in self.pq._entries:
            entry.item.write_entry_to_file()


