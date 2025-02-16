package com.example.cubexshop.fragment

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.NumberPicker
import android.widget.RadioGroup
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.Fragment
import com.example.cubexshop.R
import com.example.cubexshop.model.CartItem
import com.example.cubexshop.model.Cube
import com.example.cubexshop.utils.CartManager


class CubeDetailFragment(private val cube: Cube) : Fragment(R.layout.fragment_cube_details) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        view.findViewById<TextView>(R.id.detailName).text = cube.name
        view.findViewById<TextView>(R.id.detailDescription).text = cube.description
        view.findViewById<ImageView>(R.id.detailImage).setImageResource(cube.imageResId!!)

        // CONFIGURACION DEL NUMBER PICKER PARA LA CANTIDAD
        val quantityPicker: NumberPicker = view.findViewById(R.id.quantityPicker)
        quantityPicker.minValue = 1
        quantityPicker.maxValue = 10

        val radioGroup: RadioGroup = view.findViewById(R.id.radioGroupOptions)

        // CONFIGURACION DEL BOTON AGREGAR AL CARRITO
        view.findViewById<Button>(R.id.addToCartButton).setOnClickListener {
            val quantity = quantityPicker.value // OBTIENE LA CANTIDAD SELECCIONADA
            val selectedType = when (radioGroup.checkedRadioButtonId) { // DETERMINA EL TIPO SELECCIONADO
                R.id.radioStickers -> "Con stickers" // CON STICKERS
                R.id.radioStickerless -> "Stickerless" // SIN STICKERS
                else -> "No especificado" // SI NO SELECCIONADO NINGUNO
            }

            // VERIFICA SI YA HAY UN PRODUCTO IGUAL EN EL CARRITO PARA ACTUALIZAR LA CANTIDAD
            val existingItem =
                CartManager.cartItems.find { it.cube.name == cube.name && it.type == selectedType }
            if (existingItem != null) {
                existingItem.quantity += quantity // ACTUALIZA LA CANTIDAD SI YA EXISTE EN EL CARRITO
            } else {
                CartManager.cartItems.add(
                    CartItem(
                        cube,
                        quantity,
                        selectedType
                    )
                ) // AGREGA EL ITEM AL CARRITO SI NO EXISTE
            }

            // MUESTRA UN MENSAJE DE CONFIRMACION
            Toast.makeText(requireContext(), "Agregado al carrito", Toast.LENGTH_SHORT).show()
        }

        // CONFIGURACION DEL BOTON COMPRAR AHORA
        view.findViewById<Button>(R.id.buyNowButton).setOnClickListener {
            val quantity = quantityPicker.value // OBTIENE LA CANTIDAD SELECCIONADA
            val selectedType = when (radioGroup.checkedRadioButtonId) { // DETERMINA EL TIPO SELECCIONADO
                R.id.radioStickers -> "Con stickers"
                R.id.radioStickerless -> "Stickerless"
                else -> "No especificado"
            }

            // CREAMOS UN ITEM DE CARRITO Y MUESTRA UN DIALOGO DE CONFIRMACION DE COMPRA
            val item = CartItem(cube, quantity, selectedType)
            AlertDialog.Builder(requireContext())
                .setTitle("Confirmación de compra") // TITULO DEL DIALOGO
                .setMessage("¿Deseas comprar ${cube.name} por $quantity unidades?") // MENSAJE DEL DIALOGO
                .setPositiveButton("Comprar") { _, _ ->
                    // SI EL USUARIO ACEPTA, SE DIRIGE AL FRAGMENTO DE PAGO
                    val checkoutFragment = CheckoutFragment(mutableListOf(item))
                    requireActivity().supportFragmentManager.beginTransaction()
                        .replace(R.id.fragmentContainer, checkoutFragment)
                        .addToBackStack(null)
                        .commit()
                }
                .setNegativeButton("Cancelar", null) // SI EL USUARIO CANCELA, NO HACE NADA
                .show()
        }
    }
}