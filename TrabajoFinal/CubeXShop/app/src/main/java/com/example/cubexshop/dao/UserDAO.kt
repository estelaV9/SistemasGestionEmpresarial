package com.example.cubexshop.dao

import android.annotation.SuppressLint
import android.content.Context
import android.os.Build
import androidx.annotation.RequiresApi
import com.example.cubexshop.database.DatabaseHelper
import com.example.cubexshop.model.User
import java.time.LocalDate
import java.time.format.DateTimeFormatter

class UserDAO(private val context: Context) {
    private val dbHelper = DatabaseHelper(context)

    fun addUser(user: User): Long {
        val db = dbHelper.writableDatabase // BASE DE DATOS EN MODO ESCRITURA
        val values = android.content.ContentValues()

        // AGREGAMOS VALORES A LA BASE DE DATOS
        values.put("username", user.name)
        values.put("mail", user.email)
        values.put("password_user", user.password)
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
            "mail = ? AND password_user = ?",
            arrayOf(email, password),
            null, null, null
        ) // CONSULTA PARA OBTENER EL USUARIO POR CORREO Y CONTRASEÑA

        var user: User? = null // USUARIO PARA ALMACENAR EL REGISTRO
        if (cursor.moveToFirst()) {
            val id = cursor.getInt(cursor.getColumnIndexOrThrow("user_id"))
            val name = cursor.getString(cursor.getColumnIndexOrThrow("username"))
            val registrationDate = LocalDate.parse(
                cursor.getString(cursor.getColumnIndexOrThrow("registration_date")),
                DateTimeFormatter.ISO_DATE
            )
            user = User(id, name, email, password, registrationDate) // CREA EL OBJETO DEVUELTO
        } // SI ENCUENTRA UN RESULTADO
        cursor.close() // CIERRA EL CURSOR
        return user // DEVUELVE SI EXISTE EL USUARIO O NO
    } // METODO PARA BUSCAR UN USUARIO POR MAIL Y CONTRASEÑA

    fun updateUser(user: User): Int {
        val db = dbHelper.writableDatabase
        val values = android.content.ContentValues()

        // SE AGREGAN LOS VALORES A ACTUALIZAR
        values.put("username", user.name)
        values.put("password_user", user.password)
        if (!user.profileImage.isNullOrEmpty()) {
            // SE AGREGA IMAGEN
            values.put("profile_image", user.profileImage)
        }

        // SE EJECUTA LA ACTUALIZACION FILTRANDO POR CORREO
        return db.update("users", values, "mail = ?", arrayOf(user.email))
    } // METODO PARA ACUTLAIZAR LOS DATOS DEL USUARIO

    @SuppressLint("NewApi")
    fun getLoggedUser(): User? {
        // OBTIENE LAS PREFERENCIAS COMPARTIDAS PARA OBTENER LOS DATOS DEL USUARIO
        val sharedPreferences = context.getSharedPreferences("UserPrefs", Context.MODE_PRIVATE)

        val email = sharedPreferences.getString("user_email", null)
        val password = sharedPreferences.getString("user_password", null)
        val idUser = sharedPreferences.getInt("user_id", -1)
        val name = sharedPreferences.getString("user_name", null)
        val profileImage = sharedPreferences.getString("user_profile_image", null)

        return if (email != null && password != null && name != null) {
            // SI NO SON NULOS, CREA UN OBJETO USER
            User(idUser, name, email, password, LocalDate.now(), profileImage)
        } else {
            // SINO RETONA NULL
            null
        } // VERIFICA SI TODOS LOS DATOS SON NULOS O NO
    } // METODO PARA CONSEGUIR LOS DATOS DEL USUARIO

    fun deleteUser(email: String): Int {
        // OBTIENE UNA REFERENCIA A LA BASE DE DATOS EN MODO ESCRITURA
        val db = dbHelper.writableDatabase
        // ELIMINA SEGUN EL MAIL
        return db.delete("users", "mail = ?", arrayOf(email))
    } // METODO PARA ELIMINAR EL USUARIO
}