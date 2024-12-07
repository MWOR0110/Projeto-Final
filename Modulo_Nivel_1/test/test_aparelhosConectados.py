import unittest
from unittest.mock import patch
from logic_components.aparelhosConectados import pingar_ip, obter_ip_roteador  # Ajuste o caminho conforme sua estrutura

class TestAparelhosConectados(unittest.TestCase):
    
    @patch('platform.system', return_value='Windows')  # Mock para garantir que o sistema seja reconhecido como Windows
    def test_pingar_ip(self, mock_platform):
        # Mocking da chamada do ping
        with patch('subprocess.run') as mock_run:
            mock_run.return_value.returncode = 0  # Simula um ping bem-sucedido
            result = pingar_ip("192.168.15.1")
            self.assertTrue(result)  # Verifica se o resultado é True (ping bem-sucedido)

    @patch('platform.system', return_value='Windows')  # Mock para garantir que o sistema seja reconhecido como Windows
    @patch('subprocess.check_output')  # Mock do subprocess para obter o IP do roteador
    def test_obter_ip_roteador(self, mock_check_output, mock_platform):
        mock_check_output.return_value = b'192.168.15.1'  # Retorna exatamente o valor esperado
        ip = obter_ip_roteador()
        self.assertEqual(ip, "192.168.15.1")  # Verifica se o IP retornado é o esperado

if __name__ == '__main__':
    unittest.main()
