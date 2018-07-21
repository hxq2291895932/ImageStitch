# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_input = QtWidgets.QPushButton(self.centralwidget)
        self.bt_input.setGeometry(QtCore.QRect(200, 150, 91, 28))
        self.bt_input.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_input.setMouseTracking(False)
        self.bt_input.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bt_input.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_input.setObjectName("bt_input")
        self.lb_input = QtWidgets.QLabel(self.centralwidget)
        self.lb_input.setGeometry(QtCore.QRect(30, 160, 71, 21))
        self.lb_input.setObjectName("lb_input")
        self.lb_output = QtWidgets.QLabel(self.centralwidget)
        self.lb_output.setGeometry(QtCore.QRect(30, 400, 121, 20))
        self.lb_output.setObjectName("lb_output")
        self.bt_output = QtWidgets.QPushButton(self.centralwidget)
        self.bt_output.setGeometry(QtCore.QRect(240, 430, 51, 31))
        self.bt_output.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_output.setObjectName("bt_output")
        self.bt_startStitch = QtWidgets.QPushButton(self.centralwidget)
        self.bt_startStitch.setGeometry(QtCore.QRect(670, 500, 93, 28))
        self.bt_startStitch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_startStitch.setObjectName("bt_startStitch")
        self.lb_icon = QtWidgets.QLabel(self.centralwidget)
        self.lb_icon.setGeometry(QtCore.QRect(80, 10, 119, 119))
        self.lb_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_icon.setObjectName("lb_icon")
        self.lineEdit_output = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_output.setGeometry(QtCore.QRect(30, 430, 211, 31))
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.list_input = QtWidgets.QListWidget(self.centralwidget)
        self.list_input.setGeometry(QtCore.QRect(30, 190, 261, 192))
        self.list_input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_input.setObjectName("list_input")
        self.lineEdit_fileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fileName.setGeometry(QtCore.QRect(30, 510, 211, 31))
        self.lineEdit_fileName.setObjectName("lineEdit_fileName")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 20, 371, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.cbBox_mode = QtWidgets.QComboBox(self.layoutWidget)
        self.cbBox_mode.setObjectName("cbBox_mode")
        self.horizontalLayout_2.addWidget(self.cbBox_mode)
        self.bt_editMode = QtWidgets.QPushButton(self.layoutWidget)
        self.bt_editMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_editMode.setObjectName("bt_editMode")
        self.horizontalLayout_2.addWidget(self.bt_editMode)
        self.bt_addMode = QtWidgets.QPushButton(self.layoutWidget)
        self.bt_addMode.setObjectName("bt_addMode")
        self.horizontalLayout_2.addWidget(self.bt_addMode)
        self.lb_fileName = QtWidgets.QLabel(self.centralwidget)
        self.lb_fileName.setGeometry(QtCore.QRect(30, 480, 111, 20))
        self.lb_fileName.setObjectName("lb_fileName")
        self.groupBox_setting = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_setting.setGeometry(QtCore.QRect(360, 70, 421, 401))
        self.groupBox_setting.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_setting.setObjectName("groupBox_setting")
        self.lb_resize = QtWidgets.QLabel(self.groupBox_setting)
        self.lb_resize.setGeometry(QtCore.QRect(40, 30, 72, 15))
        self.lb_resize.setObjectName("lb_resize")
        self.bt_del = QtWidgets.QPushButton(self.groupBox_setting)
        self.bt_del.setGeometry(QtCore.QRect(30, 340, 81, 28))
        self.bt_del.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_del.setObjectName("bt_del")
        self.checkBox_resize = QtWidgets.QCheckBox(self.groupBox_setting)
        self.checkBox_resize.setGeometry(QtCore.QRect(120, 60, 111, 19))
        self.checkBox_resize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_resize.setObjectName("checkBox_resize")
        self.lb_directionPic = QtWidgets.QLabel(self.groupBox_setting)
        self.lb_directionPic.setGeometry(QtCore.QRect(230, 230, 181, 143))
        self.lb_directionPic.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_directionPic.setObjectName("lb_directionPic")
        self.lb_directionEx = QtWidgets.QLabel(self.groupBox_setting)
        self.lb_directionEx.setGeometry(QtCore.QRect(230, 210, 72, 15))
        self.lb_directionEx.setObjectName("lb_directionEx")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_setting)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 50, 181, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_resize_y = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_resize_y.setObjectName("lb_resize_y")
        self.gridLayout_2.addWidget(self.lb_resize_y, 1, 0, 1, 1)
        self.dsBox_resize_x = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.dsBox_resize_x.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.dsBox_resize_x.setDecimals(3)
        self.dsBox_resize_x.setMaximum(1.0)
        self.dsBox_resize_x.setSingleStep(0.1)
        self.dsBox_resize_x.setProperty("value", 1.0)
        self.dsBox_resize_x.setObjectName("dsBox_resize_x")
        self.gridLayout_2.addWidget(self.dsBox_resize_x, 0, 1, 1, 1)
        self.dsBox_resize_y = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.dsBox_resize_y.setDecimals(3)
        self.dsBox_resize_y.setMaximum(1.0)
        self.dsBox_resize_y.setSingleStep(0.1)
        self.dsBox_resize_y.setProperty("value", 1.0)
        self.dsBox_resize_y.setObjectName("dsBox_resize_y")
        self.gridLayout_2.addWidget(self.dsBox_resize_y, 1, 1, 1, 1)
        self.lb_resize_x = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_resize_x.setObjectName("lb_resize_x")
        self.gridLayout_2.addWidget(self.lb_resize_x, 0, 0, 1, 1)
        self.lb_search = QtWidgets.QLabel(self.groupBox_setting)
        self.lb_search.setGeometry(QtCore.QRect(30, 120, 72, 15))
        self.lb_search.setObjectName("lb_search")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_setting)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 150, 171, 135))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_featureMethod = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_featureMethod.setObjectName("lb_featureMethod")
        self.gridLayout.addWidget(self.lb_featureMethod, 0, 0, 1, 1)
        self.cbBox_featureMethod = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbBox_featureMethod.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbBox_featureMethod.setObjectName("cbBox_featureMethod")
        self.cbBox_featureMethod.addItem("")
        self.cbBox_featureMethod.addItem("")
        self.cbBox_featureMethod.addItem("")
        self.gridLayout.addWidget(self.cbBox_featureMethod, 0, 1, 1, 1)
        self.lb_offsetCaculate = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_offsetCaculate.setObjectName("lb_offsetCaculate")
        self.gridLayout.addWidget(self.lb_offsetCaculate, 1, 0, 1, 1)
        self.cbBox_offsetCaculate = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbBox_offsetCaculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbBox_offsetCaculate.setObjectName("cbBox_offsetCaculate")
        self.cbBox_offsetCaculate.addItem("")
        self.cbBox_offsetCaculate.addItem("")
        self.gridLayout.addWidget(self.cbBox_offsetCaculate, 1, 1, 1, 1)
        self.lb_direction = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_direction.setObjectName("lb_direction")
        self.gridLayout.addWidget(self.lb_direction, 2, 0, 1, 1)
        self.cbBox_direction = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbBox_direction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbBox_direction.setObjectName("cbBox_direction")
        self.cbBox_direction.addItem("")
        self.cbBox_direction.addItem("")
        self.cbBox_direction.addItem("")
        self.cbBox_direction.addItem("")
        self.cbBox_direction.addItem("")
        self.cbBox_direction.addItem("")
        self.gridLayout.addWidget(self.cbBox_direction, 2, 1, 1, 1)
        self.lb_method = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_method.setObjectName("lb_method")
        self.gridLayout.addWidget(self.lb_method, 3, 0, 1, 1)
        self.cbBox_method = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbBox_method.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbBox_method.setObjectName("cbBox_method")
        self.cbBox_method.addItem("")
        self.cbBox_method.addItem("")
        self.gridLayout.addWidget(self.cbBox_method, 3, 1, 1, 1)
        self.lb_fusion = QtWidgets.QLabel(self.layoutWidget2)
        self.lb_fusion.setObjectName("lb_fusion")
        self.gridLayout.addWidget(self.lb_fusion, 4, 0, 1, 1)
        self.cbBox_fusion = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbBox_fusion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbBox_fusion.setObjectName("cbBox_fusion")
        self.cbBox_fusion.addItem("")
        self.cbBox_fusion.addItem("")
        self.cbBox_fusion.addItem("")
        self.cbBox_fusion.addItem("")
        self.cbBox_fusion.addItem("")
        self.cbBox_fusion.addItem("")
        self.cbBox_fusion.addItem("")
        self.gridLayout.addWidget(self.cbBox_fusion, 4, 1, 1, 1)
        self.bt_save = QtWidgets.QPushButton(self.groupBox_setting)
        self.bt_save.setGeometry(QtCore.QRect(120, 340, 81, 28))
        self.bt_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_save.setObjectName("bt_save")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_setting)
        self.layoutWidget3.setGeometry(QtCore.QRect(230, 150, 181, 23))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_searchRatio = QtWidgets.QLabel(self.layoutWidget3)
        self.lb_searchRatio.setObjectName("lb_searchRatio")
        self.horizontalLayout.addWidget(self.lb_searchRatio)
        self.dsBox_searchRatio = QtWidgets.QDoubleSpinBox(self.layoutWidget3)
        self.dsBox_searchRatio.setDecimals(3)
        self.dsBox_searchRatio.setMaximum(1.0)
        self.dsBox_searchRatio.setSingleStep(0.1)
        self.dsBox_searchRatio.setObjectName("dsBox_searchRatio")
        self.horizontalLayout.addWidget(self.dsBox_searchRatio)
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_setting)
        self.layoutWidget_2.setGeometry(QtCore.QRect(230, 180, 181, 23))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_roiRatio = QtWidgets.QLabel(self.layoutWidget_2)
        self.lb_roiRatio.setObjectName("lb_roiRatio")
        self.horizontalLayout_3.addWidget(self.lb_roiRatio)
        self.dsBox_offsetEvaluate = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.dsBox_offsetEvaluate.setDecimals(0)
        self.dsBox_offsetEvaluate.setObjectName("dsBox_offsetEvaluate")
        self.horizontalLayout_3.addWidget(self.dsBox_offsetEvaluate)
        self.lb_resize.raise_()
        self.bt_del.raise_()
        self.checkBox_resize.raise_()
        self.lb_directionPic.raise_()
        self.lb_directionEx.raise_()
        self.layoutWidget.raise_()
        self.lb_search.raise_()
        self.layoutWidget.raise_()
        self.bt_save.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.lb_icon.raise_()
        self.lb_icon.raise_()
        self.bt_del.raise_()
        self.checkBox_resize.raise_()
        self.lb_directionPic.raise_()
        self.lb_directionEx.raise_()
        self.layoutWidget.raise_()
        self.lb_search.raise_()
        self.layoutWidget.raise_()
        self.bt_save.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.bt_del.raise_()
        self.checkBox_resize.raise_()
        self.lb_directionPic.raise_()
        self.lb_directionEx.raise_()
        self.layoutWidget.raise_()
        self.lb_search.raise_()
        self.layoutWidget.raise_()
        self.bt_save.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.cbBox_extension = QtWidgets.QComboBox(self.centralwidget)
        self.cbBox_extension.setGeometry(QtCore.QRect(240, 510, 51, 31))
        self.cbBox_extension.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbBox_extension.setObjectName("cbBox_extension")
        self.cbBox_extension.addItem("")
        self.cbBox_extension.addItem("")
        self.groupBox_setting.raise_()
        self.bt_input.raise_()
        self.lb_input.raise_()
        self.lb_output.raise_()
        self.bt_output.raise_()
        self.bt_startStitch.raise_()
        self.lb_icon.raise_()
        self.lineEdit_output.raise_()
        self.list_input.raise_()
        self.lineEdit_fileName.raise_()
        self.layoutWidget.raise_()
        self.lb_fileName.raise_()
        self.cbBox_extension.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        # self.menu_user = QtWidgets.QMenu(self.menubar)
        # self.menu_user.setObjectName("menu_user")
        # self.menu_set = QtWidgets.QMenu(self.menubar)
        # self.menu_set.setObjectName("menu_set")
        MainWindow.setMenuBar(self.menubar)
        # self.action_login = QtWidgets.QAction(MainWindow)
        # self.action_login.setObjectName("action_login")
        # self.action_logout = QtWidgets.QAction(MainWindow)
        # self.action_logout.setObjectName("action_logout")
        # self.action_resetPassword = QtWidgets.QAction(MainWindow)
        # self.action_resetPassword.setObjectName("action_resetPassword")
        # self.action_removePassword = QtWidgets.QAction(MainWindow)
        # self.action_removePassword.setObjectName("action_removePassword")
        # self.menu_user.addAction(self.action_logout)
        # self.menu_set.addAction(self.action_resetPassword)
        # self.menu_set.addAction(self.action_removePassword)
        # self.menubar.addAction(self.menu_user.menuAction())
        # self.menubar.addAction(self.menu_set.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cbBox_mode, self.bt_editMode)
        MainWindow.setTabOrder(self.bt_editMode, self.bt_addMode)
        MainWindow.setTabOrder(self.bt_addMode, self.checkBox_resize)
        MainWindow.setTabOrder(self.checkBox_resize, self.dsBox_resize_x)
        MainWindow.setTabOrder(self.dsBox_resize_x, self.dsBox_resize_y)
        MainWindow.setTabOrder(self.dsBox_resize_y, self.cbBox_featureMethod)
        MainWindow.setTabOrder(self.cbBox_featureMethod, self.dsBox_searchRatio)
        MainWindow.setTabOrder(self.dsBox_searchRatio, self.cbBox_offsetCaculate)
        MainWindow.setTabOrder(self.cbBox_offsetCaculate, self.dsBox_offsetEvaluate)
        MainWindow.setTabOrder(self.dsBox_offsetEvaluate, self.cbBox_direction)
        MainWindow.setTabOrder(self.cbBox_direction, self.cbBox_method)
        MainWindow.setTabOrder(self.cbBox_method, self.cbBox_fusion)
        MainWindow.setTabOrder(self.cbBox_fusion, self.bt_del)
        MainWindow.setTabOrder(self.bt_del, self.bt_save)
        MainWindow.setTabOrder(self.bt_save, self.list_input)
        MainWindow.setTabOrder(self.list_input, self.lineEdit_output)
        MainWindow.setTabOrder(self.lineEdit_output, self.bt_output)
        MainWindow.setTabOrder(self.bt_output, self.lineEdit_fileName)
        MainWindow.setTabOrder(self.lineEdit_fileName, self.bt_startStitch)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "北科大材料显微图像拼接软件"))
        self.bt_input.setText(_translate("MainWindow", "导入"))
        self.lb_input.setText(_translate("MainWindow", "图像集："))
        self.lb_output.setText(_translate("MainWindow", "结果导出地址："))
        self.bt_output.setText(_translate("MainWindow", "…"))
        self.bt_startStitch.setText(_translate("MainWindow", "开始拼接"))
        self.lb_icon.setText(_translate("MainWindow", "图标"))
        self.label_16.setText(_translate("MainWindow", "模式选择："))
        self.bt_editMode.setText(_translate("MainWindow", "编辑该模式"))
        self.bt_addMode.setText(_translate("MainWindow", "添加新模式"))
        self.lb_fileName.setText(_translate("MainWindow", "导出文件名："))
        self.groupBox_setting.setTitle(_translate("MainWindow", "参数设定："))
        self.lb_resize.setText(_translate("MainWindow", "预处理："))
        self.bt_del.setText(_translate("MainWindow", "删除该模式"))
        self.checkBox_resize.setText(_translate("MainWindow", "图像下采样"))
        self.lb_directionPic.setText(_translate("MainWindow", "顺序示意图"))
        self.lb_directionEx.setText(_translate("MainWindow", "顺序示意："))
        self.lb_resize_y.setText(_translate("MainWindow", "纵轴倍数："))
        self.lb_resize_x.setText(_translate("MainWindow", "横轴倍数："))
        self.lb_search.setText(_translate("MainWindow", "特征搜索："))
        self.lb_featureMethod.setText(_translate("MainWindow", "算子："))
        self.cbBox_featureMethod.setItemText(0, _translate("MainWindow", "sift"))
        self.cbBox_featureMethod.setItemText(1, _translate("MainWindow", "surf"))
        self.cbBox_featureMethod.setItemText(2, _translate("MainWindow", "orb"))
        self.lb_offsetCaculate.setText(_translate("MainWindow", "配准"))
        self.cbBox_offsetCaculate.setItemText(0, _translate("MainWindow", "众数"))
        self.cbBox_offsetCaculate.setItemText(1, _translate("MainWindow", "RANSAC"))
        self.lb_direction.setText(_translate("MainWindow", "顺序："))
        self.cbBox_direction.setItemText(0, _translate("MainWindow", "行拼接"))
        self.cbBox_direction.setItemText(1, _translate("MainWindow", "列拼接"))
        self.cbBox_direction.setItemText(2, _translate("MainWindow", "左向拼接"))
        self.cbBox_direction.setItemText(3, _translate("MainWindow", "右向拼接"))
        self.cbBox_direction.setItemText(4, _translate("MainWindow", "朝上拼接"))
        self.cbBox_direction.setItemText(5, _translate("MainWindow", "朝下拼接"))
        self.lb_method.setText(_translate("MainWindow", "策略"))
        self.cbBox_method.setItemText(0, _translate("MainWindow", "全局"))
        self.cbBox_method.setItemText(1, _translate("MainWindow", "增量"))
        self.lb_fusion.setText(_translate("MainWindow", "融合算法："))
        self.cbBox_fusion.setItemText(0, _translate("MainWindow", "无融合"))
        self.cbBox_fusion.setItemText(1, _translate("MainWindow", "均值融合"))
        self.cbBox_fusion.setItemText(2, _translate("MainWindow", "最大值融合"))
        self.cbBox_fusion.setItemText(3, _translate("MainWindow", "最小值融合"))
        self.cbBox_fusion.setItemText(4, _translate("MainWindow", "渐入渐出融合"))
        self.cbBox_fusion.setItemText(5, _translate("MainWindow", "三角函数融合"))
        self.cbBox_fusion.setItemText(6, _translate("MainWindow", "带权拉普拉斯金字塔融合"))
        self.bt_save.setText(_translate("MainWindow", "保存该模式"))
        self.lb_searchRatio.setText(_translate("MainWindow", "阈值："))
        self.lb_roiRatio.setText(_translate("MainWindow", "阈值："))
        self.cbBox_extension.setItemText(0, _translate("MainWindow", "jpg"))
        self.cbBox_extension.setItemText(1, _translate("MainWindow", "png"))
        # self.menu_user.setTitle(_translate("MainWindow", "用户"))
        # self.menu_set.setTitle(_translate("MainWindow", "设置"))
        # self.action_login.setText(_translate("MainWindow", "登录"))
        # self.action_logout.setText(_translate("MainWindow", "注销"))
        # self.action_resetPassword.setText(_translate("MainWindow", "修改密码"))
        # self.action_removePassword.setText(_translate("MainWindow", "删除密码"))

