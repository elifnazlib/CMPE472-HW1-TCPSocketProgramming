import socket

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(1024).decode()
            print(data, end='')
            
            if "Number exceeds the range. Game over." in data:
                print("")
                break
            
            if "Correct!" in data:
                print("")
                break  
            
            if "You entered a non-numeric value. Game over." in data:
                print("")
                break 

            prediction = input("Your guess: ")
            s.sendall(prediction.encode())

            if prediction.upper() == "END":
                print("")
                break

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 65435
    start_client(HOST, PORT)
