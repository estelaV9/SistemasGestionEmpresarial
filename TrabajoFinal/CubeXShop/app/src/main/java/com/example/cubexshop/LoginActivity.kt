package com.example.cubexshop

import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import com.example.cubexshop.dao.UserDAO
import com.example.cubexshop.databinding.ActivityLoginBinding

class LoginActivity : AppCompatActivity() {
    lateinit var miBinding: ActivityLoginBinding
    private lateinit var userDAO: UserDAO

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        miBinding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(miBinding.root)

        userDAO = UserDAO(this) // SE INICIALIZA EL USERDAO

        miBinding.SignUpTV.setOnClickListener {
            // CREA UN INTENT PARA ABRIR EL SignUpActivity
            val intent = Intent(this, SignUpActivity::class.java)
            startActivity(intent)
        } // SI NO TIENE CUENTA, SE VA A LA PANTALLA DEL SIGNUP

        miBinding.loginBtt.setOnClickListener {
            val user = userDAO.loginUser(
                miBinding.emailET.text.toString(),
                miBinding.passwordET.text.toString()
            ) // VERIFICA EL LOGIN

            if (user != null) {
                Toast.makeText(this, "¡Welcome, ${user.name}!",
                    Toast.LENGTH_SHORT).show()

                // NAVEGAR A LA SIGUIENTE PANTALLA
                val intent = Intent(this, HomePageActivity::class.java)
                startActivity(intent)
                finish()
            } else {
                Toast.makeText(this, "User o password incorrect",
                    Toast.LENGTH_SHORT).show()
            } // SI EL USUARIO NO ES NULO Y EXISTE, NAVEGARA A LA PAGINA PRINCIPAL
        } // SI PULSA EL BOTON DEL LOGIN
    }
}