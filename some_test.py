with open(r'D:\1.txt', 'w') as f:
    for i in range(3000,5000):  
        b = str(hex(i)[2:]).rjust(12, "0")
        a = '''%s   Auth-Type == CHAP,  Cleartext-Password := "%s"
	            Service-Type =  Framed-User, 
	            Framed-Protocol = PPP,
	            Filter-Id = 3010,
	            Framed-Pool = 10000,
                H3C-WEB-URL="http://82.0.0.35:8080/imc/portal/",
                h3c-avpair = "url-redirect = http://82.0.0.35:8080/imc/portal",''' % (b, b)
        f.writelines(a+"\n")
