package com.example.cubexshop.model

// CLASE DATA PARA REPRESENTAR UN CUBO
data class Cube(
    val name: String,
    val description: String,
    val marca: String,
    val imageUrl: String? = null,
    val imageResId: Int? = null
)


