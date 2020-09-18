# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/meoboot.py
import sys, os, struct

def MeobootMainEx(source, target, installsettings, passwdsettings, wifisettings):
    MeobootVu(source, target, installsettings, passwdsettings, wifisettings)


def MeobootVu(source, target, installsettings, passwdsettings, wifisettings):
    meohome = '/media/meoboot'
    meoroot = 'media/meoboot'
    cmd = 'showiframe /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/icons/meoboot.mvi > /dev/null 2>&1'
    rc = os.system(cmd)
    to = '/media/meoboot/MbootM/' + target
    cmd = 'rm -r %s > /dev/null 2<&1' % to
    rc = os.system(cmd)
    to = '/media/meoboot/MbootM/' + target
    cmd = 'mkdir %s > /dev/null 2<&1' % to
    rc = os.system(cmd)
    to = '/media/meoboot/MbootM/' + target
    cmd = 'chmod -R 0777 %s' % to
    rc = os.system(cmd)
    rc = MeobootExtract(source, target)
    cmd = 'mkdir -p %s/MbootM/%s/media > /dev/null 2>&1' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'rm %s/MbootM/%s/%s > /dev/null 2>&1' % (meohome, target, meoroot)
    rc = os.system(cmd)
    cmd = 'rmdir %s/MbootM/%s/%s > /dev/null 2>&1' % (meohome, target, meoroot)
    rc = os.system(cmd)
    cmd = 'cp /etc/network/interfaces %s/MbootM/%s/etc/network/interfaces > /dev/null 2>&1' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'cp /etc/passwd %s/MbootM/%s/etc/passwd > /dev/null 2>&1' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'cp /etc/resolv.conf %s/MbootM/%s/etc/resolv.conf > /dev/null 2>&1' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'cp /etc/wpa_supplicant.conf %s/MbootM/%s/etc/wpa_supplicant.conf > /dev/null 2>&1' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'cp -r /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot %s/MbootM/%s/usr/lib/enigma2/python/Plugins/Extensions' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'cp /etc/init.d/bootup %s/MbootM/%s/etc/init.d/bootup > /dev/null 2>&1' % (meohome, target)
    rc = os.system(cmd)
    cmd = 'cp -r /etc/rcS.d/S05bootup %s/MbootM/%s/etc/rcS.d/S05bootup' % (meohome, target)
    rc = os.system(cmd)
    if installsettings == 'True':
        cmd = 'mkdir -p %s/MbootM/%s/etc/enigma2 > /dev/null 2>&1' % (meohome, target)
        rc = os.system(cmd)
        os.system('mv /etc/enigma2/skin_user.xml /etc/enigma2/skin_user.indb')
        cmd = 'cp -f /etc/enigma2/* %s/MbootM/%s/etc/enigma2/' % (meohome, target)
        rc = os.system(cmd)
        cmd = 'cp -f /etc/tuxbox/* %s/MbootM/%s/etc/tuxbox/' % (meohome, target)
        rc = os.system(cmd)
        os.system('mv /etc/enigma2/skin_user.indb /etc/enigma2/skin_user.xml')
    if passwdsettings == 'True':
        cmd = 'cp -f /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/contrib/passwd %s/MbootM/%s/etc' % (meohome, target)
        rc = os.system(cmd)
    if wifisettings == 'True':
        cmd = 'mkdir %s/MbootM/%s/lib > /dev/null 2>&1' % (meohome, target)
        rc = os.system(cmd)
        cmd = 'cp -r /lib/modules %s/MbootM/%s/lib' % (meohome, target)
        rc = os.system(cmd)
    filename = meohome + '/MbootM/' + target + '/.meoinfo'
    out = open(filename, 'w')
    out.write(target)
    out.close()
    mypath = meohome + '/MbootM/' + target + '/var'
    if os.path.isdir(mypath):
        filename = meohome + '/MbootM/.meoboot'
        out = open(filename, 'w')
        out.write(target)
        out.close()
    rc = os.system('echo 3 > /proc/sys/vm/drop_caches')
    rc = os.system('rm -r /media/meoboot/MbootUpload/*')
    rc = os.system('sync')
    os.system('/etc/init.d/reboot')


def MeobootExtract(source, target):
    ver = ''
    text = ''
    if os.path.exists('/media/meoboot/ubi') is False:
        rc = os.system('mkdir /media/meoboot/ubi')
    sourcefile = '/media/meoboot/MbootUpload/%s.zip' % source
    if os.path.exists(sourcefile) is True:
        os.chdir('/media/meoboot/MbootUpload')
        rc = os.system('unzip ' + sourcefile)
    else:
        return 0
    rc = os.system('rm ' + sourcefile)
    os.chdir('vuplus')
    rootfname = 'rootfs.tar.bz2'
    if os.path.exists('./uno4k') is True:
        os.chdir('uno4k')
        rootfname = 'rootfs.tar.bz2'
    elif os.path.exists('./solo4k') is True:
        os.chdir('solo4k')
        rootfname = 'rootfs.tar.bz2'
    elif os.path.exists('./ultimo4k') is True:
        os.chdir('ultimo4k')
        rootfname = 'rootfs.tar.bz2'
    elif os.path.exists('./uno4kse') is True:
        os.chdir('uno4kse')
        rootfname = 'rootfs.tar.bz2'		
    cmd = '/usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/contrib/tar -xvf %s -C /media/meoboot/MbootM/%s/' % (rootfname, target)
    rc = os.system(cmd)
    if 'BlackHole' in source:
        ver = source.replace('BlackHole-', '')
        try:
            text = ver.split('-')[0]
        except:
            text = ''

        cmd = 'mkdir /media/meoboot/MbootM/%s/boot/blackhole' % target
        rc = os.system(cmd)
        cmd = 'cp /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/contrib/version /media/meoboot/MbootM/%s/boot/blackhole' % target
        rc = os.system(cmd)
        cmd = 'cp /usr/lib/enigma2/python/Plugins/Extensions/MeoBoot/contrib/ut /media/meoboot/MbootM/%s/usr/lib/enigma2/python/Blackhole/BhUtils.pyo' % target
        rc = os.system(cmd)
        localfile = '/media/meoboot/MbootM/%s/boot/blackhole/version' % target
        temp_file = open(localfile, 'w')
        temp_file.write(text)
        temp_file.close()
        cmd = 'mv /media/meoboot/MbootM/%s/usr/bin/enigma2 /media/meoboot/MbootM/%s/usr/bin/enigma2-or' % (target, target)
        rc = os.system(cmd)
        fail = '/media/meoboot/MbootM/%s/usr/bin/enigma2-or' % target
        f = open(fail, 'r')
        content = f.read()
        f.close()
        localfile2 = '/media/meoboot/MbootM/%s/usr/bin/enigma2' % target
        temp_file2 = open(localfile2, 'w')
        temp_file2.write(content.replace('/proc/blackhole/version', '/boot/blackhole/version'))
        temp_file2.close()
        cmd = 'chmod -R 0755 %s' % localfile2
        rc = os.system(cmd)
        cmd = 'rm -r /media/meoboot/MbootM/%s/usr/bin/enigma2-or' % target
        rc = os.system(cmd)
    return 1
