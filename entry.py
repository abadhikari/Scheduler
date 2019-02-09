class entry:
    def __init__(self,subject,assignment_name, date):
        self.subject = subject
        self.assignment_name = assignment_name
        self.date = date
        self.write_entry_to_file()

    def write_entry_to_file(self):
        # used to write entry to the entries txt file
        file = open('entries.txt','a')
        entry = self.subject + '/' + self.assignment_name + '/' + self.date + '\n'
        file.write(entry)
        file.close()

    def __str__(self):
        return self.subject + '/' + self.assignment_name + '/' + self.date
