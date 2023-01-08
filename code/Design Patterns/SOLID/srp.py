class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # #SRP
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()



class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Dzien dobry dzis mamy 13.12.2022")
j.add_entry("Teraz omawiamy regule SRP")
print(f"Journal entries:\n{j}\n")

file = r'journal.txt'
PersistenceManager.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
