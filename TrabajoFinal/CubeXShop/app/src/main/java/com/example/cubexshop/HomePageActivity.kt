package com.example.cubexshop

import android.content.Intent
import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentTransaction
import com.example.cubexshop.activity.LoginActivity
import com.example.cubexshop.dao.UserDAO
import com.example.cubexshop.databinding.ActivityHomePageBinding
import com.example.cubexshop.fragment.CartFragment
import com.example.cubexshop.fragment.MarketFragment
import com.example.cubexshop.fragment.ProfileFragment
import com.example.cubexshop.fragment.ShopFragment

class HomePageActivity : AppCompatActivity() {
    private lateinit var binding: ActivityHomePageBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHomePageBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // RECUPERAMOSD LOS DATOS DEL USUARIO DE SHARED PREFERENCES
        val sharedPreferences = getSharedPreferences("UserPrefs", MODE_PRIVATE)
        val userName = sharedPreferences.getString("user_name", "Nombre Usuario")
        val userEmail = sharedPreferences.getString("user_email", "email@ejemplo.com")

        // ESTABLECER EL NOMBRE Y EL CORREO EN EL HEADER DEL NAVIGATION DRAWER
        binding.navigationView.getHeaderView(0).findViewById<TextView>(R.id.drawerUserName).text =
            userName
        binding.navigationView.getHeaderView(0).findViewById<TextView>(R.id.drawerUserEmail).text =
            userEmail

        setSupportActionBar(binding.myToolbar) // ESTABLECEMOS EL TOOLBAR
        loadFragment(ShopFragment()) // CARGAMOS EL FRAGMENT DE SHOP POR DEFECTO

        // CONFIGURAR EL BOTTOMNAVIGATIONVIEW
        binding.navigation.setOnItemSelectedListener { item ->
            when (item.itemId) {
                R.id.home -> loadFragment(ShopFragment())
                R.id.profile -> loadFragment(ProfileFragment())
            }
            true
        }

        binding.menuIcon.setOnClickListener {
            binding.drawerLayout.openDrawer(binding.navigationView) // ABRIR EL DRAWER
        } // ABRIR EL DRAWER AL HACER CLICK AL ICONO

        // CONFIGURACION DE LOS ITEMS DEL DRAWER
        binding.navigationView.setNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_home -> {
                    val intent = Intent(this, HomePageActivity::class.java)
                    startActivity(intent)
                    finish() // CERRAR LA ACTIVIDAD ACTUAL
                }

                R.id.nav_delete_account -> showDeleteAccountDialog() // MOSTRAR DIALOGO PARA ELIMINAR LA CUENTA
                R.id.nav_logout -> logoutUser() // CERRAR SESION DEL USUARIO
            }
            binding.drawerLayout.closeDrawers() // CERRAR EL DRAWER DESPUES DE SELECCIONAR UNA OPCION
            true
        }

        // ACCIONES DE LOS BOTONES EN EL HOME PAGE
        binding.shopButton.setOnClickListener {
            loadFragment(ShopFragment()) // CARGAR SHOP FRAGMENT
        }

        binding.marketButton.setOnClickListener {
            loadFragment(MarketFragment()) // CARGAR MARKET FRAGMENT
        }

        binding.cartIcon.setOnClickListener {
            loadFragment(CartFragment()) // CARGAR CART FRAGMENT
        }
    }


    private fun loadFragment(fragment: Fragment) {
        val fragmentManager: FragmentManager = supportFragmentManager
        val fragmentTransaction: FragmentTransaction = fragmentManager.beginTransaction()
        fragmentTransaction.replace(R.id.fragmentContainer, fragment) // REEMPLAZAR EL FRAGMENT ACTUAL POR EL NUEVO
        fragmentTransaction.addToBackStack(null)
        fragmentTransaction.commit()
    } // METODO PARA CARGAR UN FRAGMENT DADO EN LA VISTA PRINCIPAL


    private fun showDeleteAccountDialog() {
        AlertDialog.Builder(this)
            .setTitle("Eliminar Cuenta") // TITULO DEL DIALOGO
            .setMessage("¿Estás seguro de que deseas eliminar tu cuenta? Esta acción no se puede deshacer.") // MENSAJE DE CONFIRMACION
            .setPositiveButton("Sí, eliminar") { _, _ -> // BOTON DE CONFIRMACION
                deleteAccount() // ELIMINAR LA CUENTA
            }
            .setNegativeButton("Cancelar", null) // BOTON DE CANCELACION
            .show()
    } // METODO PARA MOSTRAR EL DIALOGO DE ELIMINACION DE CUENTA


    private fun deleteAccount() {
        val userDao = UserDAO(this) // OBTENER LA INSTANCIA DE USERDAO
        val user = userDao.getLoggedUser() // OBTENER EL USUARIO LOGUEADO

        if (user != null) {
            val rowsDeleted = userDao.deleteUser(user.email) // ELIMINAR EL USUARIO DE LA BASE DE DATOS
            if (rowsDeleted > 0) {
                Toast.makeText(this, "Cuenta eliminada correctamente", Toast.LENGTH_SHORT).show()

                // REDIRIGIR AL MAINACTIVITY
                val intent = Intent(this, MainActivity::class.java)
                startActivity(intent)
                finish() // CERRAR LA ACTIVIDAD ACTUAL
            } else {
                Toast.makeText(this, "Error al eliminar la cuenta", Toast.LENGTH_SHORT).show()
            }
        }
    } // METODO PARA ELIMINAR LA CUENTA DEL USUARIO


    private fun logoutUser() {
        val intent = Intent(this, LoginActivity::class.java) // INICIAR LA ACTIVIDAD DE LOGIN
        startActivity(intent)
        finish() // CERRAR LA ACTIVIDAD ACTUAL
    } // METODO PARA CERRAR SESION DEL USUARIO
}