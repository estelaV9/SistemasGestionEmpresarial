package com.example.cubexshop.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.cubexshop.R
import com.example.cubexshop.fragment.CubeDetailFragment
import com.example.cubexshop.model.Cube

class CubeAdapter(private val cubes: List<Cube>) :
    RecyclerView.Adapter<CubeAdapter.CubeViewHolder>() {

    // CREAR EL VIEWHOLDER PARA LOS ITEMS DE CUBOS
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CubeViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_cube, parent, false)
        return CubeViewHolder(view)
    }

    // VINCULAR LOS DATOS DEL CUBO CON EL VIEWHOLDER
    override fun onBindViewHolder(holder: CubeViewHolder, position: Int) {
        val cube = cubes[position]
        holder.bind(cube)
    }

    // OBTENER LA CANTIDAD DE CUBOS
    override fun getItemCount(): Int = cubes.size

    // VIEWHOLDER PARA CADA ITEM DE CUBO
    inner class CubeViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        // VINCULAR LOS DATOS DE UN CUBO AL VIEWHOLDER
        fun bind(cube: Cube) {
            itemView.findViewById<TextView>(R.id.cubeName).text = cube.name
            itemView.findViewById<TextView>(R.id.cubeDescription).text = cube.description
            val imageView = itemView.findViewById<ImageView>(R.id.cubeImage)

            if (!cube.imageUrl.isNullOrEmpty()) {
                // CARGAR LA IMAGEN DESDE LA URL
                Glide.with(itemView.context)
                    .load(cube.imageUrl)
                    .into(imageView)
            } else {
                // SI LA URL ES NULA O VACIA, USAMOS EL imageResId
                cube.imageResId?.let {
                    imageView.setImageResource(it) // CARGAR LA IMAGEN DESDE LOS RECURSOS
                } ?: run {
                    imageView.setImageResource(R.drawable.logo_without_borders) // IMAGEN POR DEFECTO SI NO HAY URL NI ResId
                }
            } // VERIFICAMOS SI LA URL DE LA IMAGEN ES VALIDA O SI DEBE USAR LA IMAGEN DE RECURSO


            itemView.setOnClickListener {
                (itemView.context as AppCompatActivity).supportFragmentManager.beginTransaction()
                    .replace(R.id.fragmentContainer, CubeDetailFragment(cube))
                    .addToBackStack(null)
                    .commit()
            } // CUANDO SE HACE CLIC EN UN CUBO, SE REEMPLAZA EL FRAGMENTO ACTUAL CON EL CubeDetailFragment
        }
    }
}
