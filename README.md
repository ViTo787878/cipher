# SubCipher
### Python knihovna pro šifrování, dešifrování a kryptoanalýzu substituční šifry

## Cíl projektu

Vytvořit Python knihovnu, která umožní:

- Šifrování a dešifrování textu pomocí substituční šifry.
- Automatické prolomení (kryptoanalýzu) této šifry pomocí statistických metod.
- Aplikaci této knihovny na reálná šifrovaná data (např. získaná z internetu).

---

## Hlavní úkoly

### 1. Šifrování a dešifrování
- Vytvořte modul s funkcemi pro šifrování a dešifrování substituční šifrou.
- Klíč je permutace anglické abecedy (A-Z + mezera jako `_`), tedy 27 znaků.

### 2. Prolomení šifry (kryptoanalýza)
- Vytvořte **teoretickou bigramovou (přechodovou) matici** z dostatečně dlouhého českého textu (např. [Krakatit](https://cs.wikisource.org/wiki/Krakatit)).
- Implementujte **Metropolis-Hastings algoritmus**, který:
  - využívá tuto matici jako referenční model
  - hledá permutaci klíče, která vrací nejpravděpodobnější text podle bigramové struktury

### 3. Aplikační demonstrace
- Vytvořte Jupyter notebook, který demonstruje:
  - šifrování a dešifrování textu
  - vytvoření bigramové matice z textu
  - automatizovanou kryptoanalýzu poskytnutého textu
  - vizualizace a analýzy výsledků

### 4. Export výstupů
- Pro každý dešifrovaný text (po cca 20 000 iteracích):
  - uložte plaintext do: `text_<délka>_sample_<id>_plaintext.txt`
  - uložte klíč do: `text_<délka>_sample_<id>_key.txt`

### 5. Výstupy a odevzdání
- Kód knihovny s dokumentací.
- Jupyter notebook exportovaný do PDF/HTML.
- Stručný report popisující postup, metody a výsledky.
- Soubory s dešifrovanými texty a klíči.

---

## Technické požadavky

- Jazyk: Python
- Povolené knihovny: např. `NumPy`, `Pandas`, `Matplotlib`
- Důraz na: přehledný kód, testování, validaci výsledků

---

## Hodnocení

- Funkčnost a robustnost implementace
- Správnost kryptoanalýzy
- Kvalita prezentace v notebooku
- Dokumentace a komentáře

---

## Teoretický základ

### Substituční šifra
- Nahrazení každého znaku podle zvoleného klíče.
- Abeceda: `ABCDEFGHIJKLMNOPQRSTUVWXYZ_`
- Např. posun o 3: A → D, B → E, …

### Ukázka:
- Původní text: `BYL_POZDNI_VECER_PRVNI_MAJ_VECERNI_MAJ_BYL_LASKY_CAS`
- Klíč: `DEFGHIJKLMNOPQRSTUVWXYZ_ABC`
- Zašifrovaný: `EAOCSRBGQLCYHFHUCSUYQLCPDMCYHFHUQLCPDMCEAOCODVNACFDV`

---

## Automatizované prolomení

### Bigramy
- Sekvence dvou znaků.
- Používají se k vytvoření **přechodové matice**.

### Přechodová (bigramová) matice
- Relativní matice četností bigramů (součet prvků = 1).
- Nejprve vytvořte absolutní matici, přičtěte +1 k nulovým hodnotám a pak ji normalizujte.

---

## Metropolis-Hastings algoritmus

1. **Inicializace**: náhodný klíč, výpočet plausibility.
2. **Generování kandidátního klíče**: prohoďte náhodně dva znaky.
3. **Vyhodnocení kandidáta**: spočítejte novou plausibility.
4. **Rozhodnutí**:
   - Pokud nový klíč lepší → přijmout.
   - Jinak přijmout s pravděpodobností `ρ = min(1, p_new / p_current)`
5. **Iterace**: uchovávejte nejlepší výsledek.
6. **Výsledek**: klíč s nejvyšší plausibility.

---

## API – Pseudokódy

### Šifrování
```python
FUNCTION substitute_encrypt(plaintext, key)
```

### Dešifrování
```python
FUNCTION substitute_decrypt(ciphertext, key)
```

### Získání bigramů
```python
FUNCTION get_bigrams(text)
```

### Přechodová matice
```python
FUNCTION transition_matrix(bigrams)
```

### Výpočet plausibility
```python
FUNCTION plausibility(text, TM_ref)
```

### Hlavní kryptoanalytická funkce
```python
FUNCTION prolom_substitute(text, TM_ref, iter, start_key)
```

---

## Ukázková data

- `text_1000_sample_1_ciphertext.txt`
- `text_1000_sample_1_key.txt`
- `text_1000_sample_1_plaintext.txt`

---

## Doporučené zdroje

- [Krakatit – Wikisource](https://cs.wikisource.org/wiki/Krakatit) – vhodný pro tvorbu referenční matice.
