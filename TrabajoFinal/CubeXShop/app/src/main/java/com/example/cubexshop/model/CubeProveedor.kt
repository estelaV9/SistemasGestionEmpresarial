package com.example.cubexshop.model

import com.example.cubexshop.R

class CubeProveedor {
    companion object{
        private val cubes = mutableListOf(Cube("GAN 356 XS", "Un cubo 3x3 magnético de alta gama con ajustes avanzados.", "GAN", null, R.drawable.gan_356_xs),
            Cube("GAN 11 M Pro", "Cubo 3x3 de GAN con núcleo magnético y gran estabilidad.", "GAN", null,R.drawable.gan_11_m_pro),
            Cube("MoYu WeiLong WRM 2021", "Cubo 3x3 de velocidad con sistema de ajuste dual.", "MoYu", null,R.drawable.moyu_weilong_wrm_2021),
            Cube("MoYu RS3M 2020", "Una excelente opción económica con imanes y buen rendimiento.", "MoYu", null,R.drawable.moyu_rs3m_2020),
            Cube("MoYu AoShi 6x6 GTS", "Uno de los mejores cubos 6x6 para speedcubing.", "MoYu", null,R.drawable.moyu_aoshi_6x6_gts),
            Cube("QiYi Valk 3 Elite M", "Cubo 3x3 magnético con excelente sensación de giro.", "QiYi", null,R.drawable.qiyi_valk_3_elite_m),
            Cube("QiYi MS 4x4", "Cubo 4x4 de la serie MS, económico y con buen rendimiento.", "QiYi", null,R.drawable.qiyi_ms_4x4),
            Cube("QiYi X-Man Tornado V3", "Cubo 3x3 con sistema de ajuste avanzado y gran control.", "QiYi", null,R.drawable.qiyi_xman_tornado_v3),
            Cube("YJ MGC 5x5", "Uno de los mejores cubos 5x5 en calidad-precio.", "YJ", null,R.drawable.yj_mgc_5x5),
            Cube("YJ MGC Evo 3x3", "Nuevo modelo de 3x3 con características innovadoras.", "YJ", null,R.drawable.yj_mgc_evo_3x3),
            Cube("DianSheng Solar S3M", "Cubo 3x3 con núcleo magnético y rotación suave.", "DianSheng", null,R.drawable.diansheng_solar_s3m),
            Cube("DianSheng Galaxy 8M 4x4", "Cubo 4x4 magnético con excelente corte de esquinas.", "DianSheng", null,R.drawable.diansheng_galaxy_8m_4x4),
            Cube("ShengShou Mr. M 2x2", "Cubo 2x2 con imanes y diseño clásico.", "ShengShou", null,R.drawable.shengshou_mr_m_2x2),
            Cube("ShengShou Megaminx", "Megaminx con buen giro y diseño accesible.", "ShengShou", null,R.drawable.shengshou_megaminx),
            Cube("Yuxin Little Magic Pyraminx", "Pyraminx económico y de buen rendimiento.", "Yuxin", null,R.drawable.yuxin_little_magic_pyraminx)
           )

        fun getCubes(): List<Cube> = cubes

        fun addCube(cube: Cube) {
            cubes.add(cube)
        }
    }
}