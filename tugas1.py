   # Form implementation generated from reading ui file 'tutor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 260)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.random_text = QtWidgets.QPushButton(parent=Form)
        self.random_text.setObjectName("random_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.random_text)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label)
        self.progess = QtWidgets.QPushButton(parent=Form)
        self.progess.setObjectName("progess")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.progess)
        self.progressBar = QtWidgets.QProgressBar(parent=Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.progressBar)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(parent=Form)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 6, 0, 1, 1)
        self.judul = QtWidgets.QLineEdit(parent=Form)
        self.judul.setObjectName("judul")
        self.gridLayout.addWidget(self.judul, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.random_text.setText(_translate("Form", "Random text"))
        self.progess.setText(_translate("Form", "progess"))
        self.pushButton_1.setText(_translate("Form", "Open Chrome"))
        self.pushButton_3.setText(_translate("Form", "My Fov Game -v-"))
        self.pushButton_4.setText(_translate("Form", "Facebook"))
        self.pushButton_5.setText(_translate("Form", "Instagram"))
        self.pushButton_7.setText(_translate("Form", "Twicth"))
        self.pushButton_8.setText(_translate("Form", "Never give up"))
        self.label_1.setText(_translate("Form", "                  No Copryrigth©2024 Aga All done just click everything"))
        self.judul.setText(_translate("Form", "                         💻 Welcome to TechCentral Command 💻"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
