#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include "temperture.h"
#include "mass.h"
#include "flowrate.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPixmap pix("C:/Users/椎名神鬱/Desktop/unit");
    ui->label->setPixmap(pix);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    QMessageBox::information(this,"說明","從介面上選擇任意物理量做單位換算=w=");
}

void MainWindow::on_pushButton_3_clicked()
{
  //  temperture T_change;
  //  T_change.setModal(true);
  //  T_change.exec();
    T_change = new temperture(this);
    T_change->setWindowTitle("溫度轉換器");
    T_change->show();
}

void MainWindow::on_pushButton_5_clicked()
{
    M_change = new mass(this);
    M_change->setWindowTitle("質量轉換器");
    M_change->show();

}

void MainWindow::on_pushButton_2_clicked()
{
    F_change = new flowrate(this);
    F_change->setWindowTitle("流率轉換器");
    F_change->show();

}

void MainWindow::on_pushButton_4_clicked()
{
    L_change = new length(this);
    L_change->setWindowTitle("長度轉換器");
    L_change->show();
}
