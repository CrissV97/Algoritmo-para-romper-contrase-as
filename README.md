# Algoritmo-para-romper-contraseñas
1. Ejecucion  
NOTA: Para poder ejecutar el programa es necesario tener instalado Python en el sistema, en caso de no tenerlo, el programa mostrará un mensaje de error para posteriormente cerrarse.  
1.1. Como primer paso se debe descargar el archivo "bruteforce.py" que contiene el código del programa.  
1.2. En un bloc de notas debemos copiar el siguiente comando:  
            @echo off  
            python "%~dp0bruteforce.py"  
            pause  
1.3. Guardar el bloc de notas como tipo ".bat", por ejemplo, bruteforce.bat  
1.4. Abrir el archivo .bat y el programa se ejecutará solo  

3. Ejemplos de salida  
Caso de contraseña valida
<img width="476" height="283" alt="image" src="https://github.com/user-attachments/assets/e298f64d-07bc-4256-a889-8dd82686398e" />  

  Caso de contraseña invalida  
<img width="498" height="278" alt="image" src="https://github.com/user-attachments/assets/f352bfa2-f7e4-4bdd-8817-c884da4103e9" />  


5. Reflexion  
   ¿Qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?.  

   En caso de ingresar más de 8 caracteres, el programa mostrará el mensaje "La contraseña debe tener 4 caracteres." para luego cerrarse automaticamente. Al momento de ingresar letras mayúsculas o minusculas, números o simbolos, no habrá problema alguno ya que el programa está adaptado para tambien encontrar este tipo de caracteres.
