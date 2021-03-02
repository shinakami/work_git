#ifndef MASS_H
#define MASS_H

#include <QDialog>

namespace Ui {
class mass;
}

class mass : public QDialog
{
    Q_OBJECT

public:
    explicit mass(QWidget *parent = 0);
    ~mass();

private slots:
    void on_lineEdit_editingFinished();

    void on_lineEdit_3_editingFinished();

    void on_lineEdit_2_editingFinished();

    void on_lineEdit_4_editingFinished();

    void on_lineEdit_5_editingFinished();

private:
    Ui::mass *ui;
};

#endif // MASS_H
