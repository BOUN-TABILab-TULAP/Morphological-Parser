# BOUN Morphological Parser and Disambiguator

## How to run using Docker

1. Clone the repo
```bash
git clone https://github.com/BOUN-TABILab-TULAP/Morphological-Parser.git
```
2. Launch a terminal in the root directory of the repo and build the Docker image where
- `-t` is the tag for the Docker image. You can provide any name you want
- `.` is the relative path to the Dockerfile 
```bash
docker build -t morphological-parser .
```
3. Run the Docker image where
- `-d` indicates "detach", let the container run in the background
- `-p 4444:4444` indicates mapping port 4444 of the container to the port 4444 of the host.
```bash
docker run -d -p 4444:4444 morphological-parser
```
4. Send a POST request
- via curl
  - Command:
    ```bash
    curl -X POST http://localhost:4444/evaluate \
    -H 'Content-Type: application/json' \
    -d '{"textarea":"Genç çellistin büyük heyecan ve duyarlılıkla çalmasına salondaki seyirciler hayran oldu ."}'
    ```
  - Output:
    ```bash
    {{'text': 'Genç\n\tgenç[Adj]\n\tGenç[Noun]  [Prop] [A3sg] [Pnon] [Nom]\nçellistin\n\tçellist[Noun] [A3sg] [Pnon] NHn[Gen]\n\tçellist[Noun] [A3sg] Hn[P2sg] [Nom]\nbüyük\n\tbüyük[Adj] \nheyecan\n\theyecan[Noun]  [A3sg] [Pnon] [Nom]\n\tHeyecan[Noun] [Prop] [A3sg] [Pnon] [Nom]\nve\n\tve[Conj] \nduyarlılıkla\n\tduyarlı[Adj] lHk[Noun Ness] [A3sg] [Pnon] YlA[Ins]\n\tDuyar[Noun] [Prop] [A3sg] [Pnon] [Nom] lH[Adj With] lHk[Noun Ness] [A3sg] [Pnon] YlA[Ins]\n\tduyarlılık[Noun] [A3sg] [Pnon] YlA[Ins]\n\tduyar[Adj] [Noun] [A3sg] [Pnon] [Nom] lH[Adj With] lHk[Noun Ness] [A3sg] [Pnon] YlA[Ins]\nçalmasına\n\tçal[Verb] [Pos] mA[Noun Inf2] [A3sg] SH[P3sg] NA[Dat]\n\tçalma[Adj] [Noun] [A3sg] SH[P3sg] NA[Dat]\n\tçalma[Noun] [A3sg] SH[P3sg] NA[Dat]\nsalondaki\n\tsalon[Noun] [A3sg] [Pnon] DA[Loc] ki[Adj Rel]\n\tSalo[Noun] [Prop] [A3sg] Hn[P2sg] NDA[Loc] ki[Adj Rel]\nseyirciler\n\tseyirci[Noun] lAr[A3pl] [Pnon] [Nom]\n\tseyir[Noun] [A3sg] [Pnon] [Nom] CH[Noun Agt] lAr[A3pl] [Pnon] [Nom]\nhayran\n\tHayran[Noun] [Prop] [A3sg] [Pnon] [Nom]\n\thayran[Adj] \noldu\n\tol[Verb] [Pos] DH[Past] [A3sg]\n\toldu[Postp]  [PCNom]\n\toldu[Postp]  [PCNom] [A3sg] [Pnon] [Nom]\n\tol[Adj] [Noun] [A3sg] [Pnon] [Nom] YDH[Verb Past] [A3sg]\n\tol[Adj] YDH[Verb Past] [A3sg]\n\toldu[Interj] \n.\n\t.[Punc] \n--------------------------------------------------'
- via Python's requests library
  - Commands:
    ```python
    import requests
    res = requests.post('http://localhost:4444/evaluate', json={'textarea':'Genç çellistin büyük heyecan ve duyarlılıkla çalmasına salondaki seyirciler hayran oldu .'})
    print(res.json())
    ```
  - Output:
    ```python
    {{'text': 'Genç\n\tgenç[Adj]\n\tGenç[Noun]  [Prop] [A3sg] [Pnon] [Nom]\nçellistin\n\tçellist[Noun] [A3sg] [Pnon] NHn[Gen]\n\tçellist[Noun] [A3sg] Hn[P2sg] [Nom]\nbüyük\n\tbüyük[Adj] \nheyecan\n\theyecan[Noun]  [A3sg] [Pnon] [Nom]\n\tHeyecan[Noun] [Prop] [A3sg] [Pnon] [Nom]\nve\n\tve[Conj] \nduyarlılıkla\n\tduyarlı[Adj] lHk[Noun Ness] [A3sg] [Pnon] YlA[Ins]\n\tDuyar[Noun] [Prop] [A3sg] [Pnon] [Nom] lH[Adj With] lHk[Noun Ness] [A3sg] [Pnon] YlA[Ins]\n\tduyarlılık[Noun] [A3sg] [Pnon] YlA[Ins]\n\tduyar[Adj] [Noun] [A3sg] [Pnon] [Nom] lH[Adj With] lHk[Noun Ness] [A3sg] [Pnon] YlA[Ins]\nçalmasına\n\tçal[Verb] [Pos] mA[Noun Inf2] [A3sg] SH[P3sg] NA[Dat]\n\tçalma[Adj] [Noun] [A3sg] SH[P3sg] NA[Dat]\n\tçalma[Noun] [A3sg] SH[P3sg] NA[Dat]\nsalondaki\n\tsalon[Noun] [A3sg] [Pnon] DA[Loc] ki[Adj Rel]\n\tSalo[Noun] [Prop] [A3sg] Hn[P2sg] NDA[Loc] ki[Adj Rel]\nseyirciler\n\tseyirci[Noun] lAr[A3pl] [Pnon] [Nom]\n\tseyir[Noun] [A3sg] [Pnon] [Nom] CH[Noun Agt] lAr[A3pl] [Pnon] [Nom]\nhayran\n\tHayran[Noun] [Prop] [A3sg] [Pnon] [Nom]\n\thayran[Adj] \noldu\n\tol[Verb] [Pos] DH[Past] [A3sg]\n\toldu[Postp]  [PCNom]\n\toldu[Postp]  [PCNom] [A3sg] [Pnon] [Nom]\n\tol[Adj] [Noun] [A3sg] [Pnon] [Nom] YDH[Verb Past] [A3sg]\n\tol[Adj] YDH[Verb Past] [A3sg]\n\toldu[Interj] \n.\n\t.[Punc] \n--------------------------------------------------'
    ```

The original author of this program is Haşim Sak. 

Attribution Info:
Please cite the following paper if you make use of this resource in your research.

Haşim Sak, Tunga Güngör, and Murat Saraçlar. Morphological disambiguation of Turkish text with perceptron algorithm.
In CICLing 2007, volume LNCS 4394, pages 107-118, 2007.

BibTeX entry:

@inproceedings{sak-et-al-cicling-07,
    
    Author = Haşim Sak and Tunga Güngör and Murat Saraçlar,
    
    Booktitle = CICLing 2007,
    
    Pages = 107--118,
    
    Title = Morphological Disambiguation of {Turkish} Text with Perceptron Algorithm,
    
    Volume = LNCS 4394,
    
    Year = 2007,
    
    Url = http://www.cmpe.boun.edu.tr/~hasim/papers/CICLing07.pdf
