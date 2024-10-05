# VetLog Veritabanı Dokümantasyonu

## Giriş
VetLog uygulaması, hayvanların aşıları, ilaçları ve sağlık geçmişlerini yönetmek için bir SQLite veritabanı kullanmaktadır. Bu veritabanı, hayvanların sağlık durumlarını izlemek, aşı ve ilaç kayıtlarını tutmak için tasarlanmıştır.

## Veritabanı Yapısı
Aşağıda veritabanında bulunan tablolar ve bu tablolara ait özellikler açıklanmıştır.

### 1. Animal Tablosu
Hayvan bilgilerini saklamak için kullanılan tablodur.

| Alan      | Veri Tipi | Açıklama                                    |
|-----------|-----------|---------------------------------------------|
| AnimalID  | INTEGER   | Hayvanın benzersiz kimlik numarası (PK)    |
| Name      | TEXT      | Hayvanın ismi                               |
| Species   | TEXT      | Hayvanın türü                               |
| Breed     | TEXT      | Hayvanın ırkı                               |
| BirthDate | DATE      | Hayvanın doğum tarihi                       |
| Gender    | TEXT      | Hayvanın cinsiyeti                          |
| FarmID    | INTEGER   | Hayvanın bulunduğu çiftlikin kimliği       |

### 2. Vaccine Tablosu
Aşı bilgilerini saklamak için kullanılan tablodur.

| Alan         | Veri Tipi | Açıklama                                      |
|--------------|-----------|-----------------------------------------------|
| VaccineID    | INTEGER   | Aşının benzersiz kimlik numarası (PK)        |
| Name         | TEXT      | Aşının ismi                                   |
| Description  | TEXT      | Aşının açıklaması                             |
| RequiredDose | INTEGER   | Gerekli doz sayısı                            |

### 3. Vaccination Tablosu
Hayvanların aşı kayıtlarını tutmak için kullanılan tablodur.

| Alan             | Veri Tipi | Açıklama                                      |
|------------------|-----------|-----------------------------------------------|
| VaccinationID    | INTEGER   | Aşı kaydının benzersiz kimlik numarası (PK)  |
| AnimalID         | INTEGER   | Aşının uygulandığı hayvanın kimliği (FK)     |
| VaccineID        | INTEGER   | Uygulanan aşının kimliği (FK)                 |
| DoseNumber       | INTEGER   | Uygulanan doz numarası                        |
| VaccinationDate  | DATE      | Aşı uygulama tarihi                           |

### 4. User Tablosu
Kullanıcı bilgilerini saklamak için kullanılan tablodur.

| Alan         | Veri Tipi | Açıklama                                      |
|--------------|-----------|-----------------------------------------------|
| UserID       | INTEGER   | Kullanıcının benzersiz kimlik numarası (PK)  |
| Username      | TEXT      | Kullanıcı adı                                 |
| PasswordHash  | TEXT      | Kullanıcı parolasının hash'i                  |
| Role         | TEXT      | Kullanıcının rolü (örn: admin, kullanıcı)    |
| FullName     | TEXT      | Kullanıcının tam adı                          |
| Email        | TEXT      | Kullanıcının e-posta adresi                   |

### 5. Notification Tablosu
Kullanıcılara ait bildirimleri saklamak için kullanılan tablodur.

| Alan              | Veri Tipi | Açıklama                                      |
|-------------------|-----------|-----------------------------------------------|
| NotificationID    | INTEGER   | Bildirimin benzersiz kimlik numarası (PK)    |
| UserID            | INTEGER   | Bildirimin ait olduğu kullanıcının kimliği (FK) |
| Message           | TEXT      | Bildirim mesajı                              |
| NotificationDate  | DATE      | Bildirimin tarihi                            |
| IsRead            | BOOLEAN   | Bildirimin okunup okunmadığı durumu          |

### 6. Genealogy Tablosu
Hayvanların soyağacını tutmak için kullanılan tablodur.

| Alan          | Veri Tipi | Açıklama                                      |
|---------------|-----------|-----------------------------------------------|
| GenealogyID   | INTEGER   | Soy ağacı kaydının benzersiz kimlik numarası (PK) |
| ParentID      | INTEGER   | Ebeveyn hayvanın kimliği (FK)                |
| OffspringID   | INTEGER   | Yavrunun kimliği (FK)                        |

### 7. DailyReport Tablosu
Hayvanların günlük raporlarını tutmak için kullanılan tablodur.

| Alan          | Veri Tipi | Açıklama                                      |
|---------------|-----------|-----------------------------------------------|
| ReportID      | INTEGER   | Raporun benzersiz kimlik numarası (PK)       |
| AnimalID      | INTEGER   | Raporun ait olduğu hayvanın kimliği (FK)     |
| ReportDate    | DATE      | Rapor tarihi                                  |
| HealthStatus   | TEXT      | Hayvanın sağlık durumu                        |
| Weight        | DECIMAL(5, 2) | Hayvanın ağırlığı                          |
| Notes         | TEXT      | Ek notlar                                    |

### 8. VaccineStatus Tablosu
Aşı uygulama durumunu saklamak için kullanılan tablodur.

| Alan             | Veri Tipi | Açıklama                                      |
|------------------|-----------|-----------------------------------------------|
| VaccineStatusID  | INTEGER   | Aşı durumu kaydının benzersiz kimlik numarası (PK) |
| AnimalID         | INTEGER   | Aşının uygulandığı hayvanın kimliği (FK)     |
| VaccineID        | INTEGER   | Aşının kimliği (FK)                           |
| Status           | TEXT      | Aşının durumu (örn: 'Uygulandı', 'Bekleniyor') |

### 9. Medication Tablosu
Hayvanlara verilen ilaç bilgilerini saklamak için kullanılan tablodur.

| Alan             | Veri Tipi | Açıklama                                      |
|------------------|-----------|-----------------------------------------------|
| MedicationID     | INTEGER   | İlaç kaydının benzersiz kimlik numarası (PK) |
| AnimalID         | INTEGER   | İlacın uygulandığı hayvanın kimliği (FK)     |
| Name             | TEXT      | İlaç ismi                                    |
| Dosage           | TEXT      | Uygulama dozu                                |
| AdministrationDate | DATE    | İlaç uygulama tarihi                         |

### 10. HealthHistory Tablosu
Hayvanların sağlık geçmişini saklamak için kullanılan tablodur.

| Alan              | Veri Tipi | Açıklama                                      |
|-------------------|-----------|-----------------------------------------------|
| HealthHistoryID   | INTEGER   | Sağlık geçmişi kaydının benzersiz kimlik numarası (PK) |
| AnimalID          | INTEGER   | Sağlık kaydının ait olduğu hayvanın kimliği (FK) |
| Date              | DATE      | Sağlık kaydı tarihi                          |
| Description       | TEXT      | Sağlık durumu açıklaması                    |

## Sonuç
Bu dokümantasyon, VetLog veritabanının yapısını ve işlevselliğini açıklamaktadır. Her bir tablo, hayvanların sağlık kayıtlarını ve aşı bilgilerini düzenli bir şekilde tutmak amacıyla tasarlanmıştır.
