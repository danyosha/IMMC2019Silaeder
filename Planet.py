class Earth:
    def next_year_update(self):
        for i in range(len(self.people)):
            self.people[i] += (self.people[i]) / 80