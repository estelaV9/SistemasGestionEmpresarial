package com.example.cubexshop.fragment

import android.net.Uri
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.fragment.app.Fragment
import com.example.cubexshop.R
import com.example.cubexshop.model.Cube
import com.example.cubexshop.model.CubeProveedor

class MarketFragment : Fragment(R.layout.fragment_market) {

    private var selectedImageUri: Uri? =
        null // VARIABLE PARA ALMACENAR LA URI DE LA IMAGEN SELECCIONADA

    // REGISTRAMOS LA IMAGEN PARA OBTENER EL CONTENIDO DE LA GALERIA
    private val pickImage =
        registerForActivityResult(ActivityResultContracts.GetContent()) { uri: Uri? ->
            uri?.let {
                selectedImageUri = it // ASIGNAMOS LA URI DE LA IMAGEN SELECCIONADA
                view?.findViewById<ImageView>(R.id.productImage)
                    ?.setImageURI(it) // MOSTRAMOS LA IMAGEN SELECCIONADA EN LA VISTA
            }
        }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val productImage: ImageView = view.findViewById(R.id.productImage)
        val nameEditText: EditText = view.findViewById(R.id.productName)
        val brandEditText: EditText = view.findViewById(R.id.productBrand)
        val descriptionEditText: EditText = view.findViewById(R.id.productDescription)
        val submitButton: Button = view.findViewById(R.id.submitButton)

        // SELECCION DE IMAGEN DESDE LA GALERIA AL HACER CLICK EN LA IMAGEN
        productImage.setOnClickListener {
            pickImage.launch("image/*") // LANZAMOS EL CONTRATO PARA SELECCIONAR UNA IMAGEN DE LA GALERIA
        }

        // BOTON DE ENVIO DEL FORMULARIO DE PRODUCTO
        submitButton.setOnClickListener {
            val name = nameEditText.text.toString()
            val brand = brandEditText.text.toString()
            val description = descriptionEditText.text.toString()

            // VERIFICAMOS QUE TODOS LOS CAMPOS ESTEN COMPLETADOS Y QUE SE HAYA SELECCIONADO UNA IMAGEN
            if (name.isNotEmpty() && brand.isNotEmpty() && description.isNotEmpty() && selectedImageUri != null) {
                // CREAMOS UN NUEVO OBJETO CUBE CON LOS DATOS INGRESADOS
                val newCube = Cube(
                    name = name,
                    marca = brand,
                    description = description,
                    imageUrl = selectedImageUri.toString() // GUARDAMOS LA URI DE LA IMAGEN SELECCIONADA
                )

                // AGREGAMOS EL NUEVO PRODUCTO AL PROVEEDOR
                CubeProveedor.addCube(newCube)
                Toast.makeText(requireContext(), "Producto agregado", Toast.LENGTH_SHORT).show()

                // LIMPIAMOS LOS CAMPOS DESPUES DE AGREGAR EL PRODUCTO
                nameEditText.text.clear()
                brandEditText.text.clear()
                descriptionEditText.text.clear()
                productImage.setImageResource(R.drawable.logo_without_borders) // RESTAURAMOS LA IMAGEN POR DEFECTO
                selectedImageUri = null // RESETEAMOS LA URI DE LA IMAGEN
            } else {
                // MOSTRAMOS UN MENSAJE DE ERROR SI ALGUN CAMPO ESTA VACIO O NO SE SELECCIONO UNA IMAGEN
                Toast.makeText(
                    requireContext(),
                    "Todos los campos son obligatorios",
                    Toast.LENGTH_SHORT
                ).show()
            }
        }
    }
}
