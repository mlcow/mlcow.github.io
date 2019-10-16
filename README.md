# How to use

- clone the repo
- **Always commit changes to truemaster**
- Content goes in `content/` directory
- First time setup:
  - `virtualenv venv`
  - `pip install -r requirements.txt`
- Make .aka. generate html
  - Before any `make` commands: `source venv/bin/activate`
  - Useful commands in make: `html`, `serve`
  - *`html` vs `publish`: Former generates local links, later generates absolute mlcow. links, pain for local verification*
  - Help for make: `make`
    ```
    (venv) bash-3.2$ make
    Makefile for a pelican Web site

    Usage:
       make html                           (re)generate the web site
       make clean                          remove the generated files
       make regenerate                     regenerate files upon modification
       make publish                        generate using production settings
       make serve [PORT=8000]              serve site at http://localhost:8000
       make serve-global [SERVER=0.0.0.0]  serve (as root) to :80
       make devserver [PORT=8000]          start/restart develop_server.sh
       make stopserver                     stop local server
       make ssh_upload                     upload the web site via SSH
       make rsync_upload                   upload the web site via rsync+ssh
       make dropbox_upload                 upload the web site via Dropbox
       make ftp_upload                     upload the web site via FTP
       make s3_upload                      upload the web site via S3
       make cf_upload                      upload the web site via Cloud Files
       make github                         upload the web site via gh-pages
    ```
 - Github
   - commit and push to `truemaster`
   - To update prod https://mlcow.github.io , be in `truemaster` and `make github`
 
