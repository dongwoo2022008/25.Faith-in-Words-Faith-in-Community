# Final manuscript (16 October 2026): manuscript_v23.md -> manuscript_JEBO.md. The draft/version label is removed from the
# date line and a Funding statement (Baekseok University Research Fund, as stated by the author) is added above the generative-AI declaration.
s=open("manuscript_v23.md").read()
R=[
('date: "Draft v23, October 2026 (JEBO version)"','date: "October 2026"'),
("# Declaration of generative AI and AI-assisted technologies in the writing process\n",
 "# Funding\n\nThis work was supported by the Baekseok University Research Fund.\n\n# Declaration of generative AI and AI-assisted technologies in the writing process\n"),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_JEBO.md","w").write(s); print("applied",len(R))
