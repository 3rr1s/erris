import csv
import time
import operator
from typing import List, Dict

class Patient:
    def __init__(self, id: str, name: str, age: int, illness: str, score: float = 0.0):
        self.id = id
        self.name = name
        self.age = age
        self.illness = illness
        self.score = score

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Illness: {self.illness}, Score: {self.score}"

class HospitalManagementSystem:
    def __init__(self):
        self.patients: Dict[str, Patient] = {}

    def add_patient(self):
        id = input("Enter patient ID: ")
        if id in self.patients:
            print("Patient ID already exists!")
            return
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        illness = input("Enter patient illness: ")
        score = float(input("Enter patient score (0-10): "))
        self.patients[id] = Patient(id, name, age, illness, score)
        print("Patient added successfully!")

    def edit_patient(self):
        id = input("Enter patient ID to edit: ")
        if id not in self.patients:
            print("Patient not found!")
            return
        patient = self.patients[id]
        print("Current patient details:", patient)
        patient.name = input("Enter new name (or press enter to skip): ") or patient.name
        patient.age = int(input("Enter new age (or press enter to skip): ") or patient.age)
        patient.illness = input("Enter new illness (or press enter to skip): ") or patient.illness
        patient.score = float(input("Enter new score (or press enter to skip): ") or patient.score)
        print("Patient updated successfully!")

    def view_patients(self):
        if not self.patients:
            print("No patients in the system!")
            return
        for patient in self.patients.values():
            print(patient)

    def bubble_sort(self, sort_choice):

        sort_key = {
            '1': 'id',
            '2': 'name',
            '3': 'age',
            '4': 'score'
        }.get(sort_choice, 'score')

        patients_list = list(self.patients.values())
        n = len(patients_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if str(getattr(patients_list[j], sort_key)).lower() > str(getattr(patients_list[j+1], sort_key)).lower():
                    patients_list[j], patients_list[j+1] = patients_list[j+1], patients_list[j]
        return patients_list

    def merge_sort(self, sort_choice):

        sort_key = {
            '1': 'id',
            '2': 'name',
            '3': 'age',
            '4': 'score'
        }.get(sort_choice, 'score')

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if str(getattr(left[i], sort_key)).lower() <= str(getattr(right[j], sort_key)).lower():
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            return merge(left, right)

        return sort(list(self.patients.values()))

    def search_by_id(self):
        id = input("Enter patient ID to search: ")
        patient = self.patients.get(id)
        if patient:
            print(patient)
        else:
            print("Patient not found!")

    def load_from_csv(self):
        try:
            filename = input("Enter CSV file name: ")
            if not filename.endswith('.csv'):
                filename += '.csv'

            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        id = row.get('id', str(len(self.patients) + 1))
                        name = row.get('name', '')
                        age = int(row.get('age', 0))
                        illness = row.get('illness', '')
                        score = float(row.get('score', 0.0))

                        self.patients[id] = Patient(id, name, age, illness, score)
                    except (ValueError, KeyError) as e:
                        print(f"Error processing row: {row}. Error: {e}")
                        continue

            print("Data loaded successfully!")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found!")
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_csv(self):
        try:
            filename = input("Enter CSV file name to save: ")
            if not filename.endswith('.csv'):
                filename += '.csv'

            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'name', 'age', 'illness', 'score'])
                writer.writeheader()
                for patient in self.patients.values():
                    writer.writerow({
                        'id': patient.id,
                        'name': patient.name,
                        'age': patient.age,
                        'illness': patient.illness,
                        'score': patient.score
                    })
            print(f"Data saved successfully to {filename}!")
        except Exception as e:
            print(f"Error saving file: {e}")

def main():
    system = HospitalManagementSystem()
    while True:
        print("\nHospital Patient Management System")
        print("1. Add Patient")
        print("2. Edit Patient")
        print("3. View Patients")
        print("4. Sort (Bubble Sort)")
        print("5. Sort (Merge Sort)")
        print("6. Search by ID")
        print("7. Load from CSV")
        print("8. Save to CSV")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            system.add_patient()
        elif choice == '2':
            system.edit_patient()
        elif choice == '3':
            system.view_patients()
        elif choice == '4':
            print("\nSorting options:")
            print("1. Sort by ID")
            print("2. Sort by Name")
            print("3. Sort by Age")
            print("4. Sort by Score")
            sort_choice = input("Enter sorting choice (1-4): ")
            sorted_patients = system.bubble_sort()
            print("\nSorted list:")
            for patient in sorted_patients:
                if sort_choice == '1':
                    print(f"ID: {patient.id}")
                elif sort_choice == '2':
                    print(f"Name: {patient.name}")
                elif sort_choice == '3':
                    print(f"Age: {patient.age}")
                elif sort_choice == '4':
                    print(f"Score: {patient.score}")
                else:
                    print(patient)
        elif choice == '5':
            print("\nSorting options:")
            print("1. Sort by ID")
            print("2. Sort by Name")
            print("3. Sort by Age")
            print("4. Sort by Score")
            sort_choice = input("Enter sorting choice (1-4): ")
            sorted_patients = system.merge_sort()
            print("\nSorted list:")
            for patient in sorted_patients:
                if sort_choice == '1':
                    print(f"ID: {patient.id}")
                elif sort_choice == '2':
                    print(f"Name: {patient.name}")
                elif sort_choice == '3':
                    print(f"Age: {patient.age}")
                elif sort_choice == '4':
                    print(f"Score: {patient.score}")
                else:
                    print(patient)
        elif choice == '6':
            system.search_by_id()
        elif choice == '7':
            system.load_from_csv()
        elif choice == '8':
            system.save_to_csv()
        elif choice == '9':
            print("Thank you for using the Hospital Management System!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()