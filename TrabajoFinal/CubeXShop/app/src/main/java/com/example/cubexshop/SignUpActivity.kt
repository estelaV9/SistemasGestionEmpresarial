package com.example.cubexshop

import android.content.Intent
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import com.example.cubexshop.databinding.ActivitySignupBinding

class SignUpActivity : AppCompatActivity() {
    lateinit var miBinding: ActivitySignupBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        miBinding = ActivitySignupBinding.inflate(layoutInflater)
        setContentView(miBinding.root)

        miBinding.LoginTV.setOnClickListener{
            // CREA UN INTENT PARA ABRIR EL LoginActivity
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)
        } // SI YA TIENE CUENTA, SE VA A LA PANTALLA DEL LOGIN
    }
}