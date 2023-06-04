import subprocess
ans='y'
while ans=='y':
    a=('netsh wlan show profiles')
    Output1 =  subprocess.Popen(a, shell=True, stdout=subprocess.PIPE).stdout.read()
    
    #subprocess.Popen() lets us to do shell commands
    #subprocess.PIPE captures the outputs and returns it
    #stdout.read() reads all the output and assigns it to variable

    print(Output1.decode())

    #decode() decodes the byte values
    
    x=input('Enter WiFi name: ')
    y=('netsh wlan show profiles name="'+x+'" key=clear')
    Output2 =  subprocess.Popen(y, shell=True, stdout=subprocess.PIPE).stdout.read()
    print(Output2.decode())
    ans=input('Check again?(y/n): ')

else:
    print('Thank you!')
