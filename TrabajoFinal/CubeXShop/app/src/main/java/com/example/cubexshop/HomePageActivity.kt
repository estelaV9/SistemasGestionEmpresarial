package com.example.cubexshop

import android.net.Uri
import android.os.Bundle
import com.bumptech.glide.Glide
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentTransaction
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.cubexshop.databinding.ActivityHomePageBinding
import com.example.cubexshop.model.CartItem
import com.example.cubexshop.model.Cube
import com.example.cubexshop.model.CubeProveedor

class HomePageActivity : AppCompatActivity() {
    private lateinit var binding: ActivityHomePageBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHomePageBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.myToolbar)

        binding.menuIcon.setOnClickListener {
            binding.drawerLayout.openDrawer(binding.navigationView)
        }

        binding.shopButton.setOnClickListener {
            loadFragment(ShopFragment())
        }

        binding.marketButton.setOnClickListener {
            loadFragment(MarketFragment())
        }

        binding.cartIcon.setOnClickListener {
            loadFragment(CartFragment())
        }
    }

    private fun loadFragment(fragment: Fragment) {
        val fragmentManager: FragmentManager = supportFragmentManager
        val fragmentTransaction: FragmentTransaction = fragmentManager.beginTransaction()
        fragmentTransaction.replace(R.id.fragmentContainer, fragment)
        fragmentTransaction.addToBackStack(null)
        fragmentTransaction.commit()
    }
}

class ShopFragment : Fragment(R.layout.fragment_shop) {
    private lateinit var adapter: CubeAdapter

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val recyclerView: RecyclerView = view.findViewById(R.id.recyclerView)
        recyclerView.layoutManager = LinearLayoutManager(requireContext())
        adapter = CubeAdapter(CubeProveedor.getCubes())
        recyclerView.adapter = adapter
    }
}

class MarketFragment : Fragment(R.layout.fragment_market) {

    private var selectedImageUri: Uri? =
        null // Variable para almacenar la URI de la imagen seleccionada

    // Registramos la imagen para obtener contenido
    private val pickImage =
        registerForActivityResult(ActivityResultContracts.GetContent()) { uri: Uri? ->
            uri?.let {
                selectedImageUri = it
                view?.findViewById<ImageView>(R.id.productImage)
                    ?.setImageURI(it) // Mostrar la imagen seleccionada
            }
        }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val productImage: ImageView = view.findViewById(R.id.productImage)
        val nameEditText: EditText = view.findViewById(R.id.productName)
        val brandEditText: EditText = view.findViewById(R.id.productBrand)
        val descriptionEditText: EditText = view.findViewById(R.id.productDescription)
        val submitButton: Button = view.findViewById(R.id.submitButton)

        // Selección de imagen desde la galería
        productImage.setOnClickListener {
            pickImage.launch("image/*") // Lanzamos el contrato para seleccionar una imagen
        }

        submitButton.setOnClickListener {
            val name = nameEditText.text.toString()
            val brand = brandEditText.text.toString()
            val description = descriptionEditText.text.toString()

            if (name.isNotEmpty() && brand.isNotEmpty() && description.isNotEmpty() && selectedImageUri != null) {
                val newCube = Cube(
                    name = name,
                    marca = brand,
                    description = description,
                    imageUrl = selectedImageUri.toString() // Guardamos la URI de la imagen seleccionada
                )

                CubeProveedor.addCube(newCube)
                Toast.makeText(requireContext(), "Producto agregado", Toast.LENGTH_SHORT).show()

                // Limpiar campos después de agregar el producto
                nameEditText.text.clear()
                brandEditText.text.clear()
                descriptionEditText.text.clear()
                productImage.setImageResource(R.drawable.logo_without_borders) // Restablecer imagen por defecto
                selectedImageUri = null
            } else {
                Toast.makeText(
                    requireContext(),
                    "Todos los campos son obligatorios",
                    Toast.LENGTH_SHORT
                ).show()
            }
        }
    }
}


object CartManager {
    val cartItems = mutableListOf<CartItem>()
}

class CubeDetailFragment(private val cube: Cube) : Fragment(R.layout.fragment_cube_details) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        view.findViewById<TextView>(R.id.detailName).text = cube.name
        view.findViewById<TextView>(R.id.detailDescription).text = cube.description
        view.findViewById<ImageView>(R.id.detailImage).setImageResource(cube.imageResId!!)

        val quantityPicker: NumberPicker = view.findViewById(R.id.quantityPicker)
        quantityPicker.minValue = 1
        quantityPicker.maxValue = 10

        val radioGroup: RadioGroup = view.findViewById(R.id.radioGroupOptions)

        view.findViewById<Button>(R.id.addToCartButton).setOnClickListener {
            val quantity = quantityPicker.value
            val selectedType = when (radioGroup.checkedRadioButtonId) {
                R.id.radioStickers -> "Con stickers"
                R.id.radioStickerless -> "Stickerless"
                else -> "No especificado"
            }

            // Verificamos si el carrito ya tiene el mismo producto para actualizar la cantidad
            val existingItem =
                CartManager.cartItems.find { it.cube.name == cube.name && it.type == selectedType }
            if (existingItem != null) {
                existingItem.quantity += quantity // Actualizamos la cantidad si el producto ya está en el carrito
            } else {
                CartManager.cartItems.add(
                    CartItem(
                        cube,
                        quantity,
                        selectedType
                    )
                ) // Si no está, lo agregamos
            }

            Toast.makeText(requireContext(), "Agregado al carrito", Toast.LENGTH_SHORT).show()
        }

        view.findViewById<Button>(R.id.buyNowButton).setOnClickListener {
            val quantity = quantityPicker.value
            val selectedType = when (radioGroup.checkedRadioButtonId) {
                R.id.radioStickers -> "Con stickers"
                R.id.radioStickerless -> "Stickerless"
                else -> "No especificado"
            }

            val item = CartItem(cube, quantity, selectedType)
            AlertDialog.Builder(requireContext())
                .setTitle("Confirmación de compra")
                .setMessage("¿Deseas comprar ${cube.name} por $quantity unidades?")
                .setPositiveButton("Comprar") { _, _ ->
                    val checkoutFragment = CheckoutFragment(mutableListOf(item))
                    requireActivity().supportFragmentManager.beginTransaction()
                        .replace(R.id.fragmentContainer, checkoutFragment)
                        .addToBackStack(null)
                        .commit()
                }
                .setNegativeButton("Cancelar", null)
                .show()
        }
    }
}

class CartAdapter(private val cartItems: List<CartItem>) :
    RecyclerView.Adapter<CartAdapter.CartItemViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CartItemViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_card, parent, false)
        return CartItemViewHolder(view)
    }

    override fun onBindViewHolder(holder: CartItemViewHolder, position: Int) {
        val cartItem = cartItems[position]
        holder.bind(cartItem)
    }

    override fun getItemCount(): Int = cartItems.size

    inner class CartItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val nameTextView: TextView = itemView.findViewById(R.id.cartItemName)
        private val quantityTextView: TextView = itemView.findViewById(R.id.cartItemQuantity)
        private val typeTextView: TextView = itemView.findViewById(R.id.cartItemType)
        private val priceTextView: TextView = itemView.findViewById(R.id.cartItemPrice)

        fun bind(cartItem: CartItem) {
            nameTextView.text = cartItem.cube.name
            quantityTextView.text = "Cantidad: ${cartItem.quantity}"
            typeTextView.text = cartItem.type
        }
    }
}

class CartFragment : Fragment(R.layout.fragment_cart) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val recyclerView: RecyclerView = view.findViewById(R.id.cartRecyclerView)
        recyclerView.layoutManager = LinearLayoutManager(requireContext())
        val cartAdapter = CartAdapter(CartManager.cartItems)
        recyclerView.adapter = cartAdapter

        val checkoutButton: Button = view.findViewById(R.id.checkoutButton)
        checkoutButton.setOnClickListener {
            if (CartManager.cartItems.isNotEmpty()) {
                val checkoutFragment = CheckoutFragment(CartManager.cartItems)
                requireActivity().supportFragmentManager.beginTransaction()
                    .replace(R.id.fragmentContainer, checkoutFragment)
                    .addToBackStack(null)
                    .commit()
            } else {
                Toast.makeText(requireContext(), "El carrito está vacío", Toast.LENGTH_SHORT).show()
            }
        }
    }
}

class CheckoutFragment(private val cartItems: MutableList<CartItem>) :
    Fragment(R.layout.fragment_pago) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val payButton: Button = view.findViewById(R.id.payButton)

        var totalPrice = 0.0
        val cartDetails = StringBuilder("Resumen de la compra:\n")

        /*for (item in cartItems) {
            val itemTotalPrice = item.cube.price * item.quantity
            cartDetails.append("${item.cube.name}: ${item.quantity} x \$${item.cube.price} = \$${itemTotalPrice}\n")
            totalPrice += itemTotalPrice
        }*/

        cartDetails.append("\nTotal: \$${totalPrice}")
        //cartSummaryText.text = cartDetails.toString()

        payButton.setOnClickListener {
            // proceso de pago
            Toast.makeText(requireContext(), "Compra realizada con éxito", Toast.LENGTH_SHORT)
                .show()
            // vaciar el carrito
            CartManager.cartItems.clear()
            requireActivity().supportFragmentManager.popBackStack()
        }
    }
}


class CubeAdapter(private val cubes: List<Cube>) :
    RecyclerView.Adapter<CubeAdapter.CubeViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CubeViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_cube, parent, false)
        return CubeViewHolder(view)
    }

    override fun onBindViewHolder(holder: CubeViewHolder, position: Int) {
        val cube = cubes[position]
        holder.bind(cube)
    }

    override fun getItemCount(): Int = cubes.size

    inner class CubeViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bind(cube: Cube) {
            itemView.findViewById<TextView>(R.id.cubeName).text = cube.name
            itemView.findViewById<TextView>(R.id.cubeDescription).text = cube.description

            val imageView = itemView.findViewById<ImageView>(R.id.cubeImage)

            // Verificamos si la URL de la imagen es válida o si debe usar la imagen de recurso
            if (!cube.imageUrl.isNullOrEmpty()) {
                Glide.with(itemView.context)
                    .load(cube.imageUrl) // Cargar la imagen desde URL
                    .into(imageView)
            } else {
                // Si la URL es nula o vacía, usamos el imageResId
                cube.imageResId?.let {
                    imageView.setImageResource(it) // Cargar la imagen desde los recursos
                } ?: run {
                    imageView.setImageResource(R.drawable.logo_without_borders) // Imagen por defecto si no hay URL ni ResId
                }
            }

            itemView.setOnClickListener {
                (itemView.context as AppCompatActivity).supportFragmentManager.beginTransaction()
                    .replace(R.id.fragmentContainer, CubeDetailFragment(cube))
                    .addToBackStack(null)
                    .commit()
            }
        }
    }
}


