package com.example.cubexshop.dao

import android.content.Context
import android.os.Build
import androidx.annotation.RequiresApi
import com.example.cubexshop.database.DatabaseHelper
import com.example.cubexshop.model.User
import java.time.LocalDate
import java.time.format.DateTimeFormatter

class UserDAO(context: Context) {
    private val dbHelper = DatabaseHelper(context)

    fun addUser(user: User): Long {
        val db = dbHelper.writableDatabase // BASE DE DATOS EN MODO ESCRITURA
        val values = android.content.ContentValues()

        // AGREGAMOS VALORES A LA BASE DE DATOS
        values.put("username", user.name)
        values.put("mail", user.email)
        values.put("password", user.password)
        values.put("registration_date", user.registrationDate.toString())

        // SE INSERTA EL USUARIO
        return db.insert("users", null, values) // DEVUELVE EL ID DEL REGISTRO INSERTADO
        //db.close()
    } // METODO PARA AÑADIR NUEVO USUARIO

    @RequiresApi(Build.VERSION_CODES.O)
    fun loginUser(email: String, password: String): User? {
        val db = dbHelper.readableDatabase // BASE DE DATOS EN MODO LECTURA
        val cursor = db.query(
            "users", null,
            "mail = ? AND password = ?",
            arrayOf(email, password),
            null, null, null
        ) // CONSULTA PARA OBTENER EL USUARIO POR CORREO Y CONTRASEÑA

        var user: User? = null // USUARIO PARA ALMACENAR EL REGISTRO
        if (cursor.moveToFirst()) {
            val id = cursor.getInt(cursor.getColumnIndexOrThrow("user_id"))
            val name = cursor.getString(cursor.getColumnIndexOrThrow("username"))
            val registrationDate = LocalDate.parse(
                cursor.getString(cursor.getColumnIndexOrThrow("registration_Date")),
                DateTimeFormatter.ISO_DATE
            )
            user = User(id, name, email, password, registrationDate) // CREA EL OBJETO DEVUELTO
        } // SI ENCUENTRA UN RESULTADO
        cursor.close() // CIERRA EL CURSOR
        return user // DEVUELVE SI EXISTE EL USUARIO O NO
    } // METODO PARA BUSCAR UN USUARIO POR MAIL Y CONTRASEÑA
}
