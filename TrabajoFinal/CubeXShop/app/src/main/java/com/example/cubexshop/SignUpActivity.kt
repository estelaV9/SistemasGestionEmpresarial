package com.example.cubexshop

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.util.Patterns
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import com.example.cubexshop.dao.UserDAO
import com.example.cubexshop.database.DatabaseHelper
import com.example.cubexshop.databinding.ActivitySignupBinding
import com.example.cubexshop.model.User
import java.time.LocalDate

class SignUpActivity : AppCompatActivity() {
    lateinit var miBinding: ActivitySignupBinding
    private lateinit var userDAO: UserDAO

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        miBinding = ActivitySignupBinding.inflate(layoutInflater)
        setContentView(miBinding.root)

        userDAO = UserDAO(this) // SE INCIALIZA EL DAO

        miBinding.LoginTV.setOnClickListener {
            // CREA UN INTENT PARA ABRIR EL LoginActivity
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)
        } // SI YA TIENE CUENTA, SE VA A LA PANTALLA DEL LOGIN

        miBinding.signupBtt.setOnClickListener {
            // VALIDAR CADA CAMPO Y MOSTRAR MENSAJES DE ERROR EN LOS TextView CORRESPONDIENTES
            val emailIsValid = validateEmail()
            val passwordIsValid = validatePassword()
            val confirmPasswordIsValid = validateConfirmPassword()
            val nameIsValid = validateName()

            /*** falta validar el campo nombre porque sera unico ***/

            // SI NO SON VALIDOS, SE MUESTRA MENSAJE DE ERROR, SINO SE LIMPIA EL ERROR
            miBinding.messageErrorNameTV.text =
                if (!nameIsValid) validateNameMessage() else ""

            miBinding.messageErrorMailTV.text =
                if (!emailIsValid) validateEmailMessage() else ""

            miBinding.messageErrorPassTV.text =
                if (!passwordIsValid) validatePasswordMessage() else ""

            miBinding.messageErrorConfirmPassTV.text =
                if (!confirmPasswordIsValid) validateConfirmPasswordMessage() else ""

            if (validateName() && validatePassword() && validateConfirmPassword() && validateEmail()) {
                val user = User(
                    idUser = null,
                    name = miBinding.nameET.text.toString(),
                    email = miBinding.emailET.text.toString(),
                    password = miBinding.passwordET.text.toString(),
                    registrationDate = LocalDate.now()
                ) // CREAR EL USUARIO

                val userId = userDAO.addUser(user) // GUARDAMOS EN LA BASE DE DATOS

                if (userId != -1L) {
                    Toast.makeText(this, "Usuario creado con exito",
                        Toast.LENGTH_SHORT).show()
                    /**** ir a la pagina principal ***/
                } else {
                    Toast.makeText(this, "Error al crear el usuario",
                        Toast.LENGTH_SHORT).show()
                } // MOSTRAMOS UN TOAST DEPENDIENDO SI SE GUARDO BIEN
            } // SI TODOS LOS CAMPOS SON CORRECTOS, LO GUARDAMOS EN LA BD

        } // CUANDO PULSE EL BOTON DE SIGNUP, SE VALIDARAN LOS CAMPOS
    }


    private fun validateName(): Boolean {
        val value = miBinding.nameET.text.toString()
        return !value.isEmpty()
    } // METODO PARA VALIDAR QUE EL NOMBRE ES VALIDO

    private fun validateNameMessage(): String {
        val value = miBinding.nameET.text.toString()
        return when {
            value.isEmpty() -> "Name is required"
            else -> ""
        }
    } // DEVUELVE EL MENSAJE DE ERROR SEGUN LA VALIDACION DEL NOMBRE


    private fun validateEmail(): Boolean {
        val value = miBinding.emailET.text.toString()
        return !value.isEmpty() && Patterns.EMAIL_ADDRESS.matcher(value).matches()
    } // METODO PARA VALIDAR QUE EL MAIL ES VALIDO

    private fun validateEmailMessage(): String {
        val value = miBinding.emailET.text.toString()
        return when {
            value.isEmpty() -> "Email is required"
            !Patterns.EMAIL_ADDRESS.matcher(value).matches() -> "Email address is invalid"
            else -> ""
        }
    } // DEVUELVE EL MENSAJE DE ERROR SEGUN LA VALIDACION DEL MAIL


    private fun validatePassword(): Boolean {
        val value = miBinding.passwordET.text.toString()
        return !value.isEmpty() && value.length >= 6
    } // METODO PARA VALIDAR QUE LA CONTRASEÑA ES VALIDA

    private fun validatePasswordMessage(): String {
        val value = miBinding.passwordET.text.toString()
        return when {
            value.isEmpty() -> "Password is required"
            value.length < 6 -> "Password must be at least 6 characters long"
            else -> ""
        }
    } // DEVUELVE EL MENSAJE DE ERROR SEGUN LA VALIDACION DE LA CONTRASEÑA


    private fun validateConfirmPassword(): Boolean {
        val password = miBinding.passwordET.text.toString()
        val confirmPassword = miBinding.confirmPassET.text.toString()
        return confirmPassword.isNotEmpty() && confirmPassword == password
    } // METODO PARA VALIDAR LA CONFIRMACION DE LA CONTRASEÑA

    private fun validateConfirmPasswordMessage(): String {
        val password = miBinding.passwordET.text.toString()
        val confirmPassword = miBinding.confirmPassET.text.toString()
        return when {
            confirmPassword.isEmpty() -> "Confirm password is required"
            confirmPassword != password -> "Passwords do not match"
            else -> ""
        }
    } // DEVUELVE EL MENSAJE DE ERROR SEGUN LA VALIDACION DE LA CONFIRMACION DE LA CONTRASEÑA
}