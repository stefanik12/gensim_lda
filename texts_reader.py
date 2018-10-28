from ga.digger_doc_reader.doc_reader import DocReader
from ga.digger_doc_reader import lo_parser

reader = DocReader()
paths = reader.crawl_dir("/data")
txt_paths = []

for p_i in range(len(paths)):
    print(lo_parser.retrieve_plaintext(paths[p_i], "cache"))
