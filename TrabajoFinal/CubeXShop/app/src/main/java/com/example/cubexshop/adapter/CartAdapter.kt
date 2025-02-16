package com.example.cubexshop.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.cubexshop.R
import com.example.cubexshop.model.CartItem

class CartAdapter(private val cartItems: MutableList<CartItem>) :
    RecyclerView.Adapter<CartAdapter.CartItemViewHolder>() {

    // CREAR EL VIEW HOLDER PARA LOS ITEMS DEL CARRITO
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CartItemViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_card, parent, false)
        return CartItemViewHolder(view)
    }

    // ASIGNAR LOS DATOS DE CADA ITEM AL VIEW HOLDER
    override fun onBindViewHolder(holder: CartItemViewHolder, position: Int) {
        val cartItem = cartItems[position]
        holder.bind(cartItem) // VINCULAMOS LOS DATOS AL VIEW HOLDER
    }

    // OBTENER LA CANTIDAD DE ITEMS EN EL CARRITO
    override fun getItemCount(): Int = cartItems.size



    inner class CartItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val nameTextView: TextView = itemView.findViewById(R.id.cartItemName) // NOMBRE DEL PRODUCTO
        private val quantityTextView: TextView = itemView.findViewById(R.id.cartItemQuantity) // CANTIDAD
        private val imagenImageView: ImageView = itemView.findViewById(R.id.cartItemImage) // IMAGEN DEL PRODUCTO
        private val typeTextView: TextView = itemView.findViewById(R.id.cartItemType) // TIPO DE PRODUCTO
        private val priceTextView: TextView = itemView.findViewById(R.id.cartItemPrice) // PRECIO DEL PRODUCTO
        private val removeFromCartButton: Button = itemView.findViewById(R.id.removeFromCartButton) // BOTON PARA ELIMINAR ITEM DEL CARRITO

        //VINCULAR LOS DATOS AL VIEW HOLDER
        fun bind(cartItem: CartItem) {
            nameTextView.text = cartItem.cube.name // ASIGNAR NOMBRE DEL PRODUCTO

            Glide.with(itemView.context)
                .load(cartItem.cube.imageResId) // CARGAR LA IMAGEN DEL PRODUCTO
                .into(imagenImageView)

            quantityTextView.text = "Cantidad: ${cartItem.quantity}"
            typeTextView.text = cartItem.type

            // BOTON DE ELIMINAR
            removeFromCartButton.setOnClickListener {
                // DISMINUIR LA CANTIDAD DEL ITEM
                if (cartItem.quantity > 1) {
                    cartItem.quantity-- // REDUCIR CANTIDAD
                    notifyItemChanged(adapterPosition) // ACTUALIZAR EL ITEM
                } else {
                    // SI LA CANTIDAD LLEGA A 0, ELIMINAR EL ITEM
                    cartItems.removeAt(adapterPosition) // ELIMINAR EL ITEM DE LA LISTA
                    notifyItemRemoved(adapterPosition) // ELIMINAR ITEM DEL ADAPTADOR
                }
            }
        }
    }
}