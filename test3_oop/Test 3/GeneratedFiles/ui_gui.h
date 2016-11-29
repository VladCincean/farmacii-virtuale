/********************************************************************************
** Form generated from reading UI file 'gui.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GUI_H
#define UI_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_GUIClass
{
public:
    QWidget *centralWidget;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout;
    QListWidget *playersListWidget;
    QWidget *formLayoutWidget;
    QFormLayout *formLayout;
    QLabel *nameLabel;
    QLineEdit *nameLineEdit;
    QLabel *nationalityLabel;
    QLineEdit *nationalityLineEdit;
    QLabel *teamLabel;
    QLineEdit *teamLineEdit;
    QLabel *goalsLabel;
    QLineEdit *goalsLineEdit;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QPushButton *sortButton;
    QLabel *label;
    QLineEdit *showByNationalityLineEdit;
    QPushButton *showPlayersButton;
    QLineEdit *numberOfPlayersLineEdit;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *GUIClass)
    {
        if (GUIClass->objectName().isEmpty())
            GUIClass->setObjectName(QStringLiteral("GUIClass"));
        GUIClass->resize(651, 456);
        centralWidget = new QWidget(GUIClass);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        horizontalLayoutWidget = new QWidget(centralWidget);
        horizontalLayoutWidget->setObjectName(QStringLiteral("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(10, 10, 301, 351));
        horizontalLayout = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        playersListWidget = new QListWidget(horizontalLayoutWidget);
        playersListWidget->setObjectName(QStringLiteral("playersListWidget"));

        horizontalLayout->addWidget(playersListWidget);

        formLayoutWidget = new QWidget(centralWidget);
        formLayoutWidget->setObjectName(QStringLiteral("formLayoutWidget"));
        formLayoutWidget->setGeometry(QRect(330, 50, 261, 131));
        formLayout = new QFormLayout(formLayoutWidget);
        formLayout->setSpacing(6);
        formLayout->setContentsMargins(11, 11, 11, 11);
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);
        nameLabel = new QLabel(formLayoutWidget);
        nameLabel->setObjectName(QStringLiteral("nameLabel"));

        formLayout->setWidget(0, QFormLayout::LabelRole, nameLabel);

        nameLineEdit = new QLineEdit(formLayoutWidget);
        nameLineEdit->setObjectName(QStringLiteral("nameLineEdit"));

        formLayout->setWidget(0, QFormLayout::FieldRole, nameLineEdit);

        nationalityLabel = new QLabel(formLayoutWidget);
        nationalityLabel->setObjectName(QStringLiteral("nationalityLabel"));

        formLayout->setWidget(1, QFormLayout::LabelRole, nationalityLabel);

        nationalityLineEdit = new QLineEdit(formLayoutWidget);
        nationalityLineEdit->setObjectName(QStringLiteral("nationalityLineEdit"));

        formLayout->setWidget(1, QFormLayout::FieldRole, nationalityLineEdit);

        teamLabel = new QLabel(formLayoutWidget);
        teamLabel->setObjectName(QStringLiteral("teamLabel"));

        formLayout->setWidget(2, QFormLayout::LabelRole, teamLabel);

        teamLineEdit = new QLineEdit(formLayoutWidget);
        teamLineEdit->setObjectName(QStringLiteral("teamLineEdit"));

        formLayout->setWidget(2, QFormLayout::FieldRole, teamLineEdit);

        goalsLabel = new QLabel(formLayoutWidget);
        goalsLabel->setObjectName(QStringLiteral("goalsLabel"));

        formLayout->setWidget(3, QFormLayout::LabelRole, goalsLabel);

        goalsLineEdit = new QLineEdit(formLayoutWidget);
        goalsLineEdit->setObjectName(QStringLiteral("goalsLineEdit"));

        formLayout->setWidget(3, QFormLayout::FieldRole, goalsLineEdit);

        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QStringLiteral("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(330, 190, 261, 171));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        sortButton = new QPushButton(gridLayoutWidget);
        sortButton->setObjectName(QStringLiteral("sortButton"));

        gridLayout->addWidget(sortButton, 0, 0, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 1, 0, 1, 1);

        showByNationalityLineEdit = new QLineEdit(gridLayoutWidget);
        showByNationalityLineEdit->setObjectName(QStringLiteral("showByNationalityLineEdit"));

        gridLayout->addWidget(showByNationalityLineEdit, 1, 1, 1, 1);

        showPlayersButton = new QPushButton(gridLayoutWidget);
        showPlayersButton->setObjectName(QStringLiteral("showPlayersButton"));

        gridLayout->addWidget(showPlayersButton, 2, 0, 1, 1);

        numberOfPlayersLineEdit = new QLineEdit(gridLayoutWidget);
        numberOfPlayersLineEdit->setObjectName(QStringLiteral("numberOfPlayersLineEdit"));

        gridLayout->addWidget(numberOfPlayersLineEdit, 2, 1, 1, 1);

        GUIClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(GUIClass);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 651, 21));
        GUIClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(GUIClass);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        GUIClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(GUIClass);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        GUIClass->setStatusBar(statusBar);

        retranslateUi(GUIClass);

        QMetaObject::connectSlotsByName(GUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *GUIClass)
    {
        GUIClass->setWindowTitle(QApplication::translate("GUIClass", "GUI", 0));
        nameLabel->setText(QApplication::translate("GUIClass", "Name", 0));
        nationalityLabel->setText(QApplication::translate("GUIClass", "Nationality", 0));
        teamLabel->setText(QApplication::translate("GUIClass", "Team", 0));
        goalsLabel->setText(QApplication::translate("GUIClass", "Goals", 0));
        sortButton->setText(QApplication::translate("GUIClass", "Sort", 0));
        label->setText(QApplication::translate("GUIClass", "Nationality:", 0));
        showPlayersButton->setText(QApplication::translate("GUIClass", "Show players", 0));
    } // retranslateUi

};

namespace Ui {
    class GUIClass: public Ui_GUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GUI_H
