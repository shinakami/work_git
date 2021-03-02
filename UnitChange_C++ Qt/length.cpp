#include "length.h"
#include "ui_length.h"

length::length(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::length)
{
    ui->setupUi(this);
}

length::~length()
{
    delete ui;
}

void length::on_lineEdit_editingFinished()
{
    double m=ui->lineEdit->text().toDouble();
    double mm=0,km=0,cm=0,inch=0,feet=0,yd=0;
    mm=m*1000;
    km=m*0.001;
    cm=m*100;


}
