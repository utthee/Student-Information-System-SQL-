CREATE TABLE IF NOT EXISTS COLLEGE (
	collegecode VARCHAR(10) PRIMARY KEY NOT NULL,
    collegename VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS PROGRAM (
	programcode VARCHAR(50) PRIMARY KEY NOT NULL,
    programname VARCHAR(255) NOT NULL,
    collegecode VARCHAR(10) NOT NULL,
    
    CONSTRAINT fk_program_college FOREIGN KEY (collegecode) REFERENCES COLLEGE(collegecode)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS STUDENT (
	idnumber VARCHAR(10) PRIMARY KEY NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    yearlevel ENUM('1', '2', '3', '4') NOT NULL,
    gender ENUM('M', 'F') NOT NULL,
    programcode VARCHAR(50),
    
    CONSTRAINT student_ibfk_1 FOREIGN KEY (programcode) REFERENCES PROGRAM(programcode)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);
