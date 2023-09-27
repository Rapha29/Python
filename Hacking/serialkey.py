import os
import platform
import winreg

def get_windows_license_info():
    if platform.system() != "Windows":
        return "Este código só funciona em sistemas Windows."

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
            product_name, _ = winreg.QueryValueEx(key, "ProductName")
            product_id, _ = winreg.QueryValueEx(key, "ProductId")

        return f"Nome do Produto: {product_name}\nID do Produto: {product_id}"
    except Exception as e:
        return f"Erro ao obter informações da licença: {str(e)}"

if __name__ == "__main__":
    license_info = get_windows_license_info()
    print(license_info)
