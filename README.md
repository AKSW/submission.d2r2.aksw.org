# Jekyll RDF Template for CEUR Vol-XXX/index.html

This is the [Jekyll RDF](https://github.com/AKSW/jekyll-rdf) template to produce an `index.html` for a Volume for the [CEUR Workshop Proceedings](https://ceur-ws.org/).
In the current setup it is configured for the Proceedings of the [D2R2'22 Workshop](https://2022.dataweek.de/d2r2-22/).

## Usage

### Requirements
- [Task](https://taskfile.dev/#/)
- Docker or Podman
- Python
- [Rapper](https://librdf.org/raptor/)
- [tidy](https://github.com/htacg/tidy-html5/) (optional)
- [cmemc](https://documentation.eccenca.com/22.2/automate/cmemc-command-line-interface/) (optional)

### Run

```
$ task -l
task: Available tasks for this project:
* build:                           Build the site locally
* check:                           Check the correctness of the HTML
* graph:                           Join the event.ttl and paper.ttl graphs to the graph.ttl which is used to build the site
* serve:                           Serve the locally built site
* tidy:                            Tidy the HTML output with html tidy (https://github.com/htacg/tidy-html5/)
* watch:                           Serve the page and rebuild it on changes
* build:watch:                     Watch for changes in the directory and rebuild the page, should be combined with task serve in a second terminal
* check:graph-serialization:       Verify the graphs syntax is correct
* graph:check:                     Check all graph files
* graph:get-program:               Get the program from cmem and join it with the event graph (you need the correct credentials for that)
```
