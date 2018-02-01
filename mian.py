%load_ext autoreload
%autoreload 2
from craw.craw import craw
def main():
    print("hello")
    craw('https://novel12.com/241169/cirque-du-freak.htm')
if __name__ == '__main__':
    main()
