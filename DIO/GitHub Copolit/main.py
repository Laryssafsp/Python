import re
import json
import logging

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def identificar_bandeira(numero_cartao: str) -> str:
    """
    Identifica a bandeira de um cartão de crédito a partir do número informado.

    Parâmetros:
        numero_cartao (str): Número do cartão (com ou sem formatação).

    Retorna:
        str: JSON com a bandeira identificada ou uma mensagem de erro.
    """
    numero = re.sub(r"\D", "", numero_cartao)
    logging.debug(f"Número sanitizado: {numero}")

    if not numero.isdigit() or not 13 <= len(numero) <= 19:
        logging.warning("Número inválido ou fora do padrão")
        return json.dumps(
            {"erro": "Número inválido ou fora do padrão"},
            ensure_ascii=False
        )

    padroes = {
        "Visa": r"^4\d{12}(\d{3})?$",
        "MasterCard": r"^(5[1-5]\d{14}|2(2[2-9][1-9]|2[3-9]\d|[3-6]\d{2}|7[01]\d|720)\d{12})$",
        "American Express": r"^3[47]\d{13}$",
        "Diners Club": r"^3(0[0-5]|[68]\d)\d{11}$",
        "Discover": r"^6(011|5\d{2}|4[4-9]\d)\d{12}$",
        "enRoute": r"^2(014|149)\d{11}$",
        "JCB": r"^(2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699\d{11}$",
        "Hipercard": r"^6062\d{12,}$",
        "Aura": r"^50\d{14,}$"
    }

    for bandeira, padrao in padroes.items():
        if re.match(padrao, numero):
            logging.info(f"Bandeira identificada: {bandeira}")
            return json.dumps({"bandeira": bandeira}, ensure_ascii=False)

    logging.info("Bandeira não identificada")
    return json.dumps({"bandeira": "Desconhecida"}, ensure_ascii=False)


def solicitar_cartoes():
    """
    Solicita ao usuário a entrada de números de cartão para identificar as bandeiras.
    Permite múltiplos cartões separados por vírgula e oferece a opção de repetir a consulta.
    """
    while True:
        entrada = input(
            "\nDigite o(s) número(s) do cartão (separados por vírgula):\n"
            "Exemplo: 4111 1111 1111 1111, 5500-0000-0000-0004\n> "
        )

        cartoes = [c.strip() for c in entrada.split(",") if c.strip()]
        if not cartoes:
            logging.warning("Nenhum cartão fornecido.")
            print("⚠️ Nenhum cartão detectado. Tente novamente.")
            continue

        for cartao in cartoes:
            logging.info(f"Processando cartão: {cartao}")
            resultado = identificar_bandeira(cartao)
            print(f"\nCartão: {cartao} → Resultado: {resultado}")

        continuar = input("\nDeseja consultar novo cartão? (sim/não): ").strip().lower()
        if continuar not in ("sim", "s"):
            logging.info("Encerrando aplicação.")
            print("✅ Encerrando consulta. Obrigado!")
            break


if __name__ == "__main__":
    logging.info("Iniciando aplicação de consulta de bandeiras.")
    print("💳 CONSULTA DE BANDEIRA DE CARTÃO DE CRÉDITO")
    solicitar_cartoes()
