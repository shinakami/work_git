#ifndef LENGTH_H
#define LENGTH_H

#include <QDialog>

namespace Ui {
class length;
}

class length : public QDialog
{
    Q_OBJECT

public:
    explicit length(QWidget *parent = 0);
    ~length();

private slots:
    void on_lineEdit_editingFinished();

private:
    Ui::length *ui;
};

#endif // LENGTH_H
