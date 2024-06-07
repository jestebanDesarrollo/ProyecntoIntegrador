
import streamlit as st
import matplotlib.pyplot as plt

# Set the page title and header
st.title("Proyecto Integrador")
st.header("Menu de restaurante")
st.write("Se me olvido apagar la computadora, soy gordo")

# Hero Section with image and project description
st.image("img/Portada.png", width=600)
st.write("Vamos a realizar una aplicacion tanto para ordenador y aplicaciones moviles que permitira la comunicacion mas acertada entre los empleados como meseros con cocina ademas de tener un registro mas exacto de todos los productos e inventario de la empresa gastronomica.")

# Project Overview
st.subheader("Módulo 1: Login y asignación de roles (Móvil y Web)")
st.write("- Diseño intuitivo con esquema de colores negro y vino tinto. ")
st.write("- Se debe permitir el registro de usuarios con roles específicos: Administrador, Facturación, Chef y Mesero.")
st.write("- Cada rol debe tener sus propias credenciales de inicio de sesión con: \n" 
         "1. Nombre.\n"
         "2. Contraseña.")
st.write("- Las autorizaciones de perfil deben restringir el acceso a funciones específicas según el rol del usuario.\n")

st.subheader("Módulo 2: Facturación (Caja) (Web)")
st.write("-  Diseño intuitivo con esquema de colores negro y vino tinto.")
st.write("-  Visualización de pedidos en estados.")

# Features and Benefits
st.subheader("Características y Beneficios")
st.write("**Característica 1:** Descripción de la característica 1 y sus beneficios.")
st.write("**Característica 2:** Descripción de la característica 2 y sus beneficios.")
st.write("**Característica 3:** Descripción de la característica 3 y sus beneficios.")

# Interactive Chart or Visualization (Optional)
# Replace with your specific data and visualization
data = [10, 20, 30, 40, 50]
labels = ["Categoría A", "Categoría B", "Categoría C", "Categoría D", "Categoría E"]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)

# Call to Action
st.subheader("¡Toma Acción!")
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://example.com)")
st.write("**Contáctenos:** [Enlace al correo electrónico de contacto](mailto:info@example.com)")

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- Nombre 1: Cargo en el equipo.")
st.write("- Nombre 2: Cargo en el equipo.")
st.write("- Nombre 3: Cargo en el equipo.")
st.write("**Información de contacto:**")
st.write("Correo electrónico: [Enlace al correo electrónico de contacto](mailto:info@example.com)")