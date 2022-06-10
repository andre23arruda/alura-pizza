import qrcode
from setup.env import get_ip_address, URL_PROD


def create_codes():
    url_local =  f'http://{ get_ip_address() }:3000'
    img_local = qrcode.make(url_local)
    img_local.save(f'../qr_codes/code-local.png')

    url_prod = URL_PROD
    img_prod = qrcode.make(url_prod)
    img_prod.save(f'../qr_codes/code-prod.png')

create_codes()
print('Sucesso!')