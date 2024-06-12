# Get structured data from unstructure document with OpenAI Api
This solution aims to obtain structured data from information in unstructured documents. The process takes PDF documents from a folder and loads them into the context of ChatGPT to then obtain structured information through prompts. This structured data is used in models. The configuration of this process (path to folders where the PDF documents are located, or the destination Excel files, among others) is stored in an Excel file. The execution log where the obtained data is visualized is also recorded in this Excel file, but in a different sheet. This process runs on the same machine that has access to both the unstructured PDF files and the destination Excel files

## How start with this project locally

1. `virtualenv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `python start.py`

### REMEMBER!!!
If you add a new library, please update requirements.txt.
You can use this command if tou prefere.

`pip freeze > requirements.txt`
