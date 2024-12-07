import unittest
from unittest.mock import patch
import socket
from logic_components.portas import verificar_porta

class TestPortas(unittest.TestCase):

    @patch('subprocess.Popen')  # Mock para subprocess.Popen
    @patch('socket.socket')     # Mock para socket.socket
    def test_verificar_porta(self, mock_socket, mock_popen):
        # Simulando a saída do Popen para um comando que verifica a rede
        mock_popen.return_value.communicate.return_value = ("route print output", "")
        mock_popen.return_value.returncode = 0
        
        # Simulando que a conexão para a porta 80 foi bem-sucedida
        mock_socket.return_value.connect_ex.return_value = 0

        # Chamada da função a ser testada
        porta = verificar_porta("192.168.0.1", 80)
        
        # Verificando se a função retorna o número da porta correta
        self.assertEqual(porta, 80)

if __name__ == '__main__':
    unittest.main()
