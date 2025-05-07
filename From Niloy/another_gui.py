import sys
import psutil
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QTableWidget, QTableWidgetItem, QMessageBox, QHeaderView, QLineEdit, QComboBox, QLabel)
from PyQt5.QtCore import QTimer
import pyqtgraph as pg

class ProcessManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_processes()

    def initUI(self):
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["PID", "Name", "CPU %", "Memory %", "Actions", "Controls"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        control_layout = QHBoxLayout()
        
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(lambda: self.update_processes(None))
        control_layout.addWidget(self.refresh_button)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name or PID")
        control_layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_process)
        control_layout.addWidget(self.search_button)

        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Sort by PID", "Sort by CPU %", "Sort by Memory %"])
        control_layout.addWidget(self.sort_combo)

        self.sort_button = QPushButton("Sort")
        self.sort_button.clicked.connect(self.sort_processes)
        control_layout.addWidget(self.sort_button)

        layout.addLayout(control_layout)

        graph_layout = QHBoxLayout()
        
        self.cpu_graph_widget = pg.PlotWidget()
        self.cpu_graph_widget.setTitle("CPU Usage")
        self.cpu_curve = self.cpu_graph_widget.plot(pen='r', name='CPU %')
        self.cpu_label = QLabel("CPU Usage: 0% | Idle: 0%")
        graph_layout.addWidget(self.cpu_graph_widget)
        graph_layout.addWidget(self.cpu_label)
        
        self.memory_graph_widget = pg.PlotWidget()
        self.memory_graph_widget.setTitle("Memory Usage")
        self.memory_curve = self.memory_graph_widget.plot(pen='b', name='Memory %')
        self.memory_label = QLabel("Memory Usage: 0% | Free: 0%")
        graph_layout.addWidget(self.memory_graph_widget)
        graph_layout.addWidget(self.memory_label)
        
        layout.addLayout(graph_layout)
        
        self.setLayout(layout)
        self.setWindowTitle("Process Manager")
        self.resize(900, 500)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(2000)  # Update every 2 seconds
        self.cpu_data = []
        self.memory_data = []

    def update_processes(self, process_list=None):
        self.table.setRowCount(0)
        if process_list is None:
            process_list = [proc for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']) 
                            if proc.info['cpu_percent'] < 100.0]  # Filter out erroneous high CPU % values
        
        for proc in process_list:
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            self.table.setItem(row_pos, 0, QTableWidgetItem(str(proc.info['pid'])))
            self.table.setItem(row_pos, 1, QTableWidgetItem(proc.info['name']))
            self.table.setItem(row_pos, 2, QTableWidgetItem(f"{proc.info['cpu_percent']:.2f}"))
            self.table.setItem(row_pos, 3, QTableWidgetItem(f"{proc.info['memory_percent']:.2f}"))

            terminate_button = QPushButton("Terminate")
            terminate_button.clicked.connect(lambda _, pid=proc.info['pid']: self.terminate_process(pid))
            self.table.setCellWidget(row_pos, 4, terminate_button)

            pause_resume_button = QPushButton("Pause")
            pause_resume_button.clicked.connect(lambda _, pid=proc.info['pid'], btn=pause_resume_button: self.pause_resume_process(pid, btn))
            self.table.setCellWidget(row_pos, 5, pause_resume_button)

    def terminate_process(self, pid):
        try:
            psutil.Process(pid).terminate()
            QMessageBox.information(self, "Success", f"Process {pid} terminated.")
            self.update_processes()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def pause_resume_process(self, pid, button):
        try:
            process = psutil.Process(pid)
            if process.status() == psutil.STATUS_STOPPED:
                process.resume()
                button.setText("Pause")
            else:
                process.suspend()
                button.setText("Resume")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def search_process(self):
        search_text = self.search_input.text().strip().lower()
        if not search_text:
            self.update_processes()
            return

        filtered_processes = [proc for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
                              if search_text in str(proc.info['pid']) or search_text in proc.info['name'].lower()]
        self.update_processes(filtered_processes)

    def sort_processes(self):
        sort_option = self.sort_combo.currentText()
        processes = list(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']))

        if sort_option == "Sort by PID":
            processes.sort(key=lambda p: p.info['pid'])
        elif sort_option == "Sort by CPU %":
            processes.sort(key=lambda p: p.info['cpu_percent'], reverse=True)
        elif sort_option == "Sort by Memory %":
            processes.sort(key=lambda p: p.info['memory_percent'], reverse=True)
        
        self.update_processes(processes)

    def update_graph(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        idle_cpu = 100 - cpu
        free_memory = 100 - memory

        self.cpu_data.append(cpu)
        self.memory_data.append(memory)
        if len(self.cpu_data) > 50:
            self.cpu_data.pop(0)
            self.memory_data.pop(0)
        self.cpu_curve.setData(self.cpu_data)
        self.memory_curve.setData(self.memory_data)

        self.cpu_label.setText(f"CPU Usage: {cpu:.2f}% | Idle: {idle_cpu:.2f}%")
        self.memory_label.setText(f"Memory Usage: {memory:.2f}% | Free: {free_memory:.2f}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ProcessManager()
    ex.show()
    sys.exit(app.exec_())
