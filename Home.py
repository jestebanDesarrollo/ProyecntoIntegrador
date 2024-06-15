
import streamlit as st
import matplotlib.pyplot as plt

# Set the page title and header
st.title("Proyecto Integrador")
st.header("Menu de restaurante")

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
st.write("- Las autorizaciones de perfil deben restringir el acceso a funciones específicas según el rol del usuario.")

st.subheader("Módulo 2: Facturación (Caja) (Web)")
st.write("-  Diseño intuitivo con esquema de colores negro y vino tinto.")
<<<<<<< HEAD
st.write("-  Visualización de pedidos en estados:")
st.write("1. Facturados.")
st.write("2. Entregados pendientes de pago ")
st.write("- Detalles del pedido:")         
st.write("1. Mesa.")         
st.write("2. Productos")         
st.write("3. Cantidad.")         
st.write("4. Meser@.")         
st.write("5. Descripción..")         
st.write("6. Fecha-hora.")         
st.write("- Historial del día para visualización de ventas.")         

st.subheader("Módulo 3: Administración (Web)")
st.write("- Capacidad para:")
st.write("1. Agregar (Productos,Empleados e insumos)")
st.write("2. Modificar (Productos,Empleados e insumos)")
st.write("3. Eliminar (Productos,Empleados e insumos)")
st.write("3. Eliminar (Productos,Empleados e insumos)")
st.write("- Crear y descarga de un detallado de ingresos y egresos de venta por dias.")
st.write("- Visualizacion de graficos de ventas.")

st.subheader("Módulo 4: Servicio (meseros) (Movil)")
st.write("- Visualizacion detallada de productos disponibles incluyendo:")
st.write("1. Nombre del producto")
st.write("2. Descripción (De platos a gusto del cliente).")
st.write("3. Precio del producto.")
st.write("4. Disponibilidad del pedido si esta Completado o Pendiente por cobrar.")
st.write("- Selección de mesas para cada pedido.")
st.write("- Generación de un iD de pedido al guardar un pedido.")
st.write("- Notidicación automatica a la cocina al guardar un pedido.")

st.subheader("Modulo 5: Cocina (Chef)(Móvil)")
st.write("- Visualizacion de pedidos pendientes de preparacion desde el mas antiguo.")
st.write("1. Detalles de pedidos incluyendo especificaciones del cliente.")
st.write("2. Que usuario de mesero tomo el pedido.")
st.write("3. Productos")
st.write("4. Cantidad")
st.write("5. Numero de mesa")
st.write("6. Estado.")

# Features and Benefits
st.subheader("Características y Beneficios")
st.write("**Pedidos 1:** La eficiencia a la hora de la comunicacion entre meseros y cocina que a la hora de tomar pedidos muchas veces los meseros a la hora de tomar el pedido tratan de memorizar muchos ya que varios les da dificultad de memorizar todo el pedido del cliente de esta manera llegara de una forma mas exacta la informacion al cheft para su preparacion.")
st.write("**Facturacion 2:** Facturacion, de esta manera la forma de facturar y filtrar la mesa que mas clientes recibio en el dia el restaurante ademas de la busqueda y reimpresion de las facturas para l@s contador@s del restaurante.")
st.write("**Inventario 3:** Al tener un descuento de la misma aplicacion de los productos que se van sirviendo, es se lleva una manera mas controlada y exacta los productos necesarios para el restaurante al igual que cuales son los productos que mas se tienen que surtir. ")
=======
st.write("-  Visualización de pedidos en estados: "
            "1.Facturados."
            "2.Entregados pendientes de pago ")
st.write("- Detalles del pedido." 
        "1.	Mesa. " 
        "2.Productos"
        "3.Cantidad. "
        "4.Meser@. "
        "5.Descripción."
        "6.Fecha-hora.")

# Features and Benefits
st.subheader("Características y Beneficios")
st.write("**Característica 1:** Descripción de la característica 1 y sus beneficios.")
st.write("**Característica 2:** Descripción de la característica 2 y sus beneficios.")
st.write("**Característica 3:** Descripción de la característica 3 y sus beneficios.")
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4

# Interactive Chart or Visualization (Optional)
# Replace with your specific data and visualization
data = [10, 20, 30, 40, 50]
<<<<<<< HEAD
labels = ["Especias", "Bebidas", "Frutas", "Verduras", "Carnes."]
=======
labels = ["Categoría A", "Categoría B", "Categoría C", "Categoría D", "Categoría E"]
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)

# Call to Action
st.subheader("¡Toma Acción!")
<<<<<<< HEAD
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://github.com/jestebanDesarrollo/FrontEndRestaurante)")
st.write("**Contáctenos:** (https://www.linkedin.com/in/juan-esteban-muñoz-madrigal-84a7a829b/)")
=======
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://example.com)")
st.write("**Contáctenos:** [Enlace al correo electrónico de contacto](mailto:info@example.com)")
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
<<<<<<< HEAD
st.write("- Juan Esteban Muñoz Madrigal: Lider.")
st.write("- Juan Diego Morales Vásquez: Sub Lider.")
=======
st.write("- Nombre 1: Cargo en el equipo.")
st.write("- Nombre 2: Cargo en el equipo.")
st.write("- Nombre 3: Cargo en el equipo.")
st.write("**Información de contacto:**")
st.write("Correo electrónico: [Enlace al correo electrónico de contacto](mailto:info@example.com)")
>>>>>>> 71b03649009678d3c9851bb37149ce8537b4a1c4
