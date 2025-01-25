package com.example.cubexshop.database

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper
import android.util.Log

class DatabaseHelper(context: Context) :
    SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {

    companion object {
        const val DATABASE_NAME = "CubeX_ShopDB.db"
        const val DATABASE_VERSION = 1
    } // CAMPOS ESTATICOS

    override fun onCreate(db: SQLiteDatabase?) {
        // TABLA DE USUARIO
        val CREATE_USERS_TABLE = ("CREATE TABLE users ("
                + "user_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                + "username TEXT NOT NULL, "
                + "mail TEXT NOT NULL, "
                + "password_user TEXT NOT NULL, "
                + "registration_date TEXT NOT NULL)"
                )
        db?.execSQL(CREATE_USERS_TABLE) // EJECUTA LA TABLA

        Log.d("DatabaseHelper", "Tabla 'users' creada correctamente.")
    } // METODO PARA GUARDAR EL USUARIO

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        db?.execSQL("DROP TABLE IF EXISTS users") // BORRAR LA TABLA EXISTENTE
        onCreate(db) // VUELVE A CREAR LAS TABLAS
    } // ELIMINA LA TABLA SI EXISTE Y LA VUELVE A CREAR
}
