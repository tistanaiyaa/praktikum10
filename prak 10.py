# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:30:42 2024

@author: Lenovo
"""

def bubble_sort(data):
    panjang = len(data)  
    for i in range(panjang):  
        for j in range(0, panjang - i - 1):  
            if data[j] > data[j + 1]:  
                data[j], data[j + 1] = data[j + 1], data[j]
    return data  

def binary_search(data, target):
    kiri = 0  
    kanan = len(data) - 1  

    while kiri <= kanan:  
        tengah = (kiri + kanan) // 2  
        if data[tengah] == target:  
            return tengah  
        elif data[tengah] < target:  
            kiri = tengah + 1  
        else:  
            kanan = tengah - 1  
    return -1  

angka = [15, 2, 28, 23, 34, 31, 87, 56, 200, 89]
print("Daftar angka (acak):", angka)

target = int(input("Masukkan angka: "))

angka_urut = bubble_sort(angka)
print("Daftar angka setelah diurutkan:", angka_urut)

hasil = binary_search(angka_urut, target)

if hasil != -1:
    print(f"elemen {target} ditemukan di indeks {hasil}.")
else:
    print(f"elemen {target} tidak ditemukan.")