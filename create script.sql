CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Age INT,
    Gender NVARCHAR(10)
);

CREATE TABLE Visits (
    VisitID INT PRIMARY KEY,
    PatientID INT,
    VisitDate DATETIME,
    Reason NVARCHAR(100)
);

CREATE TABLE Vitals (
    VitalID INT PRIMARY KEY,
    PatientID INT,
    RecordedAt DATETIME,
    HeartRate INT,
    BloodPressure NVARCHAR(10),
    Temperature FLOAT
);