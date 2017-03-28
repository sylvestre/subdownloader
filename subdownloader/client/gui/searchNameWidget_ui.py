# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchNameWidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchNameWidget(object):
    def setupUi(self, SearchNameWidget):
        SearchNameWidget.setObjectName("SearchNameWidget")
        SearchNameWidget.resize(623, 458)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchNameWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(SearchNameWidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)
        self.searchSitesCombo = LanguageComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchSitesCombo.sizePolicy().hasHeightForWidth())
        self.searchSitesCombo.setSizePolicy(sizePolicy)
        self.searchSitesCombo.setObjectName("searchSitesCombo")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/sites/opensubtitles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSitesCombo.addItem(icon, "")
        self.gridLayout_2.addWidget(self.searchSitesCombo, 1, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 3, 1, 1)
        self.filterLanguage = LanguageComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLanguage.sizePolicy().hasHeightForWidth())
        self.filterLanguage.setSizePolicy(sizePolicy)
        self.filterLanguage.setMinimumSize(QtCore.QSize(100, 0))
        self.filterLanguage.setObjectName("filterLanguage")
        self.gridLayout_2.addWidget(self.filterLanguage, 3, 4, 1, 1)
        self.movieNameText = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieNameText.sizePolicy().hasHeightForWidth())
        self.movieNameText.setSizePolicy(sizePolicy)
        self.movieNameText.setText("")
        self.movieNameText.setObjectName("movieNameText")
        self.gridLayout_2.addWidget(self.movieNameText, 1, 1, 1, 1)
        self.buttonSearchByName = QtWidgets.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSearchByName.setIcon(icon1)
        self.buttonSearchByName.setFlat(False)
        self.buttonSearchByName.setObjectName("buttonSearchByName")
        self.gridLayout_2.addWidget(self.buttonSearchByName, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.moviesView = QtWidgets.QTreeView(SearchNameWidget)
        self.moviesView.setAlternatingRowColors(True)
        self.moviesView.setObjectName("moviesView")
        self.verticalLayout.addWidget(self.moviesView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonIMDBByTitle = QtWidgets.QPushButton(SearchNameWidget)
        self.buttonIMDBByTitle.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonIMDBByTitle.sizePolicy().hasHeightForWidth())
        self.buttonIMDBByTitle.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/imdb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIMDBByTitle.setIcon(icon2)
        self.buttonIMDBByTitle.setIconSize(QtCore.QSize(32, 16))
        self.buttonIMDBByTitle.setObjectName("buttonIMDBByTitle")
        self.horizontalLayout_3.addWidget(self.buttonIMDBByTitle)
        spacerItem = QtWidgets.QSpacerItem(118, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.buttonDownloadByTitle = QtWidgets.QPushButton(SearchNameWidget)
        self.buttonDownloadByTitle.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDownloadByTitle.sizePolicy().hasHeightForWidth())
        self.buttonDownloadByTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonDownloadByTitle.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDownloadByTitle.setIcon(icon3)
        self.buttonDownloadByTitle.setObjectName("buttonDownloadByTitle")
        self.horizontalLayout_3.addWidget(self.buttonDownloadByTitle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SearchNameWidget)
        QtCore.QMetaObject.connectSlotsByName(SearchNameWidget)

    def retranslateUi(self, SearchNameWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchNameWidget.setWindowTitle(_("Form"))
        self.label_3.setText(_("Site:"))
        self.searchSitesCombo.setItemText(0, _("OpenSubtitles.org"))
        self.label_10.setText(_("Filter by :"))
        self.buttonSearchByName.setText(_("Search"))
        self.label_12.setText(_("Subtitles found:"))
        self.buttonIMDBByTitle.setText(_("Movie Info"))
        self.buttonDownloadByTitle.setText(_("Download"))

from subdownloader.client.gui.languageComboBox import LanguageComboBox
from subdownloader.client.gui import images_rc
