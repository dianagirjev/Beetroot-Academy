print('main.py:', __name__)
import functii # executa tot fisierul functii
functii.functia_test() # executa doar functia functia_test()

if __name__ == "__main__":
    functii.functia_test()
    print("Am execuatat fisierul main.py")