# Submission package (16 October 2026): splits submission_documents_final.md into one file per upload item,
# converts each to docx (pandoc, Times New Roman 11 pt), and assembles pkg_final/ with the manuscript build and figures.
import re, os, subprocess, shutil
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
PKG="pkg_final"; os.makedirs(PKG+"/figures",exist_ok=True)
for f in os.listdir(PKG):
    if f.startswith("manuscript_JEBO"): os.remove(os.path.join(PKG,f))
src=open("submission_documents_final.md").read()
parts=re.split(r"\n---\n",src)
names={"1.":"title_page","2.":"highlights","3.":"declarations","4.":"figure_captions","5.":"cover_letter"}
files={}
for p in parts[1:]:
    m=re.search(r"^## (\d\.) ([^\n]+)",p.strip()); key=m.group(1); name=names[key]
    body=p.strip()
    body=re.sub(r"^## \d\. ","## ",body,count=1)      # drop the running number
    body=re.sub(r"\s*\(separate [^)]*\)","",body,count=1)   # drop "(separate file)" notes from headings
    if name=="highlights": body=re.sub(r"## Highlights[^\n]*","## Highlights",body,count=1)
    if name=="cover_letter": body=re.sub(r"## Cover letter[^\n]*\n\n","",body,count=1)
    body=re.sub(r"(^|\n)Dongwoo Kim\nDivision",r"\1Dongwoo Kim\\\nDivision",body).replace("Korea\nE-mail","Korea\\\nE-mail").replace("bu.ac.kr\nORCID","bu.ac.kr\\\nORCID")
    body=body.replace("University\ndongwoo.kim@bu.ac.kr","University\\\ndongwoo.kim@bu.ac.kr").replace("The Editors\n*Journal","The Editors\\\n*Journal")
    body=body.replace("signaling\n*JEL","signaling\\\n*JEL")
    files[name]=body+"\n"
files["submission_documents"]=src
def to_docx(md,out):
    subprocess.run(["pandoc","-f","markdown","-o",out,md],check=True)
    d=Document(out); st=d.styles['Normal']; st.font.name="Times New Roman"; st.font.size=Pt(11)
    st.element.rPr.rFonts.set(qn('w:eastAsia'),"Times New Roman")
    for p in d.paragraphs:
        for r in p.runs: r.font.name="Times New Roman"
    d.save(out)
for name,body in files.items():
    md=f"{PKG}/{name}.md"; open(md,"w").write(body); to_docx(md,f"{PKG}/{name}.docx")
shutil.copy("manuscript.md",f"{PKG}/manuscript.md"); shutil.copy("manuscript.docx",f"{PKG}/manuscript.docx"); shutil.copy("render/manuscript.pdf",f"{PKG}/manuscript.pdf")
print(sorted(os.listdir(PKG)))
