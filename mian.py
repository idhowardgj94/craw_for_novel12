%load_ext autoreload
%autoreload 2
from craw.craw import craw
def main():
    print("hello")
    a=craw('https://novel12.com/241169/cirque-du-freak.htm')
    a.grabIndex()
    a.grabFromChapter()
    a.outputToEpub()

if __name__ == '__main__':
    main()
