# Modern Lakehouse Platform

A containerized, enterprise-inspired modern data platform built locally to learn and practice modern Data Engineering concepts.

The objective of this project is to deeply understand how modern data platforms are designed, built, orchestrated, and operated while following software engineering best practices.

This is **not a tutorial repository**. It is an evolving engineering project that aims to simulate production-grade lakehouse architectures on a local machine.

---

# Architecture

```text
                    VSCode

        UV + Python + Jupyter Kernel

                        │

                        ▼

                   PySpark 4

                        │

                   Delta Lake

                        │

                        ▼

                      MinIO

      bronze / silver / gold layers

                        │

    ┌───────────────────┼───────────────────┐

    │                   │                   │

    ▼                   ▼                   ▼

 DuckDB             Trino           Unity Catalog

                        │

                        ▼

                     Airflow
```

---

# Project Goals

- Build an enterprise-inspired modern lakehouse platform locally.
- Deeply understand Apache Spark internals.
- Learn distributed computing concepts.
- Implement Medallion Architecture (Bronze, Silver, Gold).
- Learn workflow orchestration using Airflow.
- Implement data governance using Unity Catalog.
- Explore analytical engines such as DuckDB and Trino.
- Apply software engineering best practices to Data Engineering projects.

---

# Technology Stack

| Layer | Technology |
|------|------------|
| Development Environment | VSCode + UV |
| Compute Engine | PySpark 4 |
| Table Format | Delta Lake |
| Object Storage | MinIO |
| Orchestration | Apache Airflow |
| Governance | Open Source Unity Catalog |
| Analytics Engine | DuckDB |
| Distributed SQL Engine | Trino |
| Source Database | SQL Server (planned) |
| CI/CD | GitHub Actions (planned) |

---

# Repository Structure

```text
lakehouse_workspace/

├── dags/
├── docker/
├── notebooks/
├── src/
│   └── lakehouse/
│       ├── configs/
│       ├── pipelines/
│       ├── spark/
│       └── utils/
│
├── tests/
│
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Medallion Architecture

## Bronze Layer

Raw ingestion layer.

Responsibilities:

- Store raw source data
- Preserve source fidelity
- Minimal transformations

Examples:

- customers
- orders
- products
- transactions

---

## Silver Layer

Data cleansing and standardization layer.

Responsibilities:

- Data quality checks
- Type conversions
- Null handling
- Deduplication
- Business rules

---

## Gold Layer

Business consumption layer.

Responsibilities:

- KPI calculations
- Business metrics
- Reporting datasets
- Machine Learning feature datasets

Examples:

- customer_lifetime_value
- monthly_revenue
- daily_sales

---

# Engineering Principles

## Infrastructure

Infrastructure runs inside Docker.

Services:

- MinIO
- Airflow
- Unity Catalog
- Trino
- SQL Server (planned)

## Development Environment

Development runs locally.

Components:

- VSCode
- UV
- PySpark
- Delta Lake
- DuckDB

## Data Storage

Data is never stored locally.

The lakehouse storage layer is MinIO.

```text
bronze/
silver/
gold/
checkpoints/
```

---

# Learning Roadmap

## Phase 1

- [x] Configure VSCode environment
- [x] Configure UV
- [x] Configure PySpark 4
- [x] Configure Delta Lake
- [x] Configure MinIO
- [x] Configure S3A connector

## Phase 2

- [ ] Bronze ingestion pipelines
- [ ] Silver transformation pipelines
- [ ] Gold business datasets

## Phase 3

- [ ] Airflow orchestration
- [ ] Data quality framework
- [ ] Unit testing

## Phase 4

- [ ] Trino integration
- [ ] Unity Catalog integration
- [ ] SQL Server integration

## Phase 5

- [ ] GitHub Actions CI/CD
- [ ] Monitoring
- [ ] Production hardening

---

# Learning Objectives

This repository is also a long-term engineering notebook to deeply understand:

- Distributed Computing
- Apache Spark Internals
- Partitioning Strategies
- Adaptive Query Execution (AQE)
- Data Lakehouse Architectures
- Data Governance
- Orchestration Patterns
- Modern Data Platform Engineering

---

# Future Enhancements

- Apache Kafka
- LocalStack
- Kubernetes
- dbt
- Great Expectations
- Grafana
- Prometheus

---

# Disclaimer

This project is a learning and experimentation environment designed to emulate enterprise data engineering architectures locally.

The focus is on understanding systems, architecture decisions, and software engineering practices rather than simply installing technologies.
