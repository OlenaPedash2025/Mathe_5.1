# Projektbericht: Lieferanten-Matching (Szenario GreenFlow)
**Analyse der Anbieterstruktur mittels Vektor-Metriken**

---

## 1. Data Architect: Mathematische Modellierung
Ich habe das Geschäftsszenario in einen 4-dimensionalen Vektorraum übersetzt ($n=4$). Die Dimensionen folgen einer realistischen Marktlogik, bei der hohe Werte hohe Ausprägungen bedeuten:

* **$x_1$ (Price):** Marktpreis (1 = sehr günstig, 10 = Premium/Teuer).
* **$x_2$ (Quality):** Technische Exzellenz (10 = fehlerfrei).
* **$x_3$ (Ecology):** Nachhaltigkeits-Score (10 = CO2-neutral).
* **$x_4$ (Delivery):** Logistik-Performance (10 = extrem schnell/zuverlässig).

**Ziel-Vektor (Query):** `[8.0, 8.0, 8.0, 8.0]`  
*Wir suchen ein High-End-Segment: Wir sind bereit, einen hohen Preis (8) zu zahlen, erwarten dafür aber Spitzenwerte in Qualität, Umwelt und Logistik.*

| Anbieter | Profil $[x_1, x_2, x_3, x_4]$ | Interpretation |
| :--- | :--- | :--- |
| **Elite_supplier** | `[10.0, 10.0, 10.0, 10.0]` | Absolutes Premium, aber sehr teuer. |
| **Cheap_supplier** | `[2.0, 3.5, 2.0, 3.0]` | Billig-Segment mit großen Defiziten. |
| **Balanced_partner** | `[7.5, 8.0, 7.5, 8.5]` | Unser idealer "Match". |
| **Scale_up_pro** | `[4.0, 4.0, 4.0, 4.0]` | Perfekte Struktur, aber kleine Kapazität. |
| **Chaos_vendor** | `[9.0, 2.5, 1.5, 9.0]` | Teuer und schnell, aber qualitativ schwach. |

---

## 2. Metric Engineer (Distance): Absolute Nähe
Ich berechne die **Euklidische Distanz**, um die "physikalische" Nähe zum Zielwert zu bestimmen. Wer liegt am nächsten an unseren 8.0-Vorgaben?

$$d(q, v) = \sqrt{\sum_{i=1}^{n} (q_i - v_i)^2}$$

* **Gewinner:** `Balanced_partner` (**Distanz: 0.866**)
* **Analyse:** Er ist der einzige, der unsere Erwartungen fast punktgenau erfüllt.

---

## 3. Metric Engineer (Angle): Strukturelle Ähnlichkeit
Ich nutze die **Kosinus-Ähnlichkeit**, um die strategische Ausrichtung zu prüfen. Es geht nicht um die Größe, sondern um das Verhältnis der Werte zueinander (die "Richtung").

$$\text{sim}(q, v) = \frac{q \cdot v}{\|q\| \|v\|}$$

* **Gewinner:** `Elite_supplier` & `Scale_up_pro` (**Score: 1.000**)
* **Analyse:** Beide haben die exakt gleiche Prioritätensetzung (1:1:1:1) wie unser Zielprofil.

---

## 4. Quality Analyst: Der Konflikt-Test
Hier zeigt sich die Stärke des dualen Systems. Betrachten wir den Konflikt zwischen den Metriken:

* **Fall Scale_up_pro:** Laut **Kosinus (1.0)** ist er ein perfekter Zwilling unserer Strategie. Aber die **Distanz (8.0)** zeigt: Er ist viel zu klein/schwach für unsere aktuellen Anforderungen.
* **Fall Chaos_vendor:** Er hat eine ähnliche Distanz wie Scale_up_pro, aber sein **Kosinus (0.842)** ist miserabel. Trotz hohem Preis ($x_1=9$) bietet er keine Qualität.
* **Ergebnis:** Nur die Kombination beider Werte verhindert Fehlentscheidungen.

---

## 5. Product Owner: Business Review
Die mathematische Analyse liefert ein klares Bild für unsere Beschaffungsstrategie:

**Empfehlung:**
1. **Hauptwahl:** `Balanced_partner`. Er bietet das beste Preis-Leistungs-Verhältnis direkt an unserem Zielwert.
2. **Strategische Beobachtung:** `Scale_up_pro`. Wenn dieser Anbieter skaliert, wird er aufgrund seiner perfekten Struktur (Kosinus 1.0) zum idealen Partner.
3. **Risiko:** `Chaos_vendor`. Trotz Schnelligkeit ist er aufgrund mangelnder Qualität und Nachhaltigkeit bei hohem Preis abzulehnen.

> **Fazit:** Wir kaufen nicht einfach beim Billigsten, sondern dort, wo die Struktur (Winkel) und die Leistung (Distanz) zu unserem GreenFlow-Anspruch passen.
