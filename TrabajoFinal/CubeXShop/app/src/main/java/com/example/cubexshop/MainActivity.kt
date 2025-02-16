package com.example.cubexshop

import android.content.Intent
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import com.example.cubexshop.activity.LoginActivity
import com.example.cubexshop.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var miBinding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        miBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(miBinding.root)

        miBinding.startBtt.setOnClickListener {
            // CREA UN INTENT PARA ABRIR EL LoginActivity
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)  // LO ABRE
        } // CUANDO PULSE EL BOTON START, ABRIRA LA VENTANA DE LOGIN
    }
}