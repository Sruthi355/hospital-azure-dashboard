-- Insert Patients
INSERT INTO Patients VALUES 
(1, 'Alice', 'Smith', 30, 'Female'),
(2, 'Bob', 'Johnson', 42, 'Male'),
(3, 'Carol', 'Davis', 25, 'Female');

-- Insert Visits
INSERT INTO Visits VALUES
(101, 1, GETDATE()-2, 'Checkup'),
(102, 2, GETDATE()-1, 'Fever'),
(103, 3, GETDATE(), 'Cold');

-- Insert Vitals
INSERT INTO Vitals VALUES
(201, 1, GETDATE()-2, 75, '120/80', 36.6),
(202, 2, GETDATE()-1, 90, '130/85', 37.5),
(203, 3, GETDATE(), 88, '125/82', 38.1);