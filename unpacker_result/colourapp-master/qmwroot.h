#ifndef QMWROOT_H
#define QMWROOT_H

#include <QMainWindow>

namespace Ui {
class QMWRoot;
}

class QMWRoot : public QMainWindow
{
    Q_OBJECT

public:
    explicit QMWRoot(QWidget *parent = nullptr);
    ~QMWRoot();

private:
    Ui::QMWRoot *ui;
};

#endif // QMWROOT_H
