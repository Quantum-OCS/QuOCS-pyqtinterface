# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mrossign/QuOCS/QuOCS-pyqtinterface/quocs_pyqtinterface/gui/uifiles/RemoteConnection.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(805, 136)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.credential_file_edit_line = QtWidgets.QLineEdit(Form)
        self.credential_file_edit_line.setObjectName("credential_file_edit_line")
        self.horizontalLayout.addWidget(self.credential_file_edit_line)
        self.get_credential_file_button = QtWidgets.QPushButton(Form)
        self.get_credential_file_button.setObjectName("get_credential_file_button")
        self.horizontalLayout.addWidget(self.get_credential_file_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.check_connection_button = QtWidgets.QPushButton(Form)
        self.check_connection_button.setObjectName("check_connection_button")
        self.horizontalLayout_3.addWidget(self.check_connection_button)
        self.status_edit_line = QtWidgets.QLineEdit(Form)
        self.status_edit_line.setObjectName("status_edit_line")
        self.horizontalLayout_3.addWidget(self.status_edit_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.shared_folder_edit_line = QtWidgets.QLineEdit(Form)
        self.shared_folder_edit_line.setObjectName("shared_folder_edit_line")
        self.horizontalLayout_2.addWidget(self.shared_folder_edit_line)
        self.get_shared_folder_button = QtWidgets.QPushButton(Form)
        self.get_shared_folder_button.setObjectName("get_shared_folder_button")
        self.horizontalLayout_2.addWidget(self.get_shared_folder_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.results_folder_eddit_line = QtWidgets.QLineEdit(Form)
        self.results_folder_eddit_line.setObjectName("results_folder_eddit_line")
        self.horizontalLayout_4.addWidget(self.results_folder_eddit_line)
        self.get_results_folder_button = QtWidgets.QPushButton(Form)
        self.get_results_folder_button.setObjectName("get_results_folder_button")
        self.horizontalLayout_4.addWidget(self.get_results_folder_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Credentials File"))
        self.get_credential_file_button.setText(_translate("Form", "Get File"))
        self.check_connection_button.setText(_translate("Form", "Check Connection"))
        self.label_2.setText(_translate("Form", "Shared Folder"))
        self.get_shared_folder_button.setText(_translate("Form", "Get Folder"))
        self.label_3.setText(_translate("Form", "Results Folder"))
        self.get_results_folder_button.setText(_translate("Form", "Get Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
