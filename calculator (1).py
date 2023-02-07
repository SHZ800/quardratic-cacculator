import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,QPushButton, QFormLayout,QMessageBox

def function(a,b,c):
    a = float(a.text())
    b = float(b.text())
    c = float(c.text())
    x1=((-b+(((b**2)-(4*a*c))**(1/2)))/(2*a))
    x2=((-b-(((b**2)-(4*a*c))**(1/2)))/(2*a))
    mbox = QMessageBox()
    mbox.setText(f'x1: {x1} x2: {x2}')
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500,500)
    w.setWindowTitle("Calculator")
    layout = QFormLayout()

    # Add form fields to the layout
    a=QLineEdit()
    b=QLineEdit()
    c=QLineEdit()
    layout.addRow("Input A:", a)
    layout.addRow("Input B:",b)
    layout.addRow("Input C:", c)
    
    btn = QPushButton("Calculate")
    btn.clicked.connect(lambda: function(a, b, c))
    layout.addRow(btn)

    w.setLayout(layout)
    w.show()

    sys.exit(app.exec_())