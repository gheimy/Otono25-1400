🔎 Preguntas de Investigación y Experimentación

# Diferencia entre fullmatch y search:
Para entender la diferencia, probé ambos métodos con cadenas que contenían texto antes y después del patrón.  
Si usáramos `re.search` en la función `validar_email`, la cadena `"Esto es invalido email@valido.com el resto"` **sí sería aceptada**, porque `search` solo necesita encontrar el patrón en algún lugar del texto, aunque haya basura alrededor.  
En cambio, `re.fullmatch` exige que **toda la cadena complete** coincida exactamente con el formato esperado.  
Por eso es la opción correcta cuando se necesita una validación estricta, como un email o placa con estructura fija.

---

# Grupos de Captura:
En el TODO 2 fue importante usar el metacarácter `()` porque permite **capturar solo la parte del patrón que necesitamos**, en este caso, los 5 dígitos.  
Si no usamos paréntesis, la coincidencia se valida, pero no podemos extraer esa información específica.  
Con `match.group(1)` se puede recuperar solamente lo que está dentro del paréntesis, aislando los datos exactos que nos interesan.  
Esto hace que el procesamiento posterior sea más fácil y preciso.

---

# Clases de Caracteres y Negación:
En el TODO 3 la negación se logra con la sintaxis `[^...]`, donde el símbolo `^` dentro de corchetes significa **“todo excepto lo que está dentro del conjunto”**.  
Esto permite encontrar símbolos o caracteres no permitidos (todo excepto letras, números o espacios).  
Si usáramos `re.search`, solo encontraríamos si existe un caracter prohibido, pero **no lo eliminaríamos**.  
Con `re.sub`, en cambio, podemos reemplazar todos esos caracteres no deseados por vacío, logrando una limpieza total del texto.  
Por eso `re.sub` fue la herramienta correcta para la tarea de limpieza.

