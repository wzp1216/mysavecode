#include <QtGui>
#include <QAction>

#include "mainwindow.h"
#include "finddlg.h"
#include "gotocelldlg.h"
#include "sortdlg.h"
#include "spreadsheet.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    spreadsheet=new Spreadsheet;
    setCentralWidget(spreadsheet);
    
    createActions();
    createMenus();
    createContextMenu();
    createToolBars();
    createStatusBar();
    
    readSettings();
    finddlg=0;
    setWindowIcon(QIcon(":/images/icon.png"));
    setCurrentFile("");
}

void MainWindow::createActions(){
    newAction= new QAction(tr("&New"),this);
    newAction->setIcon(QIcon(":/images/new.png"));
    newAction->setShortcut(QKeySequence::New);
    newAction->setStatusTip(tr("Create a new spreadsheet file"));
    connect(newAction,SIGNAL(triggered()),this,SLOT(newFile()));


    for(int i=0;i<MaxRecentFiles;++i){
        recentFileActions[i]=new QAction(this);
        recentFileActions[i]->setVisible(false);
        connect(recentFileActions[i],SIGNAL(triggered()),
                this,SLOT(openRecentFile()));
    }

    exitAction= new QAction(tr("E&xit"),this);
    exitAction->setShortcut(tr("Ctrl+Q"));
    exitAction->setStatusTip(tr("Exit the application"));
    connect(exitAction,SIGNAL(triggered()),this,SLOT(close()));




    aboutQtAction =new QAction(tr("About &Qt"),this);
    aboutQtAction->setStatusTip(tr("Show the Qt About windows!"));
    connect(aboutQtAction,SIGNAL(triggered()),qApp,SLOT(aboutQt()));



}

MainWindow::~MainWindow()
{
    
}
