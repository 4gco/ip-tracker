try:
    import requests
except:
    print('[-] pip install requests')
try:
    import colorama
    from colorama import Fore
    colorama.init(autoreset=colorama)
except:
    print('[-] pip install colorama')
def banner():
    Bb = Fore.LIGHTYELLOW_EX
    print(Bb + """
    


    """, Fore.LIGHTGREEN_EX + "\n                  ( @4gco )",
          Fore.LIGHTBLUE_EX + "\n   (This tool is programmed by the programmer : @4gco)              \n",
          Fore.LIGHTYELLOW_EX + "                ( info from ip )\n\n" + Fore.RESET)
banner()
def get_information_ip_target():
    ip = input('[?] Enter Ip : ')
    url_info = f'https://api.ipgeolocation.io/ipgeo?include=hostname&ip={ip}'
    headers_info = {
        'Host': 'api.ipgeolocation.io',
        'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'Accept': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'Origin': 'https://ipgeolocation.io',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ipgeolocation.io/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close'
    }
    try:
        req_info = requests.get(url_info, headers=headers_info).json()
        continent_code = str(req_info['continent_code'])
        continent_name = str(req_info['continent_name'])
        country_code2 = str(req_info['country_code2'])
        country_code3 = str(req_info['country_code3'])
        country_name = str(req_info['country_name'])
        country_capital = str(req_info['country_capital'])
        state_prov = str(req_info['state_prov'])
        district = str(req_info['district'])
        city = str(req_info['city'])
        zipcode = str(req_info['zipcode'])
        latitude = str(req_info['latitude'])
        longitude = str(req_info['longitude'])
        is_eu = str(req_info['is_eu'])
        calling_code = str(req_info['calling_code'])
        country_tld = str(req_info['country_tld'])
        languages = str(req_info['languages'])
        country_flag = str(req_info['country_flag'])
        geoname_id = str(req_info['geoname_id'])
        isp = str(req_info['isp'])
        connection_type = str(req_info['connection_type'])
        organization = str(req_info['organization'])
        asn = str(req_info['asn'])
        code = str(req_info['currency']['code'])
        symbol = str(req_info['currency']['symbol'])
        name = str(req_info['time_zone']['name'])
        offset = str(req_info['time_zone']['offset'])
        current_time = str(req_info['time_zone']['current_time'])
        current_time_unix = str(req_info['time_zone']['current_time_unix'])
        is_dst = str(req_info['time_zone']['is_dst'])
        dst_savings = str(req_info['time_zone']['dst_savings'])
        print('========================')
        print(f'[+] Ip : {ip}')
        print(f'[+] continent_code : {continent_code}')
        print(f'[+] continent_name : {continent_name}')
        print(f'[+] country_code2 : {country_code2}')
        print(f'[+] country_code3 : {country_code3}')
        print(f'[+] country_name : {country_name}')
        print(f'[+] country_capital : {country_capital}')
        print(f'[+] state_prov : {state_prov}')
        print(f'[+] district : {district}')
        print(f'[+] city : {city}')
        print(f'[+] zipcode : {zipcode}')
        print(f'[+] latitude : {latitude}')
        print(f'[+] longitude : {longitude}')
        print(f'[+] is_eu : {is_eu}')
        print(f'[+] calling_code : {calling_code}')
        print(f'[+] country_tld : {country_tld}')
        print(f'[+] languages : {languages}')
        print(f'[+] country_flag : {country_flag}')
        print(f'[+] geoname_id : {geoname_id}')
        print(f'[+] isp : {isp}')
        print(f'[+] connection_type : {connection_type}')
        print(f'[+] organization : {organization}')
        print(f'[+] asn : {asn}')
        print(f'[+] code : {code}')
        print(f'[+] symbol : {symbol}')
        print(f'[+] name : {name}')
        print(f'[+] offset : {offset}')
        print(f'[+] current_time : {current_time}')
        print(f'[+] current_time_unix : {current_time_unix}')
        print(f'[+] is_dst : {is_dst}')
        print(f'[+] dst_savings : {dst_savings}')
        print('========================')
        print('[*] Press Enter To Exit ..')
        input()
        exit(0)
    except:
        print('[-] Error Ip')
get_information_ip_target()
