#include "mass.h"
#include "ui_mass.h"

mass::mass(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::mass)
{
    ui->setupUi(this);
}

mass::~mass()
{
    delete ui;
}

void mass::on_lineEdit_editingFinished()
{
    double g=ui->lineEdit->text().toDouble();
    double kg=0,mg=0,oz=0,pound=0;
    if(g>=0)
    {
        kg=g*0.001;
        mg=g*1000;
        oz=g*(0.035274);
        pound=g*(0.002204622);
        QString kgn=QString::number(kg,'f',3);
        QString mgn=QString::number(mg,'f',3);
        QString ozn=QString::number(oz,'f',3);
        QString poundn=QString::number(pound,'f',3);
        ui->lineEdit_2->setText(kgn);
        ui->lineEdit_3->setText(mgn);
        ui->lineEdit_4->setText(ozn);
        ui->lineEdit_5->setText(poundn);
    }
    else
    {
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_3->setText("Error");
        ui->lineEdit_4->setText("Error");
        ui->lineEdit_5->setText("Error");
    }
}

void mass::on_lineEdit_2_editingFinished()
{
    double kg=ui->lineEdit_2->text().toDouble();
    double g=0,mg=0,oz=0,pound=0;
    if(kg>=0)
    {
        g=kg*1000;
        mg=kg*1000000;
        oz=g*(0.035274);
        pound=g*(0.002204622);
        QString gn=QString::number(g,'f',3);
        QString mgn=QString::number(mg,'f',3);
        QString ozn=QString::number(oz,'f',3);
        QString poundn=QString::number(pound,'f',3);
        ui->lineEdit->setText(gn);
        ui->lineEdit_3->setText(mgn);
        ui->lineEdit_4->setText(ozn);
        ui->lineEdit_5->setText(poundn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_3->setText("Error");
        ui->lineEdit_4->setText("Error");
        ui->lineEdit_5->setText("Error");
    }
}

void mass::on_lineEdit_3_editingFinished()
{
    double mg=ui->lineEdit_3->text().toDouble();
    double g=0,kg=0,oz=0,pound=0;
    if(mg>=0)
    {
        g=mg*0.001;
        kg=mg*0.000001;
        oz=g*(0.035274);
        pound=g*(0.002204622);
        QString gn=QString::number(g,'f',3);
        QString kgn=QString::number(kg,'f',3);
        QString ozn=QString::number(oz,'f',3);
        QString poundn=QString::number(pound,'f',3);
        ui->lineEdit->setText(gn);
        ui->lineEdit_2->setText(kgn);
        ui->lineEdit_4->setText(ozn);
        ui->lineEdit_5->setText(poundn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_4->setText("Error");
        ui->lineEdit_5->setText("Error");
    }
}

void mass::on_lineEdit_4_editingFinished()
{

    double oz=ui->lineEdit_4->text().toDouble();
    double g=0,kg=0,mg=0,pound=0;
    if(oz>=0)
    {
        g=oz/(0.035274);
        kg=g*0.001;
        mg=g*1000;
        pound=g*(0.002204622);
        QString gn=QString::number(g,'f',3);
        QString kgn=QString::number(kg,'f',3);
        QString mgn=QString::number(mg,'f',3);
        QString poundn=QString::number(pound,'f',3);
        ui->lineEdit->setText(gn);
        ui->lineEdit_2->setText(kgn);
        ui->lineEdit_3->setText(mgn);
        ui->lineEdit_5->setText(poundn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_3->setText("Error");
        ui->lineEdit_5->setText("Error");
    }
}

void mass::on_lineEdit_5_editingFinished()
{
    double pound=ui->lineEdit_5->text().toDouble();
    double g=0,kg=0,oz=0,mg=0;
    if(pound>=0)
    {
        g=pound/(1/0.002204622);
        mg=g*1000;
        kg=mg*0.000001;
        oz=g*(1/0.035274);
        QString gn=QString::number(g,'f',3);
        QString kgn=QString::number(kg,'f',3);
        QString ozn=QString::number(oz,'f',3);
        QString mgn=QString::number(mg,'f',3);
        ui->lineEdit->setText(gn);
        ui->lineEdit_2->setText(kgn);
        ui->lineEdit_4->setText(ozn);
        ui->lineEdit_3->setText(mgn);
    }
    else
    {
        ui->lineEdit->setText("Error");
        ui->lineEdit_2->setText("Error");
        ui->lineEdit_4->setText("Error");
        ui->lineEdit_3->setText("Error");
    }
}
