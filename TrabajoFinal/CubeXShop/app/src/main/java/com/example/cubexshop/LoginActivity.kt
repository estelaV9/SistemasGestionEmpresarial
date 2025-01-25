package com.example.cubexshop

import android.content.Intent
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import com.example.cubexshop.databinding.ActivityLoginBinding

class LoginActivity : AppCompatActivity() {
    lateinit var miBinding: ActivityLoginBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        miBinding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(miBinding.root)
        
        miBinding.SignUpTV.setOnClickListener{
            // CREA UN INTENT PARA ABRIR EL SignUpActivity
            val intent = Intent(this, SignUpActivity::class.java)
            startActivity(intent)
        } // SI NO TIENE CUENTA, SE VA A LA PANTALLA DEL SIGNUP
    }
}