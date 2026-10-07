class Doctor:
    def __init__(self, name):
        self.name = name

    def treat(self):
        print(f"Врач {self.name} осматривает пациента.")


class Surgeon(Doctor):
    def treat(self):
        print(f"Хирург {self.name} проводит операцию.")


class Dentist(Doctor):
    def treat(self):
        print(f"Дантист {self.name} лечит зубы.")


class Therapist(Doctor):
    def treat(self):
        print(f"Терапевт {self.name} "
              f"назначает лекарства и наблюдает за состоянием.")

    def assign_doctor(self, patient):
        if patient.treatment_plan == 1:
            doctor = Surgeon("Иванов")
        elif patient.treatment_plan == 2:
            doctor = Dentist("Петрова")
        else:
            doctor = self
        patient.doctor = doctor
        print(f"Пациенту {patient.name} (план {patient.treatment_plan}) "
              f"назначен врач: {doctor.name}")
        patient.doctor.treat()


class Patient:
    def __init__(self, name, treatment_plan):
        self.name = name
        self.__treatment_plan = treatment_plan
        self.__doctor = None

    @property
    def treatment_plan(self):
        return self.__treatment_plan

    @treatment_plan.setter
    def treatment_plan(self, treatment_plan):
        self.__treatment_plan = treatment_plan

    @property
    def doctor(self):
        return self.__doctor

    @doctor.setter
    def doctor(self, doctor):
        self.__doctor = doctor


if __name__ == "__main__":
    therapist = Therapist("Сидоров")

    patients = [
        Patient("Анна", 1),
        Patient("Борис", 2),
        Patient("Вера", 5),
    ]

    for patient in patients:
        therapist.assign_doctor(patient)
