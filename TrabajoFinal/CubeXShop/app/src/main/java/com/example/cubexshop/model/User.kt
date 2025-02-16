package com.example.cubexshop.model

import java.time.LocalDate

data class User(
    var idUser: Int?,
    var name: String,
    var email: String,
    var password: String,
    var registrationDate: LocalDate,
    var profileImage: String? = null
)