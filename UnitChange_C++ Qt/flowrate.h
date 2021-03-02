#ifndef FLOWRATE_H
#define FLOWRATE_H

#include <QDialog>

namespace Ui {
class flowrate;
}

class flowrate : public QDialog
{
    Q_OBJECT

public:
    explicit flowrate(QWidget *parent = 0);
    ~flowrate();

private slots:
    double on_lineEdit_editingFinished();

    void on_lineEdit_2_editingFinished();

    void on_lineEdit_3_editingFinished();

private:
    Ui::flowrate *ui;
};

#endif // FLOWRATE_H
