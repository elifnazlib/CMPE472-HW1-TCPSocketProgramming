# CMPE 472 – Computer Networks - Programming Assignment 1

#### Topic: Plate Code Prediction
In this assignment, you must build a mini application using socket programming.

#### The requirements are as follows:
- You will use TCP sockets in this assignment.
- The sockets will belong to the same host. In other words, you will use localhost communication.
- The attached excel file contains the list of plate codes for all the cities. You have to read the excel file in the server side.

## Client side:
- It will make a connection to the server.
- It will take predictions from the user. The user will try to predict the plate code of the city picked and sent by the server side.
- The prediction will be sent to server.
- When the user fails or wins, the client socket will be closed and the program will finish.
- If the user enters “END”, both the client side and server side operation will finish.
## Server side:
- It will wait for the connection of a client until a client connects to it.
- It will randomly choose a city and send a message to the client asking for the plate code of the chosen city.
- It will receive predictions from client. If the prediction is the plate code of another city, it will inform the user about the name of the city. If the prediction is smaller than 1 or larger than 81 (not a valid plate code) or if it is not a numeric value, it will send the corresponding message and close the connection with the client. Then, it will wait for another client.
- If the prediction is correct, the corresponding message will be sent and connection with the client will be closed. Then, it will wait for another client.
- It will finish its operation if the user sends “END” string.

<br> 

*** 

#### Output:
<img width="770" alt="output" src="https://github.com/user-attachments/assets/722feb39-fc75-4aae-8c5e-8d549dd487ac">

<br> 
<br>
<br>

## Developers:
[Büşra Ekici](https://github.com/busraekicii) <br>
[Elif Nazlı Böke](https://github.com/elifnazlib) <br>
[Gülce Ayşe Döker](https://github.com/GulceAyseDoker)
