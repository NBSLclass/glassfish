import requests


def foo():
    for url in open("./1.txt"):
        url = url.strip()
        if 'http' in url or 'https' in url:
            url1 = url
            url2 = None
        else:
            url1 = f'http://{url}'
            url2 = f'https://{url}'
        try:
            ok = requests.get(url1, timeout=(5, 8))
            if ok.status_code == 200:
                print(url1, ok.status_code)
                with open("./ip.txt", 'a+') as url_ok:
                    url_ok.write(url1 + "\n")
                    url_ok.close()
            else:
                ok_1 = requests.get(url2, timeout=(5, 8))
                if ok_1.status_code == 200:
                    print(url2, ok_1.status_code)
                    with open("./ip.txt", 'a+') as url_ok:
                        url_ok.write(url2 + "\n")
                        url_ok.close()
                else:
                    print(url2, ok.status_code)
        except:
            try:
                ok2 = requests.get(url2, timeout=(5, 8))
                if ok2.status_code == 200:
                    print(url2, ok2.status_code)
                    with open("./ip.txt", 'a+') as url_ok:
                        url_ok.write(url1 + "\n")
                        url_ok.close()
                else:
                    print(url2, ok2.status_code)
            except:
                print(f"{url2} URL无效")


if __name__ == "__main__":
    foo()