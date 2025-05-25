# SubCipher

## Knihovna pro šifrování, dešifrování a kryptoanalýzu substituční šifry

SubCipher je Python knihovna, která poskytuje nástroje pro práci se substituční šifrou. Umožňuje šifrování a dešifrování textu pomocí substituční šifry a také implementuje Metropolis-Hastings algoritmus pro automatické prolomení šifry bez znalosti klíče.

### Hlavní funkce

- **Šifrování a dešifrování** textu pomocí substituční šifry
- **Analýza textu** a vytváření statistických modelů (bigramové matice)
- **Automatické prolomení šifry** pomocí Metropolis-Hastings algoritmu
- **Normalizace textu** pro práci s českými texty

## Instalace

### Požadavky

- Python 3.13 nebo vyšší
- Knihovny: NumPy, Pandas, Matplotlib, Jupyter

### Instalace z repozitáře

```bash
# Klonování repozitáře
git clone https://github.com/username/subcipher.git
cd subcipher

# Instalace knihovny
pip install -e .

# Pro vývojáře (včetně testovacích nástrojů)
pip install -e ".[dev]"
```

### Instalace z requirements.txt

```bash
pip install -r requirements.txt
```

## Použití

### Šifrování a dešifrování

```python
from subcipher.cipher import substitute_encrypt, substitute_decrypt
from subcipher.constants import ALPHABET
import random

# Generování náhodného klíče
key = list(ALPHABET)
random.shuffle(key)
key = ''.join(key)

# Šifrování
plaintext = "HELLO_WORLD"
ciphertext = substitute_encrypt(plaintext, key)
print(f"Zašifrovaný text: {ciphertext}")

# Dešifrování
decrypted = substitute_decrypt(ciphertext, key)
print(f"Dešifrovaný text: {decrypted}")
```

### Analýza textu a vytvoření bigramové matice

```python
from subcipher.analysis import get_bigrams, transition_matrix
from subcipher.utils import load_textfile, normalize_text

# Načtení a normalizace textu
text = load_textfile("data_samples/krakatit.txt")
normalized_text = normalize_text(text)

# Získání bigramů
bigrams = get_bigrams(normalized_text)

# Vytvoření přechodové matice
tm = transition_matrix(bigrams, ALPHABET)
```

### Prolomení šifry pomocí Metropolis-Hastings algoritmu

```python
from subcipher.mh_solver import metropolis_hastings

# Předpokládáme, že máme zašifrovaný text a referenční přechodovou matici
decryption_key, score = metropolis_hastings(
    ciphertext,
    tm,
    iterations=20000,
    initial_temp=1.0
)

# Dešifrování pomocí nalezeného klíče
decrypted_text = substitute_decrypt(ciphertext, decryption_key)
print(f"Dešifrovaný text: {decrypted_text}")
print(f"Skóre: {score}")
```

## Komponenty knihovny

### cipher.py

Modul obsahující funkce pro šifrování a dešifrování textu pomocí substituční šifry.

- `substitute_encrypt(text, key)`: Šifruje text pomocí zadaného klíče
- `substitute_decrypt(text, key)`: Dešifruje text pomocí zadaného klíče

### analysis.py

Modul pro analýzu textu a výpočet statistických vlastností.

- `get_bigrams(text)`: Získá seznam bigramů z textu
- `transition_matrix(bigrams, alphabet)`: Vytvoří přechodovou matici z bigramů
- `calculate_plausibility(text, tm_ref)`: Vypočítá věrohodnost textu podle referenční matice

### mh_solver.py

Implementace Metropolis-Hastings algoritmu pro prolomení substituční šifry.

- `metropolis_hastings(ciphertext, tm_ref, iterations, initial_temp)`: Hledá klíč pro dešifrování

### utils.py

Pomocné funkce pro práci s textem a soubory.

- `load_textfile(file_path)`: Načte text ze souboru
- `save_textfile(text, output_path)`: Uloží text do souboru
- `normalize_text(text)`: Normalizuje text (převod na velká písmena, odstranění diakritiky, atd.)

### constants.py

Definice konstant používaných v knihovně.

- `ALPHABET`: Definice abecedy používané pro šifrování (A-Z + podtržítko)

## Metropolis-Hastings algoritmus

Metropolis-Hastings algoritmus je metoda Markov Chain Monte Carlo (MCMC), která umožňuje vzorkování z pravděpodobnostních distribucí. V kontextu kryptoanalýzy jej používáme k prohledávání prostoru možných klíčů a nalezení toho, který s největší pravděpodobností dešifruje text správně.

### Princip algoritmu

1. **Inicializace**: Začínáme s náhodným klíčem a vypočítáme jeho skóre věrohodnosti.
2. **Iterace**: V každé iteraci:
   - Vytvoříme nový kandidátní klíč záměnou dvou náhodných znaků v aktuálním klíči
   - Dešifrujeme text pomocí nového klíče a vypočítáme jeho skóre
   - Rozhodneme, zda přijmout nový klíč:
     - Pokud je nové skóre lepší než aktuální, přijmeme nový klíč
     - Pokud je horší, přijmeme jej s pravděpodobností závislou na rozdílu skóre a teplotě
   - Teplota se postupně snižuje (simulované žíhání), což vede k menší pravděpodobnosti přijetí horších řešení
3. **Výsledek**: Algoritmus vrátí nejlepší nalezený klíč a jeho skóre

### Parametry

- `iterations`: Počet iterací algoritmu (doporučeno 10 000 - 20 000)
- `initial_temp`: Počáteční teplota pro simulované žíhání (výchozí hodnota 1.0)

## Doporučení pro použití

- Pro dosažení úspěšnosti dešifrování nad 90% je potřeba text o délce alespoň 1000 znaků
- Referenční text by měl být ze stejné domény nebo žánru jako šifrovaný text
- Optimální počet iterací je mezi 10 000 a 20 000
- Pro kritické aplikace je vhodné kombinovat automatické dešifrování s ruční analýzou

## Příklady

Podrobné příklady použití knihovny najdete v Jupyter notebooku `notebooks/subcipher_deep_analysis.ipynb`.

## Licence

Tento projekt je licencován pod MIT licencí - viz soubor LICENSE pro více informací.
