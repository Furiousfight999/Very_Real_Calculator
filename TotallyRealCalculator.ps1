#Asks the user to type in a number
Read-Host "what is your first number "

#Read line 1
Read-Host "what is your second number "

#Gives 5 very consequential options
$option = Read-Host "would you like to:
1. add
2. subtract
3. multiply
4. divide
5. sacifice to the mesh network
"
Write-Host "$option"

#"This is the part where you die"
if (5 -eq $option) {
    write-host "SACRIFICE"
    Start-Process -FilePath "C:\Program Files\Cisco Packet Tracer 8.2.2\bin\PacketTracer.exe"
}elseif (1,2,3,4 -eq $option) {
    write-host "Then Do it yourself, IDIOT"
    calc.exe
    calc.exe
    calc.exe
    calc.exe
    calc.exe
    calc.exe
    calc.exe    
    calc.exe
    calc.exe
    calc.exe
    calc.exe
    calc.exe
}
else {
    .\TotallyRealCalculator.ps1
}

