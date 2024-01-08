import subprocess

def install_python_requirements():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("Python packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install Python packages - {e}")

def install_npm_packages():
    npm_commands = [
        'npm i user-agents', 'npm i header-generator', 'npm i request', 'npm i fake-useragent',
        'npm i randomstring', 'npm i colors', 'npm i axios', 'npm i cheerio', 'npm i gradient-string',
        'npm i cloudscraper', 'npm i random-useragent', 'npm i crypto-random-string', 'npm i playwright-extra',
        'npm i fingerprint-generator', 'npm i fingerprint-injector', 'npm i ua-parser-js', 'npm i http2',
        'npm i minimist', 'npm i socks', 'npm i puppeteer', 'npm i hcaptcha-solver', 'npm i puppeteer-extra',
        'npm i puppeteer-extra-plugin-recaptcha', 'npm i puppeteer-extra-plugin-stealth', 'npm i http', 'npm i http2'
    ]
    
    try:
        for command in npm_commands:
            subprocess.run(command, shell=True, check=True)
        print("NPM packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install NPM packages - {e}")

def setup():
    install_python_requirements()
    install_npm_packages()

if __name__ == "__main__":
    setup()
