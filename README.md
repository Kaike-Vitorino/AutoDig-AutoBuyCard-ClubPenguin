# AutoDig e AutoBuyCard para Club Penguin

Este projeto consiste em um script desenvolvido em python para automatizar duas tarefas específicas no jogo Club Penguin: escavar para ganhar dinheiro (AutoDig) e comprar cartões de elementos (AutoBuyCard). 
## Funcionalidades

### AutoDig
O AutoDig é responsável por automatizar o processo de escavação no Club Penguin. Ele usa as coordenadas fornecidas pelo user para saber as áreas de escavação e realizar a ação de escavar automaticamente, sem intervenção manual do usuário. Isso permite que os jogadores coletem moedas de forma mais eficiente, rápida e automatica.

### AutoBuyCard
O AutoBuyCard foi desenvolvido para automatizar a compra de cartas dentro do jogo. Com esta funcionalidade, os jogadores podem comprar cartas de elementos automaticamente varias vezes de forma rapida. Isso economiza tempo e esforço, especialmente para aqueles que querem gastar todo o dinheiro com cartas.

Claro, vou adicionar uma seção no README para destacar as partes do código que precisam ser modificadas com as coordenadas obtidas:

---

## Como usar

1. **Requisitos:**
   - Python 3.x instalado.
   - Bibliotecas necessárias: PyAutoGUI.
     ```
     pip install pyautogui
     ```
   - Club Penguin instalado e em execução.

2. **Configuração:**
   - Execute o Club Penguin e vá para a tela onde deseja automatizar as ações.
   - Para obter as coordenadas dos botões, você pode usar o seguinte procedimento:
     1. Importe o PyAutoGUI no console do Python.
     2. Use a função `pyautogui.displayMousePosition()` para exibir as coordenadas enquanto você move o mouse sobre os botões que deseja automatizar.
     3. Anote as coordenadas dos botões relevantes.
   - **AutoDig.py:**
     - As coordenadas precisam ser inseridas nos seguintes locais:
       - Linha 18: `pyautogui.click(x, y)` - Insira as coordenadas do botão de perfil próprio.
       - Linha 21: `pyautogui.click(x, y)` - Insira as coordenadas do botão de danças.
       - Linha 22: `pyautogui.click(x, y)` - Insira as coordenadas do botão da dança específica.
       - Linha 25: `pyautogui.click(x, y)` - Insira as coordenadas do botão do puffy.
       - Linha 26: `pyautogui.click(x, y)` - Insira as coordenadas do botão do presente.
   - **AutoBuyCard.py:**
     - As coordenadas precisam ser inseridas nos seguintes locais:
       - Linha 13: `pyautogui.click(x, y)` - Insira as coordenadas do botão de compra de cartão.
       - Linha 14: `pyautogui.click(x, y)` - Insira as coordenadas do botão "Yes" (sim) para confirmar a compra.
       - Linha 15: `pyautogui.click(x, y)` - Insira as coordenadas do botão "Ok" para fechar a janela de confirmação.

3. **Execução:**
   - Execute o script `AutoDig.py` para utilizar a funcionalidade de AutoDig.
   - Execute o script `AutoBuyCard.py` para utilizar a funcionalidade de AutoBuyCard.


---

## Licença

Este projeto está licenciado sob a MIT License.
