package com.example.cubexshop

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
    }
}