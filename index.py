import logging
import re
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Frases Para el Bot
frases = [
    {
        "author": "Matsuno Yutaka",
        "manga": "Umi ga Kikoeru",
        "frase": "Un cambio de aires siempre sienta bien."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "El la ropa negra se ve mucho mejor y mas bonito cuando alguien a la moda y elegante lo lleva puesto, pero para mi es solo un color que no..."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Incluso la gente sin amigos usa las redes sociales para comunicarse, aunque solo sea con la familia."
    },
    {
        "author": "Aioi Aoi",
        "manga": "Sora no Aosa wo Shiru Hito yo",
        "frase": "Si no puedes apoyar los sentimientos de quien amas, te arrepentirás toda la vida."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Cualquiera que dude en matar terminará muerto."
    },
    {
        "author": "Ichikawa Kana",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "No se trata de tener una oportunidad, si no de lo que realmente quieres, todo empieza desde allí."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Los milagros no existen, nunca existió una oportunidad así, sin embargo quiero creer en los milagros, en mí mismo."
    },
    {
        "author": "Profesora",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "A veces las personas no se dan cuenta de lo obvio hasta que se lo mencionan."
    },
    {
        "author": "Yamada Anna",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Ya sabía que estaba mal, pero no voy a dejar de hacerlo solo porque lo dice un cartel, sabía que esto era arriesgado, seguiré comiendo en la..."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Cuando las personas se vuelven adultas se vuelven molestas."
    },
    {
        "author": "Adachi Shou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Uno se enamora de alguien sin poder evitarlo."
    },
    {
        "author": "Muto Rikako",
        "manga": "Umi ga Kikoeru",
        "frase": "¿En qué colectivo o sociedad no puede uno pensar por sí mismo? Es un derecho llamado libertad de pensamiento, nadie puede pisotearlo."
    },
    {
        "author": "Kobayashi Chihiro",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Un milagro deja de serlo si sucede todo el tiempo."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "El tipo de sangre no determina la personalidad de una persona, solo en Japón se cree eso."
    },
    {
        "author": "Kanomura Shinnosuke (Shinno)",
        "manga": "Sora no Aosa wo Shiru Hito yo",
        "frase": "La suerte y las conexiones lo son todo, ser bueno en algo no es suficiente."
    },
    {
        "author": "Jūichi",
        "manga": "Tengoku Daimakyou",
        "frase": "No tiene caso discutir si puedes acabar muerto."
    },
    {
        "author": "Kiruko (Haruki/Kiriko Takehaya)",
        "manga": "Tengoku Daimakyou",
        "frase": "Los rumores siempre son exagerados."
    },
    {
        "author": "Ichikawa Kana",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Es mejor no forzar nada, se puede ir despacio, se puede decir que, siendo joven, vas a crecer, vas a encontrar muchas cosas que te gusten y..."
    },
    {
        "author": "Ichikawa Kyoutarou",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "Decirle cumplidos a una chica es muy difícil."
    },
    {
        "author": "Ichikawa Kana",
        "manga": "Boku no Kokoro no Yabai Yatsu",
        "frase": "No busques a una chica por su cara, lo importante es su personalidad."
    }
]
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje de bienvenida cuando se emite el comando /start."""
    user = update.effective_user
    await update.message.reply_html(
        rf"¡Hola {user.first_name}! Soy un bot que puede saludarte y responder a ciertas palabras clave. Para obtener una frase. Si adivinas una palabra te dare una frase ;3"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje con información de ayuda cuando se emite el comando /help."""
    await update.message.reply_text("_No hay ayuda para los tridores, viva la republica._")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía una frase si el mensaje del usuario coincide con una palabra clave."""
    message_text = update.message.text.lower()  # Convertimos el texto del mensaje a minúsculas para hacer coincidencias sin distinción entre mayúsculas y minúsculas
    found = False  # Bandera para registrar si se encontró una coincidencia

    # Recorre la lista de frases
    for frase in frases:
        if frase['frase'].lower().find(message_text) != -1:  # Comprueba si el mensaje del usuario está en la frase
            response = f'Frase: "{frase["**frase**"]}"\nAuthor: {frase["author"]}\nManga: {frase["manga"]}'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
            found = True  # Marca que se encontró una coincidencia
            break  # Sale del bucle una vez que se encuentra una coincidencia

    # Si no se encontró ninguna coincidencia, envía un mensaje de respuesta
    if not found:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontró ninguna frase que coincida con tu mensaje.")


def main() -> None:
    """Inicio del bot."""
    application = Application.builder().token("6840272598:AAFKJyite25mihsKTlPG30HCHg53hJO5wq8").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
