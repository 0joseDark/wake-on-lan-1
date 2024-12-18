# wake-on-lan-1
 Abaixo está o script atualizado para enviar pacotes Wake-on-LAN usando o módulo **`pywakeonlan`**. Este módulo é compatível com o Windows 10 e facilita o envio de pacotes mágicos.

---

### Instalação do módulo `pywakeonlan`
Execute o seguinte comando no terminal para instalar o módulo:
```bash
pip install pywakeonlan
```
### Explicação das Alterações:
1. **Uso do `pywakeonlan`:**
   - A função `send_magic_packet` do módulo **`pywakeonlan`** envia o pacote mágico para o endereço MAC especificado.
   - O envio é simples, sem a necessidade de trabalhar diretamente com sockets.

2. **Campo de entrada para IP:**
   - Um campo opcional para o IP foi adicionado para fins de contexto no log.

3. **Gravação no ficheiro `note.log`:**
   - O log grava informações como timestamp, endereço MAC e IP para rastrear os pacotes enviados.

4. **Exibição no Terminal:**
   - O registro do log também é exibido no terminal para facilitar a depuração.

---

### Como Testar:
1. **Certifique-se de que:**
   - O PC remoto suporta Wake-on-LAN e está configurado para isso.
   - O endereço MAC está correto e segue o formato `00:1A:2B:3C:4D:5E`.

2. **Execute o Script:**
   - Insira o endereço MAC e, opcionalmente, o IP.
   - Clique em "Ligar PC Remoto".

3. **Verifique o `note.log`:**
   - Após o envio, abra o ficheiro `note.log` no diretório do script para confirmar os detalhes registrados.

