package com.example.cubexshop

import android.content.Intent
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.cubexshop.database.DatabaseHelper
import com.example.cubexshop.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    lateinit var miBinding: ActivityMainBinding
    private lateinit var dbHelper: DatabaseHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        miBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(miBinding.root)

        dbHelper = DatabaseHelper(this) // SE INICIALIZA EL HELPER

        miBinding.startBtt.setOnClickListener {
            // CREA UN INTENT PARA ABRIR EL LoginActivity
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)  // LO ABRE
        } // CUANDO PULSE EL BOTON START, ABRIRA LA VENTANA DE LOGIN
    }
}