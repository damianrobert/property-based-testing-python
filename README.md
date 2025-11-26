# Property-Based Testing cu Hypothesis (Python)

**Disciplina:** Testarea sistemelor software  
**Autori:** Radulescu Damian, Gujan Nicoleta
**Tema:** Testarea bazată pe proprietăți folosind biblioteca Hypothesis (Python)

---

## 1. Descriere generală

Acest proiect ilustrează utilizarea tehnicii **Property-Based Testing (PBT)** prin intermediul bibliotecii **Hypothesis** din Python.  
Spre deosebire de testele tradiționale, unde alegem manual cazurile de test, PBT definește **proprietăți generale** care trebuie să fie adevărate pentru _toate_ intrările valide.  
Hypothesis generează automat date de test diverse (inclusiv cazuri-limită) și identifică **contraexemple minime** atunci când proprietățile sunt încălcate.

---

## 2. Obiective

1. Înțelegerea conceptului de _testare bazată pe proprietăți_.
2. Explorarea bibliotecii **Hypothesis** și a modului în care generează date automat.
3. Implementarea unor exemple practice care demonstrează:
   - Proprietăți ale funcțiilor pure.
   - Descoperirea automată a unui bug real.
   - Teste de tip _round-trip_ (serialize/deserialize).
   - Testare _stateful_ a unui sistem simplu (cont bancar).

---

## 3. Structura proiectului

```
proiect-hypothesis/
├─ bank.py
├─ dedup.py
├─ dedup_fixed.py
├─ test_bank_stateful.py
├─ test_dedup_properties.py
├─ test_json_roundtrip.py
├─ test_sort_properties.py
├─ requirements.txt
└─ README.md
```

---

## 4. Instalare și rulare

1. Creează un mediu virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate     # Linux/Mac
   ```

2. Instalează dependențele:

   ```bash
   pip install -r requirements.txt
   ```

3. Rulează testele:
   ```bash
   pytest -q
   ```

Hypothesis va genera automat sute de cazuri de test pentru fiecare funcție.

---

## 5. Exemple incluse

### 🔹 a) Sortare (proprietăți matematice)

Fișier: `test_sort_properties.py`

Proprietăți verificate:

- Idempotentă: `sorted(sorted(xs)) == sorted(xs)`
- Lungime constantă: `len(sorted(xs)) == len(xs)`
- Ordine: lista rezultată este monoton crescătoare.

---

### 🔹 b) Descoperirea unui bug real – deduplicare

Fișiere: `dedup.py`, `test_dedup_properties.py`

Funcția `unique_preserving_order(xs)` trebuia să elimine duplicatele **fără a schimba ordinea** elementelor.  
Versiunea greșită folosea `set(xs)` și pierdea ordinea.  
Hypothesis a descoperit automat contraexemplul minim `xs = [1, 0]`.

Versiunea corectă (`dedup_fixed.py`):

```python
def unique_preserving_order(xs):
    seen = set()
    out = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
```

---

### 🔹 c) Round-trip JSON

Fișier: `test_json_roundtrip.py`

Verifică proprietatea:

```
json.loads(json.dumps(x)) == x
```

pentru structuri JSON valide.  
Hypothesis generează automat valori scalare, liste și dicționare pentru a valida această relație.

---

### 🔹 d) Testare stateful – cont bancar

Fișiere: `bank.py`, `test_bank_stateful.py`

Simulăm un cont bancar cu operații `deposit`, `withdraw`, `balance`.  
Se definește un **model simplu** (`model_balance`) și se verifică invariantul:

```
sut.balance() == model_balance
```

Hypothesis generează automat secvențe de acțiuni pentru a verifica:

- că nu se pot retrage bani în plus,
- că soldul final corespunde operațiilor efectuate,
- că sistemul se comportă consecvent în timp.

---

## 6. Beneficii ale Property-Based Testing

- Găsește cazuri-limită imposibil de intuit manual.
- Creează încredere că funcțiile respectă legi generale, nu doar exemple particulare.
- Contraexemplele minime oferă diagnostic rapid al bug-urilor.
- Combină elegant testarea funcțională cu abordarea formală.

---

## 7. Limitări

- Proprietăți prost definite → teste care nu verifică nimic util.
- Rezultate false dacă presupunerile nu sunt corecte.
- Posibilă scădere a performanței pentru teste cu multe cazuri.
- Atenție la flotanți (`NaN`, `inf`) — JSON, de exemplu, nu le suportă.

---

## 8. Concluzii

Property-Based Testing mută perspectiva de la „verific exemple” la „validez reguli generale”.  
Biblioteca **Hypothesis** face această metodă ușor de aplicat în Python, oferind generare automată, shrinking al contraexemplelor și suport pentru testare _stateful_.  
Prin exemplele incluse, proiectul demonstrează puterea și aplicabilitatea reală a acestei tehnici în detectarea erorilor subtile.

---

## 9. Bibliografie

- Documentația oficială Hypothesis: https://hypothesis.readthedocs.io
- Hughes, J. – _QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs_
- Articole și ghiduri Hypothesis despre strategii, shrinking și stateful testing
