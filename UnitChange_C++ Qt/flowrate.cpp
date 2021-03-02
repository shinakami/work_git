#include "flowrate.h"
#include "ui_flowrate.h"

flowrate::flowrate(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::flowrate)
{
    ui->setupUi(this);
}

flowrate::~flowrate()
{
    delete ui;
}

double flowrate::on_lineEdit_editingFinished()
{
    double Density=ui->lineEdit->text().toDouble();
    return Density;
}

void flowrate::on_lineEdit_2_editingFinished()
{
    double density = on_lineEdit_editingFinished();
    double Mr=0;
    double Vr=ui->lineEdit_2->text().toDouble();
    if(density>0)
    {
        Mr = density*Vr;
        QString Mrn = QString::number(Mr,'f',2);
        ui->lineEdit_3->setText(Mrn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_3->setText("Error");
    }
}

void flowrate::on_lineEdit_3_editingFinished()
{
    double density = on_lineEdit_editingFinished();
    double Vr=0;
    double Mr=ui->lineEdit_3->text().toDouble();
    if(density>0)
    {
        Vr = Mr/density;
        QString Vrn = QString::number(Vr,'f',2);
        ui->lineEdit_2->setText(Vrn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_3->setText("Error");
    }
}


