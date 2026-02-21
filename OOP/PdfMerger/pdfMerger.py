from pypdf import PdfWriter
import os

class MergePdfs:
    """
pdfMerger by Sukhman Majri
Github - https://github.com/MajriSukhman

- Basic Python Based PDF Merger

Methods

merge(pdf1, pdf2, pdf3 ...)
returns a merged pdf with name 'merged.pdf' in the opened directory

mergeAllPdfs(path, outputFileName)
path - specify the path where all the pdf exists
outputFileName - the name of the output file

returns a merged pdf with the specified outputFileName in the specified path

Thanks
"""
    @staticmethod
    def merge(*args):
        Merger = PdfWriter()
        for pdf in args:
            Merger.append(pdf)
        try:
            with open("merged.pdf", 'wb') as file:
                Merger.write(file)
        except Exception as e:
            raise RuntimeError(f"Failed to merge pdfs: {e}")
        Merger.close()

    @staticmethod
    def mergeAllPdfs(path, outputFileName):
        Merger = PdfWriter()
        if not outputFileName.endswith('.pdf'): 
            outputFileName = f'{outputFileName}.pdf' #'merge21' --> 'merge21.pdf'
        if not os.path.exists(path):
            raise ValueError("Please enter a valid path")
        outputFile = os.path.join(path, outputFileName)
        for file in os.listdir(path):
            if not file.endswith('.pdf') or file == outputFileName:
                continue #ignores non-pdf or pdf to be merged from selection
            file = os.path.join(path, file)
            Merger.append(file)
        try:
            with open(outputFile, 'wb') as file:
                Merger.write(file)
        except Exception as e:
            raise RuntimeError(f"Failed to merge pdfs: {e}")
        Merger.close()