package com.example.cubexshop.fragment

import android.annotation.SuppressLint
import android.content.Context
import android.net.Uri
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.fragment.app.Fragment
import com.bumptech.glide.Glide
import com.example.cubexshop.R
import com.example.cubexshop.dao.UserDAO
import com.example.cubexshop.model.User
import com.google.android.material.textfield.TextInputEditText
import java.time.LocalDate

class ProfileFragment : Fragment(R.layout.fragment_profile) {
    private lateinit var userDAO: UserDAO
    private lateinit var userName: TextInputEditText
    private lateinit var userEmail: TextInputEditText
    private lateinit var userPassword: TextInputEditText
    private lateinit var userProfileImage: ImageView
    private lateinit var changePhotoText: TextView
    private lateinit var saveChangesButton: Button

    private var selectedImageUri: Uri? = null // URI DE LA IMAGEN SELECCIONADA

    // METODO PARA ABRIR LA GALERIA DIRECTAMENTE
    // AL SELECCIONAR UNA IMAGEN DE LA GALERIA
    private val pickImage =
        registerForActivityResult(ActivityResultContracts.GetContent()) { uri: Uri? ->
            uri?.let {
                selectedImageUri = it // ASIGNAMOS LA URI DE LA IMAGEN SELECCIONADA
                Glide.with(requireContext())
                    .load(it)
                    .circleCrop() // SE REDONDEA LA IMAGEN
                    .into(userProfileImage) // COLOCAMOS LA IMAGEN EN EL IMAGEVIEW
                saveProfileImage(it.toString()) // GUARDAMOS LA IMAGEN SELECCIONADA
            }
        }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val rootView = inflater.inflate(R.layout.fragment_profile, container, false)

        userDAO = UserDAO(requireContext())
        userName = rootView.findViewById(R.id.etName)
        userEmail = rootView.findViewById(R.id.etEmail)
        userPassword = rootView.findViewById(R.id.etPassword)
        userProfileImage = rootView.findViewById(R.id.imgProfile)
        changePhotoText = rootView.findViewById(R.id.tvChangePhoto)
        saveChangesButton = rootView.findViewById(R.id.btnSaveChanges)

        // CARGAMOS LOS DATOS DEL USUARIO
        loadUserData()

        // ABRIR LA GALERIA AL HACER CLICK EN CAMBIAR FOTO
        changePhotoText.setOnClickListener {
            pickImage.launch("image/*") // LANZAMOS EL CONTRATO PARA SELECCIONAR UNA IMAGEN
        }

        // GUARDAR LOS CAMBIOS DEL PERFIL
        saveChangesButton.setOnClickListener {
            saveUserData() // GUARDAMOS LOS DATOS ACTUALIZADOS
        }

        return rootView
    }

    private fun loadUserData() {
        val user = getLoggedUser() // OBTENEMOS EL USUARIO LOGUEADO

        if (user != null) {
            userName.setText(user.name)
            userEmail.setText(user.email)
            userPassword.setText(user.password)

            val savedImageUri = getProfileImage() // OBTENEMOS LA URI DE LA IMAGEN DE PERFIL
            if (!savedImageUri.isNullOrEmpty()) {
                Glide.with(requireContext())
                    .load(Uri.parse(savedImageUri)) // CARGAMOS LA IMAGEN DESDE LA URI
                    .circleCrop() // HACE QUE LA IMAGEN SEA CIRCULAR
                    .into(userProfileImage) // MOSTRAMOS LA IMAGEN EN EL IMAGEVIEW
            } else {
                userProfileImage.setImageResource(R.drawable.ic_person) // IMAGEN POR DEFECTO SI NO HAY IMAGEN
            }
        } else {
            Toast.makeText(requireContext(), "Error al cargar los datos del usuario", Toast.LENGTH_SHORT).show()
        }
    } // CARGAR LOS DATOS DEL USUARIO DESDE PREFERENCIAS O BASE DE DATOS


    private fun saveUserData() {
        val user = getLoggedUser() // OBTENEMOS EL USUARIO LOGUEADO

        if (user != null) {
            val updatedUser = User(
                user.idUser,
                userName.text.toString(),
                userEmail.text.toString(),
                userPassword.text.toString(),
                user.registrationDate
            )

            val result = userDAO.updateUser(updatedUser) // ACTUALIZAMOS LOS DATOS DEL USUARIO EN LA BASE DE DATOS

            if (result > 0) {
                Toast.makeText(requireContext(), "Perfil actualizado correctamente", Toast.LENGTH_SHORT).show()
                saveLoggedUser(updatedUser) // GUARDAMOS LOS DATOS ACTUALIZADOS EN SHARED PREFERENCES
            } else {
                Toast.makeText(requireContext(), "Error al actualizar el perfil", Toast.LENGTH_SHORT).show()
            }
        }
    } // GUARDAR LOS DATOS ACTUALIZADOS DEL USUARIO


    @SuppressLint("NewApi")
    private fun getLoggedUser(): User? {
        val sharedPreferences = requireContext().getSharedPreferences("UserPrefs", Context.MODE_PRIVATE)

        val idUser = sharedPreferences.getInt("user_id", -1)
        val name = sharedPreferences.getString("user_name", null)
        val email = sharedPreferences.getString("user_email", null)
        val password = sharedPreferences.getString("user_password", null)

        return if (name != null && email != null && password != null) {
            User(idUser, name, email, password, LocalDate.now()) // DEVOLVEMOS EL USUARIO CON LOS DATOS
        } else {
            null
        }
    } // OBTENER EL USUARIO LOGUEADO DESDE SHARED PREFERENCES


    private fun saveLoggedUser(user: User) {
        val sharedPreferences = requireContext().getSharedPreferences("UserPrefs", Context.MODE_PRIVATE)
        val editor = sharedPreferences.edit()

        editor.putInt("user_id", user.idUser ?: -1)
        editor.putString("user_name", user.name)
        editor.putString("user_email", user.email)
        editor.putString("user_password", user.password)

        editor.apply()
    } // GUARDAR LOS DATOS DEL USUARIO EN SHARED PREFERENCES


    private fun saveProfileImage(imageUri: String) {
        val sharedPreferences = requireContext().getSharedPreferences("UserPrefs", Context.MODE_PRIVATE)
        val editor = sharedPreferences.edit()

        editor.putString("user_profile_image", imageUri) // GUARDAMOS LA URI DE LA IMAGEN DE PERFIL
        editor.apply()
    } // GUARDAR LA IMAGEN DE PERFIL EN SHARED PREFERENCES

    private fun getProfileImage(): String? {
        val sharedPreferences = requireContext().getSharedPreferences("UserPrefs", Context.MODE_PRIVATE)
        return sharedPreferences.getString("user_profile_image", null) // OBTENEMOS LA URI DE LA IMAGEN DE PERFIL
    } // OBTENER LA IMAGEN DE PERFIL DESDE SHARED PREFERENCES
}
