import docx


def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


if __name__ == "__main__":
    print(get_text('demo.docx'))

