import os

def leer(file):
    f = open(file, 'r')
    mensaje = f.read()
    f.close()
    return mensaje


def escribir(msn,file):

    ##message=msn.replace('\"','')
    message=msn
    print(message)

    f = open(file, 'w')
    f.write(message)
    f.close()


def run():
    file = 'autores.json'
    ##
    os.system(f'scrapy crawl scrape -o {file}')
    msn=leer(file)
    escribir(msn,file)


if __name__ == '__main__':
    run()