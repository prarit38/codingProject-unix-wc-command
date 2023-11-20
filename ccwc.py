import click
import os

def getFileSize(filename):
    return os.path.getsize(filename)

def getNoOfLinesInFile(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
            lines = len(fp.readlines())
            return lines

def getNoOfWordsInFile(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
            data=fp.read()
            lines=data.split()
            number_of_words=len(lines)
            return number_of_words
def getNoOfCharsInFile(filename):
    with open(filename, 'rb') as fp:
            data=fp.read()
            number_of_chars=len(data)
            return number_of_chars

@click.command()
@click.option("-c", is_flag=True)
@click.option("-l", is_flag=True)
@click.option("-w", is_flag=True)
@click.option("-m", is_flag=True)
@click.argument('filename')
def ccwc(c,l,w,m,filename):
    if c:
        filesize=getFileSize(filename)
        print(filesize, filename)
    elif l:
        lines = getNoOfLinesInFile(filename)
        print(lines, filename)
    elif w:
        number_of_words=getNoOfWordsInFile(filename)
        print(number_of_words, filename)
    elif m:
        number_of_chars=getNoOfCharsInFile(filename)
        print(number_of_chars,filename)
    else:
        filesize=getFileSize(filename)
        lines = getNoOfLinesInFile(filename)
        number_of_words=getNoOfWordsInFile(filename)
        print(lines, number_of_words, filesize,  filename)
        

if __name__=="__main__":
   ccwc()
    
