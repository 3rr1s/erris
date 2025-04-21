    # Project: Hospital Patient Management System

    import csv
    import pandas as pd
    import time
    from abc import ABC, abstractmethod


    # Abstract base class for a person
    class Person(ABC):
        @abstractmethod
        def __init__(self, full_name, age):
            self.full_name = full_name
            self.age = age


    # Patient class extending Person
    class Patient(Person):
        def __init__(self, patient_id, full_name, age, diagnosis, severity, logic_expression):
            super().__init__(full_name, age)
            self.patient_id = patient_id
            self.diagnosis = diagnosis
            self.severity = severity
            self.logic_expression = logic_expression


    # Abstract base class for sorting algorithms
    class SortingAlgorithm(ABC):
        @abstractmethod
        def sort(self, patients):
            pass


    # Bubble Sort implementation
    class BubbleSort(SortingAlgorithm):
        def sort(self, patients):
            n = len(patients)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if patients[j].severity < patients[j + 1].severity:
                        patients[j], patients[j + 1] = patients[j + 1], patients[j]
            return patients


    # Merge Sort implementation
    class MergeSort(SortingAlgorithm):
        def sort(self, patients):
            if len(patients) > 1:
                mid = len(patients) // 2
                left = self.sort(patients[:mid])
                right = self.sort(patients[mid:])

                merged = []
                while left and right:
                    if left[0].severity >= right[0].severity:
                        merged.append(left.pop(0))
                    else:
                        merged.append(right.pop(0))
                merged.extend(left or right)
                return merged
            return patients


    # Main Hospital System Class
    class HospitalSystem:
        def __init__(self):
            self.patients = {}
            self.logic_by_severity = {
                range(1, 4): "p and not q",
                range(4, 7): "not p or q",
                range(7, 9): "p and (q or r)",
                range(9, 11): "p and r"
            }

        def generate_logic(self, severity):
            for level_range, expr in self.logic_by_severity.items():
                if int(severity) in level_range:
                    return expr
            return "p"

        def add_patient(self):
            patient_id = input("Enter unique Patient ID: ").strip().lower()
            if patient_id in self.patients:
                print("This ID is already taken. Please use 'Edit' to change details.")
                return

            name = input("Full Name: ").strip()
            try:
                age = int(input("Age: ").strip())
            except ValueError:
                print("Invalid age entered.")
                return

            diagnosis = input("Diagnosis (e.g. flu, fracture, etc.): ").strip()

            try:
                severity = float(input("Severity (1-10): ").strip())
                if not 1 <= severity <= 10:
                    raise ValueError
            except ValueError:
                print("Invalid severity. Must be a number from 1 to 10.")
                return

            logic = self.generate_logic(severity)
            self.patients[patient_id] = Patient(patient_id, name, age, diagnosis, severity, logic)
            print("✅ Patient added successfully.")

        def edit_patient(self):
            patient_id = input("Enter Patient ID to edit: ").strip().lower()
            if patient_id not in self.patients:
                print("❌ Patient not found.")
                return

            patient = self.patients[patient_id]
            print(f"\nEditing: {patient.full_name} | Age: {patient.age} | Diagnosis: {patient.diagnosis} | Severity: {patient.severity}")

            name = input("New Name (Leave empty to keep same): ").strip() or patient.full_name
            age_input = input("New Age (Leave empty to keep same): ").strip()
            age = int(age_input) if age_input else patient.age
            diagnosis = input("New Diagnosis (Leave empty to keep same): ").strip() or patient.diagnosis

            severity_input = input("New Severity (1-10, leave blank to keep same): ").strip()
            if severity_input:
                try:
                    severity = float(severity_input)
                    if not 1 <= severity <= 10:
                        raise ValueError
                except ValueError:
                    print("Invalid severity. Update skipped.")
                    severity = patient.severity
            else:
                severity = patient.severity

            logic = self.generate_logic(severity)
            self.patients[patient_id] = Patient(patient_id, name, age, diagnosis, severity, logic)
            print("✅ Patient updated successfully.")

        def display_patients(self):
            if not self.patients:
                print("⚠️ No patients in the system.")
                return
            print("\n--- Patient List ---")
            for p in self.patients.values():
                print(f"ID: {p.patient_id} | Name: {p.full_name} | Age: {p.age} | Diagnosis: {p.diagnosis} | Severity: {p.severity} | Logic: {p.logic_expression}")

        def search_patient(self, patient_id):
            patient_id = patient_id.strip().lower()
            patient = self.patients.get(patient_id)
            if patient:
                print(f"🔍 Found Patient - ID: {patient.patient_id} | Name: {patient.full_name} | Age: {patient.age} | Diagnosis: {patient.diagnosis} | Severity: {patient.severity}")
            else:
                print("❌ Patient not found.")

        def evaluate_logic(self, expression):
            variables = {"p": True, "q": False, "r": True, "s": False}
            try:
                return eval(expression, {}, variables)
            except Exception as e:
                print(f"Error in logic expression '{expression}': {e}")
                return False

        def sort_patients(self, sorting_algorithm):
            patient_list = list(self.patients.values())
            start = time.time()
            sorted_patients = sorting_algorithm.sort(patient_list)
            duration = time.time() - start

            print(f"\n✅ Sorting complete in {duration:.4f} seconds.")
            for p in sorted_patients:
                print(f"{p.full_name} | Severity: {p.severity} | Logic: {p.logic_expression}")

        def load_csv(self, file_name):
            try:
                df = pd.read_csv(file_name)
                for _, row in df.iterrows():
                    patient_id = row['PatientID'].strip().lower()
                    severity = float(row['Severity'])
                    logic = self.generate_logic(severity)

                    self.patients[patient_id] = Patient(
                        patient_id,
                        row['Name'],
                        int(row['Age']),
                        row['Diagnosis'],
                        severity,
                        logic
                    )
                print("📂 Patients loaded from CSV successfully.")
            except Exception as e:
                print(f"❌ Failed to load CSV: {e}")

        def save_csv(self, file_name="patients.csv"):
            try:
                with open(file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['PatientID', 'Name', 'Age', 'Diagnosis', 'Severity', 'Logic'])
                    for p in self.patients.values():
                        writer.writerow([p.patient_id, p.full_name, p.age, p.diagnosis, p.severity, p.logic_expression])
                print(f"💾 Data saved to {file_name}")
            except Exception as e:
                print(f"❌ Error saving CSV: {e}")


    # Driver code
    def main():
        system = HospitalSystem()
        bubble = BubbleSort()
        merge = MergeSort()

        while True:
            print("\n--- 🏥 Hospital Patient Management Menu ---")
            print("1. Add Patient")
            print("2. Edit Patient")
            print("3. View Patients")
            print("4. Sort (Bubble Sort)")
            print("5. Sort (Merge Sort)")
            print("6. Search by ID")
            print("7. Load from CSV")
            print("8. Save to CSV")
            print("9. Exit")

            choice = input("Your choice: ").strip()

            if choice == '1':
                system.add_patient()
            elif choice == '2':
                system.edit_patient()
            elif choice == '3':
                system.display_patients()
            elif choice == '4':
                system.sort_patients(bubble)
            elif choice == '5':
                system.sort_patients(merge)
            elif choice == '6':
                pid = input("Enter Patient ID: ")
                system.search_patient(pid)
            elif choice == '7':
                fname = input("Filename (default: patients.csv): ").strip() or "patients.csv"
                system.load_csv(fname)
            elif choice == '8':
                fname = input("Filename to save (default: patients.csv): ").strip() or "patients.csv"
                system.save_csv(fname)
            elif choice == '9':
                print("👋 Goodbye!")
                break
            else:
                print("❗ Invalid choice. Try again.")


    if __name__ == "__main__":
        main()

