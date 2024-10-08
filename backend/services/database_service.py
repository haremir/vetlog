# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:48:52 2024

@author: emirh
"""

import sqlite3

class DatabaseService:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Animal Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Animal (
                AnimalID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Species TEXT NOT NULL,
                Breed TEXT,
                BirthDate DATE,
                Gender TEXT,
                FarmID INTEGER
            );
        ''')

        # Vaccine Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Vaccine (
                VaccineID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Description TEXT,
                RequiredDose INTEGER NOT NULL
            );
        ''')

        # Vaccination Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Vaccination (
                VaccinationID INTEGER PRIMARY KEY AUTOINCREMENT,
                AnimalID INTEGER,
                VaccineID INTEGER,
                DoseNumber INTEGER NOT NULL,
                VaccinationDate DATE NOT NULL,
                FOREIGN KEY (AnimalID) REFERENCES Animal (AnimalID),
                FOREIGN KEY (VaccineID) REFERENCES Vaccine (VaccineID)
            );
        ''')

        # User Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS User (
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                PasswordHash TEXT NOT NULL,
                Role TEXT NOT NULL,
                FullName TEXT NOT NULL,
                Email TEXT NOT NULL
            );
        ''')

        # Notification Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Notification (
                NotificationID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INTEGER,
                Message TEXT NOT NULL,
                NotificationDate DATE NOT NULL,
                IsRead BOOLEAN NOT NULL,
                FOREIGN KEY (UserID) REFERENCES User (UserID)
            );
        ''')

        # Genealogy Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Genealogy (
                GenealogyID INTEGER PRIMARY KEY AUTOINCREMENT,
                ParentID INTEGER,
                OffspringID INTEGER,
                FOREIGN KEY (ParentID) REFERENCES Animal (AnimalID),
                FOREIGN KEY (OffspringID) REFERENCES Animal (AnimalID)
            );
        ''')

        # DailyReport Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS DailyReport (
                ReportID INTEGER PRIMARY KEY AUTOINCREMENT,
                AnimalID INTEGER,
                ReportDate DATE NOT NULL,
                HealthStatus TEXT NOT NULL,
                Weight DECIMAL(5, 2),
                Notes TEXT,
                FOREIGN KEY (AnimalID) REFERENCES Animal (AnimalID)
            );
        ''')

        # VaccineStatus Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS VaccineStatus (
                VaccineStatusID INTEGER PRIMARY KEY AUTOINCREMENT,
                AnimalID INTEGER,
                VaccineID INTEGER,
                Status TEXT NOT NULL, -- Örn: 'Uygulandı', 'Bekleniyor', 'İptal Edildi'
                FOREIGN KEY (AnimalID) REFERENCES Animal (AnimalID),
                FOREIGN KEY (VaccineID) REFERENCES Vaccine (VaccineID)
            );
        ''')

        # Medication Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Medication (
                MedicationID INTEGER PRIMARY KEY AUTOINCREMENT,
                AnimalID INTEGER,
                Name TEXT NOT NULL,
                Dosage TEXT NOT NULL,
                AdministrationDate DATE NOT NULL,
                FOREIGN KEY (AnimalID) REFERENCES Animal (AnimalID)
            );
        ''')

        # HealthHistory Tablosu
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS HealthHistory (
                HealthHistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                AnimalID INTEGER,
                Date DATE NOT NULL,
                Description TEXT,
                FOREIGN KEY (AnimalID) REFERENCES Animal (AnimalID)
            );
        ''')

        # Değişiklikleri kaydet
        self.connection.commit()

    # CRUD İşlemleri: Animal
    def add_animal(self, name, species, breed, birth_date, gender, farm_id):
        self.cursor.execute('''
            INSERT INTO Animal (Name, Species, Breed, BirthDate, Gender, FarmID)
            VALUES (?, ?, ?, ?, ?, ?);
        ''', (name, species, breed, birth_date, gender, farm_id))
        self.connection.commit()

    def get_animals(self):
        self.cursor.execute('SELECT * FROM Animal;')
        return self.cursor.fetchall()

    def update_animal(self, animal_id, name, species, breed, birth_date, gender, farm_id):
        self.cursor.execute('''
            UPDATE Animal
            SET Name = ?, Species = ?, Breed = ?, BirthDate = ?, Gender = ?, FarmID = ?
            WHERE AnimalID = ?;
        ''', (name, species, breed, birth_date, gender, farm_id, animal_id))
        self.connection.commit()

    def delete_animal(self, animal_id):
        self.cursor.execute('DELETE FROM Animal WHERE AnimalID = ?;', (animal_id,))
        self.connection.commit()

    # CRUD İşlemleri: Vaccine
    def add_vaccine(self, name, description, required_dose):
        self.cursor.execute('''
            INSERT INTO Vaccine (Name, Description, RequiredDose)
            VALUES (?, ?, ?);
        ''', (name, description, required_dose))
        self.connection.commit()

    def get_vaccines(self):
        self.cursor.execute('SELECT * FROM Vaccine;')
        return self.cursor.fetchall()

    def update_vaccine(self, vaccine_id, name, description, required_dose):
        self.cursor.execute('''
            UPDATE Vaccine
            SET Name = ?, Description = ?, RequiredDose = ?
            WHERE VaccineID = ?;
        ''', (name, description, required_dose, vaccine_id))
        self.connection.commit()

    def delete_vaccine(self, vaccine_id):
        self.cursor.execute('DELETE FROM Vaccine WHERE VaccineID = ?;', (vaccine_id,))
        self.connection.commit()

    # CRUD İşlemleri: Vaccination
    def add_vaccination(self, animal_id, vaccine_id, dose_number, vaccination_date):
        self.cursor.execute('''
            INSERT INTO Vaccination (AnimalID, VaccineID, DoseNumber, VaccinationDate)
            VALUES (?, ?, ?, ?);
        ''', (animal_id, vaccine_id, dose_number, vaccination_date))
        self.connection.commit()

    def get_vaccinations(self):
        self.cursor.execute('SELECT * FROM Vaccination;')
        return self.cursor.fetchall()

    def update_vaccination(self, vaccination_id, animal_id, vaccine_id, dose_number, vaccination_date):
        self.cursor.execute('''
            UPDATE Vaccination
            SET AnimalID = ?, VaccineID = ?, DoseNumber = ?, VaccinationDate = ?
            WHERE VaccinationID = ?;
        ''', (animal_id, vaccine_id, dose_number, vaccination_date, vaccination_id))
        self.connection.commit()

    def delete_vaccination(self, vaccination_id):
        self.cursor.execute('DELETE FROM Vaccination WHERE VaccinationID = ?;', (vaccination_id,))
        self.connection.commit()

    # CRUD İşlemleri: User
    def add_user(self, username, password_hash, role, full_name, email):
        self.cursor.execute('''
            INSERT INTO User (Username, PasswordHash, Role, FullName, Email)
            VALUES (?, ?, ?, ?, ?);
        ''', (username, password_hash, role, full_name, email))
        self.connection.commit()

    def get_users(self):
        self.cursor.execute('SELECT * FROM User;')
        return self.cursor.fetchall()

    def update_user(self, user_id, username, password_hash, role, full_name, email):
        self.cursor.execute('''
            UPDATE User
            SET Username = ?, PasswordHash = ?, Role = ?, FullName = ?, Email = ?
            WHERE UserID = ?;
        ''', (username, password_hash, role, full_name, email, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM User WHERE UserID = ?;', (user_id,))
        self.connection.commit()

    # CRUD İşlemleri: Notification
    def add_notification(self, user_id, message, notification_date, is_read):
        self.cursor.execute('''
            INSERT INTO Notification (UserID, Message, NotificationDate, IsRead)
            VALUES (?, ?, ?, ?);
        ''', (user_id, message, notification_date, is_read))
        self.connection.commit()

    def get_notifications(self):
        self.cursor.execute('SELECT * FROM Notification;')
        return self.cursor.fetchall()

    def update_notification(self, notification_id, user_id, message, notification_date, is_read):
        self.cursor.execute('''
            UPDATE Notification
            SET UserID = ?, Message = ?, NotificationDate = ?, IsRead = ?
            WHERE NotificationID = ?;
        ''', (user_id, message, notification_date, is_read, notification_id))
        self.connection.commit()

    def delete_notification(self, notification_id):
        self.cursor.execute('DELETE FROM Notification WHERE NotificationID = ?;', (notification_id,))
        self.connection.commit()

    # CRUD İşlemleri: Genealogy
    def add_genealogy(self, parent_id, offspring_id):
        self.cursor.execute('''
            INSERT INTO Genealogy (ParentID, OffspringID)
            VALUES (?, ?);
        ''', (parent_id, offspring_id))
        self.connection.commit()

    def get_genealogy(self):
        self.cursor.execute('SELECT * FROM Genealogy;')
        return self.cursor.fetchall()

    def update_genealogy(self, genealogy_id, parent_id, offspring_id):
        self.cursor.execute('''
            UPDATE Genealogy
            SET ParentID = ?, OffspringID = ?
            WHERE GenealogyID = ?;
        ''', (parent_id, offspring_id, genealogy_id))
        self.connection.commit()

    def delete_genealogy(self, genealogy_id):
        self.cursor.execute('DELETE FROM Genealogy WHERE GenealogyID = ?;', (genealogy_id,))
        self.connection.commit()

    # CRUD İşlemleri: DailyReport
    def add_daily_report(self, animal_id, report_date, health_status, weight, notes):
        self.cursor.execute('''
            INSERT INTO DailyReport (AnimalID, ReportDate, HealthStatus, Weight, Notes)
            VALUES (?, ?, ?, ?, ?);
        ''', (animal_id, report_date, health_status, weight, notes))
        self.connection.commit()

    def get_daily_reports(self):
        self.cursor.execute('SELECT * FROM DailyReport;')
        return self.cursor.fetchall()

    def update_daily_report(self, report_id, animal_id, report_date, health_status, weight, notes):
        self.cursor.execute('''
            UPDATE DailyReport
            SET AnimalID = ?, ReportDate = ?, HealthStatus = ?, Weight = ?, Notes = ?
            WHERE ReportID = ?;
        ''', (animal_id, report_date, health_status, weight, notes, report_id))
        self.connection.commit()

    def delete_daily_report(self, report_id):
        self.cursor.execute('DELETE FROM DailyReport WHERE ReportID = ?;', (report_id,))
        self.connection.commit()

    # CRUD İşlemleri: VaccineStatus
    def add_vaccine_status(self, animal_id, vaccine_id, status):
        self.cursor.execute('''
            INSERT INTO VaccineStatus (AnimalID, VaccineID, Status)
            VALUES (?, ?, ?);
        ''', (animal_id, vaccine_id, status))
        self.connection.commit()

    def get_vaccine_statuses(self):
        self.cursor.execute('SELECT * FROM VaccineStatus;')
        return self.cursor.fetchall()

    def update_vaccine_status(self, vaccine_status_id, animal_id, vaccine_id, status):
        self.cursor.execute('''
            UPDATE VaccineStatus
            SET AnimalID = ?, VaccineID = ?, Status = ?
            WHERE VaccineStatusID = ?;
        ''', (animal_id, vaccine_id, status, vaccine_status_id))
        self.connection.commit()

    def delete_vaccine_status(self, vaccine_status_id):
        self.cursor.execute('DELETE FROM VaccineStatus WHERE VaccineStatusID = ?;', (vaccine_status_id,))
        self.connection.commit()

    # CRUD İşlemleri: Medication
    def add_medication(self, animal_id, name, dosage, administration_date):
        self.cursor.execute('''
            INSERT INTO Medication (AnimalID, Name, Dosage, AdministrationDate)
            VALUES (?, ?, ?, ?);
        ''', (animal_id, name, dosage, administration_date))
        self.connection.commit()

    def get_medications(self):
        self.cursor.execute('SELECT * FROM Medication;')
        return self.cursor.fetchall()

    def update_medication(self, medication_id, animal_id, name, dosage, administration_date):
        self.cursor.execute('''
            UPDATE Medication
            SET AnimalID = ?, Name = ?, Dosage = ?, AdministrationDate = ?
            WHERE MedicationID = ?;
        ''', (animal_id, name, dosage, administration_date, medication_id))
        self.connection.commit()

    def delete_medication(self, medication_id):
        self.cursor.execute('DELETE FROM Medication WHERE MedicationID = ?;', (medication_id,))
        self.connection.commit()

    # CRUD İşlemleri: HealthHistory
    def add_health_history(self, animal_id, date, description):
        self.cursor.execute('''
            INSERT INTO HealthHistory (AnimalID, Date, Description)
            VALUES (?, ?, ?);
        ''', (animal_id, date, description))
        self.connection.commit()

    def get_health_history(self):
        self.cursor.execute('SELECT * FROM HealthHistory;')
        return self.cursor.fetchall()

    def update_health_history(self, health_history_id, animal_id, date, description):
        self.cursor.execute('''
            UPDATE HealthHistory
            SET AnimalID = ?, Date = ?, Description = ?
            WHERE HealthHistoryID = ?;
        ''', (animal_id, date, description, health_history_id))
        self.connection.commit()

    def delete_health_history(self, health_history_id):
        self.cursor.execute('DELETE FROM HealthHistory WHERE HealthHistoryID = ?;', (health_history_id,))
        self.connection.commit()
        
    def close(self):
        self.connection.close()

if __name__ == "__main__":
    db_service = DatabaseService(r'C:/Users/emirh/Desktop/vetlog/database/vetlog.db')
    db_service.create_tables()
    
    db_service.close()  # Bağlantıyı kapatma