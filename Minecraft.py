import time
import os
import sys
from colorama import Fore, Back, Style
from zipfile import ZipFile
from colorama import init

# Colorama Inizilization
init()

time.sleep(1)

# Extracting method
def extr(name, archive, input):
	zf = ZipFile('archive/' + archive + '.zip', 'r')
	zf.extractall(input)
	zf.close()

# Logging out
def logout():
	print('')
	os.system('pause')

# Extracting java
print(Fore.GREEN + 'WARNING: Java not found or broken.' + Fore.WHITE)
try:
	extr('java', 'java', 'bin/java')
	print('[Extracting java]: done')
except Exception as e:
	print(Fore.WHITE + '[Extracting java]: ' + str(e))
	logout()

# Extracting libraries
print(Fore.GREEN + '\nWARNING: Libraries not found or broken.' + Fore.WHITE)
try:
	extr('libraries', 'libraries', 'bin/libraries')
	print('[Extracting game]: done')
except Exception as e:
	print(Fore.WHITE + '[Extracting libraries]: ' + str(e))
	logout()

# Extracting natives
print(Fore.GREEN + '\nWARNING: Natives not found or broken.' + Fore.WHITE)
try:
	extr('natives', 'natives', 'bin/natives')
	print('[Extracting natives]: done')
except Exception as e:
	print(Fore.WHITE + '[Extracting natives]: ' + str(e))
	logout()

# Extracting assets
print(Fore.GREEN + '\nWARNING: Assets not found or broken.' + Fore.WHITE)
try:
	extr('assets', 'assets', 'game')
	print('[Extracting game]: done')
except Exception as e:
	print(Fore.WHITE + '[Extracting assets]: ' + str(e))
	logout()

# Nick Name
name = input('\nEnter your name: ') 
print('\n\nLoading minecraft. Please wait...')
time.sleep(1)

# Start Minecraft
try:
	os.system('%CD%/bin/java/bin/javaw.exe -Xmx768M -Djava.library.path=game/versions/1.10/natives -cp game/libraries/optifine/OptiFine/1.10.2_HD_U_C1/OptiFine-1.10.2_HD_U_C1.jar;game/libraries/net/minecraft/launchwrapper/1.7/launchwrapper-1.7.jar;game/libraries/com/mojang/netty/1.6/netty-1.6.jar;game/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar;game/libraries/net/java/dev/jna/jna/3.4.0/jna-3.4.0.jar;game/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar;game/libraries/com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar;game/libraries/net/sf/jopt-simple/jopt-simple/4.6/jopt-simple-4.6.jar;game/libraries/com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar;game/libraries/com/paulscode/codecwav/20101023/codecwav-20101023.jar;game/libraries/com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar;game/libraries/com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar;game/libraries/com/paulscode/soundsystem/20120107/soundsystem-20120107.jar;game/libraries/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.jar;game/libraries/com/google/guava/guava/17.0/guava-17.0.jar;game/libraries/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.jar;game/libraries/commons-io/commons-io/2.4/commons-io-2.4.jar;game/libraries/commons-codec/commons-codec/1.9/commons-codec-1.9.jar;game/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar;game/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar;game/libraries/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar;game/libraries/com/mojang/authlib/1.5.22/authlib-1.5.22.jar;game/libraries/com/mojang/realms/1.9.3/realms-1.9.3.jar;game/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar;game/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar;game/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar;game/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar;game/libraries/it/unimi/dsi/fastutil/7.0.12_mojang/fastutil-7.0.12_mojang.jar;game/libraries/org/apache/logging/log4j/log4j-api/2.0-beta9/log4j-api-2.0-beta9.jar;game/libraries/org/apache/logging/log4j/log4j-core/2.0-beta9/log4j-core-2.0-beta9.jar;game/libraries/org/lwjgl/lwjgl/lwjgl/2.9.4-nightly-20150209/lwjgl-2.9.4-nightly-20150209.jar;game/libraries/org/lwjgl/lwjgl/lwjgl_util/2.9.4-nightly-20150209/lwjgl_util-2.9.4-nightly-20150209.jar;game/versions/1.10/1.10.jar -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -XX:-UseAdaptiveSizePolicy -Xmn128M net.minecraft.launchwrapper.Launch --username ' + name + ' --version 1.10 --gameDir %CD% --assetsDir game/assets --assetIndex 1.10 --uuid 00000000-0000-0000-0000-000000000000 --accessToken null --userProperties [] --userType legacy  --tweakClass optifine.OptiFineTweaker --width 925 --height 530')
	logout()
except Exception as e:
	print('[ERROR]: '  + str(e))
