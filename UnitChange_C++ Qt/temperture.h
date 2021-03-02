#ifndef TEMPERTURE_H
#define TEMPERTURE_H

#include <QDialog>

namespace Ui {
class temperture;
}

class temperture : public QDialog
{
    Q_OBJECT

public:
    explicit temperture(QWidget *parent = 0);
    ~temperture();

private slots:
    void on_lineEdit_editingFinished();

    void on_lineEdit_2_editingFinished();

    void on_lineEdit_3_editingFinished();

private:
    Ui::temperture *ui;
};

#endif // TEMPERTURE_H
