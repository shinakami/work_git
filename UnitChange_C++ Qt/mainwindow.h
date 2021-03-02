#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "temperture.h"
#include "mass.h"
#include "flowrate.h"
#include "length.h"
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_4_clicked();

private:
    Ui::MainWindow *ui;
    temperture *T_change;
    mass *M_change;
    flowrate *F_change;
    length *L_change;
};

#endif // MAINWINDOW_H
