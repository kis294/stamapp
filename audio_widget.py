from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries

class WaveformAnalyzer(QWidget):
    def __init__(self, audio_file):
        super().__init__()

        # Create QMediaPlayer object
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(audio_file)))

        # Create QLineSeries and QChart objects
        self.series = QLineSeries()
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Waveform Analyzer")
        self.chartView = QChartView(self.chart)
        #self.chartView.setRenderHint(QPainter.Antialiasing)

        # Create timer to update waveform data
        self.timer = QTimer()
        self.timer.setInterval(10) # 10 milliseconds
        self.timer.timeout.connect(self.update_waveform)

        # Create layout and add chartView
        layout = QVBoxLayout(self)
        layout.addWidget(self.chartView)

    def start(self):
        # Start player and timer
        self.player.play()
        self.timer.start()

    def stop(self):
        # Stop player and timer
        self.player.stop()
        self.timer.stop()

    def update_waveform(self):
        # Read audio data
        audio_data = self.player.read(self.player.duration() * 2)

        # Convert audio data to waveform data
        waveform_data = []
        for i in range(0, len(audio_data), 2):
            sample = int.from_bytes(audio_data[i:i+2], byteorder="little")
            waveform_data.append(sample)

        # Update the QLineSeries
        self.series.clear()
        for i, sample in enumerate(waveform_data):
            self.series.append(i, sample)

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = QMainWindow()
    stackedWidget = QStackedWidget(mainWindow)
    audio_file = "audio_file.wav"
    waveformAnalyzer = WaveformAnalyzer(audio_file)
    stackedWidget.addWidget(waveformAnalyzer)
    mainWindow.setCentralWidget(stackedWidget)
    mainWindow.show()
    waveformAnalyzer.start()
    app.exec_()
