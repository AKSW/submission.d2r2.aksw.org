# Submission for the D2R2 Workshop

## Current Workshop
[D2R2'23: Second International Workshop on Linked Data-driven Resilience Research 2023](http://aksw.org/2023.d2r2.aksw.org/) co-located with the [ESWC 2023](https://2023.eswc-conferences.org/)

## Submission Process

TBD

1. Collect Paper Metadata
2. Collect Paper Sources
3. Verify Paper Metadata
4. Vol-XXX/index.html
    1. Build index.html with Metadata (see https://github.com/AKSW/ceur-jekyll-rdf)
5. Agreement Forms
    1. Determine corresponding author to sign agreement form
    2. Generate Agreement forms
    3. Upload signed Agreement forms (to this repo)
    4. Bundle AGREEMENT submission package
6. Paper Bundle
    1. Build papers from source
    2. Verify Papers [Avoid Top errors in submissions](https://ceur-ws.org/HOWTOSUBMIT.html#TOPERRORS)
    3. Bundle Paper submission package
7. Everything complete?
8. Notify all authors to verify final submission packages (give them 1 week)
9. [Submit to CEUR](https://ceur-ws.org/HOWTOSUBMIT.html)

**[Avoid Top errors in submissions](https://ceur-ws.org/HOWTOSUBMIT.html#TOPERRORS)**

## Pieces

*These pieces need to be adjusted and put together, pathes do not match!*

- Generate the CEUR Vol-XXX/index.html with Jekyll RDF: https://github.com/AKSW/ceur-jekyll-rdf
- Generate the pre-filled agreement forms with the script in `agreement-form`
- Build the paper sources with the Taskfile and dockerimage in `source-management`
- Build the submission archives for CEUR with the Taskfile in `ceur-submission`


## Past Workshop(s)
- [D2R2'22: International Workshop on Data-driven Resilience Research 2022](https://2022.dataweek.de/d2r2-22/) co-located with the [Data Week Leipzig 2022](https://2022.dataweek.de/)
