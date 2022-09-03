import sys
from DesignLayou.design import *

from pytube import YouTube
import moviepy.editor as mp
import re
import os
import proglog
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit

class Novo(QMainWindow, Ui_YTMP3):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConvert.clicked.connect(self.baixar)


    def baixar(self):
        self.lbResult.setText("Iniciando aguarde até terminar !!!")
        #music, _ = QFileDialog.getSaveFileName(
        #    self.centralwidget,
        #    'Salvar Musica',
        #    r'C:\Users\fabio\Downloads'
        #)

        # Digite o link do vídeo e o local para salvar:
        link = self.inputLink.text()
        path = r'C:\Users\fabio\Downloads'
        yt = YouTube(link)

        # Começar a baixar:
        self.lbResult.setText("Baixando...")
        ys = yt.streams.filter(only_audio=True).first().download(path)
        # Converter mp4 > mp3:
        self.lbResult.setText("Convertendo para mp3...")
        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)

        self.lbResult.setText("Conversão concluída com sucesso!!!")
        self.inputLink.setText("")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec()