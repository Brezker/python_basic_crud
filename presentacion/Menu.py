import sys
# import os
# here you have to put your path app folder
sys.path.insert(1,'.')
from datos.conexBD import *
from negocio.Ins_est import *
from negocio.Sho_est import *
from negocio.Del_est import *
from negocio.Upd_est import *

from negocio.Ins_mat import *
from negocio.Sho_mat import *
from negocio.Del_mat import *
from negocio.Upd_mat import *

from negocio.Ins_eva import *
from negocio.Sho_eva import *
from negocio.Del_eva import *
from negocio.Upd_eva import *

from negocio.Sho_dis import *

def showMenu():
    print('\nSelect a category: ')
    print('1) Student management.')
    print('2) Courses management.')
    print('3) Evaluations management.')
    print('4) Show discounts.')
    print('q) Quit.\n')
    sel = input()
    match sel:
        case '1':
            print('')
            showEst()
            print('\nWich action do you want to execute?')
            print('1) Add student.')
            print('2) Delete student.')
            print('3) Update student.')
            print('4) Go back to menu.')
            print('q) Quit.\n')           
            # showEst()
            # print('')
            sel2 = input()
            match sel2:
                case '1':
                    print("\nWrite student's name.")
                    in_nom = input()
                    print("Write student's enrollment.")
                    in_mat = input()
                    inser_est(in_nom, in_mat)
                    print('Student added.\n')
                    showEst()
                    # os.system('clear')
                    showMenu()
                case '2':
                    print("\nWrite student's id.")
                    in_id = int(input())
                    delet_est(in_id)
                    # delet_est(10)
                    print('Student deleted.')
                    showEst()
                    showMenu()
                case '3':
                    print("\nWrite student's id.");
                    in_id = int(input())
                    print("Write student's new name.")
                    in_nom = input()
                    print("Write student's new enrollment.")
                    in_mat = int(input())
                    updat_est(in_nom, in_mat, in_id)
                    print('Student updated.')
                    showEst()
                    showMenu()
                case '4':
                    showMenu()
                case _:
                    print('Bye...');

        case '2':
            print('')
            showMat()
            print('\nWich action do you want to execute?')
            print('1) Add course.')
            print('2) Delete course.')
            print('3) Update course.')
            print('4) Go back to menu.')
            print('q) Quit.\n')           
            # showEst()
            # print('')
            sel2 = input()
            match sel2:
                case '1':
                    print("\nWrite course's name.")
                    in_nom = input()
                    inser_mat(in_nom)
                    print('Course added.\n')
                    showMat()
                    # os.system('clear')
                    showMenu()
                case '2':
                    print("\nWrite course's id.")
                    in_id = int(input())
                    delet_mat(in_id)
                    # delet_est(10)
                    print('Course deleted.')
                    showMat()
                    showMenu()
                case '3':
                    print("\nWrite course's id.");
                    in_id = int(input())
                    print("Write course's new name.")
                    in_nom = input()
                    updat_mat(in_nom, in_id)
                    print('Student updated.')
                    showMat()
                    showMenu()
                case '4':
                    showMenu()
                case _:
                    print('Bye...');


        case '3':
            print('')
            showEva()
            print('\nWich action do you want to execute?')
            print('1) Add evaluation.')
            print('2) Delete evaluation.')
            print('3) Update evaluation.')
            print('4) Go back to menu.')
            print('q) Quit.\n')           
            # showEst()
            # print('')
            sel2 = input()
            match sel2:
                case '1':
                    print("")
                    showEst()
                    print("\nWrite student's id.")
                    in_id = input()
                    print("")
                    showMat()
                    print("\nWrite enrollment's id.")
                    in_enr = input()
                    print("Write student's grade.")
                    in_gra = input()
                    inser_eva(in_id, in_enr, in_gra)
                    print('Evaluation added.\n')
                    showEva()
                    # os.system('clear')
                    showMenu()
                case '2':
                    print("\nWrite evaluation id.")
                    in_id = int(input())
                    delet_eva(in_id)
                    # delet_est(10)
                    print('\nEvaluation deleted.')
                    showEva()
                    showMenu()
                case '3':
                    print("\nWrite evaluation id.");
                    in_idev = int(input())
                    print("Write new grade")
                    in_gra = input()
                    print('')
                    showEst()
                    print("\nWrite new student id.")
                    in_ides = input()
                    print('')
                    showMat()
                    print("\nWrite new enrollment id.")
                    in_idm = int(input())
                    updat_eva(in_gra, in_ides, in_idm, in_idev)
                    print('Evaluation updated.')
                    showEva()
                    showMenu()
                case '4':
                    showMenu()
                case _:
                    print('Bye...');

        case '4':
            print('')
            showEst()
            print("\nWrite student's id");
            in_id = int(input())
            print('')
            showDis(in_id)
            showMenu()
        case _:
            print('Bye...');

