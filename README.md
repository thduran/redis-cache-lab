# Redis Cache Strategy

## Project Overview

This project is a Proof of Concept (PoC) demonstrating how to implement a **caching layer** to drastically reduce application latency and offload database stress.

It simulates a "high latency" scenario (common in legacy SQL databases or complex queries) and solves it using **Redis** with the **cache-aside** pattern.

### The Goal
To demonstrate the performance difference between:
* **Direct database access:** High latency (~3 seconds per request).
* **Cached access:** Low latency (< 10 milliseconds).

## Architecture

The application follows the **cache-aside** strategy:
1.  **Request:** User asks for data.
2.  **Cache check:** App checks if data exists in **Redis (Memory)**.
3.  **Cache miss:** If not found, App queries the **slow database** (simulated).
4.  **Cache population:** App saves the result in Redis with a **TTL** of 10s
5.  **Response:** Data is returned to the user.

## How to run

### Prerequisites
- Docker & Docker Compose

1. Start the Environment

```bash
# Builds the Python image and starts Redis
docker-compose up --build
```
2. Test Performance

Open the browser: `http://localhost:5000`

* **First Request (cache miss):**
  * The app simulates a slow database query.
  * Time: ~3.0 seconds.
  * Status: "Slow database".

* **Second Request (cache hit):**
  * Refresh the page immediately (F5).
  * The app retrieves data from Redis RAM.
  * Time: < 0.01 seconds.
  * Status: "redis cache (Memória RAM)".

* **Expiration (TTL):**
  * Wait 10 seconds and refresh again. The cache will expire, and the app will hit the slow DB again.

## Key DevOps Concepts Applied

* Latency reduction: Reducing response time from seconds to milliseconds improves User Experience (UX) and SEO.
* Database offloading: By serving 99% of read traffic from Redis, we protect the primary database (MySQL/PostgreSQL) from CPU spikes during high-traffic events (e.g., Black Friday).
* TTL: Implemented a 10-second expiration policy to ensure data consistency, preventing the cache from serving stale data indefinitely.

---

PTBR

# Estratégia Redis com Cache

## Sobre o projeto

Este projeto é um PoC que demonstra como implementar uma **camada de cache** para reduzir drasticamente a latência da aplicação e aliviar a carga do banco de dados

Simula um cenário de **alta latência** (comum em banco de dados SQL legados ou em consultas complexas) que é resolvido com **Redis** com o **padrão cache-aside**.

### Objetivo
Demonstrar a diferença de performance entre:
* **Acesso direto ao BD:** alta latência (~3s).
* **Acesso via cache:** baixa latência (< 10ms).

## Arquitetura

A aplicação usa o padrão **cache-aside**:
1.  **Requisição:** Usuário solicita dados.
2.  **Verificação do cache:** a aplicação verifica se existem dados na memória do Redis.
3.  **Cache miss:** Se não há, a aplicação consulta o banco de dados "lento" (simulado).
4.  **População do cache:** A aplicação salva no Redis com um TTL de 10s.
5.  **Resposta:** O dado é retornado ao usuário.

## Como executar

### Pré-requisitos
- Docker & Docker Compose

1. Provisione o ambiente

```bash
# Build da imagem do Python e inicia o Redis
docker-compose up --build
```
2. Teste de desempenho

Abra o navegador: `http://localhost:5000`

* **Primeira requisição (cache miss):**
  * A aplicação simula uma consulta lenta ao BD.
  * Tempo: ~3.0s
  * Status: "simulated slow database"

* **Segunda requisição (cache hit):**
  * Atualize a página imediatamente.
  * A aplicação obtém os dados da RAM do Redis.
  * Tempo: < 0.01s
  * Status: "redis cache".

* **Expiração (TTL):**
  * Espere 10s e atualize a página novamente. O cache vai expirar e a aplicação voltará a consultar o banco de dados "lento".

## Conceitos chave de DevOps aplicados

* Redução de latência: reduzir do tempo de resposta de segundos para milissegundos melhora UX E SEO.
* Alívio de carga ao BD: Com 99% do tráfego sendo direcionado ao Redis, protegemos o BD primário (MySQL, PostgreSQL...) de picos de CPU em eventos de alto tráfego (Black Friday etc).
* TTL: Política de expiração de 10s para garantir consistência de dados, evitando que o cache sirva informações obsoletas indefinidamente.