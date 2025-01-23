import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)
import openpyxl
from Categories import Categories

class MA_Finance(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("MA_Finance")
        self.setGeometry(200, 200, 800, 600)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Add a button to load Excel files
        self.load_button = QPushButton("Import Statement")
        self.load_button.clicked.connect(self.load_excel_file)
        self.layout.addWidget(self.load_button)

        # Add a table to display Excel content
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def load_excel_file(self):
        """
         # Open a file dialog to select an Excel file
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Import Statement", "", "Excel Files (*.xlsx *.xls *.csv)"
        )
        if file_path:
            #self.display_excel_content(file_path)
        """
        self.display_excel_content(r"C:\Users\jasle\OneDrive\Documents\GitHub\Budget_Plannig\2024_Chequing_Transactions_only.xlsx")

    def display_excel_content(self, file_path):
        # Load the Excel file
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            # Get the number of rows and columns
            rows = sheet.max_row
            cols = sheet.max_column

            # Set the table dimensions
            self.table.setRowCount(rows)
            self.table.setColumnCount(cols)

            # Populate the table with Excel data
            for row in range(1, rows + 1):
                for col in range(1, cols + 1):
                    cell_value = sheet.cell(row=row, column=col).value
                    self.table.setItem(row - 1, col - 1, QTableWidgetItem(str(cell_value)))
            
            #make first row items headers
            for col in range(1, cols + 1):
                header = sheet.cell(row=1, column=col).value
                self.table.setHorizontalHeaderItem(col-1, QTableWidgetItem(str(header)))
            
            #Remove the first row
            self.table.removeRow(0)

            # Add a column to the table named category and move it to the first column
            self.table.insertColumn(0)
            self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Category"))
            
            columns_to_remove = []
            for col in range(self.table.columnCount()):
                header_item = self.table.horizontalHeaderItem(col)
                if header_item and header_item.text().lower() in ["status", "filter"]:
                    columns_to_remove.append(col)

            # Remove the columns in reverse order to avoid shifting issues
            for col in sorted(columns_to_remove, reverse=True):
                self.table.removeColumn(col)

            table = self.table
            Categories(self.table)
            
        except Exception as e:
            print(f"Error loading Excel file: {e}")
    


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MA_Finance()
    window.show()
    sys.exit(app.exec_())
