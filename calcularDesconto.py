import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMainWindow, QMessageBox, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QEvent
from qdarkstyle import load_stylesheet_pyqt5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da largura e altura padrão para os botões
        self.largura_botao = 25
        self.altura_botao = 20

        # Configuração da largura e altura padrão para o botão de calcular
        self.largura_botao_calcular = 55
        self.altura_botao_calcular = 30

        # Configuração da largura e altura padrão para os campos de entrada
        self.largura_entry = 250
        self.altura_entry = 30

        # Configuração da fonte negrito para as QLabel
        self.font_negrito = QFont()
        self.font_negrito.setBold(True)

        self.init_ui()

    def init_ui(self):
        # Configuração da interface gráfica
        self.setGeometry(200, 200, 250, 200)
        self.setWindowTitle("Calculadora de Desconto")
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove barra de título padrão

        # Layout principal
        layout_principal = QVBoxLayout(self)

        # Layout para os botões de minimizar e fechar
        layout_botoes = QHBoxLayout()

        # Botão de minimizar
        self.button_minimizar = QPushButton("-")
        self.button_minimizar.clicked.connect(self.showMinimized)
        self.button_minimizar.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.button_minimizar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button_minimizar.setFixedSize(self.largura_botao, self.altura_botao)
        self.button_minimizar.setStyleSheet("font-size: 18px;")  # Ajusta o tamanho do texto

        # Botão de fechar
        self.button_fechar = QPushButton("X")
        self.button_fechar.clicked.connect(self.close)
        self.button_fechar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button_fechar.setFixedSize(self.largura_botao, self.altura_botao)
        self.button_fechar.setStyleSheet("font-size: 18px;")  # Ajusta o tamanho do texto

        # Adiciona os botões ao layout
        layout_botoes.addStretch(1)  # Adiciona um espaço elástico à esquerda
        layout_botoes.addWidget(self.button_minimizar)
        layout_botoes.addWidget(self.button_fechar)

        # Adiciona o layout dos botões ao layout principal
        layout_principal.addLayout(layout_botoes)

        # Widgets
        self.label_preco = QLabel("Informe o preço do produto:")
        self.label_preco.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.entry_preco = QLineEdit()
        self.entry_preco.setStyleSheet("font-size: 14px;")  # Ajusta o tamanho do texto
        self.entry_preco.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.entry_preco.setFixedSize(self.largura_entry, self.altura_entry)

        self.label_desconto = QLabel("Informe o Valor do Desconto:")
        self.label_desconto.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.entry_desconto = QLineEdit()
        self.entry_desconto.setStyleSheet("font-size: 14px;")  # Ajusta o tamanho do texto
        self.entry_desconto.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.entry_desconto.setFixedSize(self.largura_entry, self.altura_entry)

        self.button_calcular = QPushButton("Calcular")
        self.button_calcular.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.button_calcular.clicked.connect(self.calcular_desconto)
        self.button_calcular.setFixedSize(self.largura_botao_calcular, self.altura_botao_calcular)

        self.button_limpar = QPushButton("Limpar")
        self.button_limpar.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.button_limpar.clicked.connect(self.cancelar_calculo)
        self.button_limpar.setFixedSize(self.largura_botao_calcular, self.altura_botao_calcular)

        self.label_resultado_desconto = QLabel("O Valor do Desconto é:")
        self.label_resultado_desconto.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
        self.label_resultado_final = QLabel("O Valor Final é:")
        self.label_resultado_final.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito

        # Adiciona widgets ao layout
        layout_principal.addWidget(self.label_preco)
        layout_principal.addWidget(self.entry_preco)
        layout_principal.addWidget(self.label_desconto)
        layout_principal.addWidget(self.entry_desconto)

        # Layout para os botões Calcular e Limpar
        layout_botoes_calculo = QHBoxLayout()
        layout_botoes_calculo.addWidget(self.button_calcular)
        layout_botoes_calculo.addWidget(self.button_limpar)

        layout_principal.addLayout(layout_botoes_calculo)

        layout_principal.addWidget(self.label_resultado_desconto)
        layout_principal.addWidget(self.label_resultado_final)

        # Configuração do widget central
        central_widget = QWidget(self)
        central_widget.setLayout(layout_principal)

        # Aplicar estilo do QDarkStyleSheet ao widget central
        central_widget.setStyleSheet(load_stylesheet_pyqt5())

        # Adiciona uma classe ao widget central e aplica bordas arredondadas diretamente
        central_widget.setObjectName("rounded")
        central_widget.setStyleSheet("QWidget#rounded { background-color: #343541; border-radius: 15px; }")

        self.setCentralWidget(central_widget)

        # Configuração de eventos para permitir a movimentação da janela
        self.mousePressPos = None
        self.setMouseTracking(True)
        self.installEventFilter(self)

        self.show()

    def calcular_desconto(self):
        try:
            preco_produto = float(self.entry_preco.text())
            desconto_produto = float(self.entry_desconto.text())

            resultado_desconto = preco_produto * desconto_produto / 100
            resultado_final = preco_produto - resultado_desconto

            # Converte os resultados para strings formatadas
            resultado_desconto_str = f"O Valor do Desconto é: <font color='green'>{resultado_desconto:.2f}</font>"
            resultado_final_str = f"O Valor Final é: <font color='green'>{resultado_final:.2f}</font>"

            # Define o texto com HTML, permitindo a aplicação de cores
            self.label_resultado_desconto.setText(resultado_desconto_str)
            self.label_resultado_desconto.setFont(self.font_negrito)  # Aplica o estilo de fonte negrito
            self.label_resultado_final.setText(resultado_final_str)

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos nos campos.")

    def cancelar_calculo(self):
        # Limpa os campos e redefine a cor do texto para preto
        self.entry_preco.clear()
        self.entry_desconto.clear()
        self.label_resultado_desconto.clear()
        self.label_resultado_final.clear()

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress and source is self:
            self.mousePressPos = event.globalPos()
        elif event.type() == QEvent.MouseMove and self.mousePressPos is not None:
            self.move(self.pos() + event.globalPos() - self.mousePressPos)
            self.mousePressPos = event.globalPos()
        elif event.type() == QEvent.MouseButtonRelease:
            self.mousePressPos = None

        return super().eventFilter(source, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Aplicar folha de estilo globalmente
    app.setStyleSheet(load_stylesheet_pyqt5())

    mainWindow = MainWindow()
    sys.exit(app.exec_())
