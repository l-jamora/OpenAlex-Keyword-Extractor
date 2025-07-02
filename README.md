# OpenAlex DOI to Keywords (RIS Exporter)
This Python script takes a list of DOIs (in any format), queries the [OpenAlex API](https://openalex.org/), and exports an `.ris` file containing titles and concept keywords for use in **bibliometric tools** like [VOSviewer](https://www.vosviewer.com/).

For the sake of transpara

---

## Features

- Accepts DOIs in **raw or URL** format (e.g. `10.1016/...`, `https://doi.org/...`)
- Automatically extracts **keywords** (concepts) from OpenAlex
- Outputs a **valid RIS** file ready for import into **VOSviewer**
- Skips invalid or non-DOI URLs (e.g. `itcon.org/2016/24`)
- Progress bar for large datasets
- Gracefully handles errors

---

## 📦 Requirements

- Python 3.7+
- Packages:
  - `requests`
  - `tqdm`

Install dependencies:

```bash
pip install requests tqdm
````

---

## 📂 How to Use

1. **Prepare your list of DOIs**

Create a plain text file called `dois.txt` in the same directory. Add one DOI or DOI URL per line:

```
https://doi.org/10.1016/j.aei.2023.102137
10.36680/j.itcon.2022.020
https://doi.org/10.1061/(ASCE)ME.1943-5479.0000712
```

2. **Run the script**

```bash
python get_openalex_ris.py
```

3. **Done!**

The script will output:

* `openalex_keywords.ris` → ready to import into VOSviewer

---

## 🗺️ Using in VOSviewer

1. Open VOSviewer
2. Select:

   * *Create a map based on bibliographic data*
   * *Read data from bibliographic database files*
3. Choose `openalex_keywords.ris`
4. Choose:

   * *Type of analysis:* Co-occurrence
   * *Unit of analysis:* All keywords

---

## 🧠 About OpenAlex Concepts

The "keywords" used in this script come from OpenAlex's `concepts` field, which represents semantically-tagged research topics. These are consistent and hierarchical, making them ideal for bibliometric analysis.

---

## 🧰 Example Output

```ris
TY  - JOUR
TI  - BIM-based fire safety checking using rule automation
DO  - 10.1016/j.autcon.2020.103280
KW  - Building Information Modeling
KW  - Fire safety engineering
KW  - Digital construction
ER  -
```

---

## ❓ FAQ

**Q: What happens if a DOI isn’t found in OpenAlex?**
A: It will be skipped and logged in the terminal.

**Q: Can I include more metadata like authors or year?**
A: Not yet — but this is easy to add. Open an issue or contribute!

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🤝 Contributing

Pull requests and feature suggestions welcome!
If you’d like to add:

* Author names
* Abstracts
* Other export formats (e.g., BibTeX, CSV)

Just open an issue or PR.

---

## 🔗 Acknowledgements

* [OpenAlex](https://openalex.org/)
* [VOSviewer](https://www.vosviewer.com/)

---

## 🤖 Transparency Notice

This code and documentation were originally generated using [OpenAI’s ChatGPT API](https://platform.openai.com/). Final structure, testing, and integration were done manually by the project author.

```