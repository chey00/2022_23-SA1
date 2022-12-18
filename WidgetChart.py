from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCharts import QChart, QChartView, QSplineSeries, QValueAxis
from PySide6.QtCore import Qt, Slot


class WidgetChart(QWidget):
    add_temperature = Slot(float)
    set_temperature_range = Slot(float, float)

    def __init__(self, parent):
        super(WidgetChart, self).__init__(parent)

        self.tick = 0

        self.tick_axis = QValueAxis()

        self.value_axis = QValueAxis()

        self.chart = QChart()
        self.chart.addAxis(self.tick_axis, Qt.AlignBottom)
        self.chart.addAxis(self.value_axis, Qt.AlignLeft)

        self.chart_view = QChartView()
        self.chart_view.setChart(self.chart)

        self.h_box_layout = QHBoxLayout()
        self.h_box_layout.addWidget(self.chart_view)

        self.setLayout(self.h_box_layout)

        self.series = QSplineSeries()
        self.chart.addSeries(self.series)
        self.series.attachAxis(self.tick_axis)
        self.series.attachAxis(self.value_axis)

    def add_temperature(self, temperature):
        pass

    def set_temperature_range(self, min_tmp, max_tmp):
        pass
