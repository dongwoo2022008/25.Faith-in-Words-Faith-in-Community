# Exact edits that turn manuscript_v19.md into manuscript_v20.md (16 October 2026): the Elsevier generative-AI
# declaration placed immediately above the references, as the publisher's author instructions require (the LLM
# coder used in the method is described separately in Section 3.2 and Appendix B). Figure 1 was regenerated
# (fig_framework_v20.py) with the H1 result box reading "no detectable response to local unemployment", matching
# the abstract and Section 5.5; the figure file changes, the caption does not.
s=open("manuscript_v19.md").read()
R=[
('date: "Draft v19, October 2026 (JEBO version)"','date: "Draft v20, October 2026 (JEBO version)"'),
("What a credit market can learn from religion is not what a borrower says about it but where the borrower stands within it.\n\n# References",
 "What a credit market can learn from religion is not what a borrower says about it but where the borrower stands within it.\n\n# Declaration of generative AI and AI-assisted technologies in the writing process\n\nDuring the preparation of this work the author used Claude (Anthropic) in order to edit the English text, check the consistency of numbers between the text and the tables, and format the manuscript. After using this tool, the author reviewed and edited the content as needed and takes full responsibility for the content of the publication. The use of a large language model as a text coder in the research method is described in Section 3.2 and Appendix B.\n\n# References"),
]
for old,new in R:
    c=s.count(old); assert c==1,(c,old[:80]); s=s.replace(old,new)
open("manuscript_v20.md","w").write(s); print("applied",len(R))
