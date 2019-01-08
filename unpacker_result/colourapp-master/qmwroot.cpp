#include "qmwroot.h"
#include "ui_qmwroot.h"

QMWRoot::QMWRoot(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QMWRoot)
{
    ui->setupUi(this);
}

QMWRoot::~QMWRoot()
{
    delete ui;
}
