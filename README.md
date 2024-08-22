# Projeto-Final


## Diagrama de sequencia

```mermaid
sequenceDiagram
    participant Usuário
    participant Interface
    participant Executor
    participant Analisador
    participant API-Nmap as API Nmap
    participant API-Scapy as API Scapy
    participant API-OpenVAS as API OpenVAS
    participant Relatório
    
    %% Fase de Início da Análise
    Usuário->>+Interface: Iniciar Análise de Rede
    Interface->>+Executor: Executar Análise de Rede

    %% Fase de Coleta de Dados
    Executor->>+Analisador: Coletar Dados da Rede

    %% Varredura de Portas usando Nmap
    Analisador->>+API-Nmap: Realizar Varredura de Portas
    API-Nmap-->>-Analisador: Retornar Resultados da Varredura

    %% Análise de Tráfego usando Scapy
    Analisador->>+API-Scapy: Monitorar e Analisar Tráfego de Rede
    API-Scapy-->>-Analisador: Retornar Dados de Tráfego

    %% Análise de Vulnerabilidades usando OpenVAS
    Analisador->>+API-OpenVAS: Detectar Vulnerabilidades
    API-OpenVAS-->>-Analisador: Retornar Relatório de Vulnerabilidades

    %% Fase de Processamento de Resultados
    Analisador->>+Executor: Consolidar Resultados das Análises

    %% Geração e Exibição do Relatório
    Executor->>+Relatório: Gerar Relatório
    Relatório->>Interface: Exibir Relatório para o Usuário
    Interface->>Usuário: Exibir Relatório Final


```

## Diagrama de arquitetura


```mermaid
graph TD
    subgraph Interface
        A1[CLI/GUI]
    end
    
    subgraph Executor
        B1[Orquestrador de Análises]
    end
    
    subgraph Analisador
        C1[Varredura de Portas]
        C2[Análise de Tráfego]
        C3[Detecção de Vulnerabilidades]
    end
    
    subgraph APIs Externas
        D1[Nmap API]
        D2[Scapy]
        D3[OpenVAS API]
    end
    
    subgraph Relatório
        E1[Gerador de Relatórios]
        E2[Criador arquivo para arquivo]
    end
    
    %% Conexões
    A1 --> B1
    B1 --> C1
    B1 --> C2
    B1 --> C3
    
    C1 --> D1
    C2 --> D2
    C3 --> D3
    
    C1 --> E1
    C2 --> E1
    C3 --> E1
    
    E1 --> E2




```

## Links uteis

- [Notion](https://brief-growth-fd4.notion.site/Projeto-final-a06a5a5f64094094bab902bbca05a5ef?pvs=4)