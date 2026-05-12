
# importing necessary libraries
import qrcode  # type: ignore # ignore import error
from colorama import Fore, Style, init
import os

init()

print('='*50)
print(Fore.GREEN + 'QR Code Generator' + Style.RESET_ALL)
print('='*50)

# User input for the data to encode in the QR code
data = input('Enter text or URL to generate QR code: ')

# Ask user for filename to save the QR code
filename = input('Enter filename to save QR code (without extension): ')
if not filename:
    filename = 'qr_code'

# Create QR code instance and add data
qr = qrcode.QRCode(
    version=5,
    box_size = 20,
    border = 4
)

# Add data to the QR code (impotant to call make() after adding data)
qr.add_data(data)
qr.make(fit=True)

# Generating the QR code image and saving it
img = qr.make_image(fill_color='black', back_color='white')
full_filename = f'{filename}.png'
img.save(full_filename)

print(Fore.GREEN + f'QR code saved as {full_filename}' + Style.RESET_ALL)
print('='*50)

# Open the generated QR code image automatically
if os.name == 'nt': # For Windows
    os.startfile(full_filename)
else:
    os.system(f'open {full_filename}') # For other operating systems

print(Fore.LIGHTGREEN_EX + f' 📱 Scan it with your phone to see {data[:50]}...'+ Style.RESET_ALL)       
                                                                                                                                                                                                                              