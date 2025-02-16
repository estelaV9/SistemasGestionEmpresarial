package com.example.cubexshop.fragment

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.example.cubexshop.R
import com.example.cubexshop.model.CartItem
import com.example.cubexshop.utils.CartManager

class CheckoutFragment(private val cartItems: MutableList<CartItem>) :
    Fragment(R.layout.fragment_pago) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val payButton: Button = view.findViewById(R.id.payButton)
        var totalPrice = 0.0 // VARIABLE PARA ALMACENAR EL PRECIO TOTAL DE LA COMPRA

        // STRINGBUILDER PARA MOSTRAR LOS DETALLES DE LA COMPRA
        val cartDetails = StringBuilder("Resumen de la compra:\n")

        /*for (item in cartItems) {
            val itemTotalPrice = item.cube.price * item.quantity
            cartDetails.append("${item.cube.name}: ${item.quantity} x \$${item.cube.price} = \$${itemTotalPrice}\n")
            totalPrice += itemTotalPrice
        }*/

        // AGREGA EL TOTAL DE LA COMPRA AL RESUMEN
        cartDetails.append("\nTotal: \$${totalPrice}")
        //cartSummaryText.text = cartDetails.toString() // AQUÍ SE MOSTRARIA EL RESUMEN EN UN COMPONENTE (ACTUALMENTE ESTA COMENTADO)

        // CUANDO PULSA EL BOTON DE PAGO
        payButton.setOnClickListener {
            // PROCESO DE PAGO, MUESTRA UN MENSAJE DE COMPRA EXITOSA
            Toast.makeText(requireContext(), "Compra realizada con éxito", Toast.LENGTH_SHORT)
                .show()

            // VACIA EL CARRITO DE COMPRAS AL COMPLETAR LA COMPRA
            CartManager.cartItems.clear()

            // VUELVE AL FRAGMENT ANTERIOR (DESPARECE EL FRAGMENTO ACTUAL DE PAGO)
            requireActivity().supportFragmentManager.popBackStack()
        }
    }
}
