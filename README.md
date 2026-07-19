# Inventory Report Manager 📦

O **Inventory Report Manager** é uma aplicação em Python focada na consolidação de inventários de estoque a partir de múltiplas fontes de dados (arquivos JSON e CSV) e na geração automatizada de relatórios estatísticos de validade, fabricação e volume por empresa.

O projeto foi estruturado utilizando conceitos avançados de Orientação a Objetos (OO), padrões de projeto, tipagem estática e testes unitários rigorosos com **Pytest**.

## 🚀 O que aprendi e apliquei neste projeto

- **Programação Orientada a Objetos Avançada:**
    - Criação de classes abstratas utilizando o módulo `abc` (`ABC`, `@abstractmethod`).
    - Implementação de contratos de tipo estruturais usando **Protocolos** (`typing.Protocol`).
    - Uso de encapsulamento seguro com propriedades somente leitura (`@property`).
    - Especialização de comportamento através de herança clássica (`CompleteReport` herdando de `SimpleReport`).

- **Lógica Algorítmica e Tratamento de Datas:**
    - Uso estratégico de limites superiores de tempo (`datetime.max`) para criar acumuladores robustos de menor valor.
    - Criação de filtros inteligentes temporais para determinar prazos de validade mais próximos, gerenciando com sucesso cenários de conciliação de dados reais do sistema em relação a dados simulados/passados (mocks).

- **Testes Automatizados com Pytest:**
    - Criação de testes unitários para construtores (`__init__`) e métodos mágicos de representação textual (`__str__`).
    - Testagem baseada em dados usando a parametrização de testes (`@pytest.mark.parametrize`).

- **Evitando Armadilhas de Sintaxe (Python Pitfalls):**
    - Domínio sobre as precedências de operadores de string dentro de tuplas implícitas e parênteses de retorno, utilizando f-strings e `\n`.join() previamente isolados para evitar loops de concatenação acidentais.

---

## 🛠️ Arquitetura do Sistema e Componentes

### 1. Núcleo de Domínio

- **`Product`:** Entidade que modela as propriedades de um item de estoque (`id`, `company_name`, `product_name`, datas e instruções de armazenamento) e implementa a string de rotulagem via método mágico `__str__`.
- **`Inventory`:** Container mutável que gerencia coleções de produtos com controle de acesso somente leitura para proteção dos dados internos através de cópias.

### 2. Camada de Importação (Polimorfismo e Abstração)

- **`Importer` (Classe Abstrata):** Define a assinatura padrão para extração de arquivos.
- **`JsonImporter` & `CsvImporter`:** Implementações concretas especializadas. Utilizam apenas módulos built-in do Python para varrer e parsear arquivos populando as entidades de domínio.

### 3. Camada de Relatórios (Protocolos e Herança)

- **`Report` (Protocolo):** Contrato que exige as operações `add_inventory` e `generate`.
- **`SimpleReport`:** Computa de forma agregada a data de fabricação mais antiga, a data de validade mais próxima (filtrando de forma inteligente os itens válidos) e identifica a empresa detentora do maior volume físico.
- **`CompleteReport`:** Especialização de `SimpleReport` que adiciona uma seção detalhada mapeando quantitativamente a distribuição de produtos por empresa.

### 4. Interface de Linha de Comando (CLI)

- **`process_report_request`:** Ponto de entrada do processamento em lote. Filtra dinamicamente os arquivos por extensão (ignorando formatos inválidos), centraliza a carga de dados unificada de múltiplos arquivos e despacha a requisição para a engine de relatório apropriada, emitindo erros descritivos (`ValueError`) caso os comandos sejam inválidos.

---

## 📦 Instalação e Execução

### Configurando o ambiente

```bash
# Criar o ambiente virtual
python3 -m venv .venv

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar dependências de desenvolvimento
pip install -r dev-requirements.txt
```

### Interface de linha de comando:

| Flag | Argumento |
| --- | --- |
| `-p` | caminho/da/pasta/com/arquivos |
| `-t` | `simple` - `complete` |

- exemplo:

```bash
ir -p caminho/da/pasta -t simple
```

### Executando testes:

```bash
pytest
pytest -x
pytest tests/product/test_product.py
```
