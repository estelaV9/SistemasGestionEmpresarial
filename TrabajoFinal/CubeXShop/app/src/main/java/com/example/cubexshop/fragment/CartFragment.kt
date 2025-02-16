package com.example.cubexshop.fragment

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.cubexshop.R
import com.example.cubexshop.adapter.CartAdapter
import com.example.cubexshop.utils.CartManager

class CartFragment : Fragment(R.layout.fragment_cart) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // OBTIENE EL RECYCLER VIEW PARA MOSTRAR LOS ARTICULOS EN EL CARRITO
        val recyclerView: RecyclerView = view.findViewById(R.id.cartRecyclerView)
        // CONFIGURA EL LAYOUT MANAGER PARA EL RECYCLER VIEW
        recyclerView.layoutManager = LinearLayoutManager(requireContext())
        val cartAdapter = CartAdapter(CartManager.cartItems)
        recyclerView.adapter = cartAdapter

        val checkoutButton: Button = view.findViewById(R.id.checkoutButton)

        // CUANDO S EPULSA EL BOTON DE CHECKOUT
        checkoutButton.setOnClickListener {
            if (CartManager.cartItems.isNotEmpty()) {
                // SI EL CARRITO TIENE ITEMS, CARGA EL FRAGMENTO DE PAGO
                val checkoutFragment = CheckoutFragment(CartManager.cartItems)
                requireActivity().supportFragmentManager.beginTransaction()
                    .replace(R.id.fragmentContainer, checkoutFragment) // REEMPLAZA EL FRAGMENT ACTUAL POR EL DE PAGO
                    .addToBackStack(null) // AGREGA EL FRAGMENT AL BACKSTACK PARA QUE SE PUEDA NAVEGAR ATRAS
                    .commit()
            } else {
                // SI EL CARRITO ESTA VACIO, MUESTRA UN MENSAJE AL USUARIO
                Toast.makeText(requireContext(), "El carrito está vacío", Toast.LENGTH_SHORT).show()
            } // VERIFICA SI EL CARRITO NO ESTA VACIO
        }
    }
}
