#include "temperture.h"
#include "ui_temperture.h"

temperture::temperture(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::temperture)
{
    ui->setupUi(this);
}

temperture::~temperture()
{
    delete ui;
}

void temperture::on_lineEdit_editingFinished()
{
    double C=ui->lineEdit->text().toDouble();
    double K=0,F=0;
    if(C>=-273.15)
    {
        F=1.8*C+32;
        K=C+273.15;
        QString Fn=QString::number(F,'f',2);
        QString Kn=QString::number(K,'f',2);
        ui->lineEdit_2->setText(Fn);
        ui->lineEdit_3->setText(Kn);
    }
    else
    {
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_3->setText("Error");
    }
}

void temperture::on_lineEdit_2_editingFinished()
{
    double F=ui->lineEdit_2->text().toDouble();
    double K=0,C=0;
    if(F>=-459.67)
    {
        C=(F-32)/1.8;
        K=C+273.15;
        QString Cn=QString::number(C,'f',2);
        QString Kn=QString::number(K,'f',2);
        ui->lineEdit->setText(Cn);
        ui->lineEdit_3->setText(Kn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_3->setText("Error");
    }
}

void temperture::on_lineEdit_3_editingFinished()
{
    double K=ui->lineEdit_3->text().toDouble();
    double F=0,C=0;
    if(K>=0)
    {
        F=K-459.67;
        C=K-273.15;
        QString Cn=QString::number(C,'f',2);
        QString Fn=QString::number(F,'f',2);
        ui->lineEdit->setText(Cn);
        ui->lineEdit_2->setText(Fn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_2->setText("Error");
    }
}
