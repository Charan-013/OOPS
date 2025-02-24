class Patient:
    def __init__(self,patientID,name,age):
        self.patientID = patientID
        self.name = name
        self.age = age

    def getPatientInfo(self):
        return f"{self.patientID} {self.name} {self.age}"

class Appointment:
    def __init__(self,appointmentID,patientID,doctorName,appointmentTime):
        self.appointmentID = appointmentID
        self.patientID = patientID
        self.doctorName = doctorName
        self.appointmentTime = appointmentTime

    def getAppointmentDetails(self):
        return f"{self.appointmentID} {self.patientID} {self.doctorName} {self.appointmentTime}"

class PatientManager:
    def __init__(self,patients,appointments):
        self.patients = patients
        self.appointments = appointments
    
    def scheduleAppointment(self,appointment):
        self.appointments.append(appointment)

    def cancelAppointment(self,appointmentID):
        for ele in self.appointments:
            if ele.appointmentID == appointmentID:
                self.appointments.remove(ele)                
                return True
        return False

    def listAppointmentsForPatient(self,patientID):
        new = []
        for ele in self.appointments:
            if ele.patientID == patientID:
                new.append(ele)
        return new



def main():
    # Create a patient and two appointments
    patient = Patient(1, "Emma", 30)
    app1 = Appointment(101, patient.patientID, "Dr. Brown", "2:00 PM")
    app2 = Appointment(102, patient.patientID, "Dr. White", "3:00 PM")
    pm = PatientManager([], [])
    pm.patients.append(patient)
    pm.appointments.extend([app1, app2])
    # List appointments for patient
    print("Appointments for Emma:")
    for app in pm.listAppointmentsForPatient(1):
        print(app.getAppointmentDetails())
    # Cancel an appointment and check again
    cancelled = pm.cancelAppointment(101)
    print("Appointment 101 cancelled:", cancelled)
    print("Remaining appointments for Emma:")
    for app in pm.listAppointmentsForPatient(1):
        print(app.getAppointmentDetails())
if __name__ == '__main__':
    main()