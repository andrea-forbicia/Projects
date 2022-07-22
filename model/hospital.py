from typing import Optional


class Person:
    def __init__(self, name, surname, fiscal_code):
        self.name = name
        self.surname = surname
        self.fiscal_code = fiscal_code


class Patient(Person):
    def __init__(self, name, surname, fiscal_code, patient_code):
        super().__init__(name, surname, fiscal_code)
        self.patient_code = patient_code
        self.doctors = list()


class Doctor(Person):
    def __init__(self, name, surname, fiscal_code, serial_number):
        super().__init__(name, surname, fiscal_code)
        self.serial_number = serial_number
        self.patients = list()


class Hospital:
    def __init__(self):
        self.doctors = dict()
        self.patients = dict()

    def add_doctor(self, name: str, surname: str, fiscal_code: str, serial_number: str) -> None:
        doctor = Doctor(name, surname, fiscal_code, serial_number)
        self.doctors[serial_number] = doctor

    def add_patient(self, name: str, surname: str, fiscal_code: str, patient_code: str) -> None:
        patient = Patient(name, surname, fiscal_code, patient_code)
        self.patients[patient_code] = patient

    def get_patient(self, patient_code: str) -> Optional[Patient]:
        if patient_code not in self.patients.keys():
            return
        return self.patients[patient_code]

    def get_doctor(self, serial_number: str) -> Optional[Doctor]:
        if serial_number not in self.doctors.keys():
            return
        return self.doctors[serial_number]

    def assignment(self, serial_number: str, patient_code: str) -> None:
        doctor = self.get_doctor(serial_number)
        patient = self.get_patient(patient_code)
        doctor.patients.append(patient)
        patient.doctors.append(doctor)

    def get_patients(self, serial_number: str) -> str:
        doctor = self.get_doctor(serial_number)
        patients = doctor.patients
        text = ""
        for patient in patients:
            text = f"{text}Patient code: {patient.patient_code}, " \
                   f"Name: {patient.name}, " \
                   f"Surname: {patient.surname}, " \
                   f"FC: {patient.fiscal_code}\n"
        return text
