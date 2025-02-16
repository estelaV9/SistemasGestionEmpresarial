package com.example.cubexshop.fragment

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.cubexshop.R
import com.example.cubexshop.adapter.CubeAdapter
import com.example.cubexshop.model.CubeProveedor

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
