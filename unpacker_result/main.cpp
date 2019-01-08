#include "qmwroot.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QMWRoot w;
    w.show();

    return a.exec();
}
