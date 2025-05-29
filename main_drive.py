import sys
import re
import mysql.connector

from mainUI import Ui_MainWindow
from updateStudent import Ui_UpdateStudentDialog
from updateProgram import Ui_UpdateProgramDialog
from updateCollege  import Ui_UpdateCollegeDialog

from addStudent import Ui_AddStudentDialog
from addProgram import Ui_AddProgramDialog
from addCollege import Ui_AddCollegeDialog

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

class MainClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons to their respective functions
        self.deleteButton.clicked.connect(self.deleteEntry)
        self.editButton.clicked.connect(self.updateEntry)
        self.addButton.clicked.connect(self.addEntry)
        self.refreshButton.clicked.connect(self.loadDatabase)
        self.searchButton.clicked.connect(self.searchEntry)
        
        self.sortComboBox.currentIndexChanged.connect(self.sortLayout)
        self.displayComboBox.currentIndexChanged.connect(self.loadDatabase)

        self.displayTable = None
        self.loadDatabase()

#------------------------------------------------------------------------------      MAJOR FUNCTIONS     ------------------------------------------------------------------------------------

#------------------------------------------------------------------------------      MAJOR FUNCTIONS     ------------------------------------------------------------------------------------
    
    # Creates connection to the local host database
    def connectToDatabase(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            database = "ssis"
        )

    # Loads and displays the database
    def loadDatabase(self):
        self.displayTable = self.displayComboBox.currentText()
        self.clearHeaderBox()

        connection = self.connectToDatabase()
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.displayTable}"
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(columns))

        if self.displayTable == "STUDENT":
            self.tableWidget.setHorizontalHeaderLabels(['ID NUMBER', 'FIRST NAME', 'LAST NAME', 'YEAR LEVEL', 'GENDER', 'PROGRAM CODE'])
        elif self.displayTable == "PROGRAM":
            self.tableWidget.setHorizontalHeaderLabels(['PROGRAM CODE', 'PROGRAM NAME', 'COLLEGE CODE'])
        elif self.displayTable == "COLLEGE":
            self.tableWidget.setHorizontalHeaderLabels(['COLLEGE CODE', 'COLLEGE NAME'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row_idx, row_data in enumerate(rows):
            for col_idx, cell_data in enumerate(row_data):
                if self.displayTable == "STUDENT" and col_idx == 5 and cell_data is None:
                    displayValue = "UNENROLLED"
                else:
                    displayValue = str(cell_data)
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(displayValue))

        cursor.close()
        connection.close()
        
    # Delete and update buttons are unclickable whenever there is no selection
    def updateButtonState(self):
        has_selection = self.tableWidget.currentRow() >= 0
        self.deleteButton.setEnabled(has_selection)
        self.editButton.setEnabled(has_selection)

    def updateSearchButtonState(self):
        selected_index = self.searchComboBox.currentIndex()
        search_text = self.searchBox.text().strip()
        # Enable only if an actual filter is selected (e.g., index > 0)
        self.searchButton.setEnabled(selected_index >= 0 and bool(search_text))

    # Resets header items whenever a different table is shown
    def clearHeaderBox(self):
        self.comboBoxItems()
        self.tableWidget.clearSelection()
        self.tableWidget.setCurrentItem(None)

        # Resets hidden rows
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(row, False)

        # Resets button states
        self.deleteButton.setEnabled(False)
        self.deleteButton.setDown(False)
        self.deleteButton.clearFocus()
        self.editButton.setEnabled(False)
        self.editButton.setDown(False)
        self.editButton.clearFocus()
        self.tableWidget.itemSelectionChanged.connect(self.updateButtonState)

        self.searchButton.setEnabled(False)
        self.searchComboBox.currentIndexChanged.connect(self.updateSearchButtonState)
        self.searchBox.textChanged.connect(self.updateSearchButtonState)

    # Adds selections in sort and search combo boxes
    def comboBoxItems(self):
        self.sortComboBox.clear()
        self.searchBox.clear()
        self.searchComboBox.clear()

        if self.displayTable == "STUDENT":
            self.sortComboBox.addItems(['ID NUMBER', 'FIRST NAME', 'LAST NAME', 'YEAR LEVEL', 'GENDER', 'PROGRAM CODE'])
            self.searchComboBox.addItems(['ID NUMBER', 'FIRST NAME', 'LAST NAME', 'YEAR LEVEL', 'GENDER', 'PROGRAM CODE'])

        elif self.displayTable == "PROGRAM":
            self.sortComboBox.addItems(['PROGRAM CODE', 'PROGRAM NAME', 'COLLEGE CODE'])
            self.searchComboBox.addItems(['PROGRAM CODE', 'PROGRAM NAME', 'COLLEGE CODE'])

        elif self.displayTable == "COLLEGE":
            self.sortComboBox.addItems(['COLLEGE CODE', 'COLLEGE NAME'])
            self.searchComboBox.addItems(['COLLEGE CODE', 'COLLEGE NAME'])
        
        self.sortComboBox.setCurrentIndex(-1)
        self.searchComboBox.setCurrentIndex(-1)
    
    def searchEntry(self):
        searchedItem = self.searchBox.text().lower()
        searchFilter = self.searchComboBox.currentIndex()

        # Tracks matched entries
        matchCounter = 0

        # Iterate through table rows and hide/show based on search match
        for row in range(self.tableWidget.rowCount()):
            cell_item = self.tableWidget.item(row, searchFilter)
            cell_text = cell_item.text().lower() if cell_item else ""
            
            match = searchedItem in cell_text
            self.tableWidget.setRowHidden(row, not match)

            if match:
                matchCounter += 1

        # If no matched entries, display error message
        if matchCounter == 0:
            self.loadDatabase()
            self.searchError()
            return
        
    def deleteEntry(self):
        if self.displayComboBox.currentIndex() == 0:
            self.deleteStudentConfirmation()
            return
        
        elif self.displayComboBox.currentIndex() == 1:
            self.deleteProgramConfirmation()
            return
        
        elif self.displayComboBox.currentIndex() == 2:
            self.deleteCollegeConfirmation()
            return
        
    def updateEntry(self):
        if self.displayComboBox.currentIndex() == 0:
            self.updateStudentEntry()
            return
        elif self.displayComboBox.currentIndex() == 1:
            self.updateProgramEntry()
            return
        elif self.displayComboBox.currentIndex() == 2:
            self.updateCollegeEntry()
            return
        
    def addEntry(self):
        if self.displayComboBox.currentIndex() == 0:
            self.addStudentEntry()
            return
        elif self.displayComboBox.currentIndex() == 1:
            self.addProgramEntry()
            return
        elif self.displayComboBox.currentIndex() == 2:
            self.addCollegeEntry()
            return

    def sortLayout(self):
        self.tableWidget.clearSelection()
        col_idx = self.sortComboBox.currentIndex()
        if col_idx >= 0:
            self.tableWidget.sortItems(col_idx)
#------------------------------------------------------------------- POP UP MESSAGES -------------------------------------------------------------------------------

#------------------------------------------------------------------- POP UP MESSAGES ------------------------------------------------------------------------------

    def searchError(self):
        searchErrorMsg = QtWidgets.QMessageBox(self)
        searchErrorMsg.setWindowTitle("No Results")
        searchErrorMsg.setText("The item you are trying to search does not exist.")
        searchErrorMsg.setIcon(QtWidgets.QMessageBox.Warning)
        searchErrorMsg.exec_()

    def deleteStudentConfirmation(self):
        deleteStudentMsg = QtWidgets.QMessageBox(self)
        deleteStudentMsg.setWindowTitle("Delete Confirmation")
        deleteStudentMsg.setText("Are you sure you want to delete this student entry?")
        deleteStudentMsg.setIcon(QtWidgets.QMessageBox.Warning)
        deleteStudentMsg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        deleteStudentMsg.setDefaultButton(QMessageBox.Cancel)
        
        confirm = deleteStudentMsg.exec_()

        if confirm == QMessageBox.Yes:
            self.deleteStudentEntry()

    def deleteStudentSuccess(self):
        deleteStudentSuccessMsg = QtWidgets.QMessageBox(self)
        deleteStudentSuccessMsg.setWindowTitle("Delete Success")
        deleteStudentSuccessMsg.setText("The student entry has been successfully deleted.")
        deleteStudentSuccessMsg.setIcon(QtWidgets.QMessageBox.Information)
        deleteStudentSuccessMsg.exec_()

    def deleteProgramConfirmation(self):
        deleteProgramMsg = QtWidgets.QMessageBox(self)
        deleteProgramMsg.setWindowTitle("Delete Confirmation")
        deleteProgramMsg.setText("Are you sure you want to delete this program entry? Students enrolled in this program will be affected.")
        deleteProgramMsg.setIcon(QtWidgets.QMessageBox.Warning)
        deleteProgramMsg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        deleteProgramMsg.setDefaultButton(QMessageBox.Cancel)
        
        confirm = deleteProgramMsg.exec_()

        if confirm == QMessageBox.Yes:
            self.deleteProgramEntry()

    def deleteProgramSuccess(self):
        deleteProgramSuccessMsg = QtWidgets.QMessageBox(self)
        deleteProgramSuccessMsg.setWindowTitle("Delete Success")
        deleteProgramSuccessMsg.setText(f"The program has been successfully deleted. {self.studentCount} student(s) were affected.")
        deleteProgramSuccessMsg.setIcon(QtWidgets.QMessageBox.Information)
        deleteProgramSuccessMsg.exec_()

    def deleteCollegeConfirmation(self):
        deleteCollegeMsg = QtWidgets.QMessageBox(self)
        deleteCollegeMsg.setWindowTitle("Delete Confirmation")
        deleteCollegeMsg.setText("Are you sure you want to delete this college entry? All programs under this college will also be deleted.")
        deleteCollegeMsg.setIcon(QtWidgets.QMessageBox.Warning)
        deleteCollegeMsg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
        deleteCollegeMsg.setDefaultButton(QMessageBox.Cancel)

        confirm = deleteCollegeMsg.exec_()

        if confirm == QMessageBox.Yes:
            self.deleteCollegeEntry()

    def deleteCollegeSuccess(self):
        deleteCollegeSuccessMsg = QtWidgets.QMessageBox(self)
        deleteCollegeSuccessMsg.setWindowTitle("Delete Success")
        deleteCollegeSuccessMsg.setText(f"The college has been successfully deleted. {self.programCount} program(s) were affected. {self.studentCount} student(s) were affected.")
        deleteCollegeSuccessMsg.setIcon(QtWidgets.QMessageBox.Information)
        deleteCollegeSuccessMsg.exec_()

    def addStudentSuccess(self):
        addStudentMsg = QtWidgets.QMessageBox(self)
        addStudentMsg.setWindowTitle("Input Added")
        addStudentMsg.setText("Student entry has been successfully added")
        addStudentMsg.setIcon(QtWidgets.QMessageBox.Information)
        addStudentMsg.exec_()

    def addProgramSuccess(self):
        addProgramMsg = QtWidgets.QMessageBox(self)
        addProgramMsg.setWindowTitle("Input Added")
        addProgramMsg.setText("Program entry has been successfully added")
        addProgramMsg.setIcon(QtWidgets.QMessageBox.Information)
        addProgramMsg.exec_()

    def addCollegeSuccess(self):
        addCollegeMsg = QtWidgets.QMessageBox(self)
        addCollegeMsg.setWindowTitle("Input Added")
        addCollegeMsg.setText("College entry has been successfully added")
        addCollegeMsg.setIcon(QtWidgets.QMessageBox.Information)
        addCollegeMsg.exec_()

    def updateStudentSuccess(self):
        updateStudentMsg = QtWidgets.QMessageBox(self)
        updateStudentMsg.setWindowTitle("Input Updated")
        updateStudentMsg.setText("Student entry has been successfully updated")
        updateStudentMsg.setIcon(QtWidgets.QMessageBox.Information)
        updateStudentMsg.exec_()

    def updateProgramSuccess(self):
        updateProgramMsg = QtWidgets.QMessageBox(self)
        updateProgramMsg.setWindowTitle("Input Updated")
        updateProgramMsg.setText(f"Program entry has been successfully updated. {self.studentCount} student(s) were also affected.")
        updateProgramMsg.setIcon(QtWidgets.QMessageBox.Information)
        updateProgramMsg.exec_()

    def updateCollegeSuccess(self):
        updateCollegeMsg = QtWidgets.QMessageBox(self)
        updateCollegeMsg.setWindowTitle("Input Updated")
        updateCollegeMsg.setText(f"College entry has been successfully updated. {self.programCount} program(s) were also affected.")
        updateCollegeMsg.setIcon(QtWidgets.QMessageBox.Information)
        updateCollegeMsg.exec_()

#--------------------------------------------------------------------------------     STUDENT     ----------------------------------------------------------------------

#--------------------------------------------------------------------------------     STUDENT     ----------------------------------------------------------------------
    def addStudentEntry(self):
        studentAdder = AddStudentDialog(self)
        if studentAdder.exec_():
            self.loadDatabase()
            self.addStudentSuccess()
    
    def updateStudentEntry(self):
        selectedRow = self.tableWidget.currentRow()

        origIDNumber = self.tableWidget.item(selectedRow, 0).text()
        origFirstName = self.tableWidget.item(selectedRow, 1).text()
        origLastName = self.tableWidget.item(selectedRow, 2).text()
        origYearLevel = self.tableWidget.item(selectedRow, 3).text()
        origGender = self.tableWidget.item(selectedRow, 4).text()
        origProgramCode = self.tableWidget.item(selectedRow, 5).text()

        studentEditor = UpdateStudentDialog(origIDNumber, origFirstName, origLastName, origYearLevel, origGender, origProgramCode, self)
        if studentEditor.exec_():
            updatedStudentValues = studentEditor.updatedStudentData()

            if not updatedStudentValues:
                return
            
            newIDNumber, newFirstName, newLastName, newYearLevel, newGender, newProgramCode = updatedStudentValues

            connection = self.connectToDatabase()
            cursor = connection.cursor()

            # Update STUDENT TABLE
            updateStudentQuery = """
                UPDATE STUDENT
                SET firstname = %s, lastname = %s, yearlevel = %s, gender = %s, programcode = %s
                WHERE idnumber = %s
            """
            cursor.execute(updateStudentQuery, (newFirstName, newLastName, newYearLevel, newGender, newProgramCode, origIDNumber))
            connection.commit()

            cursor.close()
            connection.close()

            self.loadDatabase()
            if newYearLevel != origYearLevel or newProgramCode != origProgramCode: 
                self.updateStudentSuccess()

    def deleteStudentEntry(self):
        selectedRow = self.tableWidget.currentRow()
        
        idNumber = self.tableWidget.item(selectedRow, 0).text()
        connection = self.connectToDatabase()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM STUDENT WHERE idnumber = %s", (idNumber,))
        connection.commit()

        cursor.close()
        connection.close()

        self.loadDatabase()
        self.deleteStudentSuccess()

    
#--------------------------------------------------------------------------------     PROGRAM     ----------------------------------------------------------------------

#--------------------------------------------------------------------------------     PROGRAM     ----------------------------------------------------------------------

    def addProgramEntry(self):
        programAdder = AddProgramDialog(self)
        if programAdder.exec_():
            self.loadDatabase()
            self.addProgramSuccess()
    
    def updateProgramEntry(self):
        selectedRow = self.tableWidget.currentRow()

        origProgramCode = self.tableWidget.item(selectedRow, 0).text()
        origProgramName = self.tableWidget.item(selectedRow, 1).text()
        origCollegeCode = self.tableWidget.item(selectedRow, 2).text()

        programEditor = UpdateProgramDialog(origProgramCode, origProgramName, origCollegeCode, self)
        if programEditor.exec_():
            updatedProgramValues = programEditor.updatedProgramData()

            if not updatedProgramValues:
                return
            
            newProgramCode, newProgramName, newCollegeCode = updatedProgramValues

            connection = self.connectToDatabase()
            cursor = connection.cursor()

            self.studentCount = 0

            # Count how many students are affected
            cursor.execute("SELECT COUNT(*) FROM STUDENT WHERE programcode = %s", (origProgramCode,))
            self.studentCount = cursor.fetchone()[0]

            # Update PROGRAM table
            updateProgramQuery = """
                UPDATE PROGRAM
                SET programcode = %s, programname = %s, collegecode = %s
                WHERE programcode = %s
            """
            cursor.execute(updateProgramQuery, (newProgramCode, newProgramName, newCollegeCode, origProgramCode))
            connection.commit()

            cursor.close()
            connection.close()

            self.loadDatabase()
            if newProgramCode != origProgramCode or newProgramName != origProgramName or newCollegeCode != origCollegeCode:
                self.updateProgramSuccess()

    def deleteProgramEntry(self):
        selectedRow = self.tableWidget.currentRow()
        
        programCode = self.tableWidget.item(selectedRow, 0).text()
        connection = self.connectToDatabase()
        cursor = connection.cursor()

        self.studentCount = 0

        # Count how many students are affected
        cursor.execute("SELECT COUNT(*) FROM STUDENT WHERE programcode = %s", (programCode,))
        self.studentCount = cursor.fetchone()[0]

        cursor.execute("DELETE FROM PROGRAM WHERE programcode = %s", (programCode,))
        connection.commit()

        cursor.close()
        connection.close()

        self.loadDatabase()
        self.deleteProgramSuccess()

#--------------------------------------------------------------------------------     COLLEGE     ----------------------------------------------------------------------

#--------------------------------------------------------------------------------     COLLEGE     ----------------------------------------------------------------------

    def addCollegeEntry(self):
        collegeAdder = AddCollegeDialog(self) 
        if collegeAdder.exec_():
            self.loadDatabase()
            self.addCollegeSuccess()
    
    def updateCollegeEntry(self):
        selectedRow = self.tableWidget.currentRow()

        origCollegeCode = self.tableWidget.item(selectedRow, 0).text()
        origCollegeName = self.tableWidget.item(selectedRow, 1).text()

        collegeEditor = UpdateCollegeDialog(origCollegeCode, origCollegeName, self)
        if collegeEditor.exec_():
            updatedCollegeValues = collegeEditor.updatedCollegeData()

            if not updatedCollegeValues:
                return

            newCollegeCode, newCollegeName = updatedCollegeValues

            connection = self.connectToDatabase()
            cursor = connection.cursor()

            self.programCount = 0

            # Count how many programs are affected            
            cursor.execute("SELECT COUNT(*) FROM PROGRAM WHERE collegecode = %s", (origCollegeCode,))
            self.programCount = cursor.fetchone()[0]

            # Update COLLEGE table
            updateCollegeQuery = """
                UPDATE COLLEGE
                SET collegecode = %s, collegename = %s
                WHERE collegecode = %s
            """
            cursor.execute(updateCollegeQuery, (newCollegeCode, newCollegeName, origCollegeCode))
            connection.commit()

            cursor.close()
            connection.close()

            self.loadDatabase()
            if newCollegeCode != origCollegeCode or newCollegeName != origCollegeName:    
                self.updateCollegeSuccess()

    def deleteCollegeEntry(self):
        selectedRow = self.tableWidget.currentRow()
        
        collegeCode = self.tableWidget.item(selectedRow, 0).text()
        connection = self.connectToDatabase()
        cursor = connection.cursor()

        self.programCount = 0
        self.studentCount = 0

        # Count affected programs
        cursor.execute("SELECT COUNT(*) FROM PROGRAM WHERE collegecode = %s", (collegeCode,))
        self.programCount = cursor.fetchone()[0]

        # Count affected students
        cursor.execute("""
            SELECT COUNT(*) FROM STUDENT 
            WHERE programcode IN (SELECT programcode FROM PROGRAM WHERE collegecode = %s)
        """, (collegeCode,))
        self.studentCount = cursor.fetchone()[0]
        
        cursor.execute("DELETE FROM COLLEGE WHERE collegecode = %s", (collegeCode,))
        connection.commit()

        cursor.close()
        connection.close()

        self.loadDatabase()
        self.deleteCollegeSuccess()

#----------------------------------------------------------------------- EDIT & ADD STUDENT ------------------------------------------------------------------

#----------------------------------------------------------------------- EDIT & ADD STUDENT ------------------------------------------------------------------

class UpdateStudentDialog(QDialog, Ui_UpdateStudentDialog):

    def __init__(self, idNumber, firstName, lastName, yearLevel, gender, programCode, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.programChoices()

        self.idNumberEdit.setText(idNumber)
        self.firstNameEdit.setText(firstName)
        self.lastNameEdit.setText(lastName)
        self.yearLevelBox.setCurrentText(yearLevel)
        self.genderBox.setCurrentText(gender)
        
        # If student is unenrolled, program code box shows nothing
        if programCode == "None" or programCode == "UNENROLLED":
            self.programCodeBox.setCurrentIndex(-1)
        else:
            self.programCodeBox.setCurrentText(programCode)
        
        self.pushButton.clicked.connect(self.validateStudentData)

    def programChoices(self):
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        cursor.execute("SELECT DISTINCT programcode FROM PROGRAM")
        programChoices = [choice[0] for choice in cursor.fetchall()]
        self.programCodeBox.clear()
        self.programCodeBox.addItems(programChoices)

        connection.close()
        cursor.close()

    def updatedStudentData(self):
        newFirstName =  self.firstNameEdit.text()
        newLastName = self.lastNameEdit.text()
        newYearLevel = self.yearLevelBox.currentText()
        newGender = self.genderBox.currentText()
        newProgramCode = self.programCodeBox.currentText()

        if not ( newFirstName and newLastName and newYearLevel and newGender and newProgramCode):
            QMessageBox.warning(self, "Input Error", "All required fields must be filled up.")
            return
        
        if not all(char.isalpha() or char.isspace() for char in newFirstName and newLastName):
            QMessageBox.warning(self, "Input Error", "Input a valid name.")
            return
        
        if len(newFirstName) > 255 or len(newLastName) > 255:
            QMessageBox.warning(self, "Input Error", "Please input no more than 255 characters.")
            return
        
        return [
            self.idNumberEdit.text(),
            newFirstName,
            newLastName,
            newYearLevel,
            newGender,
            newProgramCode,
        ]
    
    # Ensures that the dialog does not exit if an error has occurred
    def validateStudentData(self):
        updatedStudentData = self.updatedStudentData()
        if updatedStudentData:
            self.accept()

class AddStudentDialog(QDialog, Ui_AddStudentDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        regex = QRegExp(r"^\d{4}-\d{4}$")
        validator = QRegExpValidator(regex)
        self.idNumberEdit.setValidator(validator)

        self.programChoices()
        self.programCodeBox.setCurrentIndex(-1)

        self.pushButton.clicked.connect(self.validateStudentData)
    
    def programChoices(self):
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        cursor.execute("SELECT DISTINCT programcode FROM PROGRAM")
        programChoices = [choice[0] for choice in cursor.fetchall()]
        self.programCodeBox.clear()
        self.programCodeBox.addItems(programChoices)

        connection.close()
        cursor.close()

    def addStudentData(self):
        idNumber = self.idNumberEdit.text()
        firstName = self.firstNameEdit.text().strip().title()
        lastName = self.lastNameEdit.text().strip().title()
        yearLevel = self.yearLevelBox.currentText()
        gender = self.genderBox.currentText()
        programCode = self.programCodeBox.currentText()
        
        if not (idNumber and firstName and lastName and yearLevel and gender and programCode):
            QMessageBox.warning(self, "Input Error", "All required fields must be filled up.")
            return

        if not re.fullmatch(r'20\d{2}-\d{4}', idNumber):
            QMessageBox.warning(self, "Input Error", "Input a valid ID Number.")
            return
        
        # Validates first name and last name, should not contain any numbers
        if not all(char.isalpha() or char.isspace() for char in firstName and lastName):
            QMessageBox.warning(self, "Input Error", "Input a valid name.")
            return
        
        if len(firstName) > 255 or len(lastName) > 255:
            QMessageBox.warning(self, "Input Error", "Please input no more than 255 characters.")
            return
        
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        # Check if ID Number already exists
        cursor.execute("SELECT idnumber FROM STUDENT WHERE idnumber = %s", (idNumber,))
        resultIdNumber = cursor.fetchone()

        if resultIdNumber:
            QMessageBox.warning(self, "Input Error", "The ID Number you're trying to enter already exists.")
            connection.close()
            cursor.close()
            return
        
        # Insert the new student data to the database
        insertStudentQuery = """INSERT INTO STUDENT (idnumber, firstname, lastname, yearlevel, gender, programcode)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertStudentQuery, (idNumber, firstName, lastName, yearLevel, gender, programCode))
        connection.commit()

        cursor.close()
        connection.close()

        return True
    
    def validateStudentData(self):
        newStudentData = self.addStudentData()
        if newStudentData:
            self.accept()

#----------------------------------------------------------------------- EDIT & ADD PROGRAM ------------------------------------------------------------------

#----------------------------------------------------------------------- EDIT & ADD PROGRAM ------------------------------------------------------------------
             
class UpdateProgramDialog(QDialog, Ui_UpdateProgramDialog):
    def __init__(self, programCode, programName, collegeCode, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.collegeChoices()

        # Store the original values for comparison
        self.originalProgramCode = programCode
        self.originalProgramName = programName
        self.originalCollegeCode = collegeCode

        # Input current data on to the line edits.
        self.programCodeEdit.setText(programCode)
        self.programNameEdit.setText(programName)
        self.collegeCodeBox.setCurrentText(collegeCode)

        # Validates if input is not empty
        self.confirmButton.clicked.connect(self.validateProgramData) 

    def collegeChoices(self):
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        cursor.execute("SELECT DISTINCT collegecode FROM COLLEGE")
        collegeChoices = [choice[0] for choice in cursor.fetchall()]
        self.collegeCodeBox.clear()
        self.collegeCodeBox.addItems(collegeChoices)

        connection.close()
        cursor.close()

    def updatedProgramData(self):
        newProgramCode = self.programCodeEdit.text().strip().replace(" ", "").upper()
        newProgramName = self.programNameEdit.text().strip().title()
        newCollegeCode = self.collegeCodeBox.currentText()

        # If no changes are made, return the original values
        if (newProgramCode == self.originalProgramCode and
            newProgramName == self.originalProgramName and
            newCollegeCode == self.originalCollegeCode):
            return [self.originalProgramCode, self.originalProgramName, self.originalCollegeCode]

        if not (newProgramCode and newProgramName and newCollegeCode):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return

        if not newProgramCode.isalnum() or not all(char.isalpha() or char.isspace() for char in newProgramName):
            QMessageBox.warning(self, "Input Error", "Please input a valid program name.")
            return
        
        if len(newProgramCode) > 50:
            QMessageBox.warning(self, "Input Error", "Please input no more than 10 characters for program code.")
            return
        
        if len(newProgramName) > 255:
            QMessageBox.warning(self, "Input Error", "Please input no more than 255 characters for program name.")
            return

        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        # Check if the program code exists in another record
        queryCode = """
            SELECT programcode FROM PROGRAM
            WHERE programcode = %s AND programcode <> %s
        """
        cursor.execute(queryCode, (newProgramCode, self.originalProgramCode))
        resultCode = cursor.fetchone()

        if resultCode:
            QMessageBox.warning(self, "Input Error", "The program code you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return

        # Check if the program name exists in another record
        queryName = """
            SELECT programname FROM PROGRAM
            WHERE UPPER(REPLACE(programname, ' ', '')) = %s AND programcode <> %s
        """
        cleanNewName = newProgramName.replace(" ", "").upper()
        cursor.execute(queryName, (cleanNewName, self.originalProgramCode))
        resultName = cursor.fetchone()

        if resultName:
            QMessageBox.warning(self, "Input Error", "The program name you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return

        cursor.close()
        connection.close()

        return [newProgramCode, newProgramName, newCollegeCode]

    
    def validateProgramData(self):
        updatedProgramData = self.updatedProgramData()
        if updatedProgramData:
            self.accept()

class AddProgramDialog(QDialog, Ui_AddProgramDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.collegeChoices()

        # Resets college combo box default text to empty
        self.collegeCodeBox.setCurrentIndex(-1)

        self.pushButton.clicked.connect(self.validateProgramData)
    
    def collegeChoices(self):
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        cursor.execute("SELECT DISTINCT collegecode FROM COLLEGE")
        collegeChoices = [choice[0] for choice in cursor.fetchall()]
        self.collegeCodeBox.clear()
        self.collegeCodeBox.addItems(sorted(collegeChoices))

        connection.close()
        cursor.close()

    def addProgramData(self):
        programCode = self.programCodeEdit.text().strip().replace(" ","").upper()
        programName = self.programNameEdit.text().strip().title()
        collegeCode = self.collegeCodeBox.currentText()

        if not (programCode and programName and collegeCode):
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return
        
        if not programCode.isalnum() or not all(char.isalpha() or char.isspace() for char in programName):
            QMessageBox.warning(self, "Input Error", "Please input a valid program name.")
            return
        
        if len(programCode) > 50:
            QMessageBox.warning(self, "Input Error", "Please input no more than 10 characters for program code.")
            return
        
        if len(programName) > 255:
            QMessageBox.warning(self, "Input Error", "Please input no more than 255 characters for program name.")
            return
        
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()
        
        # Check if program code already exists
        cursor.execute("SELECT programcode FROM PROGRAM WHERE programcode = %s", (programCode,))
        resultCode = cursor.fetchone()

        if resultCode:
            QMessageBox.warning(self, "Input Error", "The program code you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return
        
        # Check if program name already exists (ignoring spaces and case)
        queryName = "SELECT programname FROM PROGRAM WHERE UPPER(REPLACE(programname, ' ', '')) = %s"
        cleanProgramName = programName.replace(" ","").upper()
        cursor.execute(queryName, (cleanProgramName,))
        resultName = cursor.fetchone()

        if resultName:
            QMessageBox.warning(self, "Input Error", "The program name you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return
        
        # Insert the new program if no conflicts
        insertProgramQuery = "INSERT INTO PROGRAM (programcode, programname, collegecode) VALUES (%s, %s, %s)"
        cursor.execute(insertProgramQuery, (programCode, programName, collegeCode))
        connection.commit()

        cursor.close()
        connection.close()
            
        return True

    def validateProgramData(self):
        newProgramData = self.addProgramData()
        if newProgramData:
            self.accept()
#----------------------------------------------------------------------- EDIT & ADD COLLEGE ------------------------------------------------------------------

#----------------------------------------------------------------------- EDIT & ADD COLLEGE ------------------------------------------------------------------

class UpdateCollegeDialog(QDialog, Ui_UpdateCollegeDialog):
    def __init__(self, collegeCode, collegeName, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.originalCollegeCode = collegeCode
        self.originalCollegeName = collegeName
        
        # Input current data on to the line edits.
        self.collegeCodeEdit.setText(collegeCode)
        self.collegeNameEdit.setText(collegeName)

        self.pushButton.clicked.connect(self.validateCollegeData)

    def updatedCollegeData(self):
        newCollegeCode = self.collegeCodeEdit.text().strip().replace(" ", "").upper()
        newCollegeName = self.collegeNameEdit.text().strip().title()

        # If no changes were made, return the original values
        if (newCollegeCode == self.originalCollegeCode and newCollegeName == self.originalCollegeName):
            return [self.originalCollegeCode, self.originalCollegeName]

        if not newCollegeCode or not newCollegeName:
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return

        # Validates if the code is alphanumeric and name is alphabetic with spaces
        if not newCollegeCode.isalnum() or not all(char.isalpha() or char.isspace() for char in newCollegeName):
            QMessageBox.warning(self, "Input Error", "Please input a valid college code and name.")
            return
        
        if len(newCollegeCode) > 10:
            QMessageBox.warning(self, "Input Error", "Please input no more than 10 characters for college code.")
            return
        
        if len(newCollegeName) > 255:
            QMessageBox.warning(self, "Input Error", "Please input no more than 255 characters for college name.")
            return

        # Database validation
        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        # Check if the college code exists in another record
        queryCode = """
            SELECT collegecode FROM COLLEGE 
            WHERE collegecode = %s AND collegecode <> %s
        """
        cursor.execute(queryCode, (newCollegeCode, self.originalCollegeCode))
        resultCode = cursor.fetchone()

        if resultCode:
            QMessageBox.warning(self, "Input Error", "The college code you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return

        # Check if the college name exists in another record
        queryName = """
            SELECT collegename FROM COLLEGE 
            WHERE UPPER(REPLACE(collegename, ' ', '')) = %s AND collegecode <> %s
        """
        cleanNewName = newCollegeName.replace(" ", "").upper()
        cursor.execute(queryName, (cleanNewName, self.originalCollegeCode))
        resultName = cursor.fetchone()

        if resultName:
            QMessageBox.warning(self, "Input Error", "The college name you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return

        cursor.close()
        connection.close()

        return [newCollegeCode, newCollegeName]

    def validateCollegeData(self):
        updatedCollegeData = self.updatedCollegeData()
        if updatedCollegeData:
            self.accept()

class AddCollegeDialog(QDialog, Ui_AddCollegeDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.validateCollegeData)

    def addCollegeData(self):
        collegeCode = self.collegeCodeEdit.text().strip().replace(" ", "").upper()
        collegeName = self.collegeNameEdit.text().strip().title()

        if not collegeCode or not collegeName:
            QMessageBox.warning(self, "Input Error", "All fields must be filled up.")
            return

        if not collegeCode.isalnum() or not all(char.isalpha() or char.isspace() for char in collegeName):
            QMessageBox.warning(self, "Input Error", "Please input a valid college code and name.")
            return

        if len(collegeCode) > 10:
            QMessageBox.warning(self, "Input Error", "Please input no more than 10 characters for college code.")
            return
        
        if len(collegeName) > 255:
            QMessageBox.warning(self, "Input Error", "Please input no more than 255 characters for college name.")
            return

        connection = self.parent().connectToDatabase()
        cursor = connection.cursor()

        # Check if college code already exists
        queryCode = "SELECT collegecode FROM COLLEGE WHERE collegecode = %s"
        cursor.execute(queryCode, (collegeCode,))
        resultCode = cursor.fetchone()

        if resultCode:
            QMessageBox.warning(self, "Input Error", "The college code you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return

        # Check if college name already exists (ignoring spaces and case)
        queryName = "SELECT collegename FROM COLLEGE WHERE UPPER(REPLACE(collegename, ' ', '')) = %s"
        cleanCollegeName = collegeName.replace(" ", "").upper()
        cursor.execute(queryName, (cleanCollegeName,))
        resultName = cursor.fetchone()

        if resultName:
            QMessageBox.warning(self, "Input Error", "The college name you are trying to enter already exists.")
            cursor.close()
            connection.close()
            return

        # Insert new college if no conflicts
        insertCollegeQuery = "INSERT INTO COLLEGE (collegecode, collegename) VALUES (%s, %s)"
        cursor.execute(insertCollegeQuery, (collegeCode, collegeName))
        connection.commit()

        cursor.close()
        connection.close()

        return True
        
    def validateCollegeData(self):
        newCollegeData = self.addCollegeData()
        if newCollegeData:
            self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainClass()
    main.show()
    app.exec_()