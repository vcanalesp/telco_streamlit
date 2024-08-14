import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import time

st.set_page_config(
    page_title="Telco",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)



def main():
    """
    Main function to set up the Streamlit app layout.
    """
    cs_sidebar()
    cs_body()
    return None

#class SidebarText:


# Constantes, mensajes, rangos, etc...

# Introducción del Análisis de las columnas
dct_introduccion = {
    "gender": """
    La variable "gender" proporciona datos categóricos, indicando si un cliente es femenino o masculino. A continuación, 
    analizaremos si existe una diferencia en el comportamiento de seguimiento o abandono del servicio entre ambos 
    géneros.
    """,
    "seniorcitizen": """
    La variable "seniorcitizen" proporciona datos categóricos que indican si un cliente es jubilado o no. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "partner": """
    La variable "partner" proporciona datos categóricos que indican si un cliente esta en pareja o no. A continuación, 
    analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "dependents": """
    La variable "dependents" proporciona datos categóricos que indican si el cliente tiene personas a su cargo, como 
    hijos u otros dependientes. A continuación, analizaremos si esta variable influye en la retención o pérdida de 
    clientes.
    """,
    "tenure": """
    La variable "tenure" proporciona datos numéricos e indica la duración, en meses, que un cliente ha estado con la 
    empresa.
    """,
    "phoneservice": """
    La variable "phoneservice" proporciona datos categóricos que indican si el cliente tiene servicio telefónico. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "multiplelines": """
    La variable "multiplelines" proporciona datos categóricos que indican si el cliente tiene múltiples líneas. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "internetservice": """
    La variable "internetservice" proporciona datos categóricos que indican si el cliente tiene servicios de internet. 
    A continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "onlinesecurity": """
    La variable "onlinesecurity" proporciona datos categóricos que indican si el cliente tiene seguridad en línea. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "onlinebackup": """
    La variable "onlinebackup" proporciona datos categóricos que indican si el cliente tiene copia de seguridad en 
    línea. A continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "deviceprotection": """
    La variable "deviceprotection" proporciona datos categóricos que indican si el cliente tiene protección del 
    dispositivo. A continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "techsupport": """
    La variable "techsupport" proporciona datos categóricos que indican si el cliente tiene soporte técnico. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "streamingtv": """
    La variable "streamingtv" proporciona datos categóricos que indican si el cliente tiene transmisión de televisión. 
    A continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "streamingmovies": """
    La variable "streamingmovies" proporciona datos categóricos que indican si el cliente tiene transmisión de 
    películas. A continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "contract": """
    La variable "contract" proporciona datos categóricos que indican si el cliente tiene contrato. A continuación, 
    analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "paperlessbilling": """
    La variable "paperlessbilling" proporciona datos categóricos que indican si el cliente tiene factura electrónica. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "paymentmethod": """
    La variable "paymentmethod" proporciona datos categóricos que indican si el cliente tiene método de pago. A 
    continuación, analizaremos si esta variable influye en la retención o pérdida de clientes.
    """,
    "monthlycharges": """
    La variable "monthlycharges" proporciona datos numéricos sobre los cargos mensuales de los clientes. A continuación, 
    analizaremos si esta variable influye en la retención o pérdida de clientes.
     """,
    "totalcharges": """
     La variable "totalcharges" proporciona datos numéricos sobre los cargos totales de los clientes. A continuación, 
     analizaremos si esta variable influye en la retención o pérdida de clientes.
     """
}

# Conclusión del análisis de las columnas
dct_conclusion = {
    "gender": """
    Podemos ver que tanto mujeres como hombres muestran patrones similares en términos de retención y pérdida de 
    clientes.
    """,
    "seniorcitizen": """ 
    Los gráficos muestras una notable disparidad entre clientes jubilados y no jubilados: el número de clientes 
    jubilados es significativamente menor. Además, es probable que este grupo no sea el objetivo principal de la 
    empresa, ya que la tasa de pérdida de clientes es considerablemente más alta entre los jubilados.
    """,
    "partner": """ 
    El gráfico muestra un aumento en el número de clientes que tienen pareja, así como una mayor tasa de retención entre
    estos clientes. Por lo tanto, esta variable tiene un impacto positivo en la retención de clientes.
    """,
    "dependents": """ 
    El gráfico muestra un aumento en el número de clientes que tienen dependientes, así como una mayor tasa de retención 
    entre estos clientes. Por lo tanto, esta variable tiene un impacto positivo en la retención de clientes.
    """,
    "tenure": """
     La mayoría de las pérdidas de clientes ocurren en los primeros meses. A medida que pasa el tiempo, la cantidad de 
     usuarios retenidos (en verde) supera consistentemente la cantidad de clientes perdidos (en naranja). Esto indica 
     que los usuarios que permanecen durante mucho tiempo tienden a continuar, mientras que aquellos que se van lo 
     hacen mayormente al principio. El segundo gráfico refuerza esta observación: a medida que se acerca el año de 
     permanencia, disminuye la cantidad de personas que se van. Una vez que los clientes han pasado varios años con la 
     empresa, es menos probable que decidan irse. Estos patrones sugieren que las estrategias de retención deberían 
     enfocarse en los clientes nuevos para reducir las tasas de pérdida iniciales y fomentar la lealtad a largo plazo.
     """,
    "phoneservice": """ 
    Es evidente que el servicio telefónico tiene una gran influencia en la atracción de clientes. Sin embargo, la tasa 
    de retención en porcentaje es similar tanto para los usuarios que tienen este servicio como para los que no lo 
    tienen.
    """,
    "multiplelines": """ 
    A través de los análisis podemos observar lo siguiente:
    - Los clientes que no poseen este servicio representan la mayor cantidad de usuarios.
    - Los clientes que han contratado el servicio son un grupo ligeramente menor en comparación con el anterior.
    - Los clientes sin servicio de Internet constituyen el menor número de usuarios.
    Los tres grupos se comportan de manera similar, aunque se observa una ligera pérdida mayor de clientes en los 
    usuarios que sí contrataron el servicio.
    """,
    "internetservice": """ 
    A través de los análisis podemos ver: 
    - La fibra óptica, aunque tiene un número alto de retención de clientes, también tiene la mayor cantidad de 
    clientes perdidos. 
    - El servicio DSL muestra una buena retención con pocas pérdidas en comparación.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "onlinesecurity": """ 
    A través de los análisis podemos ver:
    - Los clientes que no poseen este servicio, aunque tiene un número alto de retención de clientes, también tiene la 
    mayor cantidad de clientes perdidos.
    - Los clientes que lo contrataron tienen una buena retención con pocas pérdidas.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "onlinebackup": """ 
    A través de los análisis podemos ver:
    - Los clientes que no poseen este servicio, tiene la mayor cantidad de usuarios perdidos.
    - Los clientes que lo contrataron tienen una buena retención con pocas pérdidas.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "deviceprotection": """ 
    A través de los análisis podemos ver: 
    - Los clientes que no poseen este servicio, tiene la mayor cantidad de usuarios perdidos.
    - Los clientes que lo contrataron tienen una buena retención con pocas pérdidas, en comparación al anterior.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "techsupport": """ 
    A través de los análisis podemos ver:
    - Los clientes que no poseen este servicio, tiene la mayor cantidad de usuarios perdidos.
    - Los clientes que lo contrataron tienen una buena retención con pocas pérdidas.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "streamingtv": """
    A través de los análisis, podemos observar lo siguiente:
    - Los clientes que no poseen este servicio y los que lo contrataron tienen una tasa de retención media, 
    ligeramente favorable para estos últimos.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "streamingmovies": """
    A través de los análisis, podemos observar lo siguiente: 
    - Los clientes que no poseen este servicio y los que lo contrataron tienen una tasa de retención media, 
    ligeramente favorable para estos últimos.
    - Los clientes sin servicio de Internet presentan la mayor tasa de retención y la menor tasa de pérdida.
    """,
    "contract": """
    Podemos observar una influencia positiva significativa del contrato a largo plazo en la retención de clientes. Los 
    datos muestran una clara diferencia en la retención entre los clientes que tienen contratos mensuales y aquellos con 
    contratos de uno o dos años.
    - Contratos mensuales: Este grupo presenta la mayor tasa de pérdida de clientes. Muchos clientes parecen cancelar su 
    servicio después del primer mes.
    - Contratos de un año: Hay una notable mejora en la retención de clientes. La tasa de cancelación disminuye 
    considerablemente en comparación con los contratos mensuales.
    - Contratos de dos años: Estos contratos logran una retención excelente, con muy pocos clientes cancelando su 
    servicio. Los clientes con contratos de dos años muestran una lealtad mucho mayor.
    En resumen, los contratos a largo plazo (uno o dos años) son muy efectivos para mejorar la retención de clientes, 
    mientras que los contratos mensuales presentan mayores desafíos en términos de pérdida de clientes.
    """,
    "paperlessbilling": """
    A diferencia de los demás aspectos, este factor incrementa la pérdida de clientes.
    """,
    "paymentmethod": """
    Al analizar los métodos de pago, observamos comportamientos diferenciados en términos de retención de clientes:
    - Tarjeta de crédito, transferencias bancarias y cheques enviados por correo: Estos métodos presentan 
    comportamientos similares en la retención de clientes. Entre ellos, la tarjeta de crédito destaca como el método 
    con la mejor tasa de retención, seguido de cerca por las transferencias bancarias y los cheques enviados por correo.
    - Cheque electrónico: Este método muestra una tendencia preocupante, con una alta tasa de pérdida de clientes. 
    Comparado con los otros métodos, el cheque electrónico resulta ser el menos efectivo en términos de retención de 
    usuarios.
    En resumen, los métodos de pago como la tarjeta de crédito, transferencias bancarias y cheques enviados por correo 
    son más efectivos para retener clientes, mientras que el cheque electrónico genera una alta tasa de pérdida de 
    usuarios.
    """,
    "monthlycharges": """
     Podemos observar una clara relación entre el costo de los cargos mensuales y el interés y retención de los 
     clientes:
     - Cargos mensuales altos: Los clientes muestran menos interés en contratar opciones con cargos mensuales elevados. 
     Aunque la retención sigue siendo alta, la proporción de clientes perdidos también es significativa, lo que indica 
     que a medida que los cargos mensuales aumentan, la tasa de pérdida de clientes también tiende a aumentar.
     - Cargos mensuales medios: Este grupo es el más popular entre los clientes, ya que prefieren esta opción en mayor 
     número. Sin embargo, también es el grupo con la mayor cantidad de pérdidas de clientes. Esto sugiere que, aunque 
     inicialmente atractivo, los cargos mensuales medios pueden no ser sostenibles para muchos clientes a largo plazo.
     - Cargos mensuales bajos: Las opciones de menor costo tienen una preferencia intermedia, pero destacan por su mejor 
     tasa de retención de clientes en comparación con los otros grupos. Los cargos mensuales bajos parecen ser más 
     manejables y atractivos para los clientes, resultando en una mayor lealtad.
     En resumen, los cargos mensuales altos disuaden a los clientes debido a su costo elevado y presentan una 
     considerable tasa de cancelación. Los cargos mensuales medios, aunque populares, resultan en la mayor cantidad de 
     pérdidas de clientes. Por otro lado, los cargos mensuales bajos logran una mejor tasa de retención, demostrando ser 
     una opción más sostenible y atractiva para los clientes a largo plazo.
     """,
    "totalcharges": """
     El gráfico muestra una relación entre los cargos totales y la fidelización de los clientes:
     - Cargos totales altos: A medida que los cargos totales aumentan, observamos un mayor grado de fidelización entre 
     los clientes. Esto sugiere que los clientes que invierten más en servicios tienden a ser más leales y menos 
     propensos a cancelar.
     - Cargos totales bajos: En contraste, los clientes con cargos totales bajos muestran una menor fidelización. Esto 
     puede indicar que estos clientes son más sensibles al precio y más propensos a cambiar de proveedor o cancelar sus 
     servicios.
     En resumen, los datos sugieren que hay una mayor retención de clientes entre aquellos con cargos totales más altos, 
     mientras que los clientes con cargos bajos tienen una menor retención y son más propensos a abandonar el servicio.
     """
                }

# Clasificación de los valores de la columna en diferentes rangos
dct_bins = {
    "tenure": [0, 1, 5, 10, 50, 100],
    "monthlycharges": [0, 50, 100, 150],
    "totalcharges": [0,1000,2000,3000,4000,5000,6000,7000]
                }

# Funciones
def cs_sidebar():
    """
    Populate the sidebar with various content sections related to Python.
    """
    st.sidebar.title("Telco")

    logo_url = ("https://images.ctfassets.net/te2janzw7nut/6IjJUb0mMnumQJsI1ko8gS/c18b92ecc3206eec9d3c85e367ac74f7/"
                "exit.png?w=1500&h=1000&q=100&fm=webp")
    st.sidebar.image(logo_url, width=200)

    with st.sidebar:
        with st.expander("¿Qué es el Churn?"):
            st.write(
                """
                El *Churn* se refiere a la pérdida de clientes o suscriptores en un período de tiempo determinado.
                En términos simples, es cuando un cliente decide dejar de usar un producto o servicio.
                Las empresas utilizan modelos de *churn* para predecir qué clientes son más propensos a abandonar,
                y así tomar acciones para retenerlos.
                """
            )
        with st.expander("Contexto de Telco"):
            st.write(
                """
                "Predecir el comportamiento para retener a los clientes. Puede analizar todos los datos relevantes de 
                los clientes y desarrollar programas de retención de clientes enfocados".
                """
            )


# Función para capturar la salida de df.info()
def capture_info(df):
    """
        Captura y devuelve la información resumida de un DataFrame.

        Esta función crea un buffer en memoria, lo utiliza para capturar
        la salida del método `info()` del DataFrame y luego devuelve la
        salida capturada como una cadena de texto.

        Parámetros:
        df (pandas.DataFrame): El DataFrame cuya información se va a capturar.

        Retorna:
        str: Una cadena de texto que contiene la información resumida del DataFrame.
        """
    buffer = StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()

def crear_tabla_de_porcentajes(df, columna_grupo, columna_objetivo):
    """
    Crea una tabla de porcentajes a partir de un DataFrame agrupado por una columna específica.

    Parámetros:
    df (pandas.DataFrame): El DataFrame de entrada que contiene los datos.
    columna_grupo (str): El nombre de la columna por la cual se agruparán los datos.
    columna_objetivo (str): El nombre de la columna cuyo conteo se utilizará para calcular los porcentajes.

    Retorna:
    pandas.DataFrame: Un DataFrame con los totales y los porcentajes calculados.
                      Las columnas del DataFrame resultante son:
                      - columna_grupo: Los valores únicos de la columna de agrupación.
                      - columna_objetivo: Los valores únicos de la columna objetivo.
                      - Count: El conteo de ocurrencias para cada combinación de columna_grupo y columna_objetivo.
                      - Percentage: El porcentaje de ocurrencias para cada combinación, calculado respecto al total de la columna_grupo.
    """
    # Calcular los totales
    df_totales = df.groupby([columna_grupo, columna_objetivo]).size().reset_index(name="Count")

    # Calcular los porcentajes
    df_totales["Percentage"] = df_totales.groupby(columna_grupo)["Count"].transform(lambda x: 100 * x / x.sum())

    return df_totales

def crear_tabla_por_rangos(df, columna_grupo, columna_objetivo, bins):
    """
    Crea una tabla que muestra el número de clientes retenidos y perdidos por rango.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        columna_grupo (str): Nombre de la columna que se usará para agrupar en rangos.
        columna_objetivo (str): Nombre de la columna que indica si un cliente se retuvo o se perdió (churn).
        bins (int): Número de bins o rangos para dividir la columna de agrupación.

    Returns:
        pd.DataFrame: DataFrame que muestra el conteo de clientes retenidos y perdidos por rango.
    """

    # Crear una nueva columna 'range' que agrupa los datos en rangos definidos por 'bins'
    df["range_"+columna_grupo] = pd.cut(df[columna_grupo], bins=bins)

    # Eliminar 'left' y 'right' de los intervalos
    df["range_"+columna_grupo] = df["range_"+columna_grupo].apply(lambda x: f"{x.left}-{x.right}")

    # Agrupar el DataFrame por la nueva columna 'range' y por la columna de churn, y contar el número de ocurrencias
    df_rango = df.groupby(["range_"+columna_grupo, columna_objetivo]).size().reset_index().rename(columns={0: "Count"})

    df_rango["Percentage"] = df_rango.groupby("range_"+columna_grupo)["Count"].transform(lambda x: 100 * x / x.sum())

    return df_rango

def crear_grafico(df, columna_grupo, columna_objetivo):
    """
    Genera y muestra un gráfico de barras comparativo entre una variable de grupo y una variable objetivo.

    Parámetros:
    df (DataFrame): El DataFrame que contiene los datos a graficar.
    columna_grupo (str): El nombre de la columna que define los grupos o categorías en el eje X.
    columna_objetivo (str): El nombre de la columna que define las categorías en el eje Y (separadas por colores).

    Funcionalidad:
    - Crea un gráfico de barras que muestra la cantidad de ocurrencias de `columna_objetivo`
      dentro de cada categoría de `columna_grupo`.
    - Añade etiquetas numéricas encima de cada barra para mostrar la cantidad exacta.
    - Personaliza el gráfico con un título, etiquetas de ejes y leyenda.
    - Muestra el gráfico en una aplicación Streamlit.

    """

    # Crear la figura y la gráfica de barras con un tamaño de 8x5 pulgadas
    plt.figure(figsize=(8, 5))

    # Crear un gráfico de barras usando Seaborn con los datos del DataFrame 'df'
    # Se utiliza 'columna_grupo' para el eje X, 'Count' para el eje Y, y se colorea por 'columna_objetivo'
    barplot = sns.barplot(x=columna_grupo, y="Count", hue=columna_objetivo, data=df, palette="Set2")

    # Añadir etiquetas de los valores encima de cada barra en el gráfico
    for p in barplot.patches:
        height = p.get_height()  # Obtener la altura de cada barra
        if height > 0:  # Sólo añadir etiquetas si la barra tiene altura mayor que 0
            barplot.annotate(format(height, ".0f"),  # Formatear el valor de la altura como un número entero
                             (p.get_x() + p.get_width() / 2., height),
                             # Posicionar la etiqueta en el centro de la barra
                             ha="center", va="center",  # Alinear el texto al centro
                             xytext=(0, 9),  # Desplazar la etiqueta hacia arriba para que no se sobreponga a la barra
                             textcoords="offset points")  # Usar unidades de puntos para el desplazamiento

    # Añadir un título a la gráfica y etiquetas a los ejes X e Y
    plt.title(f"{columna_objetivo} versus {columna_grupo}")
    plt.xlabel(columna_grupo)
    plt.ylabel("Count")

    # Ajustar la leyenda del gráfico, mostrando "No" y "Yes" como etiquetas de la leyenda
    handles, labels = barplot.get_legend_handles_labels()
    barplot.legend(handles=handles, labels=["No", "Yes"], title=columna_objetivo)

    # Mostrar la gráfica utilizando Streamlit
    st.pyplot(plt)

def crear_grafico_porcentajes(df, columna_grupo, columna_objetivo):
    """
    Genera y muestra un gráfico de barras comparativo entre una variable de grupo y una variable objetivo.

    Parámetros:
    df (DataFrame): El DataFrame que contiene los datos a graficar.
    columna_grupo (str): El nombre de la columna que define los grupos o categorías en el eje X.
    columna_objetivo (str): El nombre de la columna que define las categorías en el eje Y (separadas por colores).

    Funcionalidad:
    - Crea un gráfico de barras que muestra la cantidad de ocurrencias de `columna_objetivo`
      dentro de cada categoría de `columna_grupo`.
    - Añade etiquetas numéricas encima de cada barra para mostrar la cantidad exacta.
    - Personaliza el gráfico con un título, etiquetas de ejes y leyenda.
    - Muestra el gráfico en una aplicación Streamlit.

    """

    # Crear la figura y la gráfica de barras con un tamaño de 8x5 pulgadas
    plt.figure(figsize=(8, 5))

    # Crear un gráfico de barras usando Seaborn con los datos del DataFrame 'df'
    # Se utiliza 'columna_grupo' para el eje X, 'Count' para el eje Y, y se colorea por 'columna_objetivo'
    barplot = sns.barplot(x=columna_grupo, y="Percentage", hue=columna_objetivo, data=df, palette="Set2")

    # Añadir etiquetas de los valores encima de cada barra en el gráfico
    for p in barplot.patches:
        height = p.get_height()  # Obtener la altura de cada barra
        if height > 0:  # Sólo añadir etiquetas si la barra tiene altura mayor que 0
            barplot.annotate(format(height, ".0f"),  # Formatear el valor de la altura como un número entero
                             (p.get_x() + p.get_width() / 2., height),
                             # Posicionar la etiqueta en el centro de la barra
                             ha="center", va="center",  # Alinear el texto al centro
                             xytext=(0, 9),  # Desplazar la etiqueta hacia arriba para que no se sobreponga a la barra
                             textcoords="offset points")  # Usar unidades de puntos para el desplazamiento

    # Añadir un título a la gráfica y etiquetas a los ejes X e Y
    plt.title(f"{columna_objetivo} versus Percentage {columna_grupo}")
    plt.xlabel(columna_grupo)
    plt.ylabel("Percentage")

    # Ajustar la leyenda del gráfico, mostrando "No" y "Yes" como etiquetas de la leyenda
    handles, labels = barplot.get_legend_handles_labels()
    barplot.legend(handles=handles, labels=["No", "Yes"], title=columna_objetivo)

    # Mostrar la gráfica utilizando Streamlit
    st.pyplot(plt)

def crear_grafico_rangos(df, columna_grupo, columna_objetivo):
    """
    Esta función crea un gráfico de barras utilizando seaborn,
    donde se muestran los rangos de una columna objetivo
    en función de una columna de grupo.

    Parámetros:
    df (DataFrame): El DataFrame que contiene los datos.
    columna_grupo (str): El nombre de la columna que se utiliza como grupo en el eje x.
    columna_objetivo (str): El nombre de la columna objetivo para la que se crean los rangos.

    Retorno:
    None: La función muestra el gráfico en la aplicación Streamlit.
    """

    # Crear la figura y la gráfica de barras
    plt.figure(figsize=(8, 5))
    barplot = sns.barplot(x=columna_grupo, y="Count", hue=columna_objetivo, data=df, palette="Set2")

    # Añadir los números encima de las barras
    for p in barplot.patches:
        width = p.get_width()
        if width > 0:
            barplot.annotate(format(p.get_height(), '.0f'),
                             (p.get_x() + p.get_width() / 2., p.get_height()),
                             ha='center', va='center',
                             xytext=(0, 9),
                             textcoords='offset points')

    # Título y etiquetas
    plt.title(f"{columna_grupo} versus {columna_objetivo}")
    plt.xlabel(columna_grupo)
    plt.ylabel("Count")

    # Ajustar la leyenda
    handles, labels = barplot.get_legend_handles_labels()
    barplot.legend(handles=handles, labels=['No', 'Yes'], title='Pérdida de Clientes')

    # Mostrar la gráfica en Streamlit
    st.pyplot(plt)

def crear_grafico_rangos_porcentajes(df, columna_grupo, columna_objetivo):
    """
    Esta función crea un gráfico de barras utilizando seaborn,
    donde se muestran los rangos de una columna objetivo
    en función de una columna de grupo.

    Parámetros:
    df (DataFrame): El DataFrame que contiene los datos.
    columna_grupo (str): El nombre de la columna que se utiliza como grupo en el eje x.
    columna_objetivo (str): El nombre de la columna objetivo para la que se crean los rangos.

    Retorno:
    None: La función muestra el gráfico en la aplicación Streamlit.
    """

    # Crear la figura y la gráfica de barras
    plt.figure(figsize=(8, 5))
    barplot = sns.barplot(x=columna_grupo, y="Percentage", hue=columna_objetivo, data=df, palette="Set2")

    # Añadir los números encima de las barras
    for p in barplot.patches:
        width = p.get_width()
        if width > 0:
            barplot.annotate(format(p.get_height(), '.0f'),
                             (p.get_x() + p.get_width() / 2., p.get_height()),
                             ha='center', va='center',
                             xytext=(0, 9),
                             textcoords='offset points')

    # Título y etiquetas
    plt.title(f"{columna_grupo} versus Percentage {columna_objetivo}")
    plt.xlabel(columna_grupo)
    plt.ylabel("Percentage")

    # Ajustar la leyenda
    handles, labels = barplot.get_legend_handles_labels()
    barplot.legend(handles=handles, labels=['No', 'Yes'], title='Pérdida de Clientes')

    # Mostrar la gráfica en Streamlit
    st.pyplot(plt)
def cs_body():
    """
    Create content sections for the main body of the
    Streamlit cheat sheet with Python examples.
    """
    # Este es un título principal
    st.title("Telco Customer Churn")

    imagen_churn = ("modelo_de_churn.jpg")
    st.image(imagen_churn, width = 300)

    if st.checkbox("Análisis y Predicción del Comportamiento de los Clientes para la Retención y Mejora de Servicios"):
        st.markdown("""
        #### Contenido
        Cada fila representa un cliente, cada columna contiene los atributos del cliente descritos en la columna 
        Metadatos.
        El conjunto de datos incluye información sobre:
        * Clientes que se fueron en el último mes: la columna se llama "Churn".
        * Servicios a los que se ha registrado cada cliente: phone, multiple lines, internet, online security, online 
        backup, device protection, tech support, y streaming TV and movies.
        * Información de la cuenta del cliente: how long they’ve been a customer, contract, payment method, paperless 
        billing, monthly charges, y total charges.
        * Información demográfica sobre los clientes: sexo, rango de edad y si tienen parejas y dependientes.
        #### Inspiración
        Para explorar este tipo de modelos y conocer más sobre el tema.
        """)

    # Cargar datos
    st.markdown("### Tabla de datos")
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

    # Eliminar columna
    df = df.drop(["customerID"], axis=1)

    # Dejar nombres de columnas en minúsculas
    df.columns = df.columns.str.lower()

    # Cambiar datos a numéricos
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

    # Mostrar primeras filas
    st.dataframe(df.head())

    indices_tenure_zero = df[df["tenure"] == 0].index.tolist()

    # Eliminar filas
    df = df.drop(labels=df[df["tenure"] == 0].index, axis=0)

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Modificar los valores
    df["seniorcitizen"] = df["seniorcitizen"].map({0: "No", 1: "Yes"})

    # Crea un selectbox para seleccionar una opción
    opcion = st.selectbox(
        "Información relevante:",
        ["Seleccionar opción", "Información", "Tipos", "Nulos", "Duplicados"]
    )

    # Muestra el DataFrame y la información basada en la opción seleccionada
    if opcion == "Información":
        st.write("Información del DataFrame:")
        st.text(capture_info(df))
    if opcion == "Tipos":
        st.write("Tipos de datos en el DataFrame:")
        st.write(df.dtypes.rename("Type"))
    if opcion == "Nulos":
        st.write("Número de valores nulos en cada columna:")
        st.write(df.isnull().sum().rename("Null"))
    if opcion == "Duplicados":
        st.write("Número de filas duplicadas:")
        st.write(df.duplicated().sum())

    if st.checkbox("Mostrar conclusión de la limpieza de datos"):
        st.markdown("""
        ### Resumen
        En el proceso de análisis y limpieza de datos, se verificó el tamaño del DataFrame, compuesto por 21 columnas y 
        7043 filas con diferentes tipos de datos. Se realizaron modificaciones en los nombres de las columnas y se 
        eliminaron aquellas sin relevancia. Además, se abordaron y corrigieron incongruencias en los tipos de datos y 
        valores nulos. También se eliminaron filas duplicadas y se estandarizaron ciertos valores para mantener la 
        coherencia en el conjunto de datos.
        ### Conclusiones Intermedias
        1. *Verificación y Modificación Inicial:* Se confirmó que los datos se cargaron adecuadamente y se realizaron 
        ajustes en los nombres de las columnas, eliminando las que no aportaban información relevante.
        2. *Corrección de Tipos de Datos:* Se identificó y corrigió una incongruencia en la columna `totalcharges`, 
        cambiando su tipo de objeto a flotante y eliminando las filas con valores nulos resultantes.
        3. *Eliminación de Duplicados:* Se detectaron y eliminaron 22 filas duplicadas para asegurar la integridad del 
        conjunto de datos. 
        4. *Estandarización de Valores:* La columna `seniorcitizen` fue estandarizada para tener valores coherentes con 
        el resto de la tabla.
        ### Conclusión General
        La etapa de limpieza de datos se completó exitosamente, asegurando la integridad y coherencia del conjunto de 
        datos. Con estos ajustes, se eliminó la información redundante e incongruente, y se estandarizaron los valores 
        para proceder con un análisis exploratorio de datos más preciso y confiable.
        """
            )

    # Seleccionar las columnas para agrupar
    columnas_validas = [x for x in df.columns if x not in ["churn"]]
    default_option = "Selecciona la columna"
    columnas_options = [default_option] + columnas_validas
    # Mostrar el selector de columna
    columna_grupo = st.selectbox(default_option, columnas_options)
    columna_objetivo = "churn"
    # Asegúrate de que "columna_grupo" no sea el valor por defecto
    if columna_grupo != default_option:
        if columna_grupo not in ["tenure", "monthlycharges", "totalcharges"]:
            st.write(dct_introduccion[columna_grupo])
            resultado = crear_tabla_de_porcentajes(df, columna_grupo, columna_objetivo)
            st.write("Resultado:")
            st.write(resultado)
            crear_grafico(resultado, columna_grupo, columna_objetivo)
            crear_grafico_porcentajes(resultado, columna_grupo, columna_objetivo)
            st.write(dct_conclusion[columna_grupo])
        else:
            st.write(dct_introduccion[columna_grupo])
            temp = crear_tabla_por_rangos(df, columna_grupo, columna_objetivo, dct_bins[columna_grupo])
            st.write("Resultado:")
            st.write(temp)
            crear_grafico_rangos(temp, "range_" + columna_grupo, "churn")
            crear_grafico_rangos_porcentajes(temp, "range_" + columna_grupo, columna_objetivo)
            st.write(dct_conclusion[columna_grupo])

    if st.checkbox("Conclusión General"):
        st.markdown("""
        La retención de clientes en la empresa está fuertemente influenciada por diversos factores demográficos y 
        relacionados con los servicios ofrecidos.
        ##### Factores Demográficos:
        - Género: Tanto hombres como mujeres muestran patrones similares de retención y pérdida de clientes, sugiriendo 
        que el género no es un diferenciador significativo en la fidelización de clientes.
        - Ciudadanía Sénior: Los clientes jubilados muestran una mayor tasa de pérdida, posiblemente porque no son el 
        objetivo principal de la empresa. En contraste, los clientes que tienen pareja y dependientes tienden a mostrar 
        una mayor retención, lo que indica que estos factores demográficos contribuyen positivamente a la lealtad del 
        cliente.
        ##### Duración y Compromiso del Cliente:
        - Tenencia: La retención mejora significativamente con el tiempo, y los clientes que permanecen más allá de los 
        primeros meses son más propensos a continuar con la empresa a largo plazo. Este patrón sugiere que las 
        estrategias de retención deben enfocarse en los clientes nuevos para reducir las tasas de pérdida inicial.
        - Tipo de Contrato: Los contratos a largo plazo (uno o dos años) tienen una influencia positiva significativa en 
        la retención de clientes, en comparación con los contratos mensuales que presentan mayores tasas de cancelación.
        ##### Servicios y Métodos de Pago:
        - Servicios Adicionales: La disponibilidad de servicios como Internet, seguridad en línea y protección de 
        dispositivos tienen un impacto mixto en la retención. Los clientes con estos servicios generalmente muestran 
        una buena retención, pero aquellos sin servicio de Internet presentan la mayor tasa de retención, lo que podría 
        indicar una preferencia por servicios esenciales y básicos.
        - Métodos de Pago: La tarjeta de crédito, transferencias bancarias y cheques por correo son más efectivos en la 
        retención de clientes. Por otro lado, el cheque electrónico se asocia con una alta tasa de pérdida de clientes, 
        sugiriendo que no es un método de pago preferido.
        ##### Cargos y Costos:
        - Cargos Mensuales: Las tarifas mensuales tienen una relación directa con la retención. Los cargos altos 
        disuaden a los clientes, mientras que los cargos bajos tienden a ser más atractivos y resultan en una mayor 
        lealtad.
        - Cargos Totales: Los clientes que pagan más en términos de cargos totales tienden a ser más leales, lo que 
        sugiere que el valor percibido del servicio está alineado con un mayor compromiso y fidelización.
        """)

    # Función para mostrar el mensaje letra por letra
    def show_typing_effect(message, delay=0.1):
        # Usa un contenedor vacío para actualizar el texto
        text_placeholder = st.empty()
        text = ""

        for char in message:
            text += char
            text_placeholder.markdown(text)
            time.sleep(delay)

    # Mensaje final
    message = "🎉 ¡Gracias por leer! 🎉\nEsperamos que lo hayas disfrutado. ¡Hasta la próxima!"
    show_typing_effect(message)

    # Usar st.feedback para mostrar un botón de retroalimentación
    st.feedback()

if __name__ == "__main__":
    main()