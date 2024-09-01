USE Aaksshay;

CREATE TABLE Study_management (
    study_id INT AUTO_INCREMENT PRIMARY KEY,
    study_name VARCHAR(50),
    study_phase VARCHAR(50),
    sponsor_name VARCHAR(50),
    study_description VARCHAR(50)
);



INSERT INTO Study_management (study_name, study_phase, sponsor_name, study_description)
VALUES 
('AI in Healthcare', 'Phase 1', 'TechMed Inc.', 'Study on AI in diagnosis'),
('Blockchain for Finance', 'Phase 2', 'Fintech Solutions', 'Blockchain in financial systems'),
('Renewable Energy Projects', 'Phase 3', 'GreenWorld Corp.', 'Feasibility of renewable energy'),
('Smart Cities Development', 'Phase 1', 'UrbanFuture Ltd.', 'Smart city infrastructure');
 Select * From Study_management
 
 
 