import win32com.client

def get_installed_drivers():
    wmi = win32com.client.GetObject("winmgmts:")
    drivers = wmi.ExecQuery("SELECT * FROM Win32_PnPSignedDriver")
    installed_drivers = []
    for driver in drivers:
        if driver.DeviceName is not None:
            installed_drivers.append(driver.DeviceName)
    return installed_drivers

installed_drivers = get_installed_drivers()
for driver in installed_drivers:
    print(driver)