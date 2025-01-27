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
    QComboBox,
    QCheckBox,
    QHBoxLayout,
)
import pandas as pd
import matplotlib.pyplot as plt

class plot_spending(QMainWindow):
    def __init__(self, table, parent=None):
        super().__init__(parent)
        self.table = table
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Plot Spending')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.category_selector = QComboBox(self)
        self.category_selector.setEditable(True)
        layout.addWidget(self.category_selector)

        self.plot_button = QPushButton('Plot', self)
        self.plot_button.clicked.connect(self.plot_data)
        layout.addWidget(self.plot_button)

        self.sum_checkbox = QCheckBox('Sum categories', self)
        layout.addWidget(self.sum_checkbox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_categories()

    def load_categories(self):
        categories = set()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            if item:
                categories.add(item.text())
        self.category_selector.addItems(sorted(categories))

    def plot_data(self):
        selected_categories = self.category_selector.currentText().split(',')
        sum_categories = self.sum_checkbox.isChecked()

        data = []
        for row in range(self.table.rowCount()):
            category = self.table.item(row, 0).text()
            date = self.table.item(row, 1).text()
            amount = float(self.table.item(row, 3).text())
            if category in selected_categories:
                data.append([category, date, amount])

        df = pd.DataFrame(data, columns=['Category', 'Date', 'Amount'])
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        if sum_categories:
            df = df.groupby(pd.Grouper(freq='M')).sum()
            plt.plot(df.index, df['Amount'], label='Sum of Categories')
        else:
            for category in selected_categories:
                category_df = df[df['Category'] == category]
                category_df = category_df.groupby(pd.Grouper(freq='M')).sum()
                plt.plot(category_df.index, category_df['Amount'], label=category)

        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.title('Spending by Category')
        plt.legend()
        plt.show()