package com.example.cubexshop

import android.os.Bundle
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.drawerlayout.widget.DrawerLayout
import com.example.cubexshop.databinding.ActivityHomePageBinding
import com.example.cubexshop.databinding.ActivityLoginBinding
import com.google.android.material.navigation.NavigationView

class HomePageActivity : AppCompatActivity() {
    private lateinit var drawerLayout: DrawerLayout
    lateinit var miBinding: ActivityHomePageBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        miBinding = ActivityHomePageBinding.inflate(layoutInflater)
        setContentView(miBinding.root)

        // CONFIGURAR TOOLBAR
        val toolbar: androidx.appcompat.widget.Toolbar = miBinding.myToolbar
        setSupportActionBar(toolbar)

        // CONFIGURAR DRAWER
        drawerLayout = miBinding.drawerLayout
        val navigationView: NavigationView = miBinding.navigationView

        miBinding.menuIcon.setOnClickListener {
            drawerLayout.openDrawer(navigationView)
        } // AÑADIR CLICK AL ICONO DEL MENU

        // ACTUALIZAR EL ENCABEZADO CON DATOS DEL USUARIO
        val headerView = navigationView.getHeaderView(0)
        val userName: TextView = headerView.findViewById(R.id.drawerUserName)
        val userEmail: TextView = headerView.findViewById(R.id.drawerUserEmail)
        userName.text = "Nombre Usuario"
        userEmail.text = "email@ejemplo.com"
    }
}