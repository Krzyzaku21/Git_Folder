#__name__ == __main__
#Używanie gdy kod chce sie uruchomić
#tylko jako bazowy (name_main_module_base), a czasami chce sie uruchomić tylko importowany (name_main_module_sub)
#czytanie kodu odbywa się po całym kodzie

print("Ten tekst zawsze się uruchomi w module base i sub")

def main():
        print("Uruchom bazowy moduł name_main_module_base.py") #Uruchom bazowy moduł name_main_module.py
if __name__ == '__main__':
    main()
else:
    print("Uruchom w importowanym module name_main_module_sub.py")