import scraperwiki
import lxml.html

# Načítanie stránky
html = scraperwiki.scrape("https://www.shmu.sk/sk/?page=765&station_id=7472")

# Nájdenie tabuľky s informáciami o stanici
root = lxml.html.fromstring(html)
table = root.cssselect("table.center.w500")[0]  # Vyber prvú tabuľku s týmto triedovým selektorom

# Parsovanie informácií z tabuľky
data = {}
for row in table.cssselect("tbody tr"):
    cells = row.cssselect("td")
    if len(cells) == 2:
        attribute = cells[0].text_content().strip().rstrip(":")
        value = cells[1].text_content().strip()
        data[attribute] = value

# Výpis získaných informácií
for attribute, value in data.items():
    print(f"{attribute}: {value}")
