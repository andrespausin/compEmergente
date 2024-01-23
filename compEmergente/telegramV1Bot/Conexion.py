from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Para iniciar el bot debes poner en el terminal "python Conexion.py"

# https://blog.bitso.com/es-ar/criptomonedas-ar/que-relacion-tiene-el-blockchain-con-las-criptomonedas#:~:text=Se%20basan%20en%20el%20blockchain,%C3%A1mbito%2C%20pero%20existen%20muchas%20otras.

token = '6838676691:AAEHQ_AMtD_Bwp4swf_a27PVcbH8UUfwAHI'
user_name = 'madrizbot'

"""    Comandos     """

async def start(update: Update, context: ContextTypes):
    await update.message.reply_text("Hola, soy un bot. ¿En qué puedo ayudarte?")

async def mercado(update: Update, context: ContextTypes):
    await update.message.reply_text("¿Deseas saber de las tendencias actuales del mercado o tienes alguna duda sobre alguna tendencia?")
    
"""     Respuestas del Bot     """

def handle_response(text: str, context: ContextTypes, update: Update):
    
    texto_procesado = text.lower()
    validar_Comando = text[0]
    print(texto_procesado)
    
    # Respuestas del comando start
    
    if 'hola' == texto_procesado:
        return 'hola, ¿Como estas?'
    
    elif 'necesito ayuda' == texto_procesado:
        return 'Estaria encantado en poder ayudarte'
    
    elif '/' == validar_Comando:
        return f'El Comando "{texto_procesado}" no esta disponible'
    
    # Respuestas referente a la Blockchain
    
    elif ('conoces' in texto_procesado or 'sabes' in texto_procesado) and 'blockchain' in texto_procesado:
        respuesta = 'Sí, conozco bastante sobre blockchain. La blockchain es una tecnología de contabilidad distribuida que subyace en las criptomonedas como Bitcoin y Ethereum. ¿En qué aspecto específico de blockchain estás interesado?'

        return respuesta

    
    # Respuesta referente a los aspecto de la blockchain
    
    elif 'aspectos' in texto_procesado and 'blockchain' in texto_procesado:
        cripto = "La blockchain es fundamental para el funcionamiento de las criptomonedas como Bitcoin, Ethereum, y muchas otras. Esta aplicación específica de la blockchain se centra en la creación, transferencia y verificación de transacciones de activos digitales."
        contratos = "La blockchain también se utiliza para ejecutar contratos inteligentes, que son acuerdos digitales autoejecutables que eliminan la necesidad de intermediarios en transacciones comerciales."
        aplicaciones = "La blockchain es la base de las aplicaciones descentralizadas que operan sin un punto central de control, lo que las hace más seguras y transparentes."
        gestion = "La blockchain se utiliza para la gestión de identidad digital, lo que permite a las personas tener un control más directo sobre su información personal."
        cadena = "La blockchain se utiliza para rastrear el origen y la autenticidad de los productos a lo largo de la cadena de suministro, lo que ayuda a prevenir la falsificación y garantizar la transparencia"
        
        texto = f"la blockchain puede referirse a varios aspectos o conceptos relacionados. Aunque la tecnología blockchain es más conocida por su asociación con las criptomonedas, su alcance es mucho más amplio. Aquí hay algunos aspectos en los que la blockchain puede estar involucrada: \n\n - Criptomonedas: {cripto} \n\n - Contratos Inteligentes: {contratos} \n\n - Aplicaciones Descentralizadas (dApps): {aplicaciones} \n\n - Gestion de identidad: {gestion} \n\n - Seguimiento de la cadena de suministro: {cadena} \n\n Estos son solo algunos ejemplos de los diversos aspectos en los que la blockchain está involucrada. Su versatilidad y aplicaciones potenciales la hacen una tecnología muy prometedora en varios campos." 
        return texto
    
    # Respuesta referente a las areas de la blockchain
    
    elif 'areas' in texto_procesado and 'blockchain' in texto_procesado:
        areas = 'La tecnología Blockchain se extiende más allá de las criptomonedas como Bitcoin y abarca diversos sectores y aplicaciones. Sirve como una base de datos de red descentralizada que garantiza la inmutabilidad y trazabilidad de todos los intercambios de información dentro de ella. El potencial de blockchain abarca múltiples aspectos, incluidos los dominios financiero, logístico, legal y tecnológico. Sus cualidades clave, como eficiencia, seguridad y transparencia, lo hacen indispensable en diversos campos. Además, blockchain se ha implementado en logística, verificación de propiedad y ejecución de contratos inteligentes. Su impacto es evidente en sectores como el minorista, donde empresas como Walmart han utilizado blockchain para mejorar la gestión de datos y el seguimiento de productos. Además, la tecnología blockchain tiene el potencial de abordar desafíos en áreas con infraestructura gubernamental limitada, proporcionando un método transparente y seguro para establecer la propiedad.'
        puntos_claves_1 = "La tecnología Blockchain se extiende más allá de las criptomonedas como Bitcoin."
        puntos_claves_2 = "Garantiza la inmutabilidad y trazabilidad de los intercambios de información."
        puntos_claves_3 = "Su potencial se extiende a través de dominios financieros, logísticos, legales y tecnológicos."
        puntos_claves_4 = "Blockchain se ha implementado en logística, verificación de propiedad y ejecución de contratos inteligentes."
        puntos_claves_5 = "Empresas como Walmart han utilizado blockchain para mejorar la gestión de datos y el seguimiento de productos."
        
        return f"{areas} \n\n Puntos Claves: \n\n - {puntos_claves_1} \n - {puntos_claves_2}\n - {puntos_claves_3} \n - {puntos_claves_4} \n - {puntos_claves_5} "
    
    # Respuesta referente a Cuáles son las características / propiedades clave de Blockchain
    
    elif ('cuales' in texto_procesado or 'cuáles' in texto_procesado or 'cuantas' in texto_procesado or 'características' in texto_procesado or 'caracteristicas' in texto_procesado or 'propiedades' in texto_procesado or 'característica' in texto_procesado or 'caracteristica' in texto_procesado) and 'blockchain' in texto_procesado and 'clave' in texto_procesado:
        puntos_claves_1 = 'Blockchain como estructura de datos: Blockchain puede actuar como una estructura de datos y almacenar diferentes tipos de datos, incluida información de identidad, de seguros, médica, etc.'
        puntos_claves_2 = 'Inmutabilidad: los datos una vez almacenados en la blockchain son inmutables. Esto le da a la blockchain la propiedad de detección de manipulación indebida también.'
        puntos_claves_3 = 'Protección de datos:  la protección de datos depende completamente de la fuente. La ausencia de actores externos también significa que es seguro y ofrece la mejor protección de datos.'
        puntos_claves_4 = 'Tecnología de registro descentralizado: la tecnología de registro descentralizado es la característica más importante de una blockchain. Puede ser utilizada por una organización privada o pública en una variedad de casos de uso.'
        puntos_claves_5 = 'Mejor anonimato del usuario: los usuarios están relativamente ocultos en comparación con otras redes tradicionales.'
        puntos_claves_6 = 'Doble gasto: Blockchain resuelve problemas de doble gasto utilizando algoritmos de consenso y tecnología de registro distribuido'
        url_1 = 'https://101blockchains.com/es/caracteristicas-tecnologia-blockchain/'
        return f"- {puntos_claves_1} \n\n - {puntos_claves_2} \n\n - {puntos_claves_3} \n\n - {puntos_claves_4} \n\n - {puntos_claves_5} \n\n - {puntos_claves_6} \n\n Para más información visita a las paginas: {url_1} "
    
    # Respuesta referente a los Beneficios de Blockchain
    
    elif ('cuáles' in texto_procesado or 'cuales' in texto_procesado) and 'blockchain' in texto_procesado and 'beneficios' in texto_procesado:
        puntos_claves_1 = 'Los principales beneficios de blockchain incluyen los siguientes'
        puntos_claves_2 = 'Transparencia mejorada'
        puntos_claves_3 = 'Seguridad incrementada'
        puntos_claves_4 = 'Mejor trazabilidad'
        puntos_claves_5 = 'Mayor velocidad y eficiencia'
        puntos_claves_6 = 'Costos reducidos'
        return f"{puntos_claves_1} \n\n - {puntos_claves_2} \n - {puntos_claves_3} \n - {puntos_claves_4} \n- {puntos_claves_5} \n- {puntos_claves_6}"
    
    # Respuesta referente a las categorias de la blockchain
    
    elif ('cuales' in texto_procesado or 'cuáles' in texto_procesado or 'cuantas' in texto_procesado or 'categorias' in texto_procesado or 'categoria' in texto_procesado) and 'blockchain' in texto_procesado:
        categorias = 'La tecnología blockchain se divide en diferentes categorías, cada una con capacidades y características únicas adaptadas a diferentes necesidades. Algunas de las categorías incluyen:'
        puntos_claves_1 = 'Blockchain Público: Este tipo de blockchain es accesible para cualquier persona y permite la participación abierta en la red. Las transacciones son transparentes y verificables por cualquier usuario.'
        puntos_claves_2 = 'Blockchain Privado: A diferencia del blockchain público, el blockchain privado restringe el acceso a la red ya las transacciones a un grupo específico de participantes autorizados.'
        puntos_claves_3 = 'Federado Blockchain: En este tipo de blockchain, un grupo selecto de nodos tiene la autoridad para validar transacciones, lo que permite un mayor control sobre la red.'
        puntos_claves_4 = 'Blockchain Híbrido: La blockchain híbrida combina características de la blockchain pública y privada, permitiendo que parte de los datos almacenados en la cadena de bloques sean públicos y otros privados.'
        puntos_claves_5 = 'Estas categorías ofrecen diferentes enfoques para el uso de la tecnología blockchain en diversos contextos, desde transacciones de criptomonedas hasta aplicaciones empresariales y financieras.'
        url = 'https://www.welivesecurity.com/la-es/2022/05/13/blockchain-que-es-como-funciona-y-como-se-esta-usando-en-el-mercado/'
        
        return f"{categorias} \n\n - {puntos_claves_1} \n\n - {puntos_claves_2}\n\n - {puntos_claves_3} \n\n - {puntos_claves_4} \n\n {puntos_claves_5} \n\n Para más información visita la pagina: {url}"
    
    elif ('publicas' in texto_procesado or 'públicas' in texto_procesado or 'publica' in texto_procesado or 'pública' in texto_procesado or 'privadas' in texto_procesado or 'privada' in texto_procesado) and 'blockchain' in texto_procesado and 'diferencias' in texto_procesado:
        puntos_claves_1 = 'Se construye para uso general y es accesible para cualquier persona.'
        puntos_claves_2 = 'Es descentralizada y transparente, lo que significa que cualquiera puede participar, ver y validar transacciones.'
        puntos_claves_3 = 'Las transacciones son más costosas en términos de energía eléctrica.'
        puntos_claves_4 = 'Los ejemplos incluyen Bitcoin y Ethereum.'
        puntos_claves_5 = 'Se construye generalmente para uso empresarial y está controlado por un consorcio de usuarios privilegiados.'
        puntos_claves_6 = 'Los usuarios privilegiados pueden emitir o denegar permisos, alterar reglas, revertir transacciones y modificar saldos.'
        puntos_claves_7 = 'Los validadores son conocidos de confianza y despliegan menos costos operativos.'
        puntos_claves_8 = 'Es más rápido y escalable que la pública, pero también más centralizada y menos segura.'
        
        resumen = 'En resumen. Las blockchains públicas y privadas tienen potencialidades y características distintas. Las blockchains públicas ofrecen transparencia y seguridad, mientras que las blockchains privadas ofrecen control y privacidad. La elección entre una u otra dependerá del caso de uso y los requisitos específicos del proyecto. Ambas tecnologías tienen un papel importante en la revolución de las transacciones digitales y la gestión de datos.'
        url_1 = 'https://observatorioblockchain.com/blockchain/diferencias-entre-blockchain-publicas-y-privadas/#:~:text=Las%20blockchains%20p%C3%BAblicas%20ofrecen%20transparencia,los%20requisitos%20espec%C3%ADficos%20del%20proyecto.'
        
        return f"Las diferencias entre las blockchains privadas y públicas son significativas y se relacionan con su estructura y uso. \n\n Blockchain Pública: \n\n - {puntos_claves_1} \n - {puntos_claves_2} \n - {puntos_claves_3} \n - {puntos_claves_4} \n\n Blockchain Privada: \n\n - {puntos_claves_5} \n - {puntos_claves_6} \n - {puntos_claves_7} \n - {puntos_claves_8} \n\n {resumen} \n\n Para más información visita a las paginas: {url_1} "
    
    
    elif ('publica' in texto_procesado or 'pública' in texto_procesado) and 'blockchain' in texto_procesado:
        respuesta = 'Una blockchain pública es una red abierta y descentralizada que permite a cualquier persona participar en la validación de transacciones y la creación de nuevos bloques. Cualquier persona puede unirse a la red y utilizar sus recursos para verificar transacciones, lo que se conoce como minería. Un ejemplo de blockchain pública es Bitcoin, donde cualquier persona puede unirse a la red y convertirse en un minero.'
        return respuesta
    
    elif 'privada' in texto_procesado and 'blockchain' in texto_procesado:
        respuesta = 'Una blockchain privada es una red cerrada y controlada por una organización o entidad central. Solo las personas autorizadas pueden acceder a la red y validar transacciones. Esto hace que las blockchains privadas sean más rápidas y escalables que las públicas, pero también más centralizadas y menos seguras. Un ejemplo de blockchain privada es Hyperledger Fabric, utilizado por empresas y organizaciones para gestionar sus transacciones internas'
        return respuesta
    
    elif 'federado' in texto_procesado and 'blockchain' in texto_procesado:
        federado = 'La tecnología blockchain federada, también conocida como blockchain consorciada, combina características de los blockchains públicos y privados. Aquí hay un resumen de sus características:'
        puntos_claves_1 = 'Similitudes con Blockchain Privado: La blockchain federada comparte similitudes con la blockchain privada, ya que restringe el acceso a la red ya las transacciones a un grupo específico de participantes autorizados.'
        puntos_claves_2 = 'Ventajas sobre Blockchain Público: A diferencia de la blockchain pública, la federada puede abordar desventajas como la escalabilidad, la privacidad y la producción más lenta.'
        puntos_claves_3 = 'Uso en el Mundo Empresarial: La federada blockchain tiene el potencial de empoderar el mundo empresarial al ofrecer un equilibrio entre la transparencia y la privacidad, lo que la hace atractiva para aplicaciones empresariales.'
        resumen = 'La tecnología blockchain federada es una opción atractiva para aquellos que buscan un equilibrio entre la transparencia de un blockchain público y la privacidad de un blockchain privado.'
        respuesta = 'Una blockchain pública es una red abierta y descentralizada que permite a cualquier persona particip   ar en la validación de transacciones y la creación de nuevos bloques. Cualquier persona puede unirse a la red y utilizar sus recursos para verificar transacciones, lo que se conoce como minería. Un ejemplo de blockchain pública es Bitcoin, donde cualquier persona puede unirse a la red y convertirse en un minero.'
        return f"{federado} \n\n - {puntos_claves_1} \n\n - {puntos_claves_2}\n\n - {puntos_claves_3} \n\n {resumen}"
    
    elif ('hibrido' in texto_procesado or 'híbrido' in texto_procesado) and 'blockchain' in texto_procesado:
        puntos_claves_1 = 'La blockchain híbrida es una combinación de entidades públicas y privadas, lo que la convierte en una especie de "mejor de ambos mundos". Técnicamente, funciona al generar bloques de datos con una red privada alojada en una blockchain pública. Esto significa que hay una participación restringida que se controla a través de la propia blockchain privada. La blockchain híbrida ofrece la flexibilidad y personalización de la blockchain privada, así como la transparencia y accesibilidad de la blockchain pública'
        puntos_claves_2 = 'Esta combinación permite resolver muchos problemas de seguridad y ofrece una solución para casos de uso específicos, como el Internet de las cosas (IoT) híbrido, donde los dispositivos pueden colocarse en una red privada con acceso restringido a los datos necesarios, lo que resuelve los problemas. de seguridad asociados con soluciones de blockchain pública completa'
        url_1 = 'https://101blockchains.com/es/blockchain-hibrida/'
        url_2 = 'https://keepcoding.io/blog/que-es-una-blockchain-hibrida/'
        return f"{puntos_claves_1} \n\n {puntos_claves_2} \n\n Para más información visita a las paginas: {url_1} \n\n {url_2}"
    
    # Respuesta referente a la confianza que inspira la blockchain
    
    elif ('confianza' in texto_procesado or 'inspira' in texto_procesado) and 'blockchain' in texto_procesado:
        puntos_claves_1 = 'Blockchain es una red punto a punto que tiene su algoritmo de consenso. La razón principal detrás de su confiabilidad es cómo almacena y maneja los datos. Utiliza algoritmos criptográficos para garantizar que los datos estén protegidos contra cualquier acto malicioso de terceros. Esto significa que solo la entidad que posee los datos podrá acceder a ellos. Además, los almacenes de datos en la blockchain se pueden rastrear en cualquier momento, lo que aporta transparencia. Una cosa más que hace confiable a blockchain es la característica de integridad de datos. Con esta característica, los datos no se pueden cambiar después de que se escriben.'

        return f"{puntos_claves_1}"
    
    # Respuesta referente al Ethereum
    
    elif ('que es' in texto_procesado or 'qué es' in texto_procesado) and 'ethereum' in texto_procesado:
        puntos_claves_1 = 'Ethereum es un sistema descentralizado al igual que Bitcoin. Está completamente descentralizado, lo que significa que no hay una autoridad central que lo controle. Está desarrollado por Vitalik Buterin y utiliza un enfoque diferente en comparación con Bitcoin. Al igual que Bitcoin, los pagos digitales se pueden hacer en la plataforma. Utiliza contratos inteligentes para automatizar contratos legales dentro de dos pares. dApps (aplicaciones descentralizadas) es una aplicación que se ejecuta en Ethereum y utiliza contratos inteligentes para administrar una organización o una parte específica del proyecto.'
        url_1 = 'https://es.wikipedia.org/wiki/Ethereum'
        return f"{puntos_claves_1} \n\n Para más información visita a la pagina: {url_1}"
    
    # Respuesta referente al Bitcoin
    
    elif ('que es' in texto_procesado or 'qué es' in texto_procesado) and 'bitcoin' in texto_procesado:
        puntos_claves_1 = 'Bitcoin es una criptomoneda o moneda virtual, concretamente la primera que fue desarrollada. Es la criptomoneda que le ha marcado el camino a todos los demás que llegaron después utilizando su tecnología. Fue creado en 2009 por una persona o grupo de personas bajo el seudónimo de "Satoshi Nakamoto". Bitcoin es una moneda digital descentralizada que permite un nuevo sistema de pago y una moneda completamente digital. Es la primera red entre pares de pago descentralizado impulsado por sus usuarios sin una autoridad central o intermediarios. Las transacciones en Bitcoin quedan registradas en una base de datos pública y accesible, y es una red descentralizada, lo que implica que no hay ningún banco central que controle el precio de Bitcoin o la emisión de moneda. Bitcoin es utilizado por millones de usuarios en todo el mundo para transferir y resguardar valor, realizar compras y pagos, y hasta para ahorrar.'
        url_1 = 'https://en.wikipedia.org/wiki/Bitcoin#Introduction'
        return f"{puntos_claves_1} \n\n Para más información visita a la pagina: {url_1}"
    
    # Respuesta referente a la clave publica
    
    elif ('que es' in texto_procesado or 'qué es' in texto_procesado or 'publica' in texto_procesado or 'pública' in texto_procesado) and 'clave' in texto_procesado:
        puntos_claves_1 = 'Se utiliza una clave pública en el algoritmo criptográfico que permite a los pares en una blockchain recibir fondos en su billetera. La clave pública se adjunta a una clave privada creando un par de claves. El par de la clave pública-privada se utiliza para garantizar la seguridad de la blockchain. Una clave pública es una cadena alfanumérica que es única para un nodo o dirección en particular.'
        return f"{puntos_claves_1}"
    
    # Respuesta referente a la clave privada
    
    elif ('que es' in texto_procesado or 'qué es' in texto_procesado) and 'clave' in texto_procesado and 'privada' in texto_procesado:
        puntos_claves_1 = 'Una clave privada es una frase alfanumérica que se usa junto con una clave pública para proporcionar cifrado y descifrado. Es parte de los algoritmos criptográficos que se utilizan en la seguridad de blockchain. La clave está asignada al generador de la clave y debe permanecer solo con él. Si no lo hace, cualquiera puede acceder a los detalles o datos ubicados dentro de la cartera o la dirección para la que se asigna la clave privada.'
        return f"{puntos_claves_1}"
    
    # Respuesta referente a la diferencia entre las Blockchains Ethereum y Bitcoin
    
    elif ('diferencia' in texto_procesado or 'diferencias' in texto_procesado) and 'ethereum' in texto_procesado and 'bitcoin' in texto_procesado:
        puntos_claves_1 = 'Una blockchain es una red distribuida de punto a punto. Ofrece a sus pares el registro de datos inmutables y transparencia. La diferencia entre Bitcoin y Ethereum es su enfoque. Ethereum, al ser la solución de blockchain de segunda generación, mejora Bitcoin en casi todas las formas posibles. La principal diferencia es cómo intentan resolver el problema de la industria. Conceptualmente, Bitcoin es una moneda digital, mientras que Ethereum se trata de contratos inteligentes. Ethereum también es energéticamente eficiente ya que utiliza el algoritmo de consenso de Proof-of-Stake (PoS) en comparación con la Proof-of-Work (PoW) de Bitcoin. Esto también hace que Ethereum sea más escalable en comparación con Bitcoin.'
        return f"{puntos_claves_1}"
    
    # Respuesta referente a que si la blockchain es totalmente diferente del registro bancario
    
    elif ('diferente' in texto_procesado or 'diferentes' in texto_procesado) and 'blockchain' in texto_procesado and 'registro' in texto_procesado and 'bancario' in texto_procesado:
        puntos_claves_1 = 'Los registros bancarios se utilizan para garantizar que las transacciones puedan realizarse correctamente. Es por eso que rastrean y marcan las transacciones. La diferencia significativa entre un registro bancario y una blockchain es cómo se gobiernan. La blockchain es de naturaleza descentralizada; sin embargo, los registros bancarios están completamente centralizados a medida que los bancos los gobiernan. La blockchain es completamente transparente y confiable en comparación con los registros del banco. Los bancos están interesados en la tecnología blockchain, ya que pueden automatizar la mayoría de sus funcionalidades bancarias y también proporcionar un enfoque confiable. Sin embargo, es más probable que utilicen una blockchain federada o una blockchain privada para asegurarse de que aún tienen control sobre sus operaciones.'
        return f"{puntos_claves_1}"
    
    # Respuesta referente a las Características de la Wallet Blockchain
    
    elif ('características' in texto_procesado or 'caracteristicas' in texto_procesado or 'característica' in texto_procesado or 'caracteristica' in texto_procesado) and 'blockchain' in texto_procesado and 'wallet' in texto_procesado:
        puntos_claves_1 = 'Billetera digital : Blockchain Wallet es una billetera digital que permite a los usuarios almacenar y administrar sus Bitcoin, Ether y otras criptomonedas.'
        puntos_claves_2 = 'Servicio de billetera electrónica : proporciona un servicio de billetera electrónica que permite a las personas almacenar y transferir criptomonedas.'
        puntos_claves_3 = 'Gestión de criptomonedas : los usuarios pueden gestionar sus saldos de Bitcoin, Ether y otros criptoactivos utilizando Blockchain Wallet.'
        puntos_claves_4 = 'Tarifas de transacción dinámica : Blockchain Wallet cobra tarifas dinámicas, lo que significa que las tarifas de transacción pueden variar según factores como el tamaño de la transacción.'
        return f"- {puntos_claves_1} \n\n - {puntos_claves_2} \n\n - {puntos_claves_3} \n\n - {puntos_claves_4}"
    
    # Respuesta referente a la Seguridad o Confianza de la Wallet Blockchain
    
    elif ('seguridad' in texto_procesado or 'confianza' in texto_procesado) and 'blockchain' in texto_procesado and 'wallet' in texto_procesado:
        puntos_claves_1 = 'Blockchain Wallet es conocido por sus sólidas funciones de seguridad, que garantizan la seguridad de los activos digitales de los usuarios. La plataforma se ha ganado la confianza de millones de usuarios y se considera una de las billeteras más confiables en el espacio de las criptomonedas.'
        return f"{puntos_claves_1}"
    
    # Respuesta referente a la Blockchain wallet
    
    elif ('wallet' in texto_procesado or 'billetera' in texto_procesado) and 'blockchain' in texto_procesado:
        puntos_claves_1 = 'Blockchain.com es una plataforma ampliamente reconocida para transacciones y gestión de criptomonedas. Ofrece una gama de servicios relacionados con las criptomonedas, incluida la compra, venta y almacenamiento de diversos activos digitales. La plataforma es conocida por su interfaz fácil de usar y sus sólidas funciones de seguridad.'
        return f"{puntos_claves_1}"
    
    # Respuesta referente a las 
    
    elif ('ejemplo1' in texto_procesado or 'ejemplo2' in texto_procesado) and 'ejemplo3' in texto_procesado:
        puntos_claves_1 = ''
        url_1 = ''
        return f"{puntos_claves_1} \n\n Para más información visita a las paginas: {url_1}"
    
    # Respuestas del comando mercado
    
    else:
        return 'no tengo respuesta para lo que me acabas de indicar'
    
"""     Respuesta si es Privada o en Grupo   """

async def handle_message(update: Update, context: ContextTypes):
    
    tipo_mensaje = update.message.chat.type # privado o grupo
    text = update.message.text
    
    if tipo_mensaje == 'group':
        if text.startswith(user_name):
            new_text = text.replace(user_name, '')
            response = handle_response(new_text, context, update)
        else:
            return
    else:
        response = handle_response(text, context, update)
        
    await update.message.reply_text(response)

    
"""     Manejo de erroe    """

async def error(context: ContextTypes, update: Update):
    print(context.error)
    await update.message.reply_text('Ha ocurrido un error')
    
"""     Main    """

if __name__ == '__main__':
    print('Iniciando bot...')
    app = Application.builder().token(token).build() #Se crea la app
    
    # Creamos los comandos
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('mercado', mercado))
    
    # Creamos las respuestas
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Creamos los errores
    app.add_error_handler(error)
    
    # Iniciamos el Bot
    print('Bot iniciado')
    app.run_polling(poll_interval=1, timeout=10)