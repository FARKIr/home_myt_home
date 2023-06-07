import scraperwiki
import lxml.html

# Načítanie stránky
html = scraperwiki.scrape("https://www.shmu.sk/sk/?page=765&station_id=7472")

# Nájdenie tabuľky s informáciami o stanici
root = lxml.html.fromstring(html)
table_info = root.cssselect("table.center.w500")[0]  # Tabuľka s informáciami o stanici

# Parsovanie informácií o stanici
data_info = {}
for row in table_info.cssselect("tbody tr"):
    cells = row.cssselect("td")
    if len(cells) == 2:
        attribute = cells[0].text_content().strip().rstrip(":")
        value = cells[1].text_content().strip()
        data_info[attribute] = value

# Výpis informácií o stanici
for attribute, value in data_info.items():
    print(f"{attribute}: {value}")
print()

# Nájdenie tabuľky s meranými hodnotami vodného stavu
table_values = root.cssselect("table.merane_hodnoty")[0]  # Tabuľka s meranými hodnotami

# Parsovanie meraných hodnôt vodného stavu
data_values = []
header_row = table_values.cssselect("thead tr")[0]
headers = [header.text_content().strip() for header in header_row.cssselect("th")]

for row in table_values.cssselect("tbody tr"):
    cells = row.cssselect("td")
    values = [cell.text_content().strip() for cell in cells]
    data_values.append(dict(zip(headers, values)))

# Výpis meraných hodnôt vodného stavu
for row in data_values:
    for attribute, value in row.items():
        print(f"{attribute}: {value}")
    print()
