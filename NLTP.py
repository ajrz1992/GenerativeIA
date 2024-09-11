import difflib

# 1. Lista de productos estandarizados
productos_estandarizados = [
    "Leche Entera", "Leche Descremada", "Pan Integral", "Pan Blanco", 
    "Café Molido", "Café Instantáneo", "Yogur Natural", "Yogur de Fresa",
    "Mantequilla", "Margarina", "Arroz Blanco", "Arroz Integral", 
    "Azúcar Blanca", "Azúcar Morena", "Jugo de Naranja", "Jugo de Manzana"
]

# 2. Lista de productos ingresados con variaciones
productos_ingresados = [
    "leche entera", "LECHE DESCREMADA", "pan intgrl", "pan blnco",
    "Café molido", "cafe instantaneo", "yogurt natural", "yogur fresa",
    "matequilla", "margarinna", "arroz blaco", "arroz intgral",
    "azucar blanca", "azucar morena", "jugo naranja", "jugo de manz"
]

# 3. Función para encontrar el producto más cercano en la lista estandarizada
def encontrar_producto_mas_cercano(producto, lista_estandarizada):
    producto_normalizado = producto.lower().strip()  # Normalizar el texto (minúsculas y quitar espacios)
    coincidencia = difflib.get_close_matches(producto_normalizado, lista_estandarizada, n=1)
    if coincidencia:
        return coincidencia[0]
    else:
        return "No encontrado"

# 4. Normalizar la lista de productos estandarizados
productos_estandarizados_normalizados = [p.lower().strip() for p in productos_estandarizados]

# 5. Emparejar productos ingresados con estandarizados y mostrar resultados
for producto in productos_ingresados:
    producto_estandarizado = encontrar_producto_mas_cercano(producto, productos_estandarizados_normalizados)
    print(f"Ingresado: {producto} -> Estandarizado: {producto_estandarizado}")

