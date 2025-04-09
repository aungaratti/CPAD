import requests
from bs4 import BeautifulSoup
from collections import deque
import time
import re
import json

# Define a base URL
base_url = "https://pt.wikipedia.org"

# Fila e conjunto de controle
links_nao_visitados = deque(['/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'])
visitados = set()

# Loop principal
while len(visitados) < 5 and links_nao_visitados:
    link_atual = links_nao_visitados.popleft()

    if link_atual in visitados:
        continue

    url_completa = base_url + link_atual
    print(f"Processando: {url_completa}")

    try:
        response = requests.get(url_completa)
    except Exception as e:
        print(f"Erro ao acessar {url_completa}: {e}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    titulo_elemento = soup.select_one(".mw-page-title-main")

    if not titulo_elemento:
        visitados.add(link_atual)
        continue

    titulo = titulo_elemento.text.strip()
    titulo_sanitizado = re.sub(r'[\\/*?:"<>|]', "_", titulo)
    nome_arquivo_html = f"{titulo_sanitizado}.html"

    # Salva o HTML da página
    with open(nome_arquivo_html, "w", encoding="utf-8") as f:
        f.write(response.content.decode("utf-8"))

        visitados.add(link_atual)

    # ====== TAREFA 2 - INFOBOX ======
    infobox = soup.find("table", class_="infobox")
    dados_infobox = {}

    if infobox:

        titulo_infobox = infobox.find("th")
        if titulo_infobox:
            dados_infobox["titulo"] = titulo_infobox.text.strip()

        linhas = infobox.find_all("tr")

        for linha in linhas:
            tds = linha.find_all("td")

            if len(tds) == 2:
                chave = tds[0].get_text(strip=True)
                td_valor = tds[1]

                # Verifica se o valor contém uma lista <li>
                itens_lista = td_valor.find_all("li")
                if itens_lista:
                    valor = [item.get_text(strip=True) for item in itens_lista]
                else:
                    # Se não for lista, extrai o texto direto, com vírgulas como separador se necessário
                    valor = td_valor.get_text(separator=", ", strip=True)

                dados_infobox[chave] = valor

        # Salva os dados da infobox em JSON
        if dados_infobox:
            nome_arquivo_json = f"{titulo_sanitizado}.json"
            with open(nome_arquivo_json, "w", encoding="utf-8") as json_file:
                json.dump(dados_infobox, json_file, ensure_ascii=False, indent=2)

    # Encontra novos links internos
    todos_links = soup.find_all("a", href=True)
    novos_links = []

    for a in todos_links:
        href = a["href"]
        if href.startswith("/wiki/") and ":" not in href and "#" not in href:
            if href not in visitados and href not in links_nao_visitados:
                novos_links.append(href)

    links_nao_visitados.extend(novos_links)
    time.sleep(1)

print(f"Coleta finalizada: {len(visitados)} páginas salvas.")
