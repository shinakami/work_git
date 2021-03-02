/****************************************************************************
** Meta object code from reading C++ file 'mainwindow.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.11.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../CSVcreator/mainwindow.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'mainwindow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.11.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_MainWindow_t {
    QByteArrayData data[19];
    char stringdata0[465];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_MainWindow_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_MainWindow_t qt_meta_stringdata_MainWindow = {
    {
QT_MOC_LITERAL(0, 0, 10), // "MainWindow"
QT_MOC_LITERAL(1, 11, 23), // "on_actionopen_triggered"
QT_MOC_LITERAL(2, 35, 0), // ""
QT_MOC_LITERAL(3, 36, 25), // "on_actionopen_2_triggered"
QT_MOC_LITERAL(4, 62, 23), // "on_actionsave_triggered"
QT_MOC_LITERAL(5, 86, 25), // "on_actiondelete_triggered"
QT_MOC_LITERAL(6, 112, 22), // "on_actionadd_triggered"
QT_MOC_LITERAL(7, 135, 22), // "on_action3X3_triggered"
QT_MOC_LITERAL(8, 158, 22), // "on_action4X4_triggered"
QT_MOC_LITERAL(9, 181, 22), // "on_actionrow_triggered"
QT_MOC_LITERAL(10, 204, 25), // "on_actioncolumn_triggered"
QT_MOC_LITERAL(11, 230, 27), // "on_actionoverload_triggered"
QT_MOC_LITERAL(12, 258, 25), // "on_actionmanual_triggered"
QT_MOC_LITERAL(13, 284, 25), // "on_actionchange_triggered"
QT_MOC_LITERAL(14, 310, 28), // "on_actionopenExcel_triggered"
QT_MOC_LITERAL(15, 339, 29), // "on_actionremove_row_triggered"
QT_MOC_LITERAL(16, 369, 32), // "on_actionremove_column_triggered"
QT_MOC_LITERAL(17, 402, 33), // "on_actionclear_all_data_trigg..."
QT_MOC_LITERAL(18, 436, 28) // "on_actionTWD97_WGS_triggered"

    },
    "MainWindow\0on_actionopen_triggered\0\0"
    "on_actionopen_2_triggered\0"
    "on_actionsave_triggered\0"
    "on_actiondelete_triggered\0"
    "on_actionadd_triggered\0on_action3X3_triggered\0"
    "on_action4X4_triggered\0on_actionrow_triggered\0"
    "on_actioncolumn_triggered\0"
    "on_actionoverload_triggered\0"
    "on_actionmanual_triggered\0"
    "on_actionchange_triggered\0"
    "on_actionopenExcel_triggered\0"
    "on_actionremove_row_triggered\0"
    "on_actionremove_column_triggered\0"
    "on_actionclear_all_data_triggered\0"
    "on_actionTWD97_WGS_triggered"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_MainWindow[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
      17,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    0,   99,    2, 0x08 /* Private */,
       3,    0,  100,    2, 0x08 /* Private */,
       4,    0,  101,    2, 0x08 /* Private */,
       5,    0,  102,    2, 0x08 /* Private */,
       6,    0,  103,    2, 0x08 /* Private */,
       7,    0,  104,    2, 0x08 /* Private */,
       8,    0,  105,    2, 0x08 /* Private */,
       9,    0,  106,    2, 0x08 /* Private */,
      10,    0,  107,    2, 0x08 /* Private */,
      11,    0,  108,    2, 0x08 /* Private */,
      12,    0,  109,    2, 0x08 /* Private */,
      13,    0,  110,    2, 0x08 /* Private */,
      14,    0,  111,    2, 0x08 /* Private */,
      15,    0,  112,    2, 0x08 /* Private */,
      16,    0,  113,    2, 0x08 /* Private */,
      17,    0,  114,    2, 0x08 /* Private */,
      18,    0,  115,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        MainWindow *_t = static_cast<MainWindow *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->on_actionopen_triggered(); break;
        case 1: _t->on_actionopen_2_triggered(); break;
        case 2: _t->on_actionsave_triggered(); break;
        case 3: _t->on_actiondelete_triggered(); break;
        case 4: _t->on_actionadd_triggered(); break;
        case 5: _t->on_action3X3_triggered(); break;
        case 6: _t->on_action4X4_triggered(); break;
        case 7: _t->on_actionrow_triggered(); break;
        case 8: _t->on_actioncolumn_triggered(); break;
        case 9: _t->on_actionoverload_triggered(); break;
        case 10: _t->on_actionmanual_triggered(); break;
        case 11: _t->on_actionchange_triggered(); break;
        case 12: _t->on_actionopenExcel_triggered(); break;
        case 13: _t->on_actionremove_row_triggered(); break;
        case 14: _t->on_actionremove_column_triggered(); break;
        case 15: _t->on_actionclear_all_data_triggered(); break;
        case 16: _t->on_actionTWD97_WGS_triggered(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

QT_INIT_METAOBJECT const QMetaObject MainWindow::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_MainWindow.data,
      qt_meta_data_MainWindow,  qt_static_metacall, nullptr, nullptr}
};


const QMetaObject *MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_MainWindow.stringdata0))
        return static_cast<void*>(this);
    return QMainWindow::qt_metacast(_clname);
}

int MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 17)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 17;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 17)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 17;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
