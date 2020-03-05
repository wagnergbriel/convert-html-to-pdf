# -*- coding: utf-8 -*-
import pdfkit

def convertendo_urlhtml_em_pdf(url_html, pdf_file):
  pdfkit.from_url(url_html,pdf_file)

def convertendo_arqhtml_em_pdf(file_html, pdf_file):
  pdfkit.from_file(file_html, pdf_file)

if __name__ == "__main__":
 import argparse
 
 parse = argparse.ArgumentParser()
 parse.add_argument('-url',help= 'Url do arquivo que vai ser convertido em pdf.')
 parse.add_argument('-pdf',help= 'Caminho da pasta com o nome do arquivo para armazenar corretamente.')
 parse.add_argument('-arq_html', help= 'Caminho da pasta com o nome do arquivo para converter para pdf.')
 args = parse.parse_args()
 
 convertendo_urlhtml_em_pdf(args.url,args.pdf)
 convertendo_arqhtml_em_pdf(args.arq_html,args.pdf)
