class Patient:
    def __init__(self, id, name, family_name, age, height, weight):
        self.id = id
        self.name = name
        self.family_name = family_name
        self.age = age
        self.height = height
        self.weight = weight

class Visit:
    def __init__(self, id, beginning_time):
        self.id = id
        self.beginning_time = beginning_time

class System:
    def __init__(self):
        self.patients = {}
        self.visits = []

    def add_patient(self, id, name, family_name, age, height, weight):
        if id in self.patients:
            return "error: this ID already exists"
        if age < 0:
            return "error: invalid age"
        if height < 0:
            return "error: invalid height"
        if weight < 0:
            return "error: invalid weight"
        self.patients[id] = Patient(id, name, family_name, age, height, weight)
        return "patient added successfully"

    def display_patient(self, id):
        if id not in self.patients:
            return "error: invalid ID"
        patient = self.patients[id]
        return f"patient name: {patient.name}\npatient family name: {patient.family_name}\npatient age: {patient.age}\npatient height: {patient.height}\npatient weight: {patient.weight}"

    def add_visit(self, id, beginning_time):
        if id not in self.patients:
            return "error: invalid id"
        if beginning_time < 9 or beginning_time > 18:
            return "error: invalid time"
        for visit in self.visits:
            if visit.beginning_time == beginning_time:
                return "error: busy time"
        self.visits.append(Visit(id, beginning_time))
        return "visit added successfully!"

    def delete_patient(self, id):
        if id not in self.patients:
            return "error: invalid id"
        del self.patients[id]
        self.visits = [visit for visit in self.visits if visit.id != id]
        return "patient deleted successfully!"

    def display_visit_list(self):
        schedule = "SCHEDULE:"
        for visit in self.visits:
            patient = self.patients[visit.id]
            schedule += f"\n{visit.beginning_time}:00 {patient.name} {patient.family_name}"
        return schedule

def main():
    system = System()
    outputs = []
    while True:
        command = input().split()
        if not command:
            outputs.append("invalid command")
            continue
        if command[0] == "exit":
            break
        elif len(command) < 2:
            outputs.append("invalid command")
            continue
        if command[0] == "add" and command[1] == "patient":
            outputs.append(system.add_patient(int(command[2]), command[3], command[4], int(command[5]), int(command[6]), int(command[7])))
        elif command[0] == "display" and command[1] == "patient":
            outputs.append(system.display_patient(int(command[2])))
        elif command[0] == "add" and command[1] == "visit":
            outputs.append(system.add_visit(int(command[2]), int(command[3])))
        elif command[0] == "delete" and command[1] == "patient":
            outputs.append(system.delete_patient(int(command[2])))
        elif command[0] == "display" and command[1] == "visit" and command[2] == "list":
            outputs.append(system.display_visit_list())
        else:
            outputs.append("invalid command")
    print("\n".join(outputs))

if __name__ == "__main__":
    main()



